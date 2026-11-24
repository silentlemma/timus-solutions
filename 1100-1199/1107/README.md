# 1107. Separating multisets that differ by one item

[Timus 1107](https://acm.timus.ru/problem.aspx?space=1&num=1107) · difficulty 424 · math

Original problem by Dmitry Filimonenkov, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `K ≤ 50 000` distinct multisets of items numbered `1..N`, each
with 1 to 100 elements; the order of elements does not matter, repeats
do. Two multisets are similar if one becomes the other by removing one
element, or by replacing one element with a different item. Assign each
multiset one of `M` groups (`0 < N < M ≤ 100`) so that no two similar
multisets share a group, or print `NO` if that is impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N K M`, then `K` lines: the size of a multiset followed by its elements,
separated by single spaces.

## Output

`YES`, then the group of each multiset, one per line, in input order; or
`NO`.

## Checking

Any valid assignment is accepted. The checker hashes every multiset as a
sum of random 64-bit weights of its elements: a multiset one removal away
from another, or two multisets one replacement apart, then share the hash
of a multiset with one element removed, and such a pair must not be in
one group.

## Examples

### Example 1

Input:

```
8 20 12
5 1 3 5 6 4
5 1 3 5 6 3
4 5 6 3 3
4 5 6 3 4
4 4 6 5 8
4 7 7 7 7
3 7 7 7
2 2 2
3 2 2 7
3 1 2 3
3 1 2 4
10 1 2 3 4 5 6 7 8 7 6
10 8 7 6 5 4 3 2 1 2 1
20 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 3 5 7
5 4 6 4 6 4
5 6 4 6 4 6
6 6 6 6 6 6 6
3 6 6 6
1 1
1 2
```

Output:

```
YES
2
1
9
1
6
2
4
5
3
7
8
5
4
8
7
9
1
1
2
3
```

## Solution

The answer is always `YES`: put a multiset with element sum `S` into
group `S mod (N + 1) + 1`, which exists because `M ≥ N + 1`. Removing an
element changes the sum by its value, `1..N`; replacing one item with
another changes it by a nonzero amount between `−(N − 1)` and `N − 1`.
Neither change is a multiple of `N + 1`, so similar multisets always get
different groups. `O(total size)`.

Pitfalls:

- the input holds up to five million items, so reading must be fast:
  plain `scanf` or a token list per number is too slow or too large;
- equal multisets would share a group, but the input guarantees all of
  them are distinct.

The answers were checked by the hash checker on every test; the checker
itself was compared with a pairwise test of every two multisets on a
hundred small inputs, with correct and random assignments.

## Optimized solutions

The new C++, Go, Python and Rust implementations keep the sum-modulo-(N+1) construction. Removing an item changes the sum by 1..N; replacing one changes it by a nonzero value of absolute magnitude at most N−1. Neither change vanishes modulo N+1, so each group contains no forbidden pair. Process each collection once without retaining all its items. C++, Go and Rust use bounded input/output buffers; Python reads one collection per line and accumulates only the group labels in a bytearray. For S input items, time is O(S). Python additionally stores one input line and O(K) output bytes; the other versions use bounded auxiliary storage. The ordinary implementations and already-admitted Java base remain available.

The accepted G++ 13.2 x64 run takes 0.062 s versus 0.015 s for the base and uses 92 KB versus 404 KB.

The accepted base implementations [1107_math.java](1107_math.java) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- C++, Go and Java read the bytes through their own buffered number
  readers.
- Python reads the whole input at once and splits it into lines; a token
  list of all five million numbers would not fit in 64 MB, and reading
  line by line is twice as slow.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1107_math.cpp](1107_math.cpp) | G++ 13.2 x64 | math | O(total size) | AC | 0.015 s | 404 KB | 11279187 |
| [1107_math.go](1107_math.go) | Go 1.14 x64 | math | O(total size) | AC | 0.046 s | 980 KB | 11279188 |
| [1107_math.java](1107_math.java) | Java 1.8 | math | O(total size) | AC | 0.078 s | 1608 KB | 11279190 |
| [1107_math.py](1107_math.py) | Python 3.12 x64 | math | O(total size) | AC | 0.562 s | 16972 KB | 11279189 |
| [1107_math.rs](1107_math.rs) | Rust 1.75 x64 | math | O(total size) | AC | 0.031 s | 9300 KB | 11279191 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1107_math_optimized.cpp](1107_math_optimized.cpp) | G++ 13.2 x64 | math | O(S) | AC | 0.062 s | 92 KB | 11314882 |
| [1107_math_optimized.go](1107_math_optimized.go) | Go 1.14 x64 | math | O(S) | AC | 0.046 s | 284 KB | 11314885 |
| [1107_math_optimized.py](1107_math_optimized.py) | Python 3.12 x64 | math | O(S) | AC | 0.531 s | 608 KB | 11314887 |
| [1107_math_optimized.rs](1107_math_optimized.rs) | Rust 1.75 x64 | math | O(S) | AC | 0.015 s | 44 KB | 11314890 |
