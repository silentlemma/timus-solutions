# 2181. Counting round trips on a grid that never revisit a crossing

[Timus 2181](https://acm.timus.ru/problem.aspx?space=1&num=2181) · difficulty 1410 · dp, math

Original problem by Semyon Trifochkin, from the Ural School Programming Contest 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The city is an N × M grid of crossings with K missing roads between
neighbors. A day's route goes from (1, 1) to (N, M) moving only toward
larger coordinates, then back moving only toward smaller ones, and no
crossing other than the two ends is visited twice. Count the different
routes modulo 10⁹ + 7. The limits are 3 seconds and 256 MB.

## Input

N and M, 2 ≤ N, M ≤ 300, then K, 0 ≤ K ≤ 10⁵, and K missing roads, each
as the two neighboring crossings it joined.

## Output

The number of routes modulo 10⁹ + 7, or 0.

## Examples

### Example 1

Input:

```
3 3
2
1 2 1 3
1 3 2 3
```

Output:

```
2
```

## Solution

The way back, read backwards, is another monotone path from (1, 1) to
(N, M), so a route is an ordered pair of monotone paths that share only
their ends. They must leave (1, 1) in different directions and enter
(N, M) in different directions. The path through (1, 2) stays above the
other one, so it ends through (N − 1, M), and the path through (2, 1)
ends through (N, M − 1); the four edges at the corners have to exist.

Counting vertex-disjoint pairs of paths from A₁ = (1, 2), A₂ = (2, 1) to
B₁ = (N − 1, M), B₂ = (N, M − 1) is the Lindström–Gessel–Viennot lemma:

det = P(A₁, B₁) · P(A₂, B₂) − P(A₁, B₂) · P(A₂, B₁),

where P counts monotone paths. Any intersecting pair is cancelled by
swapping the tails after the first shared crossing, which matches it
with an intersecting pair of the other pairing, and the crossed pairing
cannot be disjoint in a planar grid. Two grid DPs, one from each start,
give all four counts. Either path can be the way there, so the answer
is 2 · det.

In the example (1, 3) has no roads, so the upper path is
(1, 2) → (2, 2) → (2, 3), the lower one has to avoid (2, 2) through
(3, 1), and the single pair gives 2 routes.

This takes O(NM + K).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2181_dp_math.cpp](2181_dp_math.cpp) | G++ 13.2 x64 | dp, math | O(NM + K) | AC | 0.062 s | 372 KB |
| [2181_dp_math.go](2181_dp_math.go) | Go 1.14 x64 | dp, math | O(NM + K) | AC | 0.031 s | 5724 KB |
| [2181_dp_math.java](2181_dp_math.java) | Java 1.8 | dp, math | O(NM + K) | AC | 0.109 s | 608 KB |
| [2181_dp_math.py](2181_dp_math.py) | Python 3.12 x64 | dp, math | O(NM + K) | AC | 0.171 s | 25224 KB |
| [2181_dp_math.rs](2181_dp_math.rs) | Rust 1.75 x64 | dp, math | O(NM + K) | AC | 0.015 s | 2936 KB |
