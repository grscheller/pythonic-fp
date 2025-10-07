"""
Module dependencies
===================

Arrows point from modules to their dependencies.

Internal dependencies
---------------------

There are no external dependency except for the Python standard library.

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

External dependencies
---------------------

.. graphviz::

    digraph Modules {
        bgcolor="#957fb8";
        node [style=filled, fillcolor="#181616", fontcolor="#dcd7ba"];
        edge [color="#181616", fontcolor="#dcd7ba"];
        booleans -> "collections.abc";
        booleans -> threading;
        booleans -> typing;
        circulararray -> "collections.abc";
        circulararray -> typing;
        containers -> "collections.abc";
        containers -> typing;
        fptools -> "collections.abc";
        fptools -> typing;
        gadgets -> "collections.abc";
        gadgets -> inspect;
        gadgets -> threading;
        gadgets -> typing;
        iterables -> "collections.abc";
        iterables -> enum;
        iterables -> typing;
        queues -> "collections.abc";
        queues -> typing;
        splitends -> "collections.abc";
        splitends -> typing;
    }

Semantic versioning
===================

Maintainer has adopted strict 3 digit `semantic versioning <https://semver.org>`_
and does not put `caps on dependencies <https://iscinumpy.dev/post/bound-version-constraints>`_.
This allows for more package management flexibility and access to the latest features.
For those concerned with stability, periodically known consistent sets of releases
are given in the Releases section of these docs.

Changelog
=========

Pythonic FP overarching
`CHANGELOG <https://github.com/grscheller/pythonic-fp/blob/main/CHANGELOG.rst>`_.

Each individual *Pythonic FP* project has its own CHANGELOG too.

"""
