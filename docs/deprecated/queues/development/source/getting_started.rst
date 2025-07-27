Usage
=====

.. deprecated:: 5.0.0

   Use package ``pythonic_fp.containers.queues`` instead.

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
    just like Python builtins ``list`` or ``tuple`` can be.

    The factory functions ``fifo_queue``, ``lifo_queue`` and ``de_queue``
    create their corresponding Queue object from the arguments given them.
