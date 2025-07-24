Getting Started
===============

How to installing the module
----------------------------

Install the project into your Python environment:

.. code:: console

   $ pip install pythonic-fp.singletons

Importing the libraries
-----------------------

Importing the singleton classes and functions into your code.

Class Nada
~~~~~~~~~~

.. code:: python

   # Singleton object representing & propagating failure.
   from pythonic_fp.singletons.nada import Nada

Class NoValue
~~~~~~~~~~~~~

.. code:: python

   # Singleton object representing a missing value.
   from pythonic_fp.singletons.novalue import NoValue

Class Sentinel
~~~~~~~~~~~~~~

.. code:: python

   # Singleton objects representing sentinel values.
   from pythonic_fp.singletons.sentinel import Sentinel

Class SBool
~~~~~~~~~~~

.. code:: python

   # Subclassable Booleans hierarchies
   from pythonic_fp.singletons.sbool import Bool, Truth, Lie

   # Convenience constants for default "truth" and "lie"
   from pythonic_fp.singletons.sbool import TRUTH, LIE
