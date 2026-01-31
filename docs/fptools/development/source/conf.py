# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
#
# Must match what is in pyproject.toml and top level index.rst.
#

project = 'Pythonic FP - Functional Programming Tools'
copyright = '2023-2026, Geoffrey R. Scheller'
author = 'Geoffrey R. Scheller'
release = '5.2.1+'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
]

autodoc_member_order = 'bysource'
autoclass_content = 'both'

templates_path = ['_templates']
exclude_patterns: list[str] = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme_options = {
    "light_css_variables": {
        "color-link--visited": "var(--color-link)",
    },
    "dark_css_variables": {
        "color-link--visited": "var(--color-link)",
    },
}
html_theme = 'furo'
html_static_path = ['_static']
