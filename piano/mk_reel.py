# -*- coding: utf-8 -*-
"""Crea la cartella di un reel del piano da una scheda in piano/specs/<id>.py
(SLUG, TITLE, BEATS, ART, COVER_TITLE, COVER_ART), partendo dal motore di reel_straordinari."""
import sys, os, shutil, importlib.util, json, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "reel_straordinari")
spec_path = sys.argv[1]
sp = importlib.util.spec_from_file_location("spec", spec_path); S = importlib.util.module_from_spec(sp); sp.loader.exec_module(S)
D = os.path.join(ROOT, S.SLUG)
os.makedirs(os.path.join(D, "rec_src"), exist_ok=True); os.makedirs(os.path.join(D, "out"), exist_ok=True)
for f in ["gen_audio.py","mix_audio.py","build_html.py","render.mjs","build.sh","setup_tts.sh","package-lock.json",".gitignore"]:
    shutil.copy2(os.path.join(BASE, f), D)
if not os.path.exists(os.path.join(D,"fonts")): shutil.copytree(os.path.join(BASE,"fonts"), os.path.join(D,"fonts"))
shutil.copy2(os.path.join(BASE,"rec_src","align_take.py"), os.path.join(D,"rec_src"))
pj = open(os.path.join(BASE,"package.json")).read().replace("pagamee-reel-straordinari","pagamee-reel-"+S.SLUG.replace("reel_","").replace("_","-"))
open(os.path.join(D,"package.json"),"w").write(pj)
for l in ["node_modules","tts"]:
    p=os.path.join(D,l)
    if not os.path.lexists(p): os.symlink("../reel_part_time/"+l, p)
# copione
with open(os.path.join(D,"scenes.py"),"w") as f:
    f.write('# -*- coding: utf-8 -*-\n"""Copione del reel "%s" (piano editoriale %s).\nCampi: id, visual, say (letto), text (a schermo, [g] [r] [i])."""\n\nBEATS = %s\n'
            % (S.TITLE, os.path.basename(spec_path)[:-3], json.dumps(S.BEATS, ensure_ascii=False, indent=1)))
# template: scene + copertina
t = open(os.path.join(BASE,"reel_template.html")).read()
a = t.index('/* ---------- le scene ---------- */'); b = t.index('/* ================= costruzione')
t = t[:a] + open(os.path.join(os.path.dirname(__file__),"common.js")).read() + "\n/* ---------- le scene ---------- */\n" + S.ART + "\n" + t[b:]
a = t.index('  title:['); b = t.index('};\nwindow.renderCover')
t = t[:a] + "  title:%s,\n  art:()=>\n%s,\n" % (json.dumps(S.COVER_TITLE, ensure_ascii=False), S.COVER_ART) + t[b:]
open(os.path.join(D,"reel_template.html"),"w").write(t)
print(D)
