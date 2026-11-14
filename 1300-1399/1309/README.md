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

## Optimized solutions

Rust composes the affine map of one period by repeated squaring, then evaluates the remaining steps. Submission 11317191 took 0.015 s and used 204 KB, versus 0.046 s and 216 KB for the base.

Go raises the affine transform for one full period by binary exponentiation and handles the remaining steps directly. Go 1.14 x64, submission 11322858. Time 0.031 → 0.031 s, memory 1120 → 312 KB.

Go reads and writes decimal digits directly. It applies the affine map of a full period by repeated squaring, then evaluates the remaining recurrence.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321826 · Java 1.8 №11321828 · Python 3.12 x64 №11321829 · Go 1.14 x64 №11322062 · Rust 1.75 x64 №11322063.

Python composes the affine map for complete periods by repeated squaring and then processes the remaining terms directly. Python 3.12 x64, submission 11322405. Time 0.109 → 0.093 s, memory 448 → 396 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1309_math.cpp](1309_math.cpp) | G++ 13.2 x64 | math | O(9973 + n / 9973) | AC | 0.015 s | 112 KB | 11321826 |
| [1309_math.go](1309_math.go) | Go 1.14 x64 | math | O(9973 + n / 9973) | AC | 0.031 s | 1120 KB | 11322062 |
| [1309_math.java](1309_math.java) | Java 1.8 | math | O(9973 + n / 9973) | AC | 0.093 s | 2180 KB | 11321828 |
| [1309_math.py](1309_math.py) | Python 3.12 x64 | math | O(9973 + n / 9973) | AC | 0.109 s | 448 KB | 11321829 |
| [1309_math.rs](1309_math.rs) | Rust 1.75 x64 | math | O(9973 + n / 9973) | AC | 0.046 s | 216 KB | 11322063 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1309_math_optimized.rs](1309_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n mod 9973 + log(n / 9973 + 1)) | AC | 0.015 s | 204 KB | 11317191 |
| [1309_math_optimized.go](1309_math_optimized.go) \* | Go 1.14 x64 | math | O(n mod 9973 + log(n / 9973 + 1)) | AC | 0.031 s | 312 KB | 11322858 |
| [1309_math_optimized.py](1309_math_optimized.py) \* | Python 3.12 x64 | math | O(n mod 9973 + log(n / 9973 + 1)) | AC | 0.093 s | 396 KB | 11322405 |

\* The marked solutions can improve their target rankings.
