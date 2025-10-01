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

project = 'Pythonic FP - Functional Programming Tools'
copyright = '2023-2025, Geoffrey R. Scheller'
author = 'Geoffrey R. Scheller'
release = '5.1.3'
release_string = 'Proposed PyPI'
# release_string = 'PyPI'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns: list[str] = []

# -- Options for Sphinx
autoclass_content = 'both'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'
html_static_path = ['_static']

rst_epilog = f"""
.. |VERSION_RELEASED| replace:: version {release}

.. |RELEASE_STRING| replace:: {release_string}
"""
