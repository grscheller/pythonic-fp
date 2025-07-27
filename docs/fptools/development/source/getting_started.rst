Getting Started
===============

How to installing the module
----------------------------

Install the project into your Python environment:

.. code:: console

   $ pip install pythonic-fp.fptools

Importing the libraries
-----------------------

Importing the queue classes and functions into your code.

.. code:: python

   # Subclassable Boolean hierarchy
   from pythonic_fp.fptools.bool import Bool, Truth, Lie
   # Convenience constants for default "truth" and "lie"
   from pythonic_fp.fptools.bool import TRUTH, LIE

   # Functional programming library for functions
   from pythonic_fp.fptools.function import swap, sequenced, partial, it, negate

   # Non-strict (lazy) delayed function evaluation
   from pythonic_fp.fptools.lazy import Lazy, lazy, real_lazy

   # Maybe monad
   from pythonic_fp.fptools.state import State

   # Either monad
   from pythonic_fp.fptools.state import State

   # State monad
   from pythonic_fp.fptools.state import State
