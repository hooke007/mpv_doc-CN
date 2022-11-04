# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'mpv_doc-CN'
copyright = '2022, hooke007'
author = 'hooke007'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_copybutton',
    #'sphinx.ext.autosectionlabel',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    '.txt': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_options = {
    "light_css_variables": {
        "color-background-primary": "#FFFBE8",
        "color-highlight-on-target": "#007ACC",
        "color-toc-background": "#F5F5F5",
        "color-toc-item-text": "#646776",
    },
}

html_title = 'mpv_CFanStation'
html_logo = 'html_logo.png'
html_favicon = 'html_favicon.png'
html_static_path = ['_static']
