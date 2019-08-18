#!/usr/bin/env python3

"""
This define the style of the drawing
it follows the principle of the css but accept only a subset:
font: size, style, variant, weight, stretch, align, family
fill: color, opacity
stroke: color, width, opacity, linecap, linejoin, mitterlimit, dasharray, opacity

colors should always be in rgba with value from 0—255
"""
from enum import Enum

class Engine(Enum):
    SVG   = 0,
    EPS   = 1,
    CAIRO = 2

class SizeUnit(Enum):
    EM = 16
    PX = 1
    PT = 1.333

class LineCap(Enum):
    BUTT   = 0,
    ROUND  = 1,
    SQUARE = 2

class LineJoin(Enum):
    MITER = 0, 
    ROUND = 1, 
    BEVEL = 2

class TextAlign(Enum):
    LEFT    = 0,
    CENTER  = 1,
    RIGHT   = 2,
    JUSTIFY = 3

# style definition for cairo renderer
DEFAULT_STYLE = {
    "title": {
        "fill"        : (0, 65, 196, 255),
        "font-weight" : 500,
        "font-size"   : (0.9, SizeUnit.EM),
        "font-family" : "monospace",
        "text-align"  : TextAlign.RIGHT
    },
    "text": {
        "fill"        : (0, 0, 0, 255),
        "font-size"   : (0.9, SizeUnit.EM),
        "font-style"  : "normal",
        "font-variant": "normal",
        "font-weight" : 500,
        "font-stretch": "normal",
        "text-align"  : TextAlign.CENTER,
        "font-family" : "monospace"
    },
    "path": {
        "fill": None,
        "stroke": (0, 0, 0, 255),
        "stroke-width": 1,
        "stroke-linecap": LineCap.ROUND,
        "stroke-linejoin": LineJoin.MITER,
        "stroke-miterlimit": 4,
        "stroke-dasharray": None
    },
    "stripe": {
        "fill": None,
        "stroke": (0, 0, 0, 255),
        "stroke-width": 0.5,
        "stroke-linecap": LineCap.ROUND,
        "stroke-linejoin": LineJoin.MITER,
        "stroke-miterlimit": 4,
        "stroke-dasharray": None
    },
    "data": {
        "text-anchor": "middle",
        "dominant-baseline": "middle",
        "alignment-baseline": "central"
    },
    "arrow": {
        "fill": (0, 0, 0, 255),
        "stroke": None
    },
    "hide": {
        "fill": (255, 255, 255, 255),
        "stroke-width": 2
    },
    "s0": {
        "fill": None,
        "stroke": (0, 0, 0, 255),
        "stroke-width": 1,
        "stroke-linecap": LineCap.ROUND,
        "stroke-linejoin": LineJoin.MITER,
        "stroke-miterlimit": 4,
        "stroke-dasharray": None
    },
    "s1": {
        "fill": None,
        "stroke": (0, 0, 0, 255),
        "stroke-width": 1,
        "stroke-linecap": LineCap.ROUND,
        "stroke-linejoin": LineJoin.MITER,
        "stroke-miterlimit": 4,
        "stroke-dasharray": None
    },
    "s2 > polygon": {
        "fill": (0, 0, 0, 0),
        "stroke": None
    },
    "s3 > polygon": {
        "fill": (255, 255, 176, 255),
        "stroke": None
    },
    "s4 > polygon": {
        "fill": (255, 224, 185, 255),
        "stroke":None
    },
    "s5 > polygon": {
        "fill": (185, 224, 255, 255),
        "stroke": None
    },
    "ticks": {
        "stroke": (136, 136, 136, 255),
        "stroke-width": 0.5,
        "stroke-dasharray": [1, 3]
    },
    "edge": {
        "fill": None,
        "stroke": (0, 0, 255, 255),
        "stroke-width": 1
    },
    "edge-arrowhead": {
        "marker-start": "#arrow",
        "overflow": "visible"
    },
    "edge-arrowtail": {
        "marker-end": "#arrow",
        "overflow": "visible"
    },
    "edge-text": {
        "font-size": (0.625, SizeUnit.EM),
        "filter": "#solid",
        "transform": "translate(0, 2.5px)"
    },
    "border": {
        "stroke-width": 1.25,
        "stroke": (0, 0, 0, 255)
    },
    "h1": {
        "fill": (0, 0, 0, 255),
        "font-size": (18.31, SizeUnit.PX),
        "font-weight": "bold",
        "font-family" : "monospace",
        "text-align"  : TextAlign.LEFT
    },
    "h2": {
        "fill": (0, 0, 0, 255),
        "font-size": (14.65, SizeUnit.PX),
        "font-weight": "bold",
        "font-family" : "monospace",
        "text-align"  : TextAlign.LEFT
    },
    "h3": {
        "fill": (0, 0, 0, 255),
        "font-size": (11.72, SizeUnit.PX),
        "font-weight": "bold",
        "font-family" : "monospace",
        "text-align"  : TextAlign.LEFT
    },
    "h4": {
        "fill": (0, 0, 0, 255),
        "font-size": (9.38, SizeUnit.PX),
        "font-weight": "bold",
        "font-family" : "monospace",
        "text-align"  : TextAlign.LEFT
    },
    "h5": {
        "fill": (0, 0, 0, 255),
        "font-size": (7.5, SizeUnit.PX),
        "font-weight": "bold",
        "font-family" : "monospace",
        "text-align"  : TextAlign.LEFT
    },
    "h6": {
        "fill": (0, 0, 0, 255),
        "font-size": (6, SizeUnit.PX),
        "font-weight": "bold",
        "font-family" : "monospace",
        "text-align"  : TextAlign.LEFT
    }
}

