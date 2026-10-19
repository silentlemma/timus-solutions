# 1875. Angry Birds

[Timus 1875](https://acm.timus.ru/problem.aspx?space=1&num=1875) · difficulty 965 · geometry

Original problem by Fedor Fominykh, from the Ural Regional Team Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A slingshot at the origin launches birds with any speed at any angle;
only gravity acts on them, so each flies along a parabola that opens
downwards. Birds pass through the monkeys they hit. Five monkeys hang
at points with positive coordinates, no two of them on one line with
the slingshot. What is the least number of shots that hits them all?

## Input

Five lines with the coordinates of the monkeys, positive integers up to
10 000.

## Output

The least number of shots.

## Examples

### Example 1

Input:

```
1 5
2 8
3 9
4 8
5 5
```

Output:

```
1
```

## Solution

A shot follows y = bx − cx² with c > 0, and any such curve can be
flown. Dividing by x, the slope y/x = b − cx falls linearly in x. So a
shot hits several monkeys exactly when their slopes y/x lie on one
falling line as a function of x. Two monkeys can share a shot only if
they have different x and the one further right has the smaller slope.
Such a pair fixes the shot, and the other monkeys on it are found with
the line test, all in integers after clearing denominators. With every
single monkey and every pair's shot as candidate sets, a DP over the
2⁵ subsets finds the fewest sets that cover all five. `O(1)`.

In the example the slopes are 5, 4, 3, 2, 1 at x = 1 … 5: one falling
line, so the parabola y = x(6 − x) hits all monkeys with one shot.

Pitfalls:

- monkeys above one another (same x) can never share a shot;
- a pair whose slope grows with x would need an upward parabola, which
  gravity does not allow;
- products reach about 10¹⁶, so 64-bit integers are needed.

The answers agree with an independent accepted implementation on 300
random levels, many with three to five monkeys on one parabola.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1875_geometry.cpp](1875_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 196 KB |
| [1875_geometry.go](1875_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1072 KB |
| [1875_geometry.java](1875_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1700 KB |
| [1875_geometry.py](1875_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.125 s | 588 KB |
| [1875_geometry.rs](1875_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 236 KB |
