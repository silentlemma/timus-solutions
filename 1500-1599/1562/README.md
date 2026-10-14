# 1562. GM-pineapple

[Timus 1562](https://acm.timus.ru/problem.aspx?space=1&num=1562) · difficulty 402 · geometry

Original problem by Denis Musin, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A pineapple is a prolate ellipsoid of revolution of width a and height
b (1 ≤ a < b ≤ 100, in centimetres). It lies on its side and is cut
across its axis into n pieces of equal thickness (1 ≤ n ≤ 100). One
cubic centimetre weighs one gram. Print the weight of every piece in
the order they are cut, to a microgram.

Time limit: 1 second. Memory limit: 64 MB.

## Input

a, b and n on one line; a and b may be fractional.

## Output

n lines, the weights in grams with six digits after the point.

## Examples

### Example 1

Input:

```
15 20.5 8
```

Output:

```
103.773800
273.585474
386.793256
443.397147
443.397147
386.793256
273.585474
103.773800
```

## Solution

Put the axis along z with the middle at 0. The cross-section at height
z is a disc of radius (a/2)·√(1 − (2z/b)²), so its area is
π·a²/4·(1 − 4z²/b²). Its integral from 0 to z,

V(z) = π·a²/4·(z − 4z³/(3b²)),

gives the piece between cuts z₁ and z₂ as V(z₂) − V(z₁), with cuts at
−b/2 + b·i/n. The whole pineapple weighs π·a²·b/6, the sum of all
pieces. `O(n)`.

Pitfalls:

- a is the full width, not the radius;
- the sizes may be fractional (tests 05 and the example);
- the end pieces of a long thin pineapple weigh only hundredths of a
  gram, and they still need six digits (test 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1562_geometry.cpp](1562_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 156 KB |
| [1562_geometry.go](1562_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1100 KB |
| [1562_geometry.java](1562_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.109 s | 2072 KB |
| [1562_geometry.py](1562_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.093 s | 424 KB |
| [1562_geometry.rs](1562_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.015 s | 268 KB |
