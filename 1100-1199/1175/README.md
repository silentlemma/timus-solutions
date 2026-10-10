# 1175. Where a two-term recurrence starts repeating, and its period

[Timus 1175](https://acm.timus.ru/problem.aspx?space=1&num=1175) · difficulty 946 · math

Original problem by Alexander Klepinin, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sequence starts with `X1`, `X2`, and each next term is `F(Xn−1, Xn)`:
take `H = A1·X·Y + A2·X + A3·Y + A4`, and if `H > B1`, subtract `C` until
`H ≤ B2`. Every `H` stays within `0..100000`. Find the smallest `p` and
`q` such that `Xp+n = Xp+q+n` for all `n ≥ 0`.

Time limit: 1 second. Memory limit: 2 MB.

## Input

`A1 A2 A3 A4 B1 B2 C`, then `X1 X2`.

## Output

`p` and `q`.

## Examples

### Example 1

Input:

```
0 0 2 3 20 5 7
0 1
```

Output:

```
2 3
```

## Solution

The next term depends on the last two, so the pair `(Xn, Xn+1)` evolves
on its own, and the terms repeat from `p` with period `q` exactly when the
pairs do. The pairs are a walk in a finite set, so they run into a cycle:
`p` is the index of the first pair on it and `q` its length.

With 2 MB of memory the pairs cannot be stored, so the cycle is found
with Brent's method. A slow pointer waits at a power-of-two step while a
fast one walks ahead; when the fast one meets it, the distance walked
since the last jump is the cycle length `q`. Then two pointers start at
the beginning, one of them `q` steps ahead, and walk together; they first
meet at the start of the cycle, which gives `p`. `O(p + q)` steps and
`O(1)` memory.

The subtraction loop is replaced by one division: when `H > B1` and
`H > B2`, subtract `C` times `⌈(H − B2) / C⌉`.

Pitfalls:

- `p` is counted from 1, the index of the first term of the pair;
- the cycle can be long, for example Fibonacci numbers modulo 31250 have
  a period of 187,500, so storing the pairs would break the memory limit;
- if `B1 < H ≤ B2`, nothing is subtracted.

The answers were compared with a direct search that stores the pairs in a
dictionary on 300 random parameter sets, and with a separately written
solution on every test.

## Language notes

- All languages run the same Brent search on pairs of 64-bit integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1175_math.cpp](1175_math.cpp) | G++ 13.2 x64 | math | O(p + q) | AC | 0.015 s | 128 KB |
| [1175_math.go](1175_math.go) | Go 1.14 x64 | math | O(p + q) | AC | 0.046 s | 1072 KB |
| [1175_math.java](1175_math.java) | Java 1.8 | math | O(p + q) | AC | 0.156 s | 1632 KB |
| [1175_math.py](1175_math.py) | Python 3.12 x64 | math | O(p + q) | AC | 0.171 s | 460 KB |
| [1175_math.rs](1175_math.rs) | Rust 1.75 x64 | math | O(p + q) | AC | 0.015 s | 224 KB |
