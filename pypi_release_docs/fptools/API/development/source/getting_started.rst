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

   # FP tools library for functions
   from pythonic_fp.fptools.function import swap, sequenced, partial, it, negate

   # Non-strict delayed function evaluation
   from pythonic_fp.fptools.lazy import Lazy, lazy, real_lazy

   # Singleton classes
   from pythonic_fp.fptools.singltons import NoValue
   from pythonic_fp.fptools.singletons import Sentinel
   from pythonic_fp.fptools.singletons import Nada
   
   # State Monad
   from pythonic_fp.fptools.state import State
