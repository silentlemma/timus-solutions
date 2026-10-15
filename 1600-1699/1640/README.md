# 1640. Circle of Winter

[Timus 1640](https://acm.timus.ru/problem.aspx?space=1&num=1640) · difficulty 178 · geometry

Original problem by Dmitry Ivankov (prepared by Alexander Ipatov), from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Demons stand at n lattice points. Sandro may teleport to any point that
holds no demon and cast a ring of ice of radius at most 10000 centred
there. The ring must kill at least one demon (one lying on the circle),
and every demon left alive must be inside it. Output a centre and a
radius.

## Input

n (1 ≤ n ≤ 100), then the coordinates of the demons, integers up to
1000 in absolute value, measured from Sandro's current position. All
demons are at distinct points, none at Sandro's.

## Output

The centre and the radius, accurate to 10⁻⁹. Any valid answer is
accepted.

## Examples

### Example 1

Input:

```
7
1 1
1 5
3 6
5 3
8 0
9 5
5 9
```

Output:

```
5 4 5
```

### Example 2

Input:

```
2
0 2
2 0
```

Output:

```
1 1 1.41421356237309
```

## Solution

No teleport is needed. Sandro's own position holds no demon, and the
circle around it through the farthest demon kills that demon and
encloses all the others. Its radius is at most 1000 · √2, well within
10000. `O(n)`.

Pitfalls:

- the centre must not be a demon's point, so the centre of the smallest
  enclosing circle is not always allowed; the start point always is;
- several valid answers exist, so a checker accepts any circle that
  meets the rules.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1640_geometry.cpp](1640_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 148 KB |
| [1640_geometry.go](1640_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.015 s | 1112 KB |
| [1640_geometry.java](1640_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 2032 KB |
| [1640_geometry.py](1640_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 488 KB |
| [1640_geometry.rs](1640_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.015 s | 256 KB |