# default style for the SvgRenderer
DEFAULT = """
text{font-size:0.9em;
    font-style:normal;
    font-variant:normal;
    font-weight:500;
    font-stretch:normal;
    text-align:center;
    fill-opacity:1;
    font-family:fira mono, droid sans mono, monospace;}
.muted{fill:#aaa}
.warning{fill:#f6b900}
.error{fill:#f60000}
.info, .title{fill:#0041c4}
.success{fill:#00ab00}
.attr{font-size:9px;}
.h1{font-size:18.31px;font-weight:bold}
.border{stroke-width: 1.25px; stroke: #000}
.h2{font-size:14.65px;font-weight:bold}
.h3{font-size:11.72px;font-weight:bold}
.h4{font-size:9.38px;font-weight:bold}
.h5{font-size:7.50px;font-weight:bold}
.h6{font-size:6px;font-weight:bold}
.s0, .s1, .path{fill:none;
    stroke:#000;
    stroke-width:1;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:none}
.stripe{fill:none;
    stroke:#000;
    stroke-width:0.5;
    stroke-linecap:round;
    stroke-linejoin:miter;
    stroke-miterlimit:4;
    stroke-opacity:1;
    stroke-dasharray:none}
.arrow{fill:#000000;fill-opacity:1;stroke:none}
.hide{fill:#ffffff;fill-opacity:1;stroke:2}
.s3 > polygon {fill:#ffffb4;fill-opacity:1,stroke:none}
.s4 > polygon {fill:#ffe0b9;fill-opacity:1,stroke:none}
.s5 > polygon {fill:#b9e0ff;fill-opacity:1,stroke:none}
.ticks {stroke: rgb(136, 136, 136); stroke-width: 0.5; stroke-dasharray: 1,3;}
.edges {fill:none;stroke:#00F;stroke-width:1}
.edges.arrowhead {marker-start:url(#arrow); overflow:visible;}
.edges.arrowtail {marker-end:url(#arrow); overflow:visible;}
.edges + text {font-size:0.625em; filter: url(#solid); transform: translate(0, 2.5px);}
"""

DEFINITION = """
<defs>
    <pattern id="diagonalHatch" width="5" height="5" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
        <line x1="0" y1="0" x2="0" y2="5" style="stroke:black; stroke-width:1" />
    </pattern>
    <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5"
        markerWidth="7" markerHeight="7" markerUnits="userSpaceOnUse"
        orient="auto-start-reverse" style="fill:#00F;">
      <path d="M 0 0 L 10 5 L 0 10 z" />
    </marker>
    <filter x="0" y="0" width="1" height="1" id="solid">
      <feFlood flood-color="white"/>
      <feComposite in="SourceGraphic"/>
    </filter>
</defs>
"""

try:
    import cairo
except ImportError:
    print("Cairo is not installed and cannot be used")
