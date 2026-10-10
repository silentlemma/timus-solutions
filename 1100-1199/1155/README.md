# 1155. Clearing particles from the corners of a cube by pairs

[Timus 1155](https://acm.timus.ru/problem.aspx?space=1&num=1155) · difficulty 178 · constructive

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

Eight counts, for `A` to `H`.

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
- empty input needs no operations at all;
- `IMPOSSIBLE` depends only on the two side totals, not on how the
  particles are spread.

The answers were checked by the checker on every test and on 3000 random
inputs, the longest of which needed 442 operations.

## Language notes

- All languages go over the edges in the same order and print the same
  operations.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1155_constructive.cpp](1155_constructive.cpp) | G++ 13.2 x64 | constructive | O(total) | AC | 0.015 s | 404 KB |
| [1155_constructive.go](1155_constructive.go) | Go 1.14 x64 | constructive | O(total) | AC | 0.031 s | 1116 KB |
| [1155_constructive.java](1155_constructive.java) | Java 1.8 | constructive | O(total) | AC | 0.156 s | 3884 KB |
| [1155_constructive.py](1155_constructive.py) | Python 3.12 x64 | constructive | O(total) | AC | 0.078 s | 612 KB |
| [1155_constructive.rs](1155_constructive.rs) | Rust 1.75 x64 | constructive | O(total) | AC | 0.015 s | 436 KB |
