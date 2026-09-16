import { staticFile } from "remotion";

export const CSS = `
@font-face{
  font-family:'Humor Sans';
  src:url('${staticFile("fonts/Humor-Sans.ttf")}') format('truetype');
  font-weight:normal;font-style:normal;font-display:block;
}
@font-face{
  font-family:'Comic Neue';
  src:url('${staticFile("fonts/ComicNeue-Regular.otf")}') format('opentype');
  font-weight:400;font-style:normal;font-display:block;
}
@font-face{
  font-family:'Comic Neue';
  src:url('${staticFile("fonts/ComicNeue-Bold.otf")}') format('opentype');
  font-weight:700;font-style:normal;font-display:block;
}
.stage{
  width:1080px;height:1920px;position:relative;overflow:hidden;background:#ffffff;
  font-family:'Humor Sans','Comic Neue',sans-serif;color:#141414;
  -webkit-font-smoothing:antialiased;
}
.scene{position:absolute;inset:0;}
.scene svg.fig{position:absolute;inset:0;}
.eur{font-family:'Comic Neue','DejaVu Sans',sans-serif;font-weight:700;}
.txt{position:absolute;left:0;right:0;text-align:center;padding:0 60px;box-sizing:border-box;}
.headline{font-size:82px;line-height:1.1;font-weight:700;}
.headline.small{font-size:64px;}
.caption{font-size:50px;line-height:1.24;color:#333;}
.red{color:#e5342b;} .green{color:#1a9e4b;} .blue{color:#2b5fb3;} .grey{color:#777;}
.bubble{
  position:absolute;background:#fff;border:6px solid #141414;border-radius:38px;
  padding:30px 38px;font-size:50px;line-height:1.22;font-weight:700;
  text-align:center;box-sizing:border-box;
  box-shadow:9px 11px 0 rgba(20,20,20,.10);
}
.tailsvg{position:absolute;overflow:visible;pointer-events:none;}
.ln{white-space:nowrap;display:inline-block;}
.stack{position:absolute;left:0;right:0;text-align:center;}
.stack .row{font-size:74px;font-weight:700;margin:10px 0;line-height:1.06;}
.wordmark{font-size:100px;font-weight:700;letter-spacing:2px;}
.prog{position:absolute;left:0;bottom:0;height:12px;background:#e5342b;}
`;
