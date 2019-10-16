
![](https://img.shields.io/badge/coverage-95%25-green)
[![Build Status](https://travis-ci.com/LudwigCRON/pywave.svg?branch=master)](https://travis-ci.com/LudwigCRON/pywave)

![](https://img.shields.io/badge/python-3.5+-blue)

[New documentation under construction](https://ludwigcron.github.io/pywave/html/)

## Introduction

**WaveDrom** is a Free and Open Source online digital timing diagram (waveform) rendering engine that uses javascript, HTML5 and SVG to convert a [WaveJSON](https://github.com/drom/wavedrom/wiki/WaveJSON) input text description into SVG vector graphics.

[WaveJSON](https://github.com/drom/wavedrom/wiki/WaveJSON) is an application of the [JSON](http://json.org/) format. The purpose of [WaveJSON](https://github.com/drom/wavedrom/wiki/WaveJSON) is to provide a compact exchange format for digital timing diagrams utilized by digital HW / IC engineers.

However, this great tool need either a headless web browser or node to generate documentations. Python being mainstream and cross-platform why not leverage its power?

This version is not a mere copy of the original one. The goals are to ensure the compatibility and to add new features. To name a few:
- long name for nodes for creating edges
- metastability wave
- analogue waveforms (step, capacitive step, slewing, arbitrary waves, overlay up to 4 waves)
- add annotations (global time compression, vertical/horizontal lines)
- style overloading (font-size, fill color, stroke color, stroke-width, stroke-dasharray, ...)

The inputs could be either json, WaveJSON (cson), yaml or toml while outputs would be svg, postscript, pdf, and png.

## License

See [LICENSE](https://github.com/drom/wavedrom/blob/master/LICENSE).
