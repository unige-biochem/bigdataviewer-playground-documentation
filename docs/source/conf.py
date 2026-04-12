# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'BigDataViewer Playground Documentation'
copyright = '2026, Nicolas Chiaruttini'
author = 'Nicolas Chiaruttini'

release = '0.20.4'
version = '0.20.4'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx_search.extension',
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design',
]

# Source code links — update these two version strings when bumping the tracked release.
_bdvpg_version = "0.20.2"   # bigdataviewer-playground (sc.fiji.bdvpg.*)
_biop_bdv_tools_version  = "0.20.4"   # bigdataviewer-biop-tools  (ch.epfl.biop.*)
_bdv_image_loaders_version  = "0.20.1"   # bigdataviewer-biop-tools  (ch.epfl.biop.*)
_bdvpg_display_version = "0.20.0"
_ijp_kheops_version = "0.20.0"

extlinks = {
    "bdvpg-src": (
        f"https://github.com/bigdataviewer/bigdataviewer-playground/blob/"
        f"bigdataviewer-playground-{_bdvpg_version}/src/main/java/%s",
        "%s",
    ),
    "biop-src": (
        f"https://github.com/BIOP/bigdataviewer-biop-tools/blob/"
        f"bigdataviewer-biop-tools-{_biop_bdv_tools_version}/src/main/java/%s",
        "%s",
    ),
    "image-loaders-src": (
        f"https://github.com/BIOP/bigdataviewer-image-loaders/blob/"
        f"bigdataviewer-image-loaders-{_bdv_image_loaders_version}/src/main/java/%s",
        "%s",
    ),
    "image-loaders-src": (
        f"https://github.com/BIOP/bigdataviewer-playground-display/blob/"
        f"bigdataviewer-playground-display-{_bdvpg_display_version}/src/main/java/%s",
        "%s",
    ),
    "kheops-src": (
        f"https://github.com/BIOP/ijp-kheops/blob/"
        f"ijp-kheops-{_ijp_kheops_version}/src/main/java/%s",
        "%s",
    ),

}

# Copy button configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ |> "
copybutton_prompt_is_regexp = True

master_doc = "index"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = 'assets/img/bdv_logo.png'
html_theme_options = {
    'logo_only': True
}
html_static_path = ['_static']
html_js_files = ['js/external_links.js']

# -- Options for EPUB output
epub_show_urls = 'footnote'

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

source_suffix = ['.rst', '.md']

from pygments.lexer import RegexLexer, include
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation
import re

