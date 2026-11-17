# Generated conf.py Sphinx configuration executable

from importlib.metadata import version as installed_version

# from sphinx.application import Sphinx
# from sphinx.errors import ConfigError

# -- Project information -----------------------------------------------------

project = 'Pythonic FP - homepage'
author = 'Geoffrey R. Scheller'
copyright = f'2023-2026, {author}'
release = installed_version('pythonic-fp')

project = 'Pythonic FP'
author = 'Geoffrey R. Scheller'
copyright = '2023-2026, Geoffrey R. Scheller'
release = '6.1.0'
release_string = '**Current Pythonic FP rolling release**'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz',
]

templates_path = ['_templates']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Autodoc -----------------------------------------------------------------

autodoc_default_options = {
    'members': True,
    'special-members': True,
    'show-inheritance': True,
}
autodoc_member_order = 'bysource'
autodoc_class_signature = 'separated'
autodoc_docstring_signature = False
autodoc_preserve_defaults = True

# -- HTML output -------------------------------------------------------------

html_theme = 'furo'
html_theme_options = {
    'light_css_variables': {'color-link--visited': 'var(--color-link)'},
    'dark_css_variables': {'color-link--visited': 'var(--color-link)'},
}
html_static_path = ['_static']
