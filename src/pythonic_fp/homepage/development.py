"""
Development Practices
=====================

The only supported version of the Pythonic FP projects will be the ones
with the same top level major release numbers.

Documentation for each Pythonic FP project will be generated on GH-Pages
for the current top level PyPI release, the last top level PyPi release
of the previous rolling release series, and proposed documentation for
the next PyPI release from the main GitHub branch.

Module Dependencies
-------------------

All non-typing related dependencies.
Arrows point from modules to their dependencies.

Internal to Pythonic FP
~~~~~~~~~~~~~~~~~~~~~~~

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
        numpy;
    }

External to Pythonic FP
~~~~~~~~~~~~~~~~~~~~~~~

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

Semantic Versioning and Rolling Releases
----------------------------------------

For the individual projects strict 3 digit semantic versioning
has been adopted, see `semantic versioning <https://semver.org>`_
and to avoid putting
`caps on dependencies <https://iscinumpy.dev/post/bound-version-constraints>`_
for library modules. Sometimes caps are necessary to prevent API
changes from leaking back to prior releases. No caps are used for
external dependencies.

To accomplish this, a series of rolling releases ``>=X.0.0,<X+1`` for
each Pythonic FP project will be used. The over all effort, pythonic-fp,
will also use the same three digit semantic versioning.

- **MAJOR** for incompatible API changes across the projects
- **MINOR** for backward compatible added functionality
- **PATCH** incremented for backward compatible bug fixes

All projects libraries and the overall effort will share the same
``MAJOR`` release number to indicate a rolling release series.
Changes in ``MAJOR`` will provide opportunities for breaking API changes
based on lessons learned from library use.

This allows for more package management flexibility for software
developers using these libraries, and provides easier access
to the latest features.

Changelog
---------

Pythonic FP overarching
`CHANGELOG <https://github.com/grscheller/pythonic-fp/blob/main/CHANGELOG.md>`_.

Each individual Pythonic FP project has its own CHANGELOG too.

Test suites
-----------

Pytest based test suites are provided for unit and integration tests.
Each project has its own pytest based unit test suite. Integrated tests
are provided by the pythonic-fp project itself.

Any necessary dependency changes are made in pyproject.toml.

Unit test example
~~~~~~~~~~~~~~~~~

Test one project locally.

Clone the Pythonic FP fptools GitHub repo and its dependency repos in
the same parent directory.

  - grscheller/pythonic-fp-fptools
  - grscheller/pythonic-fp-booleans
  - grscheller/pythonic-fp-circulararray
  - grscheller/pythonic-fp-gadgets

Then,

.. code-block:: console

   $ cd pythonic-fp-fptools/
   $ uv lock --upgrade
   $ uv sync --group test
   $ uv run pytest

Integration tests
~~~~~~~~~~~~~~~~~

Clone the grscheller/pythonic-fp GitHub repo and all the Pythonic FP
projects all in the same parent directory.

.. code-block:: console

   $ cd pythonic-fp/
   $ uv lock --upgrade
   $ uv sync --group test
   $ uv run pytest

Building documentation
----------------------

Both the Pythonic FP homepage and documentation for each project are
automatically built with GitHub actions on pushing to GitHub.
Documentation for the latest release and the next release currently in
development is built.

The Sphinx based documentation can also be built locally.

Build development docs locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone say the ``grscheller/pythonic-fp-fptools`` repo. Release
information needs to be updated in ``docs/Makefile``.

.. code-block:: console

   $ cd pythonic-fp-fptools
   $ uv lock --upgrade
   $ uv sync --group docs
   $ cd docs/
   $ uv run make devel

Docs are built in ``docs/build/html``.

Build homepage locally
~~~~~~~~~~~~~~~~~~~~~~

Clone ``grscheller/pythonic-fp``. Release information needs to be
updated in the ``docs/source/conf.py`` and be consistent with the last
PyPI pythonic-fp release.

.. code-block:: console

   $ cd pythonic-fp
   $ uv lock --upgrade
   $ uv sync --group docs
   $ cd docs/
   $ uv run make homepage

Docs are built in ``docs/build/``.

Documentation builds use Sphinx from the docs dependency group. The
simplest way to build locally is ``uv run make -C docs homepage``,
which creates the environment for you. Any environment with the docs
group installed will work; ``make`` will error out if sphinx-build
is not on the PATH.

View docs locally
~~~~~~~~~~~~~~~~~

To view either the development docs or Pythonic FP homepage.

  - from docs/ directory: ``$ python -m http.server 8080 -d build``
  - go to in browser: ``http://localhost:8080/``

"""
