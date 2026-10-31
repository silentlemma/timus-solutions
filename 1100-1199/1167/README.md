# 1167. Splitting a line of black and white horses into stables with the least unhappiness

[Timus 1167](https://acm.timus.ru/problem.aspx?space=1&num=1167) · difficulty 136 · dp

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 500` horses, each black or white, stand in a line. Split the line
into exactly `K` non-empty consecutive groups (`1 ≤ K ≤ N`), one per
stable. A stable with `i` black and `j` white horses has unhappiness
`i·j`. Find the least possible total unhappiness.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `K`, then `N` colours: `1` for black, `0` for white.

## Output

The least total unhappiness.

## Examples

### Example 1

Input:

```
6 3
1
1
0
1
0
1
```

Output:

```
2
```

## Solution

Let `best[s][i]` be the least unhappiness of the first `i` horses in `s`
stables. The last stable takes some horses `j..i−1`, so
`best[s][i] = min over j of best[s−1][j] + cost(j, i)`, where the cost is
black times white, read off prefix counts of black horses. That is
`O(K·N²)` in all, about 20 million steps at the limits, which is fine for
compiled languages but slow for Python.

The cost has a useful property. For `a ≤ b ≤ c ≤ d`, write `x`, `y`, `z`
for the pieces `a..b`, `b..c`, `c..d`; then
`cost(a, d) + cost(b, c) − cost(a, c) − cost(b, d) = Bx·Wz + Bz·Wx ≥ 0`,
with `B` and `W` the black and white counts. By this quadrangle
inequality, the best last split never moves left when `i` grows. So each
layer is filled by divide and conquer: find the best split for the middle
`i`, then the left half only searches splits up to it and the right half
only splits from it. Each layer costs `O(N log N)`, all of them
`O(K·N log N)`.

Pitfalls:

- the stables must all be used, so `best[s][i]` only exists for `i ≥ s`;
- with no stables yet, only `best[0][0] = 0` is possible, and every other
  start must count as unreachable.

The answers were compared with the plain `O(K·N²)` recurrence on
400 random inputs of up to 40 horses and on every test.

## Optimized solutions

The optimized C++ solution keeps the prefix counts and the two layers in
fixed `int` arrays of 501 entries, enough since `N ≤ 500`, instead of
vectors, and swaps the pointers to the two layers instead of assigning a
fresh layer and copying it back after every stable:
{1167_dp_optimized.cpp}.

The optimized Go solution allocates the two layers once and swaps them
after every stable instead of making a new slice per stable. The stale
values left in the reused layer do no harm, since layer `s` reads only
the positions from `s − 1` on, which the previous layer has just
written. The garbage collector then has nothing to collect:
{1167_dp_optimized.go}.

The optimized Java solution allocates the two layers once and swaps them
after every stable instead of creating a new array per stable. The stale
values left in the reused layer do no harm, since layer `s` reads only
the positions from `s − 1` on, which the previous layer has just
written. The loop then allocates nothing: {1167_dp_optimized.java}.

The optimized Python solution cuts the work of the interpreter. If `K`
is at least the number of single-colour runs, it prints 0 at once: every
run gets its own stable, and runs can be split further at no cost until
there are exactly `K` stables, which is possible since `K ≤ N`. The
first layer is the cost of one stable, computed directly. Layer `s` only
fills the positions up to `N − K + s`, since every later stable needs a
horse of its own. The cost is inlined into the innermost loop, and empty
ranges never go on the stack: {1167_dp_optimized.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1167_dp_optimized.cpp`: time reduction +0.00%; memory reduction
  +44.90%; base: `1167_dp.cpp`.

- `1167_dp_optimized.go`: time reduction +0.00%; memory reduction
  +65.79%; base: `1167_dp.go`.

- `1167_dp_optimized.java`: time reduction +12.80%; memory reduction
  +67.49%; base: `1167_dp.java`.

- `1167_dp_optimized.py`: time reduction +59.38%; memory reduction
  -25.36%; base: `1167_dp.py`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1167_dp.rs](1167_dp.rs).

- All languages run the same divide and conquer; Python uses an explicit
  stack instead of recursion.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1167_dp.cpp](1167_dp.cpp) | G++ 13.2 x64 | dp | O(K·N log N) | AC | 0.015 s | 196 KB | 11283090 |
| [1167_dp.go](1167_dp.go) | Go 1.14 x64 | dp | O(K·N log N) | AC | 0.031 s | 3204 KB | 11283095 |
| [1167_dp.java](1167_dp.java) | Java 1.8 | dp | O(K·N log N) | AC | 0.125 s | 1464 KB | 11283098 |
| [1167_dp.py](1167_dp.py) | Python 3.12 x64 | dp | O(K·N log N) | AC | 0.421 s | 552 KB | 11283096 |
| [1167_dp.rs](1167_dp.rs) | Rust 1.75 x64 | dp | O(K·N log N) | AC | 0.031 s | 244 KB | 11283104 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1167_dp_optimized.cpp](1167_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(K·N log N) | AC | 0.015 s | 108 KB | 11304442 |
| [1167_dp_optimized.go](1167_dp_optimized.go) | Go 1.14 x64 | dp | O(K·N log N) | AC | 0.031 s | 1096 KB | 11304443 |
| [1167_dp_optimized.java](1167_dp_optimized.java) | Java 1.8 | dp | O(K·N log N) | AC | 0.109 s | 476 KB | 11304444 |
| [1167_dp_optimized.py](1167_dp_optimized.py) \* | Python 3.12 x64 | dp | O(K·N log N) | AC | 0.171 s | 692 KB | 11304446 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
