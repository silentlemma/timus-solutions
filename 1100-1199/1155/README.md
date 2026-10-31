# 1155. Clearing particles from the corners of a cube by pairs

[Timus 1155](https://acm.timus.ru/problem.aspx?space=1&num=1155) · difficulty 171 · constructive

Original problem from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Eight chambers `A` to `H` sit at the corners of a cube (`A B C D` around
one face, `E F G H` above them in the same order), each holding 0 to 100
particles. One operation creates or destroys two particles in two
neighbouring chambers, one in each. Print at most 1000 operations that
empty every chamber, or `IMPOSSIBLE`.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

One line with eight integers from 0 to 100, for `A` to `H` in order.

## Output

One operation per line: the two chambers and `+` or `-`; or
`IMPOSSIBLE`.

## Checking

Any valid sequence is accepted. The checker replays the operations: each
must join neighbouring chambers, no chamber may go below zero, there may
be at most 1000 of them, and all chambers must end empty. `IMPOSSIBLE`
must be printed exactly when the sides below differ.

## Examples

### Example 1

Input:

```
1 0 1 0 3 1 0 0
```

Output:

```
EF-
AE-
BA+
CB-
AE-
```

### Example 2

Input:

```
0 1 0 1 2 3 2 2
```

Output:

```
IMPOSSIBLE
```

## Solution

Colour the corners like a chessboard: `A C F H` on one side and
`B D E G` on the other. Every edge joins the two sides, so every operation
changes both side totals by the same amount, and their difference never
changes. If the difference is not zero, the answer is `IMPOSSIBLE`.

Otherwise, first go over the twelve edges once and destroy as many pairs
on each as both ends allow. Counts only fall, so afterwards every edge
has an empty end. A corner that still holds particles then has all three
neighbours empty, and its opposite corner, which is the only one of the
other side not next to it, holds all the particles of that side. Since
the totals are equal, what is left is `k` particles in each of two
opposite corners `u` and `w`. They are three edges apart, `u x y w`, and
the triple "create on `x y`, destroy on `u x`, destroy on `y w`" removes
one from each. The first pass takes at most 400 operations and the
leftover at most `3·100`, so the 1000 limit is never reached.

Pitfalls:

- a pair can be destroyed only if both chambers hold a particle, so the
  creation comes first in each triple;
- all-zero counts need no operations at all (test 03);
- all eight counts must be on one line; splitting them across lines is
  outside the input format, and Python reads only the first line;
- `IMPOSSIBLE` depends only on the two side totals, not on how the
  particles are spread.

The answers were checked by the checker on all 13 stored and generated
test cases. Independent oracle and operation replay checks passed on
3000 random small inputs and 374 boundary cases, with at most 500 operations.

## Optimized solutions

The optimized C++ solution prints the same operations, but keeps the
counts and the three neighbours of every corner in small fixed arrays
indexed by the letter of the corner instead of `std::map`, reads with
`scanf` instead of `iostream`, and prints every operation with `printf`
right away instead of collecting the whole output in a string:
{1155_constructive_optimized.cpp}.

The optimized Java solution prints the same operations, but keeps the
counts and the three neighbours of every corner in fixed arrays indexed
by the letter of the corner instead of maps of boxed characters and
lists built by lambdas, and reads the eight numbers byte by byte from
4 KB blocks instead of with `Scanner`:
{1155_constructive_optimized.java}.

The optimized Rust solution prints the same operations, but keeps the
counts and the three neighbours of every corner in fixed arrays indexed
by the letter of the corner instead of hash maps, and writes every
operation straight to a `BufWriter` instead of collecting the whole
output in a string: {1155_constructive_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1155_constructive_optimized.cpp`: time reduction -106.67%; memory
  reduction +75.25%; base: `1155_constructive.cpp`.

- `1155_constructive_optimized.java`: time reduction +40.38%; memory
  reduction +88.26%; base: `1155_constructive.java`.

- `1155_constructive_optimized.rs`: time reduction +0.00%; memory
  reduction +50.46%; base: `1155_constructive.rs`.

## Language notes

- All languages go over the edges in the same order and print the same
  operations.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1155_constructive.cpp](1155_constructive.cpp) | G++ 13.2 x64 | constructive | O(total) | AC | 0.015 s | 404 KB | 11281010 |
| [1155_constructive.go](1155_constructive.go) | Go 1.14 x64 | constructive | O(total) | AC | 0.031 s | 1116 KB | 11281106 |
| [1155_constructive.java](1155_constructive.java) | Java 1.8 | constructive | O(total) | AC | 0.156 s | 3884 KB | 11281181 |
| [1155_constructive.py](1155_constructive.py) | Python 3.12 x64 | constructive | O(total) | AC | 0.078 s | 612 KB | 11281128 |
| [1155_constructive.rs](1155_constructive.rs) | Rust 1.75 x64 | constructive | O(total) | AC | 0.015 s | 436 KB | 11281207 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1155_constructive_optimized.cpp](1155_constructive_optimized.cpp) \* | G++ 13.2 x64 | constructive | O(total) | AC | 0.031 s | 100 KB | 11307258 |
| [1155_constructive_optimized.java](1155_constructive_optimized.java) \* | Java 1.8 | constructive | O(total) | AC | 0.093 s | 456 KB | 11307261 |
| [1155_constructive_optimized.rs](1155_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(total) | AC | 0.015 s | 216 KB | 11307262 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
