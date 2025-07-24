usage
=====

How to installing the module
----------------------------

Install the project into your Python environment:

.. code:: console

   $ pip install pythonic-fp.circulararray

Importing the module
--------------------

Import the ``CA`` class and ``ca`` "factory function" into your code.

.. code:: python

    from pythonic_fp.circulararray.resizing import CA, ca
    from pythonic_fp.circulararray.fixed_capacity import CAFix, ca_fix

.. note::

    The ``CA`` and ``CAFix`` classes can be instantiated with either one iterable or no arguments,
    just like Python builtins ``list`` or ``tuple``.

    The factory functions ``ca`` and ``ca_fix`` behaves like Python's ``[]`` syntax. Each creates
    its corresponding circular array object from the arguments past to it.
    a ``CA`` object from the arguments passed to it.
