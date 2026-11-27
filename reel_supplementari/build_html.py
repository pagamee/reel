# -*- coding: utf-8 -*-
"""Inietta timeline.json dentro reel_template.html -> reel.html"""
import json, io
tl = json.load(open("timeline.json"))
html = io.open("reel_template.html", encoding="utf-8").read()
html = html.replace("__TIMELINE_JSON__", json.dumps(tl, ensure_ascii=False))
io.open("reel.html", "w", encoding="utf-8").write(html)
print("reel.html scritto — %.2fs, %d battute" % (tl["total"], len(tl["beats"])))
