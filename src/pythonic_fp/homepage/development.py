"""
Module Dependencies
===================

All non-typing related dependencies.
Arrows point from modules to their dependencies.

Internal to Pythonic FP
-----------------------

Dependencies between the Pythonic FP projects.

.. graphviz::

    digraph Modules {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba"];
        edge [color="#181616", fontcolor="#dcd7ba"];
        containers -> fptools;
        containers -> iterables;
        containers -> circulararray;
        splitends -> fptools;
        splitends -> iterables;
        splitends -> queues;
        queues -> fptools;
        queues -> circulararray;
        circulararray -> gadgets;
        fptools -> circulararray;
        fptools -> gadgets;
        fptools -> booleans;
        booleans -> gadgets;
        iterables -> gadgets;
        iterables -> fptools;
        numpy
    }

External to Pythonic FP
-----------------------

All Python external dependencies, except for typing related standard
library dependencies.

.. graphviz::

    digraph Modules {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba"];
        edge [color="#181616", fontcolor="#dcd7ba"];
        "pythonic_fp.booleans" -> threading;
        "pythonic_fp.gadgets" -> inspect;
        "pythonic_fp.gadgets" -> threading;
        "pythonic_fp.iterables" -> enum;
        "pythonic_fp.numpy" -> numpy;
    }

Semantic Versioning
===================

Pythonic FP Projects
--------------------

Maintainer has adopted strict 3 digit
`semantic versioning <https://semver.org>`_
and tries not put
`caps on dependencies <https://iscinumpy.dev/post/bound-version-constraints>`_
for library modules. Sometimes caps are necessary to prevent API changes
from leaking back to prior releases.

This allows for more package management flexibility for software
developers using these libraries, and provides easier access
to the latest features.

For individual Pythonic FP projects, the meanings of version numbers are

- **MAJOR:** incompatible API changes across all Pythonic FP projects
- **MINOR:** added API compatible functionality
- **PATCH:** incremented for backward compatible bug fixes and doc improvements

Homepage & Integrated Testing (pythonic-fp)
-------------------------------------------

The meanings for version numbers can change with paradigm shifts.
Currently they are

- **MAJOR:** for paradigm shifts
- **MINOR:** homepage changes, additional integration tests
- **PATCH:** typos, git/pypi thrashing, pure eye-candy

Changelog
=========

Pythonic FP overarching
`CHANGELOG <https://github.com/grscheller/pythonic-fp/blob/main/CHANGELOG.md>`_.

Each individual Pythonic FP project has its own CHANGELOG too.

Test suites
===========

Pytest based test suites are provided for unit and integration tests.
Remember to make any necessary dependency changes in pyproject.toml.

Unit test example
-----------------

Project is tested locally.

- clone say grscheller/pythonic-fp-circulararray GitHub repo
- uv lock --upgrade
- uv sync --group test
- uv run pytest

Integration tests
-----------------

All projects are installed from PyPI.

- clone the grscheller/pythonic-fp GitHub repo
- uv lock --upgrade
- uv sync --group test
- uv run pytest

Building documentation
======================

Both the Pythonic FP homepage and documentation for each project are
automatically built with GitHub actions on pushing to GitHub.
Documentation for the latest release and the next release currently in
development is built.

The Sphinx based documentation can also be built locally.

Build development docs locally
------------------------------

- clone say grscheller/pythonic-fp-fptools repo
- release information needs to be updated in 3 places

  - pyproject.toml
  - .github/workflows/static.yml
  - docs/Makefile

- uv lock --upgrade
- uv sync --group docs
- cd docs/
- uv run make devel
- docs are built in docs/build/html

Build homepage locally
----------------------

- clone the grscheller/pythonic-fp repo
- release information needs to be updated in 2 places

  - pyproject.toml
  - docs/source/conf.py

- uv lock --upgrade
- uv sync --group docs
- cd docs/
- uv run make html
- docs are built in docs/build/html

"""
