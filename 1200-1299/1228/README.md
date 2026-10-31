# 1228. The bounds of an array from its index multipliers

[Timus 1228](https://acm.timus.ru/problem.aspx?space=1&num=1228) · difficulty 109 · math

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An `n`-dimensional array `array[0..k1, 0..k2, …, 0..kn]`, `n ≤ 20`, is
laid out with the last index changing fastest, so element
`X[i1, …, in]` has number `1 + D1·i1 + … + Dn·in` for some multipliers
`Di`. Given the multipliers and the total number of elements `s`, find
the upper bounds `k1, …, kn`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` (`1 ≤ n ≤ 20`) and `s` (`1 ≤ s < 2³¹ − 1`), then `D1, …, Dn`.

## Output

`k1, …, kn` (`0 < ki ≤ 1000`) separated by spaces or line breaks.

## Examples

### Example 1

Input:

```
3 24
8
4
1
```

Output:

```
2 1 3
```

## Solution

Stepping index `i` by one skips a whole block of the dimensions after
it, so `D(i−1) = Di · (ki + 1)`, and the whole array is one block of the
first dimension: `s = D1 · (k1 + 1)`. Reading the multipliers with `s` in
front, every bound is one less than the quotient of two neighbours:
`k1 = s/D1 − 1` and `ki = D(i−1)/Di − 1`. `O(n)`.

Pitfalls:

- the last multiplier is always 1, and the first bound comes from `s`,
  not from a multiplier;
- the products stay below `2³¹ − 1`, so signed 32-bit integers suffice
  for the arithmetic.

The bounds were checked by multiplying `ki + 1` back into `s` on 59 generated
arrays, and compared with a separately written solution on every test.

## Optimized solutions

The optimized C++ solution reads the multipliers one at a time and keeps
only the previous one, printing each bound as soon as its divisor
arrives, instead of storing `s` and all the multipliers in a
`std::vector`: {1228_math_optimized.cpp}.

The optimized Java solution parses the numbers digit by digit straight
from `System.in` instead of creating a `Scanner`, and keeps only the
previous multiplier instead of an array of all of them:
{1228_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1228_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +36.00%; base: `1228_math.cpp`.

- `1228_math_optimized.java`: time reduction +50.40%; memory reduction
  +78.22%; base: `1228_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1228_math.go](1228_math.go).
- [1228_math.rs](1228_math.rs).

- All languages put `s` in front of the multipliers and divide
  neighbours.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1228_math.cpp](1228_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 200 KB | 11283732 |
| [1228_math.go](1228_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.001 s | 1136 KB | 11283735 |
| [1228_math.java](1228_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1616 KB | 11283739 |
| [1228_math.py](1228_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 424 KB | 11283737 |
| [1228_math.rs](1228_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 216 KB | 11283740 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1228_math_optimized.cpp](1228_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.001 s | 128 KB | 11304270 |
| [1228_math_optimized.java](1228_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.062 s | 352 KB | 11304271 |
