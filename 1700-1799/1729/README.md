# 1729. Dead Man's Chest

[Timus 1729](https://acm.timus.ru/problem.aspx?space=1&num=1729) · difficulty 630 · geometry

Original problem by Fedor Fominykh (prepared by Denis Dublennykh), from the Ural Regional Team Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Jack stands at the center of a round island of radius r covered with
jungle, so he sees the sea only from the shore. His boat lies off the
shore somewhere, and it is visible from the shore points within a
degrees of the shore point nearest to it. Find the shortest route
length that lets him see the boat in the worst case.

## Input

r and a (1 ≤ r ≤ 1000, 0.001 ≤ a ≤ 45), with at most three digits
after the decimal point.

## Output

The worst-case distance for the best route, with at least six digits
after the decimal point.

## Examples

### Example 1

Input:

```
1.000 30.000
```

Output:

```
6.0000000
```

## Solution

Reaching the shore takes r. From then on, each shore point Jack visits
shows him an arc of 2a degrees centered on it, and in the worst case
the boat is seen only at the last one. Between two shore points the
shortest way is the chord, and consecutive points may be at most 2a
apart, while the sweep from the first to the last must cover at least
360 − 2a so that the arcs close up around the island.

So the route is r plus chords whose angles add up to 360 − 2a, each at
most 2a. A chord of angle θ has length 2r·sin(θ/2), which grows slower
than θ, so for a fixed total the sum is smallest when the pieces are as
unequal as possible: k − 1 full chords of 2a, with k = ⌊180/a⌋, and one
short chord for the rest, 360 − 2ka degrees, which is empty when 2a
divides 360. `O(1)`.

In the example a = 30: six points 60° apart, five chords of length r,
so the answer is 1 + 5 = 6.

Pitfalls:

- ⌊180/a⌋ computed in floating point can come out one too small; the
  solutions read a exactly as thousandths of a degree. Such an error
  would happen to give the same length anyway, since the missing full
  chord comes back as a short chord of 2a;
- for a = 0.001 the route has 179 999 chords, so the sum is a product,
  not a loop over them.

The answers match an independent accepted implementation in all seven
printed digits on 300 random cases.

## Optimized solutions

The C++ version uses standard C input and output. The input angle has at most three fractional digits. Multiplying by 1000 and rounding recovers the integer number of thousandths before division and remainder. The same chord formula then takes constant time and space. The metrics come from submission 11316978.

The angle is converted to integer thousandths before computing the number of full chords and the remainder. Rust 1.75 x64, submission 11318489. Time 0.046 → 0.031 s, memory 260 → 256 KB.

The angle is converted to integer thousandths before computing the number of full chords and the remainder. Python 3.12 x64, submission 11318496. Time 0.109 → 0.078 s, memory 464 → 520 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322451 · Rust 1.75 x64 №11321953 · Go 1.14 x64 №11322452 · Java 1.8 №11322453 · Python 3.12 x64 №11322454.

The angle is converted to integer thousandths before computing the number of full chords and the remainder. Java 1.8, submission 11322411. Time 0.14 → 0.125 s, memory 1800 → 392 KB.

Go computes the distance with the chord formula and writes a fixed-precision result from a small buffer. Go 1.14 x64, submission 11322864. Time 0.031 → 0.031 s, memory 1088 → 304 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1729_geometry_parsing_optimized.rs`. Replace floating-point input conversion with exact thousandths and retain the chord formula and seven-place C output.

Accepted #11328988 (Rust 1.75 x64): **0.015 s / 84 KB**. Archived comparison: `1729_geometry_optimized.rs` (Rust 1.75 x64) — 0.031 s / 256 KB (#11318489).

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1729_geometry_parsing_optimized.java`. Parse the bounded decimal inputs as exact thousandths and retain the chord formula. Write seven fixed decimal places directly, avoiding general floating-point input and output conversion. Place the bounded input buffer and parsing methods directly in Main, removing one helper-class load and allocation. The complete mathematical formula, output scale and fixed-point formatter are unchanged. Flush both output streams before Runtime.halt(0), after the complete standalone answer has been written.

Accepted #11329243 (Java 1.8): **0.078 s / 476 KB**. Archived comparison: `1729_geometry_optimized.java` (Java 1.8) — 0.125 s / 392 KB (#11322411).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1729_geometry.cpp](1729_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 452 KB | 11322451 |
| [1729_geometry.go](1729_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB | 11322452 |
| [1729_geometry.java](1729_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.14 s | 1800 KB | 11322453 |
| [1729_geometry.py](1729_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 464 KB | 11322454 |
| [1729_geometry.rs](1729_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 256 KB | 11321953 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1729_geometry_optimized.cpp](1729_geometry_optimized.cpp) \* | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 136 KB | 11316978 |
| [1729_geometry_optimized.rs](1729_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 256 KB | 11318489 |
| [1729_geometry_optimized.py](1729_geometry_optimized.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 520 KB | 11318496 |
| [1729_geometry_optimized.java](1729_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.125 s | 392 KB | 11322411 |
| [1729_geometry_optimized.go](1729_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 304 KB | 11322864 |
| [1729_geometry_parsing_optimized.rs](1729_geometry_parsing_optimized.rs) | Rust 1.75 x64 | geometry, parsing | O(1) | AC | 0.015 s | 84 KB | 11328988 |
| [1729_geometry_parsing_optimized.java](1729_geometry_parsing_optimized.java) | Java 1.8 | geometry, parsing | O(1) | AC | 0.078 s | 476 KB | 11329243 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