class ImageJMacroLexer(RegexLexer):
    """
    Pygments Lexer for ImageJ Macro files (.ijm).
    See https://imagej.nih.gov/ij/developer/macro/functions.html
    """

    name = 'ImageJ Macro'
    aliases = ['imagej', 'ijm', 'ijmacro']
    filenames = ['*.ijm']
    mimetypes = ['text/ijm']

    tokens = {
        'root': [
            # Whitespace and comments
            (r'\s+', Text),
            (r'//.*?$', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),

            # Script parameter annotations (ImageJ specific)
            (r'#@.*?$', Comment.Preproc),

            # Numbers
            (r'(\.\d+|[0-9]+\.[0-9]*)([eE][-+]?[0-9]+)?', Number.Float),
            (r'0[xX][0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),

            # Keywords
            (r'\b(for|in|while|do|return|if|else)\b', Keyword),
            (r'\b(var|macro|function)\b', Keyword.Declaration),
            (r'\b(true|false|NaN|PI)\b', Keyword.Constant),

            # Built-in functions (comprehensive list from ImageJ)
            (r'\b(Array\.concat|Array\.copy|Array\.fill|Array\.findMaxima|'
                r'Array\.findMinima|Array\.fourier|Array\.getSequence|'
                r'Array\.getStatistics|Array\.getVertexAngles|Array\.print|'
                r'Array\.rankPositions|Array\.resample|Array\.reverse|'
                r'Array\.rotate|Array\.show|Array\.slice|Array\.sort|Array\.trim|'
                r'Dialog\.addCheckbox|Dialog\.addCheckboxGroup|Dialog\.addChoice|'
                r'Dialog\.addHelp|Dialog\.addMessage|Dialog\.addNumber|'
                r'Dialog\.addRadioButtonGroup|Dialog\.addSlider|Dialog\.addString|'
                r'Dialog\.create|Dialog\.getCheckbox|Dialog\.getChoice|Dialog\.getNumber|'
                r'Dialog\.getRadioButton|Dialog\.getString|Dialog\.setInsets|Dialog\.setLocation|'
                r'Dialog\.show|Ext|File\.append|File\.close|File\.copy|File\.dateLastModified|'
                r'File\.delete|File\.directory|File\.exists|File\.getName|File\.getParent|File\.isDirectory|'
                r'File\.lastModified|File\.length|File\.makeDirectory|File\.name|'
                r'File\.nameWithoutExtension|File\.open|File\.openAsRawString|File\.openAsString|'
                r'File\.openDialog|File\.openUrlAsString|File\.rename|File\.saveString|File\.separator|'
                r'Fit\.doFit|Fit\.f|Fit\.getEquation|Fit\.logResults|Fit\.nEquations|Fit\.nParams|Fit\.p|'
                r'Fit\.plot|Fit\.rSquared|Fit\.showDialog|IJ\.currentMemory|IJ\.deleteRows|'
                r'IJ\.freeMemory|IJ\.getToolName|IJ\.log|IJ\.maxMemory|IJ\.pad|'
                r'IJ\.redirectErrorMessages|IJ\.renameResults|List\.clear|List\.get|List\.getList|'
                r'List\.getValue|List\.set|List\.setCommands|List\.setList|List\.setMeasurements|'
                r'List\.size|Overlay\.activateSelection|Overlay\.add|Overlay\.addSelection|'
                r'Overlay\.clear|Overlay\.copy|Overlay\.drawEllipse|Overlay\.drawLabels|'
                r'Overlay\.drawLine|Overlay\.drawRect|Overlay\.drawString|Overlay\.hidden|'
                r'Overlay\.hide|Overlay\.lineTo|Overlay\.measure|Overlay\.moveSelection|'
                r'Overlay\.moveTo|Overlay\.paste|Overlay\.remove|Overlay\.removeSelection|'
                r'Overlay\.setPosition|Overlay\.show|Overlay\.size|Plot\.add|Plot\.addText|Plot\.create|'
                r'Plot\.drawLine|Plot\.drawNormalizedLine|Plot\.drawVectors|Plot\.getLimits|'
                r'Plot\.getValues|Plot\.makeHighResolution|Plot\.setAxisLabelSize|'
                r'Plot\.setBackgroundColor|Plot\.setColor|Plot\.setFontSize|Plot\.setFormatFlags|'
                r'Plot\.setFrameSize|Plot\.setJustification|Plot\.setLegend|Plot\.setLimits|'
                r'Plot\.setLimitsToFit|Plot\.setLineWidth|Plot\.setLogScaleX|Plot\.setLogScaleY|'
                r'Plot\.setXYLabels|Plot\.show|Plot\.showValues|Plot\.update|Plot\.useTemplate|'
                r'Roi\.contains|Roi\.getBounds|Roi\.getCoordinates|Roi\.getDefaultColor|'
                r'Roi\.getFillColor|Roi\.getName|Roi\.getProperties|Roi\.getProperty|'
                r'Roi\.getSplineAnchors|Roi\.getStrokeColor|Roi\.getType|Roi\.move|Roi\.setFillColor|'
                r'Roi\.setName|Roi\.setPolygonSplineAnchors|Roi\.setPolylineSplineAnchors|'
                r'Roi\.setProperty|Roi\.setStrokeColor|Roi\.setStrokeWidth|'
                r'Stack\.getActiveChannels|Stack\.getDimensions|Stack\.getDisplayMode|'
                r'Stack\.getFrameInterval|Stack\.getFrameRate|Stack\.getOrthoViewsID|'
                r'Stack\.getPosition|Stack\.getStatistics|Stack\.getUnits|Stack\.isHyperstack|'
                r'Stack\.setActiveChannels|Stack\.setChannel|Stack\.setDimensions|'
                r'Stack\.setDisplayMode|Stack\.setFrame|Stack\.setFrameInterval|'
                r'Stack\.setFrameRate|Stack\.setOrthoViews|Stack\.setPosition|Stack\.setSlice|'
                r'Stack\.setTUnit|Stack\.setZUnit|Stack\.stopOrthoViews|Stack\.swap|String\.append|'
                r'String\.buffer|String\.copy|String\.copyResults|String\.getResultsHeadings|'
                r'String\.paste|String\.resetBuffer|String\.show|abs|acos|asin|atan|atan2|autoUpdate|'
                r'beep|bitDepth|calibrate|call|changeValues|charCodeAt|close|cos|d2s|'
                r'doCommand|doWand|drawLine|drawOval|drawRect|drawString|dump|endsWith|'
                r'eval|exec|exit|exp|fill|fillOval|fillRect|floodFill|floor|fromCharCode|getArgument|'
                r'getBoolean|getBoundingRect|getCursorLoc|getDateAndTime|getDimensions|'
                r'getDirectory|getDisplayedArea|getFileList|getFontList|getHeight|getHistogram|'
                r'getImageID|getImageInfo|getInfo|getLine|getList|getLocationAndSize|getLut|'
                r'getMetadata|getMinAndMax|getNumber|getPixel|getPixelSize|getProfile|'
                r'getRawStatistics|getResult|getResultLabel|getResultString|getSelectionBounds|'
                r'getSelectionCoordinates|getSliceNumber|getStatistics|getString|getStringWidth|'
                r'getThreshold|getTime|getTitle|getValue|getVersion|getVoxelSize|getWidth|'
                r'getZoom|imageCalculator|indexOf|is|isActive|isKeyDown|isNaN|isOpen|'
                r'lastIndexOf|lengthOf|lineTo|log|makeArrow|makeEllipse|makeLine|makeOval|'
                r'makePoint|makePolygon|makeRectangle|makeSelection|makeText|matches|'
                r'maxOf|minOf|moveTo|nImages|nResults|nSlices|newArray|newImage|newMenu|'
                r'open|parseFloat|parseInt|pow|print|random|rename|replace|requires|reset|'
                r'resetMinAndMax|resetThreshold|restoreSettings|roiManager|round|run|'
                r'runMacro|save|saveAs|saveSettings|screenHeight|screenWidth|selectImage|'
                r'selectWindow|selectionContains|selectionName|selectionType|setAutoThreshold|'
                r'setBackgroundColor|setBatchMode|setColor|setFont|setForegroundColor|'
                r'setJustification|setKeyDown|setLineWidth|setLocation|setLut|setMetadata|'
                r'setMinAndMax|setOption|setPasteMode|setPixel|setRGBWeights|setResult|'
                r'setSelectionLocation|setSelectionName|setSlice|setThreshold|setTool|'
                r'setVoxelSize|setZCoordinate|setupUndo|showMessage|'
                r'showMessageWithCancel|showProgress|showStatus|showText|sin|snapshot|'
                r'split|sqrt|startsWith|substring|tan|toBinary|toHex|toLowerCase|toScaled|toString|'
                r'toUnscaled|toUpperCase|toolID|updateDisplay|updateResults|wait|waitForUser)\b',
                Name.Builtin),

            # Strings
            (r'"([^"\\]|\\.)*"', String.Double),
            (r"'([^'\\]|\\.)*'", String.Single),

            # Operators
            (r'(\+\+|--|\+=|-=|\*=|/=|%=|&&|\|\||==|!=|<=|>=|[+\-*/%<>=!&|])', Operator),

            # Punctuation - THIS IS KEY to avoid red rectangles
            (r'[{}\[\]().,;:]', Punctuation),

            # Variables and identifiers
            (r'[a-zA-Z_]\w*', Name.Other),
        ]
    }

from pygments.lexers.jvm import GroovyLexer
from pygments.token import Comment
import re

class ImageJGroovyLexer(GroovyLexer):
    """
    Groovy lexer with support for SciJava/ImageJ script parameters (#@).
    """

    name = 'ImageJ Groovy'
    aliases = ['imagej-groovy']
    filenames = []

    def get_tokens_unprocessed(self, text):
        """
        Preprocess #@ lines as comments, then use normal Groovy lexing.
        """
        # Process the text line by line
        lines = text.split('\n')
        processed_lines = []

        for line in lines:
            # If line starts with #@ (with optional whitespace), treat as comment
            if re.match(r'^\s*#@', line):
                # Replace #@ with // to make it a valid Groovy comment
                processed_lines.append(re.sub(r'^(\s*)#@', r'\1//@', line))
            else:
                processed_lines.append(line)

        processed_text = '\n'.join(processed_lines)

        # Now tokenize with the parent Groovy lexer
        for index, token, value in GroovyLexer.get_tokens_unprocessed(self, processed_text):
            # Change //@  comments back to #@ in the output and mark as preprocessor
            if token == Comment.Single and value.lstrip().startswith('//@'):
                # Restore original #@ and mark as preprocessor directive
                yield index, Comment.Preproc, value.replace('//@', '#@', 1)
            else:
                yield index, token, value

def setup(app):
    app.add_lexer('imagej', ImageJMacroLexer)
    app.add_lexer('ijm', ImageJMacroLexer)
    app.add_lexer('ijmacro', ImageJMacroLexer)
    app.add_lexer('imagej-groovy', ImageJGroovyLexer)