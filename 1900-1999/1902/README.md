# 1902. Meeting Times

[Timus 1902](https://acm.timus.ru/problem.aspx?space=1&num=1902) · difficulty 116 · math

Original problem by Denis Dublennykh, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

One object enters a segment at time s. Another n objects traverse the
same segment in the opposite direction, entering at times sᵢ. Every
object has the same constant speed and takes t time units to traverse
the segment. Find the encounter times. Limits: 1 second and 64 MB.

## Input

The first line gives n, t, s, with 1 ≤ n ≤ 100, 1 ≤ t ≤ 100 and
360 ≤ s ≤ 1200. The next line contains n integer entry times in strictly
increasing order: s−t < s₁ < … < sₙ < s+t. Only feasible combinations
of these constraints occur.

## Output

Print the n encounter times in input order, separated by whitespace.
Absolute or relative error at most 10⁻⁶ is accepted.

## Checking

Numeric tokens are compared with absolute/relative tolerance 10⁻⁶.
There must be exactly n finite values. Tests use `float:1e-6` judging.

## Examples

```
2 60 600
600 630
```

```
630.000000
645.000000
```

## Solution

Measure distance in units traveled per unit time, so the segment length
is t and both speeds are 1. At an encounter time u, the first object
has covered u−s and the opposing object has covered u−sᵢ. Their distances
add to the segment length:

`(u − s) + (u − sᵢ) = t`, hence `2u = s + sᵢ + t`.

Output `(s + sᵢ + t) / 2` for each entry. The strict input bounds ensure
`max(s, sᵢ) < u < min(s+t, sᵢ+t)`, so neither trip has ended or is yet
to begin. No filtering or event simulation is necessary.

The encounter equation is necessary because the objects occupy the same
point. Their combined covered distance increases strictly at rate 2,
so the equation has exactly one solution. It lies within both trips by
the input bounds, proving that each printed time is the unique encounter.

All inputs are integers; the answer is an integer or half-integer.
Keep the numerator as an integer and print `.000000` when it is even
and `.500000` when it is odd. This is exact and avoids rounding and
locale issues. Do not perform integer division without printing the
remainder. Each numerator is below 2600, so 32-bit integers suffice.

The sample gives `(600+600+60)/2=630` and `(600+630+60)/2=645`.

Time is `O(n)`. Each encounter needs `O(1)` arithmetic state; implementations
that retain input tokens or buffered output use `O(n)` total space.

## Language notes

All five versions format the integer quotient and the parity suffix.
Buffered input/output is enough; Python targets CPython 3.12. Reading n
and then exactly n entry times avoids confusing t with an absolute time.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1902_math.cpp](1902_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 436 KB |
| [1902_math.go](1902_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1104 KB |
| [1902_math.java](1902_math.java) | Java 1.8 | math | O(n) | AC | 0.109 s | 388 KB |
| [1902_math.py](1902_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 336 KB |
| [1902_math.rs](1902_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 228 KB |
