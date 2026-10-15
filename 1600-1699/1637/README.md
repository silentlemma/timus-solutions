# 1637. Triangle Game 2

[Timus 1637](https://acm.timus.ru/problem.aspx?space=1&num=1637) · difficulty 3157 · geometry

Original problem by Alexander Ipatov, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A map has a drawn triangle and a congruent cardboard piece. One move
reflects the piece in any line. Find the fewest moves that make the
piece cover the drawn triangle exactly, or report that it cannot be
done.

## Input

Two lines with six integers each: the corners of the drawn triangle and
the current corners of the piece, all within 2000 in absolute value. The
drawn triangle is not degenerate.

## Output

The least number of moves, or `IMPOSSIBLE`.

## Examples

### Example 1

Input:

```
4 0 6 3 7 0
0 0 2 3 3 0
```

Output:

```
2
```

## Solution

The piece must reach the triangle by an isometry, which sends its
corners to the drawn ones in one of the six orders; an order is possible
only if all three side lengths agree. Every plane isometry is a product
of reflections, and the fewest reflections depend only on its kind:

- the identity: 0;
- a nontrivial rotation or translation (orientation kept): 2, since a
  single reflection always reverses orientation;
- a reflection: 1;
- a glide reflection (orientation reversed, no line of fixed points): 3,
  as two reflections never reverse orientation.

Orientation compares the signs of the cross products of the two
triangles. When it is reversed, the isometry is a single reflection
exactly when one line fits: every corner that moves has the same
perpendicular bisector with its image, and every corner that stays lies
on it. Lines a x + b y = c with a = 2(x' − x), b = 2(y' − y),
c = x'² + y'² − x² − y² are compared by cross-multiplication, using
64-bit integers (arbitrary precision in Python). The answer is the minimum
over the valid orders. `O(1)`.

Pitfalls:

- the corners may be listed in any order, so all six matchings matter
  (test 03);
- in an isosceles triangle a glide reflection under one matching can be a
  half turn under another, so the answer can be 2, not 3 (test 07);
- for a fixed matching, reversed orientation requires a reflection
  (1 move) or a glide reflection (3 moves).

The answers match an independent accepted implementation on 240 random
lattice isometries.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1637_geometry.cpp](1637_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 192 KB |
| [1637_geometry.go](1637_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1100 KB |
| [1637_geometry.java](1637_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1644 KB |
| [1637_geometry.py](1637_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 760 KB |
| [1637_geometry.rs](1637_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 240 KB |
