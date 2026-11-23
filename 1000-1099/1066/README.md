# 1066. The lowest end of a sagging garland

[Timus 1066](https://acm.timus.ru/problem.aspx?space=1&num=1066) · difficulty 583 · math

Original problem from the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A garland of `N` lamps (`3 ≤ N ≤ 1000`) hangs by its ends. Every inner lamp
hangs 1 millimetre lower than the average height of its two neighbours:
`H(i) = (H(i−1) + H(i+1)) / 2 − 1`. The first lamp is at height `A`
(`10 ≤ A ≤ 1000`, a real number). No lamp may be below the ground, though
some may touch it (`H(i) ≥ 0`). Find the smallest possible height `B` of
the last lamp.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N` and `A` on one line.

## Output

`B`, with at least two digits after the decimal point.

## Checking

Numbers are compared with an absolute error of 0.011: the answers are
printed with two decimals, so the last digit may differ by one.

## Examples

### Example 1

Input:

```
8 15
```

Output:

```
9.75
```

### Example 2

Input:

```
692 532.81
```

Output:

```
446113.34
```

## Solution

The rule is the same as `H(i+1) = 2·H(i) − H(i−1) + 2`: the second
difference of the heights is always 2. So the second height `x` fixes the
whole garland:

`H(i) = A + (i−1)·(x − A) + (i−1)·(i−2)`.

The last height grows with `x` (its coefficient `N − 1` is positive), so
the answer comes from the smallest `x` that keeps every lamp at height 0 or
above. For lamp `k + 1` the condition `H(k+1) ≥ 0` means
`x ≥ A − A/k − (k − 1)`, and `x` is the largest of these bounds over
`k = 1 … N−1` (the bound for `k = 1` is `x ≥ 0`). Then `B = H(N)`. `O(N)`.

Pitfalls:

- the lamp that touches the ground is not always in the middle: the bound
  is largest where `A/k + k` is smallest, near `k = √A`, and when that is
  past the end of the garland the last lamp itself touches the ground and
  `B = 0`;
- `B` grows like `N^2` and reaches about `10^6`, which doubles hold with
  room to spare;
- a binary search on the second height also works, but the closed form
  needs no search iterations and no tolerance.

The answers were checked with exact fractions: the recurrence run forward
from the chosen second height keeps every lamp at height 0 or above, and
one of them at exactly 0.

## Language notes

- Python finds the second height with one `max` over a generator.
- Java reads `A` with `Locale.US`, so a decimal point is accepted whatever
  the system locale is.

## Optimized solutions

Java finds the binding lamp from the integer minimum of A/k + k near the square root of A. It then computes the final height directly. Submission 11317218 took 0.093 s and used 508 KB, versus 0.109 s and 1992 KB for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321845 · Python 3.12 x64 №11321849 · Rust 1.75 x64 №11321850 · Go 1.14 x64 №11322191 · Java 1.8 №11322192.

Python finds the binding lamp in constant time by comparing the two integer indices around the square root of the first height. Python 3.12 x64, submission 11322406. Time 0.062 → 0.078 s, memory 452 → 404 KB.

Go finds the minimum of the height constraint around the square root of the first height, then computes the last height in factored form. Go 1.14 x64, submission 11322851. Time 0.031 → 0.031 s, memory 1100 → 300 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1066_math_parsing_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328659 (Go 1.14 x64): **0.015 s / 936 KB**. Archived comparison: `1066_math.go` (Go 1.14 x64) — 0.031 s / 1100 KB (#11322191).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1066_math.cpp](1066_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 140 KB | 11321845 |
| [1066_math.go](1066_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1100 KB | 11322191 |
| [1066_math.java](1066_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 1992 KB | 11322192 |
| [1066_math.py](1066_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 452 KB | 11321849 |
| [1066_math.rs](1066_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 268 KB | 11321850 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1066_math_optimized.java](1066_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 508 KB | 11317218 |
| [1066_math_optimized.py](1066_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB | 11322406 |
| [1066_math_optimized.go](1066_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 300 KB | 11322851 |
| [1066_math_parsing_optimized.go](1066_math_parsing_optimized.go) | Go 1.14 x64 | math, parsing | O(N) | AC | 0.015 s | 936 KB | 11328659 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
