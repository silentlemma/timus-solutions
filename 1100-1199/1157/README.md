# 1157. The fewest tiles that make N rectangles, with M rectangles K tiles earlier

[Timus 1157](https://acm.timus.ru/problem.aspx?space=1&num=1157) · difficulty 200 · number_theory

Original problem from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A boy lays out all his square tiles as rectangles. Given `M`, `N` and
`K` (`M, N ≤ 50`, `K ≤ 9999`), find the smallest number of tiles `L` such
that `L` tiles can form exactly `N` different rectangles and `L − K` tiles
exactly `M` different rectangles. Print `0` if there is no such `L` up to
10000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`M`, `N` and `K`.

## Output

The smallest `L`, or `0`.

## Examples

### Example 1

Input:

```
2 3 1
```

Output:

```
16
```

## Solution

`x` tiles form one rectangle `a × b` for every way to write `x = a·b` with
`a ≤ b`, so the number of rectangles is the number of divisors of `x`
divided by two and rounded up (the square root, if any, pairs with
itself). A sieve over `d` from 1 to 10000 adds one to every multiple of
`d` and counts the divisors of all numbers up to 10000 in
`O(10000·log 10000)` steps. Then try `L` from `K + 1` up and stop at the
first one with `N` rectangles whose `L − K` has `M`.

Pitfalls:

- `L − K` must be at least one tile, so `L` starts at `K + 1`;
- a square number has an odd count of divisors, and its square rectangle
  counts once;
- no number up to 10000 has more than 64 divisors, so `N` or `M` above 32
  always gives `0`.

The answers were compared with counting rectangles directly by trial
division on every test.

## Language notes

- All languages run the same sieve and search.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1157_number_theory.cpp](1157_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log L) | AC | 0.015 s | 216 KB |
| [1157_number_theory.go](1157_number_theory.go) | Go 1.14 x64 | number_theory | O(L log L) | AC | 0.031 s | 1172 KB |
| [1157_number_theory.java](1157_number_theory.java) | Java 1.8 | number_theory | O(L log L) | AC | 0.125 s | 1620 KB |
| [1157_number_theory.py](1157_number_theory.py) | Python 3.12 x64 | number_theory | O(L log L) | AC | 0.078 s | 712 KB |
| [1157_number_theory.rs](1157_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log L) | AC | 0.046 s | 300 KB |
