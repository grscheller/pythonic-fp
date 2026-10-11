# CHANGELOG

PyPI **pythonic-fp** projects.

Pythonic Functional Programming (FP) projects. Developer Tools
supporting a functional style of programming yet endeavoring to remain
Pythonic. All done under the Python pythonic_fp namespace.

## Release versioning

Unlike the PyPI projects that make up Pythonic FP, which now use
a tiered strict semantic versioning, the release string for
`pythonic-fp` changes when

- **MAJOR:** for major release number bumps (formally paradigm shifts)
- **MINOR:** homepage changes, additional integration tests
- **PATCH:** typos, git/pypi thrashing, pure eye-candy/wordsmithing

## Important Milestones

### PyPI release 6.0.0 - 2026-10-TBA

**Major Paradigm Shift**

The only supported version of the Pythonic FP projects will be the ones
with the top level major release numbers.

A tiered strict 3 digit semantic versioning will be used

- **MAJOR** incremented for incompatible API changes across Pythonic FP libraries
- **MINOR** incremented for backward compatible added functionality
- **PATCH** incremented for backward compatible bug fixes

After the release of pythonic-fp version `6.0.0`, all Pythonic FP
projects with the same major release numbers will be attempted to be
kept consistent with each other.

**Warning:** Releases before `6.0.0` are unsupported and are not
guaranteed to resolve consistently.

TODO: list major changes made for this release.

### PyPI release 5.1.0 - 2026-10-10

Preparing for another major paradigm shift.

Releases will now be capped to the next upcoming major release.

### PyPI release 5.0.0 - 2026-09-13

**Major Paradigm Shift**

Transitioned the management of my virtual environments from pyenv to uv.
Unlike pyenv, which is shell based, uv is project based. I can treat the
individual projects making up the Pythonic FP effort as independent
projects with regards to calculating their dependencies. With uv there
will be no need to have coordinated releases of known consistent
versions of the projects.

### PyPI release 4.1.0 - 2026-06-29

**Coordinated Release**

| PyPI Project              | Version |
|:------------------------- |:-------:|
| pythonic-fp-booleans      | 4.0.0   |
| pythonic-fp-circulararray | 6.1.1   |
| pythonic-fp-containers    | 4.1.0   |
| pythonic-fp-fptools       | 5.4.0   |
| pythonic-fp-gadgets       | 4.1.0   |
| pythonic-fp-iterables     | 5.1.4   |
| pythonic-fp-numpy         | 1.0.0   |
| pythonic-fp-queues        | 5.1.3   |
| pythonic-fp-splitends     | 2.0.3   |

### Feat - 2026-05-02

All Pythonic FP projects automatically build their docs on GitHub pages.

GitHub Actions builds only the last release and whatever is in
development for all pythonic-fp project repos.

At this point only the pythonic-fp-queues docs are in excellent
shape. Redid build process. Can build docs locally or on GitHub
pages via GitHub Actions.

The homepage links work but the PyPI repos have broken links for
everything except pythonic-fp-queues. The PyPI links will gradually
be fixed as I do releases.

### PyPI release 4.0.1 - 2026-05-03

Homepage updates. Also preparing for a minor PyPI release
when all documentation building are fixed for all projects.

Four projects have been released to PyPI.

- pythonic-fp-circulararray v6.1.0 - 2026-05-03
- pythonic-fp-queues v5.1.2 - 2026-05-02
- pythonic-fp-gadgets v6.1.0 - 2026-04-26 (doc build needs updating)
- pythonic-fp-booleans v3.0.2 - 2026-04-25 (doc build needs updating)

### Milestones - 2026-05-05

Got all Pythonic FP projects to build documentation through
GitHub Actions and display the results on GH-Pages. The last
release and the current state of development are built.

What gets built still needs to be cleaned up. At this point in
time only the documentation foe circulararray and queues are
in their final form. Documentation for gadgets is close.

### PyPI release 4.0.0 - 2026-04-25

**Coordinated Release**

| PyPI Project | Version |
|:------------ |:-------:|
| pythonic-fp-booleans | 3.0.0 |
| pythonic-fp-circulararray | 6.0.1 |
| pythonic-fp-containers | 4.0.1 |
| pythonic-fp-fptools | 5.2.0 |
| pythonic-fp-gadgets | 4.0.2 |
| pythonic-fp-iterables | 5.1.3 |
| pythonic-fp-numpy | 0.1.2 |
| pythonic-fp-queues | 5.1.1 |
| pythonic-fp-splitends | 2.0.1 |

Major change. Each Pythonic FP project will be automatically
building the current release documentation and the latest development
documentation on GitHub.

So far,

- pythonic-fp-circulararray
- pythonic-fp-booleans

The rest may be broken for the next few week or so.

### Milestone - 2026-04-21

