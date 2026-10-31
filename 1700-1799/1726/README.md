# 1726. Visits

[Timus 1726](https://acm.timus.ru/problem.aspx?space=1&num=1726) · difficulty 120 · sorting

Original problem by Denis Dublennykh, from the Ural Regional Team Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The n members of a committee live at street crossings of a grid city
and walk to each other along the streets by shortest paths. Everyone
visits everyone equally often. Find the average walking distance,
rounded down.

## Input

n (2 ≤ n ≤ 10⁵) on the first line, then n lines with coordinates x and
y (1 ≤ x, y ≤ 10⁶).

## Output

The average distance between two members' houses, rounded down.

## Examples

### Example 1

Input:

```
3
10 10
20 20
10 20
```

Output:

```
13
```

## Solution

A shortest walk along the streets has length |dx| + |dy|, so the sum
over all pairs splits into the sum of |x_i − x_j| and the sum of
|y_i − y_j|. Sort the x values: the i-th one (from 0) is at least each
of the i before it, so it adds i·x_i minus their sum, which a running
total keeps. The same goes for y. The average over the n(n − 1)/2
pairs is that sum divided by the number of pairs, rounded down.
`O(n log n)`.

In the example the distances are 20, 10 and 10, so the average is
40/3, rounded down to 13.

Pitfalls:

- the sum reaches about 5·10¹⁵ when half of the houses stand in each of
  two far corners, so it needs 64 bits;
- comparing all pairs directly takes about 5·10⁹ steps, far too many.

The averages match a sum over all pairs on 300 small random maps, and
an independent accepted implementation on the large tests.

## Optimized solutions

The optimized C++ solution keeps the coordinates in static `int` arrays,
which hold them since they are at most 10⁶, instead of vectors of
`long long`, and parses the 2·10⁵ numbers by hand from 4 KB blocks read
with `fread` instead of calling `scanf` for each; the sums are still
taken in `long long`: {1726_sorting_optimized.cpp}.

The optimized Go solution parses the 2·10⁵ numbers by hand from a 64 KB
buffered reader instead of `fmt.Fscan`, which is the slow part of the
simple program: {1726_sorting_optimized.go}.

The optimized Python solution reads the lines in batches of about 64 KB
into arrays of 32-bit integers, which hold the coordinates since they
are at most 10⁶, instead of keeping every token of the input as a byte
string and two lists of Python integers. It also computes each sum
without a Python loop: in sorted order the `i`-th of `n` values (from 0)
is at least the `i` before it and at most the `n − 1 − i` after it, so
it enters the sum with weight `2i − (n − 1)`, and `sum(map(mul, …))`
over the sorted values and a `range` of weights runs entirely in C:
{1726_sorting_optimized.py}.

The optimized Rust solution parses the numbers by hand from 4 KB blocks
instead of reading the whole input into a string, and keeps the
coordinates as `u32`, which holds them since they are at most 10⁶,
instead of `i64`; the sums are taken in `u64`:
{1726_sorting_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1726_sorting_optimized.cpp`: time reduction +91.23%; memory reduction
  +49.43%; base: `1726_sorting.cpp`.

- `1726_sorting_optimized.go`: time reduction +70.51%; memory reduction
  +37.78%; base: `1726_sorting.go`.

- `1726_sorting_optimized.py`: time reduction +0.00%; memory reduction
  +70.45%; base: `1726_sorting.py`.

- `1726_sorting_optimized.rs`: time reduction +0.00%; memory reduction
  +79.09%; base: `1726_sorting.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1726_sorting.cpp](1726_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.171 s | 1756 KB | 11304062 |
| [1726_sorting.go](1726_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.156 s | 4404 KB | 11304355 |
| [1726_sorting.java](1726_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.125 s | 2092 KB | 11304357 |
| [1726_sorting.py](1726_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.187 s | 20644 KB | 11304063 |
| [1726_sorting.rs](1726_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 4744 KB | 11304064 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1726_sorting_optimized.cpp](1726_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 888 KB | 11304358 |
| [1726_sorting_optimized.go](1726_sorting_optimized.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.046 s | 2740 KB | 11304362 |
| [1726_sorting_optimized.py](1726_sorting_optimized.py) \* | Python 3.12 x64 | sorting | O(n log n) | AC | 0.187 s | 6100 KB | 11304360 |
| [1726_sorting_optimized.rs](1726_sorting_optimized.rs) \* | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 992 KB | 11304361 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
