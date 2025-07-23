Getting Started
===============

How to installing the module
----------------------------

Install the project into your Python environment:

.. code:: console

   $ pip install pythonic-fp.iterables

Importing the module
--------------------

Import the functions and the ``FM`` enum class into your code.

.. code:: python

   from pythonic_fp.iterables import FM, concat, exhaust, merge
   from pythonic_fp.iterables import drop, drop_while
   from pythonic_fp.iterables import take, take_while
   from pythonic_fp.iterables import take_split, take_while_split
   from pythonic_fp.iterables import accumulate
   from pythonic_fp.iterables import reduce_left, fold_left, mb_fold_left
   from pythonic_fp.iterables import sc_reduce_left, sc_reduce_right

.. Warning::

   The ``reduce_left``, ``fold_left`` and ``mb_fold_left`` functions
   never return if given an infinite iterable.

.. Warning::

   When using the ``take_split`` and ``take_while_split`` functions there
   is a **contract:** Do not access the second returned iterator until the
   first one is exhausted.