At this time I thought Sphinx docs were more or less in their final
form for the pythonic-fp-circulararray library.

### Milestone - 2026-04-03

Homogenized documentation across pythonic-fp projects. Based on what
I did for my boring-math effort.

### PyPI release 3.4.0 - 2026-01-22

**Coordinated Release**

| PyPI Project | Version |
|:------------ |:-------:|
| pythonic-fp-booleans | 3.0.0 |
| pythonic-fp-circulararray | 6.0.1 |
| pythonic-fp-containers | 4.0.1 |
| pythonic-fp-fptools | 5.2.0 |
| pythonic-fp-gadgets | 4.0.2 |
| pythonic-fp-iterables | 5.1.3 |
| pythonic-fp-numpy | 0.1.2 |
| pythonic-fp-queues | 5.1.1 |
| pythonic-fp-splitends | 2.0.2 |

### PyPI release v3.3.3 - 2025-12-02

I never pushed pythonic-fp-gadgets `4.0.0` to PyPI!
Pushed version `4.0.1`.

Discovered when tests failed off of installed libraries.
Also had to update pythonic-fp-booleans to `2.0.0 -> 2.1.0` as a result.

Consistent set of Pythonic FP projects:

| PyPI Project | Version |
|:------------ |:-------:|
| pythonic-fp-booleans | 2.1.0 |
| pythonic-fp-circulararray | 6.0.0 |
| pythonic-fp-containers | 4.0.0 |
| pythonic-fp-fptools | 5.1.2 |
| pythonic-fp-gadgets | 4.0.1 |
| pythonic-fp-iterables | 5.1.2 |
| pythonic-fp-numpy | 0.1.1 |
| pythonic-fp-queues | 5.1.0 |
| pythonic-fp-splitends | 2.0.0 |

### PyPI release 3.3.2 - 2025-12-02

**Coordinated Release**

| PyPI Project | Version |
|:------------ |:-------:|
| pythonic-fp-booleans | 2.1.0 |
| pythonic-fp-circulararray | 6.0.0 |
| pythonic-fp-containers | 4.0.0 |
| pythonic-fp-fptools | 5.1.2 |
| pythonic-fp-gadgets | 4.0.0 |
| pythonic-fp-iterables | 5.1.2 |
| pythonic-fp-numpy | 0.1.1 |
| pythonic-fp-queues | 5.1.0 |
| pythonic-fp-splitends | 2.0.0 |

### PyPI release v3.3.1 - 2025-12-02

PyPI pythonic-fp-numpy `0.1.1` was released. The test dependencies for
boring-math-abstract-algebra was missing.

All development docs regenerated with :special-members: enabled.

### PyPI release v3.3.0 - 2025-11-30

PyPI pythonic-fp-numpy version `0.1.0` was released. Ability to
wrap a non-writable NumPy NDArray with a hashable container.

### PyPI release v3.2.2 - 2025-10-12

Incorporated lessons learned from Boring Math project into homepage.

### Milestone - 2025-10-06

Rebuilt homepage (development) and all Pythonic FP projects docs with
furo theme.

### PyPI release v3.2.1 - 2025-09-30

Spent a lot of effort to make the homepage smooth and concise.

TODO: Incorporate ideas into the docs for the individual PyPI projects.

### PyPI release v3.2.0 - 2025-09-28

Consistent set of Pythonic FP projects:

| PyPI Project | Version |
|:------------ |:-------:|
| pythonic-fp-booleans | 2.0.0 |
| pythonic-fp-circulararray | 6.0.0 |
| pythonic-fp-containers | 4.0.0 |
| pythonic-fp-fptools | 5.1.2 |
| pythonic-fp-gadgets | 3.1.0 |
| pythonic-fp-iterables | 5.1.2 |
| pythonic-fp-queues | 5.1.0 |
| pythonic-fp-splitends | 1.0.2 |

### PyPI release v3.1.1 - 2025-09-28

Got homepage to a finished state.

### PyPI release v3.0.1 - 2025-09-26

- modified 3 digit release string (Changed! See above)
  - major release will remain 3 for this homepage module paradigm
  - minor release will increase for coordinated release points
  - patch release will increase when src/ gets updated
- released with or after this version and before next
  - circulararray 6.0.0
  - queues 5.1.0
  - gadgets 3.1.0

### PyPI release v3.0.0 - 2025-09-26

Project's homepage taking shape. Provides overarching documentation
for the entire Pythonic FP project.

### Update - 2025-09-22

Started effort to host the project's "homepage" with Sphinx.

Development is somewhat ahead of what is on PyPI. I need to do
a new coordinated release soon.

### Update - 2025-09-21

Deprecated the pythonic-fp-sentinels PyPI project.

- code moved to pythonic-fp-gadgets
  - wanted to make gadgets independent of all external code
  - except the Python standard library
