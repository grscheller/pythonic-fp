# Copyright 2023-2025 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Pythonic FP projects
====================

Developer Tools supporting a functional style of programming yet endeavoring to
remain Pythonic. All project names begin ``pythonic-fp-`` on PyPI and are Python
namespace packages under the ``pythonic_fp`` name.

For the complete list of all available pythonic-fp on PyPI, see the
`README.md
<https://github.com/grscheller/pythonic-fp/blob/main/README.md>`_
file from the grscheller/pythonic-fp GitHub repo.

Semantic versioning
-------------------

Maintainer has adopted strict 3 digit semantic versioning and does not
use caps on dependencies. See `Semantic Versioning 2.0.0 <https://semver.org>`_.

Periodically coordinated versions of compatible releases will be posted in the
`CHANGELOG <https://github.com/grscheller/pythonic-fp/blob/main/CHANGELOG.rst>`_.

See below for the last coordinated release.

Latest coordinated release - 2025-09-15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------+---------------------------+---------+---------------------------+
| Name           | PyPI Project              | version | Python Module             |
+================+===========================+=========+===========================+
| Booleans       | pythonic-fp-booleans      | 1.1.2   | pythonic_fp.booleans      |
+----------------+---------------------------+---------+---------------------------+
| Circular Array | pythonic-fp-circulararray | 5.3.2   | pythonic_fp.circulararray |
+----------------+---------------------------+---------+---------------------------+
| Containers     | pythonic-fp-containers    | 3.0.1   | pythonic_fp.containers    |
+----------------+---------------------------+---------+---------------------------+
| FP Tools       | pythonic-fp-fptools       | 5.1.1   | pythonic_fp.fptools       |
+----------------+---------------------------+---------+---------------------------+
| Gadgets        | pythonic-fp-gadgets       | 3.0.1   | pythonic_fp.gadgets       |
+----------------+---------------------------+---------+---------------------------+
| Iterables      | pythonic-fp-iterables     | 5.1.1   | pythonic_fp.iterables     |
+----------------+---------------------------+---------+---------------------------+
| Sentinels      | pythonic-fp-sentinels     | 2.1.0   | pythonic_fp.sentinels     |
+----------------+---------------------------+---------+---------------------------+
| Splitends      | pythonic-fp-splitends     | 1.0.2   | pythonic_fp.splitends     |
+----------------+---------------------------+---------+---------------------------+

PyPI pythonic-fp project descriptions
-------------------------------------

Pythonic FP: pythonic_fp.overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PyPI pythonic-fp project has several purposes.

- claims the pythonic-fp name on PyPI for the overall effort
- hosts a homepage on GitHub Pages
- hosts detailed Sphinx based documentation for each pythonic_fp project

The pythonic_fp.overview is used to document the overall effort. There is
no need to install it, but does not hurt anything if it is installed.

----

Booleans: pythonic_fp.booleans
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Boolean type classes which interact well with Python's boolean
infrastructure.

- class **SBool:** Python's bool cannot be inherited from, this one can be
- class **FBool:** Family of booleans with different "flavors" of truth
- class **TF_Bool:** A Boolean whose truthy and falsy values are distinct subclasses

----

Circular Array: pythonic_fp.circulararray
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stateful circular array data structures.

- O(1) pushes and pops either end
- comparisons compare identity before equality, like builtins do
- iterable and reverse iterable

  - can safely be mutated while previous iterators iterate over previous state

Two types

- variable storage capacity

  - O(1) pops either end
  - O(1) amortized pushes either end
  - O(1) indexing, fully supports slicing
  - truthy if not empty
  - Auto-resizing larger storage capacity when necessary
  - manually compatible

- fixed storage capacity

  - O(1) pushes and pops either end
  - O(1) indexing, does not support slicing
  - truthy if not empty or at capacity

Both types can be safely mutated while previous iterators continue to
leisurely iterate over previous state. Comparisons compare identity
before equality, like builtin do.

----

Containers: pythonic_fp.containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python package of container like data structures.

- *FTuple:* tuple-like object with a more FP interface
- *IList:* immutable list where hashability is enforced at runtime

----

FP Tools: pythonic_fp.fptools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Functional programming library for Python.

This library implements tools to aid in Python functional programming
in a way which endeavors to remain Pythonic.

----

Gadgets: pythonic_fp.gadgets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The gadgets package is intended for **simple tools** with minimal
dependencies that may have multiple locations, or no good location,
to where they can go.

----

Tools for Iterables - pythonic_fp.iterables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tools for creating iterators from iterables.

- Concatenating and merging iterables
- Dropping and taking values from iterables
- Reducing and accumulating iterables

----

Queues - pythonic_fp.queues
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Queue classes

- supports queue based algorithms

  - without having to "bit fiddle" the underlying data structures

----

Sentinels - pythonic_fp.sentinels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Singleton classes **DEPRECATED**

- All code migrated to the Gadgets project.

----

Splitends - pythonic_fp.splitends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The splitends package implements a singularly linked LIFO queue called
a ``SplitEnd``. These data structures can safely share data nodes
between themselves and form branching *hair-like* graphs.

Module dependencies
-------------------

Future version. TODO: update to this version

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
        bool -> gadgets;
        iterables -> gadgets;
        iterables -> fptools;
    }

"""

__author__ = 'Geoffrey R. Scheller'
__copyright__ = 'Copyright (c) 2023-2025 Geoffrey R. Scheller'
__license__ = 'Apache License 2.0'
