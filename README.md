# PyPI Pythonic FP Namespace Projects

Collection of Functional Programming (FP) oriented Python libraries.
While taking a functional programming approach, these packages endeavor
to remain Pythonic.
:wq
Pythonic FP is a hobby project, but the maintainer
is serious about its quality.

## Pythonic FP

The overall project's name is **Pythonic FP** and consists of PyPI Python projects all under the
`pythonic-fp` namespace.

| Name | Python Package | PyPI | GitHub | Docs |
|:---- |:-------------- |:----:|:------:|:----:|
| Circular Array | pythonic_fp.circulararray | [pythonic-fp.circulararray][101] | [pythonic-fp-circulararray][201] | [docs][301] |
| Containers | pythonic_fp.containers | [pythonic-fp.containers][102] | [pythonic-fp-containers][202] | [docs][302] |
| FP Tools | pythonic_fp.fptools | [pythonic-fp.fptools][103] | [pythonic-fp-fptools][203] | [docs][303] |
| Iterables | pythonic_fp.iterables | [pythonic-fp.iterables][104] | [pythonic-fp-iterables][204] | [docs][304] |
| Queues | pythonic_fp.queues | [pythonic-fp.queues][105] | [pythonic-fp-queues][205] | [docs][305] |
| Splitends | pythonic_fp.splitends | [pythonic-fp.splitends][106] | [pythonic-fp-splitends][206] | [docs][306] |

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

| Description | Module |
|:-----------:|:------:|
| Single item box | `pythonic_fp.containers.box` |
| Functional tuple | `pythonic_fp.containers.functional_tuple` |
| Immutable list | `pythonic_fp.containers.immutable_list` |
| Maybe monad | `pythonic_fp.containers.maybe` |
| Either monad | `pythonic_fp.containers.xor` |

______________________________________________________________________

### FP Tools: pythonic_fp.fptools

Tools to aid with functional programming in Python yet still endeavoring to
remain Pythonic.

- Subclassable Boolean datatype (pythonic_fp.fptools.bool)
- Functions as first class objects (pythonic_fp.fptools.function)
- Lazy (non-strict) function evaluation (pythonic_fp.fptools.lazy)
- Singletons (pythonic_fp.fptools.singletons)
  - 3 singleton classes representing
    - a missing value (actually missing, not potentially missing)
    - a sentinel values
    - a failed calculation
- State monad implementation (pythonic_fp.fptools.state)
  - pure FP handling of state (the state monad)
  - Classic FP implementation
    - the monad encapsulates a state transformation, not a "state"

______________________________________________________________________

### Iterable Tools: pythonic_fp.iterables

- Concatenating and merging iterables
- Dropping and taking values from iterables
- Reducing and accumulating iterables

______________________________________________________________________

### Queues: pythonic_fp.queues

Queue based data structures which provide the "bit twiddling" necessary
to guarantee behaviors supporting certain algorithmic use cases.

- FIFOQueue: First-In-First-Out Queue
- LIFOQueue: Last-In-First-Out Queue
- DEQueue: Double-Ended Queue

______________________________________________________________________

### Splitends: pythonic_fp.splitends

Python package Implementing a singularly linked LIFO queue called
a ``SplitEnd``. These data structures can safely share data nodes
between themselves.

______________________________________________________________________

### Basename Project: pythonic_fp

**DO NOT INSTALL**

The PyPI `pythonic-fp` project's sole purpose is to claim the name on
PyPI. Do not install it, otherwise all `pythonic-fp` namespace projects
will **break**.

I don't want to cause anyone any confusion if someone chooses the name
because PyPI said it was available.

Its source code is in the name_claim directory.

______________________________________________________________________

[101]: https://pypi.org/project/pythonic-fp.circulararray
[102]: https://pypi.org/project/pythonic-fp.containers
[103]: https://pypi.org/project/pythonic-fp.fptools
[104]: https://pypi.org/project/pythonic-fp.iterables
[105]: https://pypi.org/project/pythonic-fp.queues
[106]: https://pypi.org/project/pythonic-fp.splitends
[201]: https://github.com/grscheller/pythonic-fp-circulararray
[202]: https://github.com/grscheller/pythonic-fp-containers
[203]: https://github.com/grscheller/pythonic-fp-fptools
[204]: https://github.com/grscheller/pythonic-fp-iterables
[205]: https://github.com/grscheller/pythonic-fp-queues
[206]: https://github.com/grscheller/pythonic-fp-splitends
[301]: https://grscheller.github.io/pythonic-fp/circulararray/API/development/build/html/releases.html
[302]: https://grscheller.github.io/pythonic-fp/containers/API/development/build/html/releases.html
[303]: https://grscheller.github.io/pythonic-fp/fptools/API/development/build/html/releases.html
[304]: https://grscheller.github.io/pythonic-fp/iterables/API/development/build/html/releases.html
[305]: https://grscheller.github.io/pythonic-fp/queues/API/development/build/html/releases.html
[306]: https://grscheller.github.io/pythonic-fp/splitends/API/development/build/html/releases.html
