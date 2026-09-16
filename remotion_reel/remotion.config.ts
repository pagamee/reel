import { Config } from "@remotion/cli/config";

Config.setVideoImageFormat("jpeg");
Config.setConcurrency(4);
// Il browser NON viene scaricato: usiamo il Chromium locale via --browser-executable in CLI.
