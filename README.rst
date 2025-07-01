***********************************
PyPI Pythonic FP Namespace Projects
***********************************

Collection of Functional Programming (FP) oriented Python libraries. This collection consists of
Python packages packaged as PyPI projects all under the ``pythonic-fp`` namespace. While taking
a functional programming approach, these packages endeavor to remain Pythonic.

Pythonic FP Projects:
=====================

+---------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Python Package            | Project on PyPI                                                                   | Source Code on GitHub                                                                  |
+===========================+===================================================================================+========================================================================================+
| pythonic_fp.circulararray | `pythonic-fp.circulararray <https://pypi.org/project/pythonic-fp.circulararray>`_ | `pythonic-fp-circulararray <https://github.com/grscheller/pythonic-fp-circulararray>`_ |
+---------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| pythonic_fp.containers    | `pythonic-fp.containers <https://pypi.org/project/pythonic-fp.containers>`_       | `pythonic-fp-containers <https://github.com/grscheller/pythonic-fp-containers>`_       |
+---------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| pythonic_fp.fptools       | `pythonic-fp.fptools <https://pypi.org/project/pythonic-fp.fptools>`_             | `pythonic-fp-fptools <https://github.com/grscheller/pythonic-fp-fptools>`_             |
+---------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| pythonic_fp.iterables     | `pythonic-fp.iterables <https://pypi.org/project/pythonic-fp.iterables>`_         | `pythonic-fp-iterables <https://github.com/grscheller/pythonic-fp-iterables>`_         |
+---------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| pythonic_fp.queues        | `pythonic-fp.queues <https://pypi.org/project/pythonic-fp.queues>`_               | `pythonic-fp-queues <https://github.com/grscheller/pythonic-fp-queues>`_               |
+---------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| pythonic_fp.splitends     | `pythonic-fp.splitends <https://pypi.org/project/pythonic-fp.splitends>`_         | `pythonic-fp-splitends <https://github.com/grscheller/pythonic-fp-splitends>`_         |
+---------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

Overview
========

Circular Array
--------------

Python module implementing a stateful circular array data structure.

- O(1) pops either end
- O(1) amortized pushes either end
- O(1) indexing, fully supports slicing
- Auto-resizing larger when necessary, manually compatible
- Iterable, can safely mutate while iterators continue iterating over previous state

Containers
----------

Python package implementing container-like classes.

- Single item box: holds at most one item of a given type, invariant in its contents
- Functional tuple: subclassed tuple, designed to be further inherited from, more FP interface
- Immutable list: hashability enforced when instantiated, mutable methods return new objects
- Maybe monad: data structure represents a possibly missing value
- Either monad: left biased, represents a "left" or "right" value, never both

FP Tools
--------

Modules aiding in Functional programming. TODO: break apart to separate repos

- Subclassable boolean: Python bool cannot be subclassed, this on can
- Functions as first class objects: utilities to manipulate and partially apply functions
- Lazy function evaluation: non-strict function evaluation
- Singletons: three singleton classes representing

  - a missing value (actually missing, not potentially missing)
  - sentinel values
  - failed calculations

- The State monad

Tools for Iterables
-------------------

- merging iterables
- dropping and taking values from iterables
- accumulating and reducing iterables

Queues
------

Data structures restricting developer to algorithmic use cases.

- FIFOQueue: First-In-First-Out Queue
- LIFOQueue: Last-In-First-Out Queue
- DEQueue: Double-Ended Queue

Splitends
---------

A singularly linked data structures allowing data sharing between multiple instances.

Pythonic FP
===========

The overall project's name is **Pythonic FP** and consists of Python packages packaged as PyPI
projects all under the ``pythonic-fp`` namespace.

There is a PyPI project with the name ``pythonic-fp``. It is a stub PyPI project whose sole purpose
is to reserve the ``pythonic-fp`` name on PyPI. It is **NOT TO BE INSTALLED**. It is there to
prevent others claiming the name and causing confusion. Installing it will break all ``pythonic-fp``
namespace projects. Its source code is located under the ``name_claim/`` directory.

Pythonic FP is a hobby project, but the maintainer is serious about its quality.

Credits:
--------

+-----------------------------------------------+----------------------+--------------------+
| Contributors                                  | Name                 | Role               |
+===============================================+======================+====================+
| `grscheller <https://github.com/grscheller>`_ | Geoffrey R. Scheller | author, maintainer |
+-----------------------------------------------+----------------------+--------------------+

License Information
===================

This repo itself, as well as all other Pythonic FP namespace projects,
are licensed under the Apache License Version 2.0, January 2004.

- See the `LICENCE file <https://github.com/grscheller/pythonic-fp/blob/main/LICENSE>`_
  for details.
- See the `CHANGELOG <https://github.com/grscheller/pythonic-fp/blob/main/CHANGELOG.rst>`_
  for ongoing changes.
