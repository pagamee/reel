/* eslint-disable */
import React, { useEffect, useState } from "react";
import { AbsoluteFill, Audio, Sequence, staticFile, useVideoConfig, delayRender, continueRender } from "remotion";
import { SCENES } from "./scenes";
import { Scene } from "./Scene";
import { CSS } from "./styles";
import timeline from "./timeline.json";

type TL = { total: number; scenes: { id: string; start: number; end: number; dur: number }[] };
const TIMELINE = timeline as TL;

export const Reel: React.FC = () => {
  const { fps, durationInFrames } = useVideoConfig();
  const [handle] = useState(() => delayRender("load-fonts"));
  const [fontsReady, setFontsReady] = useState(false);

  useEffect(() => {
    const done = () => {
      setFontsReady(true);
      continueRender(handle);
    };
    Promise.all([
      (document as any).fonts.load('normal 100px "Humor Sans"'),
      (document as any).fonts.load('700 100px "Comic Neue"'),
      (document as any).fonts.load('400 100px "Comic Neue"'),
    ])
      .then(() => (document as any).fonts.ready)
      .then(done)
      .catch(done);
  }, [handle]);

  // frame di inizio contigui (nessun buco per arrotondamento)
  const froms = TIMELINE.scenes.map((s) => Math.round(s.start * fps));
  const byId = new Map(TIMELINE.scenes.map((s) => [s.id, s]));

  return (
    <AbsoluteFill style={{ backgroundColor: "#ffffff" }}>
      <style>{CSS}</style>
      <Audio src={staticFile("voiceover.wav")} />
      <div className="stage">
        {SCENES.map((sc, i) => {
          const tl = byId.get(sc.id);
          if (!tl) return null;
          const from = froms[i];
          const to = i < SCENES.length - 1 ? froms[i + 1] : durationInFrames;
          return (
            <Sequence key={sc.id} from={from} durationInFrames={Math.max(1, to - from)} name={sc.id} layout="none">
              <Scene scene={sc} startSec={tl.start} durSec={tl.dur} totalSec={TIMELINE.total} fontsReady={fontsReady} />
            </Sequence>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
