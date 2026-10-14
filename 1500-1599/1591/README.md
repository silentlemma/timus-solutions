# 1591. Abstract Thinking

[Timus 1591](https://acm.timus.ru/problem.aspx?space=1&num=1591) · difficulty 1050 · math

Original problem by Denis Musin, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n points (3 ≤ n ≤ 2000) are spaced evenly on a circle, and every two of
them are joined by a chord. An interesting triangle is formed by three
chords that meet pairwise, with at least one of the meeting points
inside the circle rather than on it. Count the interesting triangles.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n.

## Output

The number of interesting triangles.

## Examples

### Example 1

Input:

```
4
```

Output:

```
4
```

### Example 2

Input:

```
5
```

Output:

```
25
```

## Solution

A triangle is fixed by the set of chord ends it uses, so count by that
set. Two chords meet inside the circle exactly when their ends
alternate around it, which depends only on the order of the points.

- Three corners inside: the chords have six different ends, and of the
  ways to pair six points only the three long diagonals of the hexagon
  all cross each other; one triangle per 6 points.
- Two corners inside: two chords leave one point P and the third chord
  crosses both, so its ends lie on either side of the pair; with 5
  points the triangle is fixed by the choice of P: five per 5 points.
- One corner inside: two corners are on the circle, so one chord is a
  side of a quadrilateral and the other two are its diagonals, which
  cross; one triangle per side, four per 4 points.

The answer is C(n, 6) + 5·C(n, 5) + 4·C(n, 4), in `O(1)`. For n ≤ 12
this was checked against counting all triples of chords, using only the
order of their ends.

Pitfalls:

- in a regular polygon several chords can pass through one point, for
  example the three long diagonals of a hexagon through the centre; the
  answer still counts such a triple as a triangle, as the formula does;
- the answer reaches about 9·10¹⁶, so it needs 64-bit integers, and
  C(n, k) is built as a running product divided step by step, which
  stays below C(n, k)·n.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1591_math.cpp](1591_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB |
| [1591_math.go](1591_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1124 KB |
| [1591_math.java](1591_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1584 KB |
| [1591_math.py](1591_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 432 KB |
| [1591_math.rs](1591_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB |
