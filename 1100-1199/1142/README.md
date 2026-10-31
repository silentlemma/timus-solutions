# 1142. Counting the orderings with ties of N objects

[Timus 1142](https://acm.timus.ru/problem.aspx?space=1&num=1142) · difficulty 155 · combinatorics

Original problem on Timus; its author and source are not given.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Between any two of `N` comparable objects one of `a = b`, `a < b`,
`b < a` holds. Count the different ways to order `N` objects in this
sense, allowing ties: for three objects there are 13, from
`a = b = c` to `c < b < a`. Answer this for several `N` from 2 to 10; the
input ends with `-1`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Values of `N`, one per line, then `-1`.

## Output

The count for each `N`, one per line.

## Examples

### Example 1

Input:

```
2
3
-1
```

Output:

```
3
13
```

## Solution

An ordering with ties is a sequence of groups of equal objects, the
groups strictly increasing. Look at the first group: it is any nonempty
set of `k` objects, chosen in `C(n, k)` ways, and the remaining `n − k`
objects form an ordering with ties of their own. So with `a(0) = 1`

`a(n) = Σ_{k=1..n} C(n, k)·a(n − k)`.

These are the ordered Bell (Fubini) numbers 1, 1, 3, 13, 75, 541, …; the
largest needed, `a(10) = 102247563`, fits in 32 bits. The table is built
once with Pascal's triangle, and each query is a lookup. `O(10²)` to build.

Pitfalls:

- the input has no count; read until `-1`;
- the same `N` may be asked several times.

The values were compared with the independent formula
`a(n) = Σ k!·S(n, k)` with Stirling numbers of the second kind, and for
`n ≤ 6` with a listing of all orderings.

## Optimized solutions

The optimized Java solution reads the queries with `StreamTokenizer`
over a `BufferedReader` instead of `Scanner`, whose regular-expression
machinery costs time and memory to load, and prints each answer through
a buffered `PrintWriter` at once instead of collecting all of them in a
`StringBuilder`: {1142_combinatorics_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1142_combinatorics_optimized.java`: time reduction -34.41%; memory
  reduction +74.81%; base: `1142_combinatorics.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1142_combinatorics.cpp](1142_combinatorics.cpp).
- [1142_combinatorics.go](1142_combinatorics.go).
- [1142_combinatorics.rs](1142_combinatorics.rs).

- All languages build the same table before reading the queries.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics.cpp](1142_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(1) per query | AC | 0.001 s | 128 KB | 11279451 |
| [1142_combinatorics.go](1142_combinatorics.go) | Go 1.14 x64 | combinatorics | O(1) per query | AC | 0.001 s | 1084 KB | 11279453 |
| [1142_combinatorics.java](1142_combinatorics.java) | Java 1.8 | combinatorics | O(1) per query | AC | 0.093 s | 1604 KB | 11279455 |
| [1142_combinatorics.py](1142_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) per query | AC | 0.031 s | 436 KB | 11279454 |
| [1142_combinatorics.rs](1142_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(1) per query | AC | 0.001 s | 220 KB | 11279457 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1142_combinatorics_optimized.java](1142_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(1) per query | AC | 0.125 s | 404 KB | 11305854 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
