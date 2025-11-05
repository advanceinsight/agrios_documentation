# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'AgriOS'
copyright = '2025, Advance Insight'
author = 'Advance Insight'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    "myst_parser",           # enables Markdown
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'
# html_static_path = ["_static"]
# html_css_files = ["custom.css"]

# FURO CSS
# https://github.com/pradyunsg/furo/tree/main/src/furo/assets/styles/variables

html_theme_options = {
    "source_repository": "https://github.com/advanceinsight/agrios_documentation/",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "light_css_variables" : {
        "color-brand-primary" : "#6b6f76",
        "color-sidebar-caption-text" : "#458A77",
        "color-sidebar-brand-text" : "#458A77",
        "color-foreground-primary": "#458A77",
        "font-size-h1": "1.4rem",
        },
    "dark_css_variables" : {
        # "color-brand-primary" : "#e17f00"
        }
    }

# -- Options for EPUB output
epub_show_urls = 'footnote'
