# -*- coding: utf-8 -*-
"""
Base musicale lo-fi generata da zero (nessun campione esterno, nessun diritto di terzi):
accordi di piano elettrico morbido, basso e una ritmica leggera, in loop.
Uso: python3 make_music.py <secondi> <out.wav> [seed]
"""
import sys, wave, numpy as np
SR = 44100
dur = float(sys.argv[1]); out = sys.argv[2]; seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
rng = np.random.default_rng(seed)
bpm = 82; beat = 60 / bpm; bar = 4 * beat
progs = [[60, 64, 67, 71], [57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 65]]   # Cmaj7 Am7 Fmaj7 G7
if seed % 2 == 0: progs = [progs[1], progs[2], progs[0], progs[3]]
f = lambda m: 440 * 2 ** ((m - 69) / 12)
n = int(dur * SR) + SR
mix = np.zeros(n)
def add(sig, t0, gain):
    i = int(t0 * SR); j = min(n, i + len(sig))
    if i < n: mix[i:j] += gain * sig[:j - i]
def epiano(freq, length):
    t = np.arange(int(length * SR)) / SR
    env = np.exp(-t * 1.6) * (1 - np.exp(-t * 60))
    s = np.sin(2*np.pi*freq*t) + 0.35*np.sin(2*np.pi*2*freq*t)*np.exp(-t*3) + 0.12*np.sin(2*np.pi*3*freq*t)*np.exp(-t*5)
    return s * env * (1 + 0.03 * np.sin(2*np.pi*5*t))
def kick():
    t = np.arange(int(0.35 * SR)) / SR
    return np.sin(2*np.pi*(50 + 70*np.exp(-t*30))*t) * np.exp(-t*9)
def hat():
    t = np.arange(int(0.06 * SR)) / SR
    return rng.standard_normal(len(t)) * np.exp(-t*80)
t0 = 0.0; k = 0
while t0 < dur:
    ch = progs[k % 4]
    for i, m in enumerate(ch):
        add(epiano(f(m), bar * 1.1), t0 + i * 0.03, 0.16)
    add(epiano(f(ch[0] - 24), bar), t0, 0.22)
    add(epiano(f(ch[2] + 12), beat * 1.5), t0 + 2.5 * beat, 0.07)
    for b in range(4):
        if b in (0, 2): add(kick(), t0 + b * beat, 0.35)
        add(hat(), t0 + b * beat + beat / 2, 0.05)
    t0 += bar; k += 1
# filtro passa-basso semplice (suono "caldo") e dissolvenze
a = 0.25
y = np.zeros_like(mix); acc = 0.0
for i in range(len(mix)):
    acc += a * (mix[i] - acc); y[i] = acc
y = y[:int(dur * SR)]
fi, fo = int(1.5 * SR), int(3 * SR)
y[:fi] *= np.linspace(0, 1, fi); y[-fo:] *= np.linspace(1, 0, fo)
y = y / np.max(np.abs(y)) * 0.7
st = np.stack([y, y], 1)
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype('<i2').tobytes())
print(out, round(dur, 1), "s")
