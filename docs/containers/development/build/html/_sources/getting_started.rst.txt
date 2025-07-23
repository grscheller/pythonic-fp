Getting Started
===============

How to installing the module
----------------------------

Install the project into your Python environment:

.. code:: console

    $ pip install pythonic-fp.containers

Importing the module
--------------------

.. code:: python

    from pythonic_fp.containers.box import Box
    from pythonic_fp.containers.functional_tuple import FunctionalTuple, functional_tuple
    from pythonic_fp.containers.immutable_list import ImmutableList, immutable_list
    from pythonic_fp.containers.maybe import MayBe, maybe
    from pythonic_fp.containers.either import Xor, xor

.. Note::

   Maintainer intends to move ``maybe`` and ``xor`` modules to the ``pythonic_fp.fptools``
   package. Also, ``Xor`` and ``xor`` will be renamed to ``Either`` and ``either`` when
   the move takes place. The ``Xor`` and ``xor`` names will eventually be repurposed.

