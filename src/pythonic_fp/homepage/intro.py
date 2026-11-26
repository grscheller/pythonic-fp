"""
Pythonic FP is a collection of Python libraries to enable functional
programming paradigms in Python in a Pythonic way.

- These libraries work alongside

  - ordinary Python code
  - Python iterables
  - your type checkers

Install only the libraries you need. Each one brings along only the
Pythonic FP libraries it depends on.

Projects
--------

.. graphviz::

    digraph PythonicFP {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba",
              color="#181616", target="_top"];
        edge [color="#181616"];

        booleans      [URL="https://grscheller.github.io/pythonic-fp-booleans/",      tooltip="pythonic-fp-booleans"];
        circulararray [URL="https://grscheller.github.io/pythonic-fp-circulararray/", tooltip="pythonic-fp-circulararray"];
        containers    [URL="https://grscheller.github.io/pythonic-fp-containers/",    tooltip="pythonic-fp-containers"];
        fptools       [URL="https://grscheller.github.io/pythonic-fp-fptools/",       tooltip="pythonic-fp-fptools"];
        gadgets       [URL="https://grscheller.github.io/pythonic-fp-gadgets/",       tooltip="pythonic-fp-gadgets"];
        iterables     [URL="https://grscheller.github.io/pythonic-fp-iterables/",     tooltip="pythonic-fp-iterables"];
        fp_numpy      [label="numpy", URL="https://grscheller.github.io/pythonic-fp-numpy/", tooltip="pythonic-fp-numpy"];
        queues        [URL="https://grscheller.github.io/pythonic-fp-queues/",        tooltip="pythonic-fp-queues"];
        splitends     [URL="https://grscheller.github.io/pythonic-fp-splitends/",     tooltip="pythonic-fp-splitends"];

        numpy_pkg [label="NumPy (third party)", shape=box,
                   style="filled,dashed", fillcolor="#957fb8",
                   fontcolor="#181616", URL="https://numpy.org/",
                   tooltip="numpy"];

        containers    -> fptools;
        containers    -> iterables;
        containers    -> circulararray;
        splitends     -> fptools;
        splitends     -> iterables;
        splitends     -> queues;
        queues        -> fptools;
        queues        -> circulararray;
        fptools       -> circulararray;
        fptools       -> gadgets;
        fptools       -> booleans;
        circulararray -> gadgets;
        booleans      -> gadgets;
        iterables     -> gadgets;
        iterables     -> fptools;
        fp_numpy      -> numpy_pkg;
    }

Each oval is a Pythonic FP project, published on PyPI as
``pythonic-fp-<name>``. Each arrow points from a project to a project
it installs. Click a project to open its documentation.

.. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Project
      - Description
    * - `pythonic-fp-booleans <https://grscheller.github.io/pythonic-fp-booleans/>`_
      - Boolean-like singleton classes that compose with Python's bitwise
        operators as true Booleans, not as integers.
    * - `pythonic-fp-circulararray <https://grscheller.github.io/pythonic-fp-circulararray/>`_
      - Circular arrays with O(1) pushes and pops at either end, in
        auto-resizing and fixed-capacity versions.
    * - `pythonic-fp-containers <https://grscheller.github.io/pythonic-fp-containers/>`_
      - Containers with FP-inspired interfaces: a functional tuple and an
        immutable list.
    * - `pythonic-fp-fptools <https://grscheller.github.io/pythonic-fp-fptools/>`_
      - Functional programming tools: the ``MayBe``, ``Either`` and
        ``State`` monads, and lazy function evaluation.
    * - `pythonic-fp-gadgets <https://grscheller.github.io/pythonic-fp-gadgets/>`_
      - Small utility classes and functions, such as boxes, wrappers and
        sentinels, depending only on the standard library.
    * - `pythonic-fp-iterables <https://grscheller.github.io/pythonic-fp-iterables/>`_
      - Functions for concatenating, merging, dropping, taking, reducing
        and accumulating iterables.
    * - `pythonic-fp-numpy <https://grscheller.github.io/pythonic-fp-numpy/>`_
      - Hashable wrappers for read-only NumPy arrays.
    * - `pythonic-fp-queues <https://grscheller.github.io/pythonic-fp-queues/>`_
      - FIFO, LIFO and double-ended queues.
    * - `pythonic-fp-splitends <https://grscheller.github.io/pythonic-fp-splitends/>`_
      - Mutable LIFO stacks that can safely share data with each other.

Installation
------------

Pythonic FP requires Python 3.14 or later. Install each library you
need from PyPI, for example:

.. code-block:: console

    $ pip install pythonic-fp-fptools

Or, in a uv-managed project:

.. code-block:: console

    $ uv add pythonic-fp-fptools

.. note::

    Do not install the ``pythonic-fp`` package itself. It exists only
    to host this homepage and the integration tests.

Versioning
----------

All Pythonic FP projects share a major version number, currently 6,
and projects within the same major version work together. Constrain
each dependency to the current major version, for example
``pythonic-fp-fptools>=6.2,<7``. See :doc:`development` for the full
versioning policy.

Goals
-----

- Support both stateful and functional programming styles
- Be efficient, extensible and fully embrace Python 3.14+ typing
- Threadsafe when practical, thread tolerant otherwise
- Be Pythonic

Non-Goals
---------

- Try to make Python a pure functional language
- Implement a functional domain specific language in Python

"""
