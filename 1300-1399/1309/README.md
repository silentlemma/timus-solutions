# 1309. Dispute

[Timus 1309](https://acm.timus.ru/problem.aspx?space=1&num=1309) · difficulty 602 · math

Original problem: idea by Alexander Klepinin, prepared by Alexander Klepinin and Stanislav Vasiliev, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

f(0) = 0 and f(n) = g(n, f(n − 1)), where

g(x, y) = ((y − 1)x⁵ + x³ − xy + 3x + 7y) mod 9973.

Compute f(n) for 0 ≤ n ≤ 10⁸ within half a second.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The number n.

## Output

f(n).

## Examples

### Example 1

Input:

```
50
```

Output:

```
6300
```

## Solution

Collect the terms in y:

g(x, y) = y · (x⁵ − x + 7) + (x³ + 3x − x⁵) mod 9973,

so every step is an affine map y → a(x) · y + b(x) modulo 9973, and its
coefficients depend only on x mod 9973. The steps x = 1, …, 9973 are
therefore repeated, in the same order, in every block of 9973
consecutive values of x.

- Compose the 9973 maps of one block into a single map
  y → A · y + B.
- Write n = q · 9973 + r. Apply y → A · y + B q times (q ≤ 10 028),
  then the single steps x = 1, …, r.

Three short loops of about 10 000 steps each instead of 10⁸.
`O(9973 + n / 9973)`.

Pitfalls:

- with y = 0 the expression is negative for x ≥ 2, so the remainder
  must be taken the mathematical way, from 0 to 9972. A truncating `%`
  as in C would first give a different answer at n = 1893 (test 04);
- x⁵ does not fit in 64 bits even for x near 9973, so the powers are
  reduced modulo 9973 after every multiplication;
- n = 0 gives 0 (test 02), and n just below, at or just above a
  multiple of 9973 checks the joins (tests 05–07).

The results were compared with the plain recurrence for every n up to
60 000, and for large n with a second method that raises the block map
to the q-th power by repeated squaring.

## Language notes

- Java uses `Math.floorMod` and Rust `rem_euclid` for the non-negative
  remainder; C++ and Go add 9973 before the last `%`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1309_math.cpp](1309_math.cpp) | G++ 13.2 x64 | math | O(9973 + n / 9973) | AC | 0.015 s | 128 KB |
| [1309_math.go](1309_math.go) | Go 1.14 x64 | math | O(9973 + n / 9973) | AC | 0.031 s | 1092 KB |
| [1309_math.java](1309_math.java) | Java 1.8 | math | O(9973 + n / 9973) | AC | 0.125 s | 2148 KB |
| [1309_math.py](1309_math.py) | Python 3.12 x64 | math | O(9973 + n / 9973) | AC | 0.078 s | 464 KB |
| [1309_math.rs](1309_math.rs) | Rust 1.75 x64 | math | O(9973 + n / 9973) | AC | 0.046 s | 224 KB |
