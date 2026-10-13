# 1473. Farm 2

[Timus 1473](https://acm.timus.ru/problem.aspx?space=1&num=1473) · difficulty 5038 · geometry

Original problem by Alexander Ipatov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An expert picks integers a_i, b_i (|a_i|, |b_i| ≤ 2·10⁹) and calls an
animal with parameters (A, B) a camel if a_i·A + b_i·B > 0, a sheep if
it is < 0, and says nothing if it is 0. A commission of K experts calls
an animal a camel (a sheep) when strictly more than half of the experts
say so. Given N known animals (1 ≤ N ≤ 10000, 0 ≤ A, B ≤ 10000, kind 1
for a camel and 2 for a sheep), find the smallest K and the experts'
numbers that judge every animal right, or print −1 if no commission
can.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines A B kind.

## Output

−1, or K and K lines a_i b_i. Any fitting experts are accepted.

## Examples

### Example 1

Input:

```
2
10 0 1
0 10 2
```

Output:

```
1
1 -1
```

## Solution

An expert's verdict depends only on the direction of (A, B): an animal
at the origin gets no vote from anybody, and two animals on one ray from
the origin get the same votes, so either case with different kinds on a
ray means −1. Reduce every point by the gcd and sort the rays by angle;
they all lie in the first quadrant, an arc shorter than π, so an expert
switches the verdict at most once along it. Let r be the number of runs
of one kind.

Count the experts saying "camel". With K odd, that count must cross from
above K / 2 to below it at every boundary between runs, which takes at
least one expert switching there; with K even it must drop from K/2 + 1
or more to K/2 − 1 or less, which takes two. So K ≥ r − 1 for odd K and
K ≥ 2(r − 1) for even K, and the smallest K is r − 1 when that is odd
and r otherwise (including K = 1 for one run). It is reached: at each
boundary between rays p and q, the line through the origin along p + q
lies strictly between them, and the expert perpendicular to it votes for
the earlier kind before it and the other kind after it. When the count
of those experts is even, one more expert, (1, 1) or (−1, −1), votes for
the first kind everywhere; then the vote margin alternates between +1
and −1 across the runs. All numbers stay below 20001. `O(N log N)`.

Pitfalls:

- an animal at the origin can never be judged (test 02);
- points on one ray, like (2, 4) and (1, 2), are the same direction:
  different kinds there mean −1, equal kinds are one run (tests 03, 05,
  gen3, gen5);
- an odd number of runs needs one extra expert, because an even
  commission needs two switches per boundary (tests 06, 08);
- rays as close as (9999, 9998) and (10000, 9999) must be told apart
  with exact integer cross products (test 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1473_geometry.cpp](1473_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.031 s | 516 KB |
| [1473_geometry.go](1473_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 2544 KB |
| [1473_geometry.java](1473_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 4224 KB |
| [1473_geometry.py](1473_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.109 s | 5840 KB |
| [1473_geometry.rs](1473_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 832 KB |
