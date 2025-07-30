usage
=====

How to installing the module
----------------------------

Install the project into your Python environment:

.. code:: console

   $ pip install pythonic-fp.queues

Importing the module
--------------------

Import the queues classes and "factory functions" into your code.

.. code:: python

    from pythonic_fp.queues.fifo import FIFOQueue, fifo_queue
    from pythonic_fp.queues.fifo import LIFOQueue, lifo_queue
    from pythonic_fp.queues.de import DEQueue, de_queue

.. note::

    The behaviors of the queue classes were modeled after the Python builtin ``list``.

    - they can be instantiated with data by supplying an iterable
    - with no unnamed arguments they are instantiated empty
    - methods which modify the objects return no values
    - their corresponding queue factory functions behave like Python's ``[]`` syntax.

      - each creates its corresponding queue object from the arguments passed to it
