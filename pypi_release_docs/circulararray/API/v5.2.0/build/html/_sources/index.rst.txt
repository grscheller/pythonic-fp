..
   Pythonic FP - Queues documentation master file. To regenerate the sphinx
   documentation do: "$ make html" from the "docs/" directory.

Pythonic FP - Circular Array Overview
=====================================

PyPI project `pythonic-fp.circulararray <https://pypi.org/project/pythonic-fp.circulararray/>`_.

This project implements a full featured, generic, stateful circular array data structure.

- O(1) amortized pushes and pops either end
- O(1) indexing
- Auto-resizing larger when necessary, can be manually compacted if desired
- Iterable, can safely be mutated while iterators continue iterating over previous state
- Fully supports slicing

Part of of the
`pythonic-fp namespace projects <https://github.com/grscheller/pythonic-fp/blob/main/README.md>`_.

Getting Started
---------------

:doc:`Getting Started <getting_started>`
    Getting started with the PyPI pythonic-fp.circulararray project.

:doc:`PyPI Releases <releases>`
    Documentation for pythonic-fp.circulararray PyPI releases.

Documentation
-------------

Programming API:
~~~~~~~~~~~~~~~~

:doc:`Package pythonic_fp.circulararray <api/index>`
    For |PROPOSED_RELEASE_STRING| PyPI pythonic-fp.circulararray project |VERSION_RELEASED| release.

CHANGELOG:
~~~~~~~~~~

Change log for the
`pythonic-fp circulararray <https://github.com/grscheller/pythonic-fp-circulararray/blob/main/CHANGELOG.rst>`_
PyPI project.

.. toctree::
   :caption: Overview
   :maxdepth: 1
   :hidden:

   self

.. toctree::
   :caption: Getting Started
   :maxdepth: 1
   :hidden:

   getting_started
   releases

.. toctree::
   :caption: Documentation
   :maxdepth: 1
   :hidden:

   api/index
