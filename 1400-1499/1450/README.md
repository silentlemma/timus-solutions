# 1450. Russian Pipelines

[Timus 1450](https://acm.timus.ru/problem.aspx?space=1&num=1450) · difficulty 149 · dp

Original problem by Dmitry Kovalioff, Ilya Grebnov and Nikita Rybak, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A gas network has N stations (2 ≤ N ≤ 500) and M one-way pipelines
(0 ≤ M ≤ 124750), each from A to B with profit C (1 ≤ C ≤ 10000); a pair
of stations has at most one pipeline, and the network has no cycles: if
gas can flow from X to Y, it cannot flow back. Find the most profitable
route from station S to station F, the profit of a route being the sum
over its pipelines, or print "No solution" if F cannot be reached.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N and M on the first line, then M lines A, B, C with 1 ≤ A, B ≤ N,
then S and F on the last line, where 1 ≤ S, F ≤ N and S ≠ F.

## Output

The largest profit, or "No solution".

## Examples

### Example 1

Input:

```
6 7
6 5 10
1 4 11
1 2 4
3 1 5
2 4 5
6 3 1
6 1 3
6 4
```

Output:

```
17
```

The best route in the example is 6, 3, 1, 4.

## Solution

Without cycles the longest path is a simple dynamic programme. Order the
stations topologically with Kahn's method: start from the stations with
no incoming pipelines and release a station once all pipelines into it
have been taken. In that order every station is final before any of its
pipelines is used, so best[w] = max(best[v] + C) over the pipelines
v → w, with best[S] = 0 and stations unreachable from S left empty. The
answer is best[F]. `O(N + M)`.

Pitfalls:

- an unreachable F, including when the pipelines lead from F to S
  (tests 02, 03, 06);
- the longest route may take more pipelines than the direct one (test
  07);
- stations unreachable from S must not pass on a profit, even though
  they still have to be ordered.

## Optimized solutions

The optimized C++ solution parses the numbers by hand from a 4 KB buffer
instead of `scanf` and keeps the network as a matrix of 16-bit
`uint16_t` profits, about 490 KB for `N = 500`, instead of a `vector` of
`vector`s of pairs. Profits are at least 1 and a pair of stations has at
most one pipeline, so a zero cell means no pipeline; a station taken
from the queue scans its whole row, `O(N²)` in total. The best profits
are `int` instead of `long long`: a route has at most 499 pipelines, so
its profit is at most 4 990 000: {1450_dp_optimized.cpp}.

The optimized Go solution parses the numbers byte by byte from a
`bufio.Reader` instead of `fmt.Fscan` and keeps the network as a matrix
of `uint16` profits, about 490 KB for `N = 500`, instead of slices of
structs with two `int` fields. Profits are at least 1 and a pair of
stations has at most one pipeline, so a zero cell means no pipeline; a
station taken from the queue scans its whole row, `O(N²)` in total:
{1450_dp_optimized.go}.

The optimized Java solution parses the numbers by hand from a 4 KB
buffer instead of `StreamTokenizer` and keeps the network as a matrix of
`short` profits, which hold values up to 10 000, instead of three `int`
arrays of pipelines and the arrays that group them by station. Profits
are at least 1 and a pair of stations has at most one pipeline, so a
zero cell means no pipeline; a station taken from the queue scans its
whole row, `O(N²)` in total. The best profits are `int` instead of
`long`: a route has at most 499 pipelines, so its profit is at most
4 990 000: {1450_dp_optimized.java}.

The optimized Python solution relies on the line layout of the input and
reads it line by line instead of splitting the whole input into a list.
It keeps the network as one `array("H")` row of unsigned 16-bit profits
per station instead of lists of tuples; profits are at least 1 and a
pair of stations has at most one pipeline, so a zero cell means no
pipeline, and a station taken from the queue scans its whole row with
`enumerate`: {1450_dp_optimized.py}.

The optimized Rust solution parses the numbers by hand from a 4 KB
buffer instead of reading the whole input into a `String` and keeps the
network as a matrix of `u16` profits, about 490 KB for `N = 500`,
instead of vectors of `(usize, i64)` pairs. Profits are at least 1 and a
pair of stations has at most one pipeline, so a zero cell means no
pipeline; a station taken from the queue scans its whole row, `O(N²)` in
total. The best profits are plain `i32` with -1 for unreachable instead
of `Option<i64>`: a route has at most 499 pipelines, so its profit is at
most 4 990 000: {1450_dp_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1450_dp_optimized.cpp`: time reduction +91.98%; memory reduction
  +62.59%; base: `1450_dp.cpp`.

- `1450_dp_optimized.go`: time reduction +84.73%; memory reduction
  +75.87%; base: `1450_dp.go`.

- `1450_dp_optimized.java`: time reduction -11.43%; memory reduction
  +62.93%; base: `1450_dp.java`.

- `1450_dp_optimized.py`: time reduction +38.42%; memory reduction
  +96.92%; base: `1450_dp.py`.

- `1450_dp_optimized.rs`: time reduction +67.39%; memory reduction
  +87.71%; base: `1450_dp.rs`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1450_dp.cpp](1450_dp.cpp) | G++ 13.2 x64 | dp | O(N + M) | AC | 0.187 s | 1668 KB | 11286341 |
| [1450_dp.go](1450_dp.go) | Go 1.14 x64 | dp | O(N + M) | AC | 0.203 s | 6332 KB | 11286345 |
| [1450_dp.java](1450_dp.java) | Java 1.8 | dp | O(N + M) | AC | 0.140 s | 2460 KB | 11286355 |
| [1450_dp.py](1450_dp.py) | Python 3.12 x64 | dp | O(N + M) | AC | 0.406 s | 35968 KB | 11286349 |
| [1450_dp.rs](1450_dp.rs) | Rust 1.75 x64 | dp | O(N + M) | AC | 0.046 s | 5760 KB | 11286358 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1450_dp_optimized.cpp](1450_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N² + M) | AC | 0.015 s | 624 KB | 11304540 |
| [1450_dp_optimized.go](1450_dp_optimized.go) | Go 1.14 x64 | dp | O(N² + M) | AC | 0.031 s | 1528 KB | 11304541 |
| [1450_dp_optimized.java](1450_dp_optimized.java) \* | Java 1.8 | dp | O(N² + M) | AC | 0.156 s | 912 KB | 11304542 |
| [1450_dp_optimized.py](1450_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N² + M) | AC | 0.250 s | 1108 KB | 11304544 |
| [1450_dp_optimized.rs](1450_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N² + M) | AC | 0.015 s | 708 KB | 11304543 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
