# 1729. Dead Man's Chest

[Timus 1729](https://acm.timus.ru/problem.aspx?space=1&num=1729) · difficulty 629 · geometry

Original problem by Fedor Fominykh (prepared by Denis Dublennykh), from the Ural Regional School Programming Contest 2009.

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
apart, while the first and last ones must be at least 360 − 2a apart
so that the arcs close up around the island.

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
- for a = 0.001 the route has 180 000 chords, so the sum is a product,
  not a loop over them.

The answers match an independent accepted implementation in all seven
printed digits on 300 random cases.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1729_geometry.cpp](1729_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 468 KB |
| [1729_geometry.go](1729_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1100 KB |
| [1729_geometry.java](1729_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1840 KB |
| [1729_geometry.py](1729_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 520 KB |
| [1729_geometry.rs](1729_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 260 KB |
