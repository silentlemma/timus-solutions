# 1154. The best moment of the day for a battle of elemental mages

[Timus 1154](https://acm.timus.ru/problem.aspx?space=1&num=1154) · difficulty 885 · math

Original problem by Evgeny Bryzgalov, from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Mages of four elements, Air, Earth, Fire and Water, fight for Light and
for Darkness. Each element has a moment of strength and a moment of
weakness during the day, with its power at each; between them the power
changes linearly, and the day repeats. A side's strength is the sum of
the powers of its mages. Choose the second of the day, from `00:00:00` to
`23:59:59`, when Light's advantage over Darkness is largest, the earliest
one if several are equally good, and print it with the advantage to two
decimals. If Light cannot be stronger at any moment, print
`We can't win!`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Four lines `code strong-time strong-power weak-time weak-power`, then the
mages of Light and of Darkness as strings of the letters `A`, `E`, `F`,
`W`, each with 1 to 1000 mages.

## Output

The time and the advantage, or `We can't win!`.

## Examples

### Example 1

Input:

```
A 10:00:00 130 18:00:00 40
E 14:00:00 150 21:30:00 25
F 06:00:00 105 18:00:00 70
W 23:00:00 140 02:00:00 20
A
WWW
```

Output:

```
02:00:00
25.00
```

### Example 2

Input:

```
A 10:00:00 130 18:00:00 40
E 14:00:00 150 21:30:00 25
F 06:00:00 105 18:00:00 70
W 23:00:00 140 02:00:00 20
A
WWWF
```

Output:

```
We can't win!
```

## Solution

Only the difference matters: for each element let `c` be the number of
its mages on Light's side minus those on Darkness's side. The advantage at
time `t` is `Σ c·power(t)`. Each power falls linearly from the moment of
strength to the moment of weakness, going forward around the day, and
rises linearly back; so the advantage is piecewise linear, with breaks
only at the eight moments. A linear piece is largest at one of its ends,
and the day itself is cut at midnight, so the best second is one of the
eight moments, `00:00:00` or `23:59:59`. Evaluate the advantage there,
keep the largest value and, among equal ones, the earliest time. Light
wins only if that value is positive.

Pitfalls:

- the time from strength to weakness wraps around midnight when weakness
  comes first in the day, so differences are taken modulo 86400;
- if the advantage stays at its maximum over an interval, the earliest
  second of it is a moment or midnight, which is among the candidates;
- an advantage of exactly zero is not a win;
- the advantage is fractional and printed with two decimals.

The answers were compared on every test and on 40 random inputs with an
exact computation, in fractions, at all 86400 seconds of the day.

## Language notes

- Python evaluates the candidates in exact fractions.
- C++, Go, Java and Rust use doubles and treat values within `10⁻⁹` as
  equal when choosing the earliest best moment.
- Java rounds the advantage through `BigDecimal` with ties to even, as
  `printf` does in C, because its own `%.2f` rounds the decimal string
  half up and could differ on exact halves.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1154_math.cpp](1154_math.cpp) | G++ 13.2 x64 | math | O(L + D) | AC | 0.015 s | 440 KB |
| [1154_math.go](1154_math.go) | Go 1.14 x64 | math | O(L + D) | AC | 0.015 s | 1152 KB |
| [1154_math.java](1154_math.java) | Java 1.8 | math | O(L + D) | AC | 0.140 s | 4336 KB |
| [1154_math.py](1154_math.py) | Python 3.12 x64 | math | O(L + D) | AC | 0.078 s | 1012 KB |
| [1154_math.rs](1154_math.rs) | Rust 1.75 x64 | math | O(L + D) | AC | 0.031 s | 468 KB |
