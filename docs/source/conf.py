# Sphinx conf.py configuration file

from importlib.metadata import version as installed_version

# -- Project information -----------------------------------------------

project = 'Pythonic FP - homepage'
author = 'Geoffrey R. Scheller'
copyright = f'2023-2026, {author}'
release = installed_version('pythonic-fp')

# -- General configuration ---------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
]

templates_path = ['_templates']

graphviz_output_format = 'svg'

# -- Autodoc -----------------------------------------------------------

autodoc_default_options = {
    'members': True,
    'special-members': True,
    'show-inheritance': True,
}
autodoc_member_order = 'bysource'
autodoc_class_signature = 'separated'
autodoc_docstring_signature = False
autodoc_preserve_defaults = True

# -- HTML output -------------------------------------------------------

html_title = f'{project} {release}'
html_theme = 'furo'
html_theme_options = {
    'light_css_variables': {'color-link--visited': 'var(--color-link)'},
    'dark_css_variables': {'color-link--visited': 'var(--color-link)'},
}
html_static_path = ['_static']
