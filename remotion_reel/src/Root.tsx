import { Composition } from "remotion";
import { Reel } from "./Reel";
import timeline from "./timeline.json";

const FPS = 30;

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Reel"
      component={Reel}
      durationInFrames={Math.round((timeline as { total: number }).total * FPS)}
      fps={FPS}
      width={1080}
      height={1920}
    />
  );
};
