import json

# These tags where taken from dompurify
# START HTML NS

HTML_SE_TAGS = [
  'a',
  'abbr',
  'acronym',
  'address',
  'article',
  'aside',
  'audio',
  'b',
  'bdi',
  'bdo',
  'big',
  'blink',
  'blockquote',
  'button',
  'canvas',
  'caption',
  'center',
  'cite',
  'code',
  'col',
  'colgroup',
  'content',
  'data',
  'datalist',
  'dd',
  'decorator',
  'del',
  'details',
  'dfn',
  'dialog',
  'dir',
  'div',
  'dl',
  'dt',
  'element',
  'em',
  'fieldset',
  'figcaption',
  'figure',
  'font',
  'footer',
  'header',
  'hgroup',
  'i',
  'ins',
  'kbd',
  'label',
  'legend',
  'li',
  'main',
  'map',
  'mark',
  'marquee',
  'menu',
  'menuitem',
  'meter',
  'nav',
  'nobr',
  'ol',
  'optgroup',
  'option',
  'output',
  'p',
  'picture',
  'pre',
  'progress',
  'q',
  'rp',
  'rt',
  'ruby',
  's',
  'samp',
  'section',
  'select',
  'shadow',
  'small',
  'spacer',
  'span',
  'strike',
  'strong',
  'sub',
  'summary',
  'sup',
  'tbody',
  'td',
  'tfoot',
  'th',
  'thead',
  'time',
  'tr',
  'tt',
  'u',
  'ul',
  'var',
  'video',
  'h1',
  'h2',
  'h3',
  'h4',
  'h5',
  'h6',
  'template',
  'form'
];

HTML_SNG_TAGS = [
  'area',
  'hr',
  'img',
  'input',
  'source',
  'track',
  'wbr',
]


HTML_TABLE_TAGS = [
  'table',
  'tbody',
  'td',
  'tfoot',
  'th',
  'thead',
  'tr',
  'caption',
  'col',
  'colgroup',
]


HTML_TEXT_INT_TAGS = [
  'textarea',
  'style',
]

HTML_BOTH_TAGS = [
  'p',
  'br',
]


# START SVG NS

SVG_TAGS = [
  'svg',
  'a',
  'style',
  'altglyph',
  'altglyphdef',
  'altglyphitem',
  'animatecolor',
  'animatemotion',
  'animatetransform',
  'audio',
  'canvas',
  'circle',
  'clippath',
  'defs',
  'ellipse',
  'filter',
  'font',
  'g',
  'glyph',
  'glyphref',
  'hkern',
  'image',
  'line',
  'lineargradient',
  'marker',
  'mask',
  'metadata',
  'mpath',
  'path',
  'pattern',
  'polygon',
  'polyline',
  'radialgradient',
  'rect',
  'stop',
  'switch',
  'symbol',
  'text',
  'textpath',
  'tref',
  'tspan',
  'video',
  'view',
  'vkern',
];

SVG_INT_HTML_TAGS = [
  'title',
  'desc',
  #'foreignObject',
]

SVG_FILTER_TAGS = [
  'feBlend',
  'feColorMatrix',
  'feComponentTransfer',
  'feComposite',
  'feConvolveMatrix',
  'feDiffuseLighting',
  'feDisplacementMap',
  'feDistantLight',
  'feFlood',
  'feFuncA',
  'feFuncB',
  'feFuncG',
  'feFuncR',
  'feGaussianBlur',
  'feMerge',
  'feMergeNode',
  'feMorphology',
  'feOffset',
  'fePointLight',
  'feSpecularLighting',
  'feSpotLight',
  'feTile',
  'feTurbulence',
];

MATH_MAIN_TAG = ['svg'];

# START MATH NS


MATH_TAGS = [
  #'math',
  'menclose',
  'merror',
  'mfenced',
  'mfrac',
  'mlabeledtr',
  'mmultiscripts',
  'mover',
  'mpadded',
  'mphantom',
  'mroot',
  'mrow',
  'mspace',
  'msqrt',
  'mstyle',
  'msub',
  'msup',
  'msubsup',
  'mtable',
  'mtd',
  'mtr',
  'munder',
  'munderover',
];

MATH_MAIN_TAG = ['math'];


MATH_INT_HTML_TAGS = [
  'mi',
  'mo',
  'mn',
  'ms',
  'mtext',
]

MATH_DEINT_HTML_TAGS = [
  'mglyph'
]

def install(name,data):
    f = open(f"tags/{name}","w")
    f.write(json.dumps(data))
    f.close()

HTML = {"nstag":'html',"single":HTML_SNG_TAGS, "double":HTML_SE_TAGS,"both":HTML_BOTH_TAGS,"special":{"table":HTML_TABLE_TAGS,"text":HTML_TEXT_INT_TAGS}}
install('html',HTML)

MATHML = {"nstag":'math',"single":[],"double":MATH_TAGS,"both":[],"special": {"math2html": MATH_INT_HTML_TAGS, "html2math":MATH_DEINT_HTML_TAGS} }
install('math',MATHML)

SVG = {"nstag":'svg',"single":[],"double":SVG_TAGS.extend(SVG_FILTER_TAGS),"both":[],"special":{"svg2html":SVG_INT_HTML_TAGS}}
install('svg',SVG)
