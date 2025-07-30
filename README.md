# PyPI Pythonic FP Namespace Projects

Collection of Functional Programming (FP) oriented Python libraries.
While taking a functional programming approach, these packages endeavor
to remain Pythonic.

Pythonic FP is a hobby project, but the maintainer is serious about its quality.

## Pythonic FP

The overall project's name is **Pythonic FP** and consists of PyPI Python projects
all under the `pythonic-fp` namespace.

| Name | Python Package | PyPI | GitHub | Docs |
|:---- |:-------------- |:----:|:------:|:----:|
| Circular Array | pythonic_fp.circulararray | [pythonic-fp.circulararray][101] | [pythonic-fp-circulararray][201] | [docs][301] |
| Containers | pythonic_fp.containers | [pythonic-fp.containers][102] | [pythonic-fp-containers][202] | [docs][302] |
| FP Tools | pythonic_fp.fptools | [pythonic-fp.fptools][103] | [pythonic-fp-fptools][203] | [docs][303] |
| Gadgets | pythonic_fp.gadgets | [pythonic-fp.gadgets][104] | [pythonic-fp-gadgets][204] | [docs][304] |
| Iterables | pythonic_fp.iterables | [pythonic-fp.iterables][105] | [pythonic-fp-iterables][205] | [docs][305] |
| Splitends | pythonic_fp.splitends | [pythonic-fp.splitends][106] | [pythonic-fp-splitends][206] | [docs][306] |
| Queues (deprecated) | pythonic_fp.queues | [pythonic-fp.queues][107] | [pythonic-fp-queues][207] | [docs][307] |

## Namespace Projects

### Circular Array: pythonic_fp.circulararray

Python module implementing a stateful circular array data structure.

- O(1) pops either end
- O(1) amortized pushes either end
- O(1) indexing, fully supports slicing
- Auto-resizing larger when necessary, manually compatible
- iterable, can safely mutate while iterators continue iterating over previous state
- comparisons compare identity before equality, like builtins
- in boolean context returns true when not empty, false when empty

______________________________________________________________________

### Containers: pythonic_fp.containers

Python package of container like data structures.

______________________________________________________________________

### pythonic_fp.fptools

Functional programming library for Python.

This library implements tools to aid in Python functional programming
in a way which endeavors to be Pythonic.

______________________________________________________________________

### pythonic_fp.gadgets

Queue based data structures which provide the "bit twiddling" necessary
to guarantee behaviors supporting certain algorithmic use cases.

- Box: Single item box

______________________________________________________________________

### pythonic_fp.iterables

Tools for creating iterators from iterables.

- Concatenating and merging iterables
- Dropping and taking values from iterables
- Reducing and accumulating iterables

______________________________________________________________________

### pythonic_fp.singletons

Singleton classes representing

- missing values (actually missing, not potentially missing)
- sentinel values
- failed calculations
- subtypeable Booleans

______________________________________________________________________

### pythonic_fp.splitends

The splitends package implements a singularly linked LIFO queue called
a ``SplitEnd``. These data structures can safely share data nodes
between themselves and form branching *hair-like* data structures.

______________________________________________________________________

## Basename Project

### pythonic_fp

**DO NOT INSTALL**

The PyPI `pythonic-fp` project's sole purpose is to claim the name on
PyPI. Do not install it, otherwise all `pythonic-fp` namespace projects
will **break**.

I don't want to cause any confusion if someone chooses the name
``pythonic-fp`` for their project because PyPI said it was available.

The source code for this "project" is located in the name_claim
directory.

______________________________________________________________________

[101]: https://pypi.org/project/pythonic-fp.circulararray
[102]: https://pypi.org/project/pythonic-fp.containers
[103]: https://pypi.org/project/pythonic-fp.fptools
[104]: https://pypi.org/project/pythonic-fp.gadgets
[105]: https://pypi.org/project/pythonic-fp.iterables
[106]: https://pypi.org/project/pythonic-fp.splitends
[107]: https://pypi.org/project/pythonic-fp.queues
[201]: https://github.com/grscheller/pythonic-fp-circulararray
[202]: https://github.com/grscheller/pythonic-fp-containers
[203]: https://github.com/grscheller/pythonic-fp-fptools
[204]: https://github.com/grscheller/pythonic-fp-gadgets
[205]: https://github.com/grscheller/pythonic-fp-iterables
[206]: https://github.com/grscheller/pythonic-fp-splitends
[207]: https://github.com/grscheller/pythonic-fp-queues
[301]: https://grscheller.github.io/pythonic-fp/circulararray/development/build/html
[302]: https://grscheller.github.io/pythonic-fp/containers/development/build/html
[303]: https://grscheller.github.io/pythonic-fp/fptools/development/build/html
[304]: https://grscheller.github.io/pythonic-fp/gadgets/development/build/html
[305]: https://grscheller.github.io/pythonic-fp/iterables/development/build/html
[306]: https://grscheller.github.io/pythonic-fp/splitends/development/build/html
[307]: https://grscheller.github.io/pythonic-fp/deprecated/queues/development/build/html
