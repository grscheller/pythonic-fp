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

Developer Tools supporting a functional style of programming yet endeavoring
to remain Pythonic. Project names begin ``pythonic-fp-`` on PyPI and
``grscheller/pythonic-fp-`` on GitHub. As Python modules, all are under
the ``pythonic_fp`` package name.

A complete list of links to the PyPI and GitHub repos making up the project
can be found
`here <https://github.com/grscheller/pythonic-fp/blob/main/README.md>`_.

Goals
-----

- to assist in a functional style of programming
- to fulling support typing and tooling like `mypy <https://mypy-lang.org/>`_
- support stateful as well as functional paradigms
- good documentation
- be extensible

Non-Goals
---------

- try and make Python a pure functional language like Haskell

Releases
--------

+----------------+---------------------------+---------+---------------------------+
| Name           | PyPI Project              | version | Python Module             |
+================+===========================+=========+===========================+
| Booleans       | pythonic-fp-booleans      | 1.1.2   | pythonic_fp.booleans      |
+----------------+---------------------------+---------+---------------------------+
| Circular Array | pythonic-fp-circulararray | 5.3.3   | pythonic_fp.circulararray |
+----------------+---------------------------+---------+---------------------------+
| Containers     | pythonic-fp-containers    | 3.0.1   | pythonic_fp.containers    |
+----------------+---------------------------+---------+---------------------------+
| FP Tools       | pythonic-fp-fptools       | 5.1.1   | pythonic_fp.fptools       |
+----------------+---------------------------+---------+---------------------------+
| Gadgets        | pythonic-fp-gadgets       | 3.0.1   | pythonic_fp.gadgets       |
+----------------+---------------------------+---------+---------------------------+
| Iterables      | pythonic-fp-iterables     | 5.1.1   | pythonic_fp.iterables     |
+----------------+---------------------------+---------+---------------------------+
| Queues         | pythonic-fp-queues        | TBD     | pythonic_fp.queues        |
+----------------+---------------------------+---------+---------------------------+
| Sentinels *    | pythonic-fp-sentinels     | 2.1.3   | pythonic_fp.sentinels     |
+----------------+---------------------------+---------+---------------------------+
| Singletons **  | pythonic-fp-singletons    | 1.0.0   | pythonic_fp.singletons    |
+----------------+---------------------------+---------+---------------------------+
| Splitends      | pythonic-fp-splitends     | 1.0.2   | pythonic_fp.splitends     |
+----------------+---------------------------+---------+---------------------------+

**\* DEPRECATED:** Use ``Gadgets`` instead.

**\*\* DEPRECATED:** Use ``Booleans`` and ``Gadgets`` instead.

Module dependencies
-------------------

Current module dependencies where arrows point to dependencies. There
are no external dependency except for the Python standard library.

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
    }

"""
