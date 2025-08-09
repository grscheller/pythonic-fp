# PyPI Pythonic FP Namespace Projects

Collection of Functional Programming (FP) oriented Python libraries.
While taking a functional programming approach, these packages endeavor
to remain Pythonic.

Pythonic FP is a hobby project, but the maintainer is serious about its quality.

## Pythonic FP `pythonic-fp` namespace projects

| Name | PyPI | GitHub | Docs | Python Package |
|:---- |:----:|:------:|:----:|:-------------- |
| [Booleans](#booleans-pythonic_fpbooleans) | [pythonic-fp-booleans][100] | [gh][200] | [gh_pages][300] | pythonic_fp.Booleans |
| [Circular Array](#circular-array-pythonic_fpcirculararray) | [pythonic-fp-circulararray][101] | [gh][201] | [gh_pages][301] | pythonic_fp.circulararray |
| [Containers](#containers-pythonic_fpcontainers) | [pythonic-fp-containers][102] | [gh][202] | [gh_pages][302] | pythonic_fp.containers |
| [FP Tools](#fp-tools-pythonic_fpfptools) | [pythonic-fp-fptools][103] | [gh][203] | [gh_pages][303] | pythonic_fp.fptools |
| [Gadgets](#gadgets-pythonic_fpgadgets) | [pythonic-fp][104] | [gh][204] | [gh_pages][304] | pythonic_fp.gadgets |
| [Iterables](#tools-for-iterables---pythonic_fpiterables) | [pythonic-fp-iterables][105] | [gh][205] | [gh_pages][305] | pythonic_fp.iterables |
| [Singletons](#useful-singletons---pythonic_fpsingletons) | [pythonic-fp-singletons][106] | [gh][206] | [gh_pages][306] | pythonic_fp.singletons |
| [Splitends](#splitends---pythonic_fpsplitends) | [pythonic-fp-splitends][107] | [gh][207] | [gh_pages][307] | pythonic_fp.splitends |

The overall project's name is **Pythonic FP** and consists of PyPI
projects all under the `pythonic-fp` project namespace. This corresponds
to the Python `pythonic_fp` package namespace.

## Namespace Projects

### Pythonic Functional Programming: pythonic-fp

The PyPI `pythonic-fp` project has several purposes.

- Its README.md file provides a "homepage" for the overall effort.
- It is used to claim the `pythonic-fp` namespace on PyPI.
- It hosts the Sphinx documentation for all the pythonic-fp namespace projects.
- It contains the source code for the pythonic-fp-gadgets project.

______________________________________________________________________

### Booleans pythonic_fp.booleans

Boolean type classes which interact well with Python's boolean
infrastructure.

- class **IBool:** Python's bool cannot be inherited from, this one can be
- class **SBool[H]:** Subclassed IBool from any hashable type

  - class **Truth[H]:** "truthy" **SBool[H]** subtype 
  - class **Lie[H]:** "falsy" **SBool[H]** subtype 

______________________________________________________________________

### Circular Array: pythonic_fp.circulararray

Stateful circular array data structures each with

- O(1) pops either end
- comparisons compare identity before equality, like builtins
- in boolean context returns true when not empty, false when empty
- iterable and reverse iterable, can safely be mutated
  - while previous iterators leisurely iterate over their previous state

Two types

- fixed storage capacity
  - O(1) pushes either end
  - O(1) indexing, does not support slicing
- variable storage capacity
  - O(1) amortized pushes either end
  - O(1) indexing, fully supports slicing
  - Auto-resizing larger storage capacity when necessary
  - manually compatible

______________________________________________________________________

### Containers: pythonic_fp.containers

Python package of container like data structures.

- **FTuple:** tuple-like object with a more FP interface
- **IList:** immutable list where hashability is enforced at runtime

______________________________________________________________________

### FP Tools: pythonic_fp.fptools

A Functional programming library for Python.

This library implements tools to aid in Python functional programming
in a way which endeavors to remain Pythonic.

______________________________________________________________________

### Gadgets: pythonic_fp.gadgets

The gadgets package is intended for **simple tools** with minimal
dependencies that may have multiple locations, or no good location,
to where they can go.

______________________________________________________________________

### Tools for Iterables - pythonic_fp.iterables

Tools for creating iterators from iterables.

- Concatenating and merging iterables
- Dropping and taking values from iterables
- Reducing and accumulating iterables

______________________________________________________________________

### Useful Singletons - pythonic_fp.singletons

Singleton classes representing

- missing values (actually missing, not potentially missing)
- sentinel values
- failed calculations

______________________________________________________________________

### Splitends - pythonic_fp.splitends

The splitends package implements a singularly linked LIFO queue called
a ``SplitEnd``. These data structures can safely share data nodes
between themselves and form branching *hair-like* data structures.


[100]: https://pypi.org/project/pythonic-fp-booleans
[101]: https://pypi.org/project/pythonic-fp-circulararray
[102]: https://pypi.org/project/pythonic-fp-containers
[103]: https://pypi.org/project/pythonic-fp-fptools
[104]: https://pypi.org/project/pythonic-fp
[105]: https://pypi.org/project/pythonic-fp-iterables
[106]: https://pypi.org/project/pythonic-fp-singletons
[107]: https://pypi.org/project/pythonic-fp-splitends
[200]: https://github.com/grscheller/pythonic-fp-booleans/README.rst
[201]: https://github.com/grscheller/pythonic-fp-circulararray/README.rst
[202]: https://github.com/grscheller/pythonic-fp-containers/README.rst
[203]: https://github.com/grscheller/pythonic-fp-fptools/README.rst
[204]: https://github.com/grscheller/pythonic-fp/README.rst
[205]: https://github.com/grscheller/pythonic-fp-iterables/README.rst
[206]: https://github.com/grscheller/pythonic-fp-singletons/README.rst
[207]: https://github.com/grscheller/pythonic-fp-splitends/README.rst
[300]: https://grscheller.github.io/pythonic-fp/booleans/development/build/html
[301]: https://grscheller.github.io/pythonic-fp/circulararray/development/build/html
[302]: https://grscheller.github.io/pythonic-fp/containers/development/build/html
[303]: https://grscheller.github.io/pythonic-fp/fptools/development/build/html
[304]: https://grscheller.github.io/pythonic-fp/gadgets/development/build/html
[305]: https://grscheller.github.io/pythonic-fp/iterables/development/build/html
[306]: https://grscheller.github.io/pythonic-fp/singletons/development/build/html
[307]: https://grscheller.github.io/pythonic-fp/splitends/development/build/html
