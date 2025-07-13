Getting Started
===============

How to installing the module
----------------------------

Install the project into your Python environment:

.. code:: console

   $ pip install pythonic-fp.circulararray

Importing the module
--------------------

Import the ``CA`` class and ``ca`` "factory function" into your code.

.. code:: python

   from pythonic_fp.circulararray import CA, ca

.. Note::

   The ``CA`` class can be instantiated with either one iterable or no arguments.
   The factory function ``ca``  behaves like Python's ``[]`` syntax. It creates
   a ``CA`` object from the arguments passed to it.
