# 1286. Starship from the VAZ plant

[Timus 1286](https://acm.timus.ru/problem.aspx?space=1&num=1286) · difficulty 654 · number_theory

Original problem by Alexander Klepinin, from the Ural State University Personal Contest 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A ship at integer point (x, y) can only jump like a generalized knight:
by (±p, ±q) or by (±q, ±p). Can it reach (x1, y1)? All numbers are
integers with absolute value at most 2 · 10⁹.

Time limit: 1 second. Memory limit: 64 MB.

## Input

p and q, then x and y, then x1 and y1.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
4 6
0 0
10 10
```

Output:

```
YES
```

### Example 2

Input:

```
4 6
0 0
9 9
```

Output:

```
NO
```

## Solution

Let g = gcd(|p|, |q|). Every jump changes both coordinates by multiples
of g, so the offset (dx, dy) must be divisible by g. Dividing everything
by g leaves coprime steps a and b. Two jumps (a, b) and (a, −b) add up
to (2a, 0), and likewise (2b, 0) is reachable, so by Bézout (2, 0) and
(0, 2) are. Then:

- if a and b are both odd, every jump changes x + y by an even amount,
  so dx/g + dy/g must be even; and the jump (a, b) shifted by multiples
  of (2, 0) and (0, 2) gives (1, 1), so every such point is reachable;
- otherwise, say a is odd and b even: the jump (a, b) shifted the same
  way gives (1, 0), the jump (b, a) gives (0, 1), and every point is
  reachable.

When p = q = 0 the ship cannot move at all. `O(log max(|p|, |q|))`.

Pitfalls:

- p and q may both be zero (tests 03, 04), and one of them may be zero
  (test 05);
- steps may be negative (test 11);
- the offset reaches 4 · 10⁹, beyond 32 bits (tests 08, 09);
- in C-like languages the remainder of a negative odd number is −1, so
  oddness is tested with `% 2 != 0`.

The answers were compared with a breadth-first search on a large board
for all steps from 0 to 4 and all targets within 8 of the start.

## Language notes

- All languages compute the same gcd and parity test. C++, Go, Java and
  Rust use signed 64-bit integers; Python uses arbitrary-precision integers.

## Optimized solutions

The optimized versions test parity using remainders modulo twice the gcd. The coordinates and steps stay in their original units.

Python 3.12 x64, submission 11318499. Time 0.109 → 0.078 s, memory 400 → 436 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322401 · Go 1.14 x64 №11322465 · Java 1.8 №11322466 · Python 3.12 x64 №11322467 · Rust 1.75 x64 №11322468.

Java 1.8, submission 11322444. Time 0.093 → 0.093 s, memory 1560 → 360 KB.

Go 1.14 x64, submission 11322469. Time 0.015 → 0.015 s, memory 1068 → 304 KB.

Rust uses binary GCD for divisibility and compares powers of two to decide whether both normalized steps are odd. Rust 1.75 x64, submission 11323306. Time 0.015 → 0.015 s, memory 208 → 52 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1286_number_theory.cpp](1286_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 112 KB | 11322401 |
| [1286_number_theory.go](1286_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 1068 KB | 11322465 |
| [1286_number_theory.java](1286_number_theory.java) | Java 1.8 | number_theory | O(log max(abs p, abs q)) | AC | 0.093 s | 1560 KB | 11322466 |
| [1286_number_theory.py](1286_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.109 s | 400 KB | 11322467 |
| [1286_number_theory.rs](1286_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 208 KB | 11322468 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1286_number_theory_optimized.py](1286_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.078 s | 436 KB | 11318499 |
| [1286_number_theory_optimized.java](1286_number_theory_optimized.java) | Java 1.8 | number_theory | O(log max(abs p, abs q)) | AC | 0.093 s | 360 KB | 11322444 |
| [1286_number_theory_optimized.go](1286_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 304 KB | 11322469 |
| [1286_number_theory_optimized.rs](1286_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(log max(abs p, abs q)) | AC | 0.015 s | 52 KB | 11323306 |

\* The marked versions have room to improve in the ratings.
