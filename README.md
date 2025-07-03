# PyPI Pythonic FP Namespace Projects

Collection of Functional Programming (FP) oriented Python libraries.
While taking a functional programming approach, these packages endeavor
to remain Pythonic. Pythonic FP is a hobby project, but the maintainer
is serious about its quality.

## Pythonic FP

The overall project's name is **Pythonic FP** and consists of PyPI Python projects all under the
`pythonic-fp` namespace.

| Name | Python Package | PyPI Release Docs | Current Dev Docs | PyPI Name | GitHub Name |
|:---- |:--------------:|:-----------------:|:----------------:|:---------:|:-----------:|
| Circular Array | pythonic_fp.circulararray | [GH-Pages][101] | [GH-Pages][201] | [PyPI][301] | [GitHub][401] |
| Containers | pythonic_fp.containers | [GH-Pages][102] | [GH-Pages][202] | [PyPI][302] | [GitHub][402] |
| FP Tools | pythonic_fp.fptools | [GH-Pages][103] | [GH-Pages][203] | [PyPI][303] | [GitHub][403] |
| Iterables | pythonic_fp.iterables | [GH-Pages][104] | [GH-Pages][203] | [PyPI][304] | [GitHub][404] |
| Queues | pythonic_fp.queues | [GH-Pages][105] | [GH-Pages][205] | [PyPI][305] | [GitHub][405] |
| Splitends | pythonic_fp.splitends | [GH-Pages][106] | [GH-Pages][206] | [PyPI][306] | [GitHub][406] |


### Stub project

Project `pythonic-fp` sole purpose is to claim the name on PyPI. **DO NOT INSTALL IT**, otherwise
all `pythonic-fp` namespace projects will break. I don't want to cause anyone any confusion if
they should choose the name because PyPI says it is available. Its source code is in the name_claim
directory.

______________________________________________________________________

## Circular Array

Python module implementing a stateful circular array data structure.

- O(1) pops either end
- O(1) amortized pushes either end
- O(1) indexing, fully supports slicing
- Auto-resizing larger when necessary, manually compatible
- Iterable, can safely mutate while iterators continue iterating over previous state

______________________________________________________________________

## Containers

Python package implementing container-like classes.

- Single item box: holds at most one item of a given type, invariant in its contents
- Functional tuple: subclassed tuple, designed to be further inherited from, more FP interface
- Immutable list: hashability enforced when instantiated, mutable methods return new objects
- Maybe monad: data structure represents a possibly missing value
- Either monad: left biased, represents a "left" or "right" value, never both

______________________________________________________________________

## FP Tools

Modules aiding in Functional programming. TODO: break some out to separate repos.

- Subclassable boolean: Python bool cannot be subclassed, this on can
- Functions as first class objects: utilities to manipulate and partially apply functions
- Lazy function evaluation: non-strict function evaluation
- Singletons: three singleton classes representing
  - a missing value (actually missing, not potentially missing)
  - sentinel values
  - failed calculations
- The State monad

______________________________________________________________________

## Iterable Tools

Functions to work with iterables.

- merging iterables
- dropping and taking values from iterables
- accumulating and reducing iterables

______________________________________________________________________

## Queues

Data structures providing the "bit twiddling" necessary to guarantee behaviors supporting certain
algorithmic use cases.

- FIFOQueue: First-In-First-Out Queue
- LIFOQueue: Last-In-First-Out Queue
- DEQueue: Double-Ended Queue

______________________________________________________________________

## Splitends

A singularly linked data structures allowing data sharing between multiple instances.

______________________________________________________________________

[101]: https://grscheller.github.io/pythonic-fp/circulararray
[102]: https://grscheller.github.io/pythonic-fp/containers
[103]: https://grscheller.github.io/pythonic-fp/fptools
[104]: https://grscheller.github.io/pythonic-fp/iterables
[105]: https://grscheller.github.io/pythonic-fp/queues
[106]: https://grscheller.github.io/pythonic-fp/splitends

[201]: https://grscheller.github.io/pythonic-fp-circulararray/html
[202]: https://grscheller.github.io/pythonic-fp-containers/html
[203]: https://grscheller.github.io/pythonic-fp-fptools/html
[204]: https://grscheller.github.io/pythonic-fp-iterables/html
[205]: https://grscheller.github.io/pythonic-fp-queues/html
[206]: https://grscheller.github.io/pythonic-fp-splitends/html

[301]: https://pypi.org/project/pythonic-fp.circulararray
[302]: https://pypi.org/project/pythonic-fp.containers
[303]: https://pypi.org/project/pythonic-fp.fptools
[304]: https://pypi.org/project/pythonic-fp.iterables
[305]: https://pypi.org/project/pythonic-fp.queues
[306]: https://pypi.org/project/pythonic-fp.splitends

[401]: https://github.com/grscheller/pythonic-fp-circulararray
[402]: https://github.com/grscheller/pythonic-fp-containers
[403]: https://github.com/grscheller/pythonic-fp-fptools
[404]: https://github.com/grscheller/pythonic-fp-iterables
[405]: https://github.com/grscheller/pythonic-fp-queues
[406]: https://github.com/grscheller/pythonic-fp-splitends





