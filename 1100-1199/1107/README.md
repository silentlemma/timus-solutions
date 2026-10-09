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

- the input holds up to five million numbers, so reading must be fast:
  plain `scanf` or a token list per number is too slow or too large;
- equal multisets would share a group, but the input guarantees all of
  them are distinct.

The answers were checked by the hash checker on every test; the checker
itself was compared with a pairwise test of every two multisets on a
hundred small inputs, with correct and random assignments.

## Language notes

- C++, Go and Java read the bytes through their own buffered number
  readers.
- Python reads the whole input at once and splits it into lines; a token
  list of all five million numbers would not fit in 64 MB, and reading
  line by line is twice as slow.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1107_math.cpp](1107_math.cpp) | G++ 13.2 x64 | math | O(total size) | AC | 0.015 s | 404 KB |
| [1107_math.go](1107_math.go) | Go 1.14 x64 | math | O(total size) | AC | 0.046 s | 980 KB |
| [1107_math.java](1107_math.java) | Java 1.8 | math | O(total size) | AC | 0.078 s | 1608 KB |
| [1107_math.py](1107_math.py) | Python 3.12 x64 | math | O(total size) | AC | 0.562 s | 16972 KB |
| [1107_math.rs](1107_math.rs) | Rust 1.75 x64 | math | O(total size) | AC | 0.031 s | 9300 KB |
