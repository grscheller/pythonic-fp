usage
=====

.. admonition:: **DEPRECATED**

    This package is deprecated, use package ``pythonic_fp.containers.queues`` instead.

How to installing the module
----------------------------

Install the project into your Python environment:

.. code:: console

   $ pip install pythonic-fp.queues

Importing the module
--------------------

Importing the queue classes and "factory functions" into your code.

.. code:: python

   from pythonic_fp.queues.fifo import FIFOQueue, fifo_queue
   from pythonic_fp.queues.lifo import LIFOQueue, lifo_queue
   from pythonic_fp.queues.de import DEQueue, de_queue

.. note::

    Each type of Queue can be instantiated with either one iterable or no arguments,
    just like Python builtins ``list`` or ``tuple``.

    The factory functions behaves like Python's ``[]`` syntax. Each creates its
    corresponding Queue object from the arguments given it.
