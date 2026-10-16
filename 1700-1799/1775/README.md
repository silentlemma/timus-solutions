# 1775. Space Bowling

[Timus 1775](https://acm.timus.ru/problem.aspx?space=1&num=1775) · difficulty 935 · geometry

Original problem by Alexander Mironenko, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n round pins of diameter 1 stand on a plane with distinct integer
centres. A ball of a chosen diameter, thrown from any point, rolls in a
straight line and knocks down every pin it touches. Find the smallest
diameter that knocks down at least k pins with one throw.

## Input

n and k (1 ≤ k ≤ n ≤ 200), then the centres xᵢ, yᵢ
(|xᵢ|, |yᵢ| ≤ 10⁵).

## Output

The smallest diameter with an absolute or relative error of at most
10⁻⁶, or 0 if any ball, however small, will do.

## Examples

### Example 1

Input:

```
5 4
0 4
0 6
6 4
6 6
3 0
```

Output:

```
1.0000000000
```

## Solution

A ball of diameter D touches a pin when the pin's centre is within
(D + 1)/2 of the line the ball's centre follows, that is, inside a
strip of width D + 1. Throwing from far enough away, the ball can cover
any whole line, so the task is the narrowest strip that holds k
centres, and the answer is its width minus 1, but not below 0.

For a fixed direction, the narrowest such strip comes from sorting the
centres by their distance across that direction and taking the closest
k in a row. As the direction turns, the width of each such group
changes like |sin| between the moments when two centres line up, and
|sin| has no inner minimum there, so the best direction is one in which
some two centres line up along the strip. That leaves n(n − 1)/2
directions, each a sort; the distances across use the whole-number
cross product with the direction, divided by its length only at the
end. `O(n³ log n)`.

In the example the four centres (0, 4), (0, 6), (6, 4), (6, 6) fit in a
horizontal strip of width 2, so a ball of diameter 1 takes them all.

Pitfalls:

- k centres on one line, or k = 1, give 0;
- a strip narrower than 1 also gives 0, never a negative diameter;
- the thrower may start anywhere, so the path is a whole line, not a
  ray from a pin.

The answers agree with an independent accepted implementation, which
searches on the diameter, on 60 random cases with up to 200 pins. The
Python solution runs on PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1775_geometry.cpp](1775_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^3 log n) | AC | 0.109 s | 228 KB |
| [1775_geometry.go](1775_geometry.go) | Go 1.14 x64 | geometry | O(n^3 log n) | AC | 0.375 s | 2480 KB |
| [1775_geometry.java](1775_geometry.java) | Java 1.8 | geometry | O(n^3 log n) | AC | 0.375 s | 2240 KB |
| [1775_geometry.py](1775_geometry.py) | PyPy 3.10 x64 | geometry | O(n^3 log n) | AC | 0.640 s | 5944 KB |
| [1775_geometry.rs](1775_geometry.rs) | Rust 1.75 x64 | geometry | O(n^3 log n) | AC | 0.109 s | 272 KB |