- moved rest of pythonic-fp development off sentinels and onto gadgets
- with some difficulty, final release version is `2.1.3`

### Update - 2025-09-15

Consistent set of Pythonic FP projects:

| PyPI Project | Version |
|:------------ |:-------:|
| pythonic-fp-booleans | 1.1.2 |
| pythonic-fp-circulararray | 5.3.2 |
| pythonic-fp-containers | 3.0.1 |
| pythonic-fp-fptools | 5.1.1 |
| pythonic-fp-gadgets | 3.0.1 |
| pythonic-fp-iterables | 5.1.1 |
| pythonic-fp-sentinels | 2.1.0 |
| pythonic-fp-splitends | 1.0.2 |

### PyPI release v2.0.1 - 2025-09-11

- Removed Documentation link in pyproject.toml
  - decided for now not to provide overarching Sphinx docs for entire effort
- Changes to better describe overall the Pythonic FP project
  - Updated README.md & CHANGELOG.md

### Update - 2025-08-13

Generated docs for pythonic-fp-booleans PyPI project. First development
(prerelease) generation of of docs for booleans.sbool

### Update - 2025-08-11

The next gadget's release will be v1.2.0. Added module
pythonic_fp.gadgets.lca for function latest common ancestor.

### Update - 2025-08-09

Preparing for upcoming PyPI release for gadgets.

- decided to make gadget's pyproject.toml the exemplar for rest of pythonic-fp namespace
- pythonic_fp.gadget works with previous and next release of singletons

### PyPI release 1.1.0 - 2025-08-02

Completed a coordinated, consistent release of pythonic-fp namespace projects

- released pythonic-fp v1.1.0 which contains pythonic_fp.gadgets package
- released pythonic-fp-circulararray v5.3.0 immediately followed by v5.3.1
  - had to fix a link in README.rst, changed
    - pythonic-fp.circulararray to pythonic-fp-circulararray 
      - linked still worked since PyPI maps `.` and `_` to `-`
    - had to update development/source/conf.py
    - had to update development/source/releases.py
    - had to copy generated html to release directories
- released pythonic-fp-containers v3.0.0
- released pythonic-fp-fptools v5.0.0
- released pythonic-fp-iterables v5.0.0
- released pythonic-fp-singletons v1.0.0
- released pythonic-fp-splitends v1.0.0
- setup Sphinx for development environment documentation
  - bumped all version numbers by one patch level
  - redid Sphinx development docs for entire namespace project

### Milestone - 2025-08-01

Added package pythonic_fp.gadgets to PyPI project pythonic-fp. Now
this "name-claim" package is installable.

The gadgets library is for simple, but useful, data structures with
minimal dependencies.

### Milestone - 2025-07-30

Updated Sphinx docs for all pythonic_fp namespace projects to
the latest format. Still need to do consistency checks.

### Update - 2025-07-30

Updated Sphinx docs for the pythonic_fp.queues module.

### Update - 2025-07-30

Added Sphinx docs for gadgets. Fairly easy copy and edit
from circulararray.

### 2025-07-29 - Complete redo of circulararray docs

Now PyPI project pythonic-fp.circulararray will be the exemplar for
Sphinx documentation. The toctrees are no longer hidden.

### Update - 2025-07-27

Finished Sphinx documentation for two PyPI projects, the development
versions of Sphinx documentation for `pythonic-fp.circulararray`
and `pythonic-fp.queues`.

### Update - 2025-07-21

Unified coordinated upgrade all pythonic-fp projects

Updated all pyproject.toml files and corresponding Sphinx documentation
for an upcoming coordinated release of all packages. From a flowchart of
library dependencies, a better organization became apparent to the
maintainer. Will be removing all "from future import annotations" from
the code. All this does is replace module names with strings. It was
a hack to support a future feature that will never happen. This future
import will be deprecated in Python 3.14.

- rename GH-Pages mount point from pypi-release-docs/ to just docs/
- removed `/API/` from `docs/*/API/*`
- move maybe and (xor -> either) modules back to fptools
- broke out module fptools/singletons to its own repo
- moved fptools.bool -> singletons.sbool

TODO:

- finish pdoc -> Sphinx migration
  - all informational content will come from docstrings
  - replace the Markdown Pythonic FP "homepage" with Sphinx based one
    - grscheller/pythonic-fp/README.md will point to the new docs
- next PyPI release will happen when "everything is ready"

### Feat - 2025-07-13

All document generation brought back to this repo.

- Sphinx now used
  - looks much more professional
  - all documentation generation moved back to this repo
  - docstrings in code a bit rough, but now more terse
- Updated docs for circulararray PyPI release v5.2.0
- Updated docs for queues PyPI release v4.0.1
- the docs links on the README.md pythonic-fp homepage updated
  - now points to docs development's release page instead of docs development itself

