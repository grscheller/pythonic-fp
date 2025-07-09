# PyPI Pythonic FP Namespace Projects

Collection of Functional Programming (FP) oriented Python libraries.
While taking a functional programming approach, these packages endeavor
to remain Pythonic. Pythonic FP is a hobby project, but the maintainer
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
- Iterable, can safely mutate while iterators continue iterating over previous state

______________________________________________________________________

### Containers: pythonic_fp.containers

Python package implementing container-like classes.

- Single item box
  - holds at most one item of a given type
  - invariant in its contents
- Functional tuple
  - subclassed tuple
  - designed to be further inherited from
  - has a more FP interface
- Immutable list
  - hashability enforced when instantiated
  - mutable methods return new objects
- Maybe monad
  - data structure represents a possibly missing value
- Either monad
  - represents either a "left" or "right" value, never both
  - left biased

______________________________________________________________________

### FP Tools: pythonic_fp.fptools

Modules aiding in Functional programming.

- Subclassable boolean
  - Python's builtin bool cannot be subclassed
  - this one can
- Functions as first class objects
  - manipulate and partially apply functions
- Lazy function evaluation: non-strict function evaluation
- Singletons: three singleton classes representing
  - a missing value (actually missing, not potentially missing)
  - sentinel values
  - failed calculations
- The State monad

______________________________________________________________________

### Iterable Tools: pythonic_fp.iterables

Functions to work with iterables.

- merging iterables
- dropping and taking values from iterables
- accumulating and reducing iterables

______________________________________________________________________

### Queues: pythonic_fp.queues

Queue based data structures which provide the "bit twiddling" necessary
to guarantee behaviors supporting certain algorithmic use cases.

- FIFOQueue: First-In-First-Out Queue
- LIFOQueue: Last-In-First-Out Queue
- DEQueue: Double-Ended Queue

______________________________________________________________________

### Splitends: pythonic_fp.splitends

A singularly linked data structures allowing data sharing between
multiple instances. Very much Alpha level software.

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

[301]: https://grscheller.github.io/pythonic-fp-circulararray/html/api_pypi.html
[302]: https://grscheller.github.io/pythonic-fp-containers/html/api_pypi.html
[303]: https://grscheller.github.io/pythonic-fp-fptools/html/api_pypi.html
[304]: https://grscheller.github.io/pythonic-fp-iterables/html/api_pypi.html
[305]: https://grscheller.github.io/pythonic-fp-queues/html/api_pypi.html
[306]: https://grscheller.github.io/pythonic-fp-splitends/html/api_pypi.html
