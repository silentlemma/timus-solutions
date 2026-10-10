# 1116. Cutting one piecewise-constant function by the domain of another

[Timus 1116](https://acm.timus.ru/problem.aspx?space=1&num=1116) · difficulty 332 · two_pointers

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

## Language notes

- All languages run the same pass; the output is built in one buffer.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1116_two_pointers.cpp](1116_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 1880 KB |
| [1116_two_pointers.go](1116_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 6832 KB |
| [1116_two_pointers.java](1116_two_pointers.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 5400 KB |
| [1116_two_pointers.py](1116_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N1 + N2) | AC | 0.140 s | 13144 KB |
| [1116_two_pointers.rs](1116_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 2112 KB |
