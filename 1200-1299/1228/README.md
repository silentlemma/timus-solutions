# 1228. The bounds of an array from its index multipliers

[Timus 1228](https://acm.timus.ru/problem.aspx?space=1&num=1228) · difficulty 108 · math

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

`n` and `s`, then `D1, …, Dn`.

## Output

`k1, …, kn` separated by spaces or line breaks.

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
- the products reach almost `2³¹`, so the arithmetic should not be done
  in 32-bit signed integers on the way.

The bounds were checked by multiplying them back into `s` on 59 generated
arrays, and compared with a separately written solution on every test.

## Language notes

- All languages put `s` in front of the multipliers and divide
  neighbours.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1228_math.cpp](1228_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 200 KB |
| [1228_math.go](1228_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.001 s | 1136 KB |
| [1228_math.java](1228_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1616 KB |
| [1228_math.py](1228_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 424 KB |
| [1228_math.rs](1228_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 216 KB |
