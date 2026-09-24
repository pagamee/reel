# Allinea una lettura continua (rec_src/take.wav) alle battute di scenes.py.
# Candidati = pause reali (silencedetect); scelta dei 24 confini con programmazione
# dinamica, usando come durate attese quelle della timeline Kokoro.
import json, re, subprocess, sys, math
sys.path.insert(0, '.')
from scenes import BEATS
src = sys.argv[1] if len(sys.argv) > 1 else 'rec_src/take.wav'
ref = json.load(open(sys.argv[2] if len(sys.argv) > 2 else 'rec_src/kokoro_timeline.json'))['beats']
out = subprocess.run(['ffmpeg', '-i', src, '-af', 'silencedetect=n=-38dB:d=0.12', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr
st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', out)]
en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', out)]
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src],
                           capture_output=True, text=True).stdout)
sil = list(zip(st, en[:len(st)]))
head = sil[0][1] if sil and sil[0][0] < 0.05 else 0.0
sil = [s for s in sil if s[0] > 0.05 and s[1] < dur - 0.05]
tail = min([s[0] for s in sil if s[1] >= dur - 0.2] + [dur])
speech_start, speech_end = head, dur
# ultimo silenzio fino in fondo
m = re.findall(r'silence_start: ([\d.]+)', out)
if st and (len(en) < len(st)):  # silenzio finale senza end
    speech_end = st[-1]
exp = [b['s1'] - b['s0'] for b in ref]
scale = (speech_end - speech_start) / sum(exp)
n, K = len(BEATS), len(sil)
# dp[i][k]: confine i (dopo battuta i) nella pausa k
INF = 1e18
def cost(a, b, i):  # battuta i parla da a a b
    d = max(b - a, 0.05)
    e = exp[i] * scale
    return math.log(d / e) ** 2
dp = [[INF] * K for _ in range(n - 1)]
bk = [[-1] * K for _ in range(n - 1)]
for k in range(K):
    dp[0][k] = cost(speech_start, sil[k][0], 0)
for i in range(1, n - 1):
    for k in range(K):
        best, arg = INF, -1
        for j in range(k):
            v = dp[i - 1][j] + cost(sil[j][1], sil[k][0], i)
            if v < best:
                best, arg = v, j
        dp[i][k], bk[i][k] = best, arg
fin = min(range(K), key=lambda k: dp[n - 2][k] + cost(sil[k][1], speech_end, n - 1))
ks = [fin]
for i in range(n - 2, 0, -1):
    ks.append(bk[i][ks[-1]])
ks.reverse()
spans, a = [], speech_start
for i, k in enumerate(ks):
    spans.append((a, sil[k][0])); a = sil[k][1]
spans.append((a, speech_end))
for b, (a, e), x in zip(BEATS, spans, exp):
    print(f"{b['id']} {a:7.2f}-{e:7.2f} ({e-a:5.2f}s, atteso {x*scale:5.2f})  {b['say'][:50]}")
json.dump({"file": src, "spans": spans}, open('rec_src/take_spans.json', 'w'), indent=1)
