Usage
=====

How to installing the package
-----------------------------

Install the project into your Python environment:

.. code:: console

   $ pip install pythonic-fp-booleans

Importing the module
--------------------

Import package booleans classes, functions and constants into your code.

.. code:: python

    from pythonic_fp.booleans.subtypable SBool, snot, TRUTH, LIE

    from pythonic_fp.booleans.subtypes.flavored FBool, truthy, falsy

    from pythonic_fp.booleans.subtypes.truthy_falsy TF_Booleans
    from pythonic_fp.booleans.subtypes.truthy_falsy TF_Bool, T_Bool, F_Bool
    from pythonic_fp.booleans.subtypes.truthy_falsy ALWAYS, NEVER_EVER

Best practices
--------------

Subtypable Booleans
~~~~~~~~~~~~~~~~~~~

- use the ``~`` to return the same ``SBool`` subtype but of the opposite truthiness

  - Python's ``not`` operator always returns a ``bool``

- constants ``TRUTH`` and ``LIE`` are the unique truthy and falsy ``SBool`` values

Flavored Booleans
~~~~~~~~~~~~~~~~~

- functions ``truthy`` and ``falsy`` take any hashable value called its flavor
- they return the unique truthy or falsy ``FBool`` respectively of that flavor

Truthy_Falsy Booleans
~~~~~~~~~~~~~~~~~~~~~

- use ``TF_Booleans = T_Bool | F_Bool | TF_Bool`` only as a type
- directly use ``T_Bool``, ``F_Bool``, ``TF_Bool`` as the type constructors
- constants ``ALWAYS`` and ``Never`` are the unique truthy and falsy values

  - but they have distinct distinct types

    - we have ``type(ALWAYS) is T_Bool`` and ``type(NEVER) is F_Bool``
    - while ``type(True) is bool`` and ``type(False) is bool``
