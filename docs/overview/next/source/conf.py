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
release = '3.0.0' 
title_string = 'Next Coordinated Release'
date_string = 'TBD'
# title_string = 'Coordinated Release'
# date_string = '2025-09-15'

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

html_theme = 'piccolo_theme'
html_static_path = ['_static']

rst_epilog = f"""
.. |RELEASE_STRING| replace::

    {title_string} - {release} ({date_string})
"""
