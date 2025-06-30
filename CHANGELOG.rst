=========================================
CHANGELOG: Pythonic FP namespace projects
=========================================

Developer Tools supporting a functional style of programming yet endeavoring to
remain Pythonic. For the PyPI ``pythonic-fp`` namespace projects.

Important Milestones
--------------------

2025-06-29 - Switching from pdoc to Sphinx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- building pythonic-fp.circulararray docs with Sphinx

  - ended up using the Sphinx autodoc extension
  - using the `piccolo-theme <https://pypi.org/project/piccolo-theme>`_ as the html_theme

- not yet "publishing" them on gh-pages, looking into ``sphinx.ext.githubpages``

  - realized I will need to move docs over to pythonic-fp repo for PyPI releases
  - the gh-pages for the namespace repos will host the current devel env docs

2025-05-29 - Beginning transition pdoc -> Sphinx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- stumble on PyPI project python-sphinx-doc
- supposedly will parse Python type annotations

  - uninstall ``pdoc``, install ``python-sphinx-doc``
  - when I it I get these packages with "sphinx" in their names

    ================================= =====
    ``python-sphinx-doc``             0.1
    ``Sphinx``                        8.2.3
    ``sphinxcontrib-applehelp``       2.0.0
    ``sphinxcontrib-devhelp``         2.0.0
    ``sphinxcontrib-htmlhelp``        2.1.0
    ``sphinxcontrib-jsmath``          1.0.1
    ``sphinxcontrib-qthelp``          2.0.0
    ``sphinxcontrib-serializinghtml`` 2.0.0
    ``sphinx_design``                 0.6.1
    ================================= =====

  - Only ``sphinx_design`` is a ``python-sphinx-doc`` dependency
    that is not also a ``Sphinx`` dependency.

2025-05-24 - More work "biting-the-bullet"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- decided on the pythonic-fp namespace name instead of fpythonic 
- brought over source code from all dtools namespace projects

  - pythonic-fp.circulararray 5.0.0
  - pythonic-fp.containers 2.0.0
  - pythonic-fp.fptools 3.0.0
  - pythonic-fp.iterables 3.0.0
  - pythonic-fp.queues 3.0.0
  - pythonic-fp.splitends 0.30.0
  - pythonic-fp (name_claim) 1.0.0 - DO NOT INSTALL

2025-05-23 - Decided to "bite-the-bullet" and drop dtools name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- decided on the unclaimed name fpythonic

  - for fp + pythonic

- releases under this name

  - fpythonic 1.2.0
  - fpythonic 1.1.0
  - fpythonic 1.0.0
  - fpythonic.circular-array v4.1.0
  - fpythonic.circular-array v4.0.0 (Yanked)
  - yanked because v4.0.0 was published on PyPI too soon

- fpythonic is an empty module

  - will permanently be <2.0
  - has a __init__.py file

    - DO NOT INSTALL IT!!!
    - if you do, fpythonic will no longer be a namespace module!
    - PyPI was happy to accept it

      - thought it best to take the name

  - its GitHub repo has 2 purposes other than implementing this "module"

    - serves as a homepage for the fpythonic namespace modules
    - hosts the generated documentation on gh-pages

2025-05-22 - Rebuilt docs for all projects for next PyPI releases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- dtools.circular-array 3.15.0
- dtools.containers 1.0.0
- dtools.fp 2.0.0
- dtools.iterables 2.0.0
- dtools.queues 2.0.0
- dtools.splitends 0.29.0

2025-05-20 - Broke out dtools.fp.iterables to its own repo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- dtools.fp.iterables -> dtools.iterables
- GitHub repo: https://github.com/grscheller/dtools-iterables/

2025-05-12 - MayBe and Xor moved
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- from dtools.fp
- to dtools.containers

2025-05-10 - Changed GitHub name of this repo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
- GitHub repo name change

  - grscheller/dtools-docs -> grscheller/dtools-namespace-projects
  - will double as a project homepage as well as the document repo

Date:   Mon May 5 02:43:45 2025 -0600

2025-05-05 Added dtools.containers project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- added dtools.containers project and deprecated dtools.tuples
- dtools.tuples content moved to dtools.containers

  - actually dtools.tuples repo just renamed to dtools.containers

    - this allows older PyPI source code links to keep working
    - thought necessary since my Boring Math Library not updated yet

2025-04-24: Decided to change name back to dtools-docs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
- a PyPI project named dtools already exists
- unfortunately, I missed this back in January

2025-04-24: Renamed repo from dtools-docs to just dtools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
- morphing README.md into a project-wide Homepage
- created CHANGELOG.md file
- removed README.md links to deprecated dtools.datastructures project

2025-03-31: Updates for new dtools project Mar 31
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- adding infrastructure for dtools.tuples

2025-03-28: updated docs for all dtools projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ran linters and against all dtools namespace repos

2025-02-06: Standardized dtools and bm docs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- standardized Developer Tools and Boring Math project documentation

2025-01-17: Created this repo - dtools-docs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- created this repo for pdoc generated dtools project documentation

  - purpose to keep actual source code repos smaller
  - detailed documentation generated from source code docstrings
  - replaces grscheller-pypi-namespace-docs 

    - older repo still exits as a "zombie" project

      - to keep older PyPI document links working

- added development documentation infrastructure for all dtools repos

  - dtools.datastructures
  - dtools.fp
  - dtools.circular-array

- generated docs for first PyPI releases under dtools namespace