else:
    def apply_cairo_style(context, name: str):
        style = get_style(name)
        apply_cairo_font(context, style)
        apply_cairo_fill(context, style)
        apply_cairo_stroke(context, style)
        
    def apply_cairo_fill(context, style: dict):
        # color
        t = style.get("fill", None)
        if not t is None:
            r, g, b, a = t
            context.set_source_rgba(r/255, g/255, b/255, a/255)
    
    def apply_cairo_stroke(context, style: dict):
        # color
        t = style.get("stroke", None)
        if not t is None:
            r, g, b, a = t
            context.set_source_rgba(r/255, g/255, b/255, a/255)
        # width
        w = style.get("stroke-width", 1.0)
        if not w is None:
            context.set_line_width(w)
        # line cap
        lc = style.get("stroke-linecap", LineCap.ROUND)
        if lc == LineCap.SQUARE:
            context.set_line_cap(cairo.LINE_CAP_SQUARE)
        elif lc == LineCap.BUTT:
            context.set_line_cap(cairo.LINE_CAP_BUTT)
        else:
            context.set_line_cap(cairo.LINE_CAP_ROUND)
        # line join
        lj = style.get("stroke-linejoin", LineJoin.MITER)
        if lj == LineJoin.BEVEL:
            context.set_line_join(cairo.LINE_JOIN_BEVEL)
        elif lj == LineJoin.ROUND:
            context.set_line_join(cairo.LINE_JOIN_ROUND)
        else:
            context.set_line_join(cairo.LINE_JOIN_MITER)
        # dash array
        da = style.get("stroke-dasharray", [])
        of = style.get("stroke-dasharray-offset", 0)
        if of is None:
            of = 0
        if da:
            context.set_dash(da, of)

    def cairo_text_align(context, style: dict, text: str):
        text_align = style.get("text-align", TextAlign.CENTER)
        # get text width
        xbearing, ybearing, width, height, xadvance, yadvance = context.text_extents(text)
        # apply style
        if text_align == TextAlign.LEFT:
            return (0, 0)
        elif text_align == TextAlign.RIGHT:
            return (width, 0)
        else:
            return (width/2, 0)

    def apply_cairo_font(context, style: dict):
        # font slant
        font_style  = style.get("font-style", "")
        if "it" in font_style:
            font_style = cairo.FONT_SLANT_ITALIC
        elif "ob" in font_style:
            font_style = cairo.FONT_SLANT_OBLIQUE
        else:
            font_style = cairo.FONT_SLANT_NORMAL
        # normal or bold
        w = style.get("font-weight", 200)
        if isinstance(w, str) and "bold" in w:
            font_weight = cairo.FONT_WEIGHT_BOLD
        elif isinstance(w, int) and w > 400:
            font_weight = cairo.FONT_WEIGHT_BOLD
        else:
            font_weight = cairo.FONT_WEIGHT_NORMAL
        # fetch font family
        font_family = style.get("font-family", None)
        if not font_family is None and isinstance(font_family, str):
            context.select_font_face(font_family, font_style, font_weight)
        # font size
        font_size = style.get("font-size", None)
        if not font_size is None:
            s, u = font_size
            context.set_font_size(s*u.value)

def apply_style(context, name: str, engine: Engine):
    if engine in [Engine.SVG, Engine.EPS]:
        # not yet implemented for eps and not needed for SVGRenderer
        pass
    elif engine == Engine.CAIRO:
        apply_cairo_style(context, name)
    else:
        raise "Engine selected is not yet supported"

def apply_fill(context, name: str, engine: Engine):
    if engine == Engine.CAIRO:
        apply_cairo_fill(context, get_style(name))

def apply_stroke(context, name: str, engine: Engine):
    if engine == Engine.CAIRO:
        apply_cairo_stroke(context, get_style(name))

def apply_font(context, name: str, engine: Engine):
    if engine == Engine.CAIRO:
        apply_cairo_font(context, get_style(name))

def get_style(name: str) -> dict:
    selectors = DEFAULT_STYLE.keys()
    if name in selectors:
        return DEFAULT_STYLE.get(name, {})
    else:
        return DEFAULT_STYLE.get(name.split(' ')[0], {})

def text_align(context, name: str, text: str, engine: Engine):
    if engine == Engine.CAIRO:
        return cairo_text_align(context, get_style(name), text)