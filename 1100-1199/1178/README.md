# 1178. Pairing up cities with straight roads that do not cross

[Timus 1178](https://acm.timus.ru/problem.aspx?space=1&num=1178) · difficulty 151 · geometry

Original problem by Pavel Atnashev, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There is an even number `N ≤ 10000` of cities at integer points with
coordinates up to `10⁹` in absolute value, no three on one line. Join
them in pairs by straight roads, each city in exactly one road, so that no
two roads cross.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines, each with the two coordinates of a city.

## Output

`N/2` lines, each with the numbers of the two cities a road joins.

## Checking

Any plan is accepted if it pairs every city exactly once and no two roads
meet; the checker compares the roads whose x-ranges overlap.

## Examples

### Example 1

Input:

```
4
0 2
1 1
3 4
4 4
```

Output:

```
1 3
2 4
```

## Solution

Sort the cities by `x` and join the first with the second, the third
with the fourth, and so on. Each road then lies in its own vertical strip
between the `x` of its ends, and the strips of different roads overlap at
most in one border line. On that line each road has only an end, and the
ends are different cities, so the roads do not meet there. A road can be
vertical when its two cities share `x`, but then no other city lies on
that line, as no three cities are on one line. So no two roads meet.
`O(N log N)`.

Pitfalls:

- ties on `x` need no special care, though the solutions break them by
  `y` to make the output reproducible;
- coordinates reach `10⁹` and fit in 32-bit integers; the solution
  only compares them.

Every printed plan passed the checker on all tests, including ten
thousand cities on conics with many shared `x` values.

## Optimized solutions

The optimized Java solution parses the numbers by hand from a 4 KB
buffer instead of collecting all lines into one string for a
`StringTokenizer`, and sorts a plain `long` array instead of boxed
`Integer` city numbers with a comparator. Each key is `x + 10⁹`, at most
2·10⁹ and so 31 bits, shifted above the 14-bit city index (less than
10000 < 2¹⁴). Only `x` is in the key: since no three cities are on one
line, at most two share an `x`, and one pass afterwards swaps such a
neighbouring pair when their `y` are in the wrong order:
{1178_geometry_optimized.java}.

The optimized Python solution relies on one city per line and reads the
lines one by one instead of splitting the whole input. It packs each
city into one integer, `x + 10⁹` and `y + 10⁹` of 31 bits each above the
14-bit city number, so that a plain `sort` orders the cities by `(x, y)`
without a key function or tuples, and it writes the pairs as it goes
instead of collecting a list of lines: {1178_geometry_optimized.py}.

The optimized Rust solution parses the numbers by hand from a 4 KB
buffer instead of reading the whole input into a `String` and a vector
of all numbers. It sorts `(x, y, number)` tuples of `i32`, enough for
coordinates up to `10⁹` in absolute value, with `sort_unstable`, which
needs no extra buffer, and writes through a `BufWriter`:
{1178_geometry_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1178_geometry_optimized.java`: time reduction +33.57%; memory
  reduction +85.16%; base: `1178_geometry.java`.

- `1178_geometry_optimized.py`: time reduction +0.00%; memory reduction
  +66.30%; base: `1178_geometry.py`.

- `1178_geometry_optimized.rs`: time reduction -106.67%; memory
  reduction +61.78%; base: `1178_geometry.rs`.

## Language notes

- All languages sort the cities by `x`, breaking ties by `y`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1178_geometry.cpp](1178_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 388 KB | 11283266 |
| [1178_geometry.go](1178_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1676 KB | 11283270 |
| [1178_geometry.java](1178_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 6872 KB | 11283277 |
| [1178_geometry.py](1178_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 3276 KB | 11283275 |
| [1178_geometry.rs](1178_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.015 s | 764 KB | 11283279 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1178_geometry_optimized.java](1178_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.093 s | 1020 KB | 11305836 |
| [1178_geometry_optimized.py](1178_geometry_optimized.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 1104 KB | 11305838 |
| [1178_geometry_optimized.rs](1178_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 292 KB | 11305833 |
