# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# 
# Must match what is in pyproject.toml, also update proposed_release_string accordingly
# when generating the docs for an actual, not proposed, release.
#

project = 'Pythonic FP - Containers'
copyright = '2023-2025, Geoffrey R. Scheller'
author = 'Geoffrey R. Scheller'
release = '2.1.0' 
# proposed_release_string = 'a proposed'
proposed_release_string = 'the'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
exclude_patterns: list[str] = []

# -- Options for Sphinx
autoclass_content = 'both'

# -- Options for sphinx_autodoc_typehints
always_use_bars_union = True
typehints_fully_qualified = False
always_document_param_types = True
typehints_use_rtype = True
simplify_optional_unions = False
typehints_document_rtype_none = True
typehints_use_signatures = True
typehints_use_signatures_return = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'
html_static_path = ['_static']

rst_epilog = f"""
.. |VERSION_RELEASED| replace:: v{release}

.. |PROPOSED_RELEASE_STRING| replace:: {proposed_release_string}
"""