### Update - 2025-07-04

Beginning the dtools deprecation process.

- Published version v5.1.0 pythonic-fp.circulararray to PyPI
- Updated pyproject.toml files for all pythonic-fp namespace repos
- Updated all README.md files to use GitHub, not GH-Pages, for Pythonic FP Homepage
- Updated all repo root CHANGELOG.rst files
  - preparing to rename them docs/source/changelog.rst for Sphinx build
  - all except this one

### Update - 2025-06-29

Building pythonic-fp.circulararray docs with Sphinx. Ended up using the
Sphinx autodoc extension with the
[piccolo-theme](https://pypi.org/project/piccolo-theme) html_theme.

Not yet publishing them on gh-pages. Realized I will need to move docs
over to pythonic-fp repo for PyPI releases. The gh-pages for the
namespace repos will host the current devel env docs.

### Update - 2025-05-29

Beginning transition pdoc -> Sphinx.

Stumble on PyPI project python-sphinx-doc. Supposedly it will
parse Python type annotations.

Uninstall pdoc, install python-sphinx-doc. I then got these packages
with "sphinx" in their names:

| PyPI Project | Version |
|:------------ |:-------:|
| python-sphinx-doc | 0.1 |
| Sphinx | 8.2.3 |
| sphinxcontrib-applehelp | 2.0.0 |
| sphinxcontrib-devhelp | 2.0.0 |
| sphinxcontrib-htmlhelp | 2.1.0 |
| sphinxcontrib-jsmath | 1.0.1 |
| sphinxcontrib-qthelp | 2.0.0 |
| sphinxcontrib-serializinghtml | 2.0.0 |
| sphinx_design | 0.6.1 |

Only sphinx_design is a python-sphinx-doc dependency
that is not also a Sphinx dependency.

### Update - 2025-05-24

Decided on the pythonic-fp namespace name instead of the fpythonic name.

- Brought over source code from all dtools namespace projects
  - pythonic-fp.circulararray 5.0.0
  - pythonic-fp.containers 2.0.0
  - pythonic-fp.fptools 3.0.0
  - pythonic-fp.iterables 3.0.0
  - pythonic-fp.queues 3.0.0
  - pythonic-fp.splitends 0.30.0
  - pythonic-fp (name_claim) 1.0.0 - DO NOT INSTALL

### Update - 2025-05-23

Decided to "bite-the-bullet" and drop dtools name.

- Decided on the unclaimed name fpythonic
  - for fp + pythonic
- Releases under this name
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

### Update - 2025-05-22

Rebuilt docs for all projects for next PyPI releases.

- dtools.circular-array 3.15.0
- dtools.containers 1.0.0
- dtools.fp 2.0.0
- dtools.iterables 2.0.0
- dtools.queues 2.0.0
- dtools.splitends 0.29.0

### Milestone - 2025-05-20

Broke out dtools.fp.iterables to its own repo

- dtools.fp.iterables -> dtools.iterables
- GitHub repo: https://github.com/grscheller/dtools-iterables/

### Update - 2025-05-12

MayBe and Xor moved from dtools.fp to dtools.containers repo.

### Update - 2025-05-10

Changed GitHub name of this repo
    
- grscheller/dtools-docs -> grscheller/dtools-namespace-projects
- will double as a project homepage as well as the document repo

### Milestone - 2025-05-05

Added dtools.containers project.

- Added dtools.containers project and deprecated dtools.tuples
- dtools.tuples content moved to dtools.containers
  - actually dtools.tuples repo just renamed to dtools.containers
    - this allows older PyPI source code links to keep working
    - thought necessary since my Boring Math Library not updated yet

### Update - 2025-04-24

Decided to change name back to dtools-docs.
    
A PyPI project named dtools already exists. Unfortunately, I missed this
back in January.

### Update - 2025-04-24

Renamed repo from dtools-docs to just dtools

- Morphing README.md into a project-wide Homepage
- Created CHANGELOG.md file
- Removed README.md links to deprecated dtools.datastructures project

### Update - 2025-03-31

Adding infrastructure for dtools.tuples.

### Milestone - 2025-03-28

Updated docs for all dtools projects.

Ran linters and against all dtools namespace repos.

### Milestone - 2025-02-06

Attempt to standardized dtools and bm documentation.

### Milestone - 2025-01-17

Created this repo under the dtools-docs name.

- Created this repo for pdoc generated dtools project documentation
  - purpose to keep actual source code repos smaller
  - detailed documentation generated from source code docstrings
  - replaces grscheller-pypi-namespace-docs 
    - older repo still exits as a "zombie" project
      - to keep older PyPI document links working
- Added development documentation infrastructure for all dtools repos
  - dtools.datastructures
  - dtools.fp
  - dtools.circular-array
- Generated docs for first PyPI releases under dtools namespace
