# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# 
# Must match what is in pyproject.toml, also update proposed_release accordingly
# when generating the docs for an actual, not proposed, release.
#

project = 'Pythonic FP'
copyright = '2023-2025, Geoffrey R. Scheller'
author = 'Geoffrey R. Scheller'
release = '3.2.2' 

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
