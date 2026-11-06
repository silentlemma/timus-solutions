# 1116. Cutting one piecewise-constant function by the domain of another

[Timus 1116](https://acm.timus.ru/problem.aspx?space=1&num=1116) · difficulty 333 · two_pointers

Original problem by Oleg Kats, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A piecewise-constant function is a list of disjoint half-open intervals
`[A, B)` with a value `Y` on each, sorted by `A`; two touching intervals
never have the same value. Given two such functions `F1` and `F2` (each
with `1 ≤ N ≤ 15000` intervals, `|A|, |B| < 32000`, `A < B`, `|Y| ≤ 100`),
build `F`: it equals `F1` wherever `F1` is defined and `F2` is not, and is
undefined everywhere else.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

Two lines, one per function: `N`, then `N` triples `A B Y`.

## Output

One line in the same format describing `F`; `0` alone if `F` is defined
nowhere.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 -1 1 2 1 3 4 4 6 3
2 -2 2 1 5 7 5
```

Output:

```
2 2 3 4 4 5 3
```

## Solution

Both lists are sorted, so a single pass with two pointers is enough. For
each interval `[A, B)` of `F1`, walk a cursor from `A` to `B`: skip the
intervals of `F2` that end at or before the cursor; if the next one
already covers the cursor, jump the cursor to its end; otherwise emit the
piece from the cursor to the start of that interval (or to `B`) with the
value `Y`. The pointer into `F2` never moves back, so the whole pass is
`O(N1 + N2)`.

The pieces need no merging: pieces cut from one interval are separated by
holes, and pieces of two different intervals can only touch where the
intervals touched, and those have different values.

Pitfalls:

- the intervals are half-open: `[0, 2)` and `[2, 4)` touch but do not
  overlap, so an interval of `F2` ending at `x` does not cover `x`;
- an interval of `F2` may span several intervals of `F1`, so its pointer
  must not advance just because one interval of `F1` is finished;
- when nothing is left, the answer is the single number `0`.

The answers were checked against a brute force that evaluates both
functions on every unit cell of the coordinate range and merges runs of
equal values back into intervals, on every test and 100 random pairs.

## Optimized solutions

The C++ and Go versions store each interval as three signed 16-bit values. They keep the first list and read the second as needed, retaining only the current masking interval. Each masking interval is read at most once. The output intervals are collected in a compact array because their count must be printed first. Time is O(N1 + N2).

The accepted G++ 13.2 x64 run takes 0.062 s versus 0.046 s for the base and uses 444 KB versus 1880 KB.

The accepted base implementations [1116_two_pointers.java](1116_two_pointers.java), [1116_two_pointers.py](1116_two_pointers.py), [1116_two_pointers.rs](1116_two_pointers.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- All languages run the same pass; Go buffers writes, while the others
  build an output string.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1116_two_pointers.cpp](1116_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 1880 KB | 11279235 |
| [1116_two_pointers.go](1116_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 6832 KB | 11279236 |
| [1116_two_pointers.java](1116_two_pointers.java) \* | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 5400 KB | 11279239 |
| [1116_two_pointers.py](1116_two_pointers.py) \* | Python 3.12 x64 | two_pointers | O(N1 + N2) | AC | 0.140 s | 13144 KB | 11279238 |
| [1116_two_pointers.rs](1116_two_pointers.rs) \* | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 2112 KB | 11279241 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1116_two_pointers_optimized.cpp](1116_two_pointers_optimized.cpp) \* | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 444 KB | 11310386 |
| [1116_two_pointers_optimized.go](1116_two_pointers_optimized.go) \* | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.031 s | 1712 KB | 11310385 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
