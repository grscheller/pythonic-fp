#!/usr/bin/env python3
# Generate conf.py Sphinx configuration executable

import sys

project = 'Pythonic FP'
pypi_repo = 'pythonic-fp'
author = 'Geoffrey R. Scheller'
copyright = f'2023-2026, {author}'

args = sys.argv[1:]
if len(args) == 1:
    release = args[0]
else:
    sys.exit('Error: gen_conf.py takes exactly 1 argument')

release_string = f'**Current {project} rolling release**'

print(f'''# Generated conf.py Sphinx configuration executable

project = '{project}'
author = '{author}'
copyright = '{copyright}'
release = '{release}'
release_string = '{release_string}'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
]

autodoc_member_order = 'bysource'
autoclass_content = 'both'

templates_path = ['_templates']
exclude_patterns: list[str] = []

html_theme_options = {{
    'light_css_variables': {{
        'color-link--visited': 'var(--color-link)',
    }},
    'dark_css_variables': {{
        'color-link--visited': 'var(--color-link)',
    }},
}}
html_theme = 'furo'
html_static_path = ['_static']

''')
