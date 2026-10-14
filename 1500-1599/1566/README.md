# 1566. Triangular Postcards

[Timus 1566](https://acm.timus.ru/problem.aspx?space=1&num=1566) · difficulty 3034 · geometry

Original problem by Vladimir Yakovlev, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given the integer sides of a triangular envelope and of a triangular
card, all at most 1000 millimetres, decide whether the card fits into
the envelope. The card may be moved, turned and flipped, and it may
touch the edges of the envelope.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The sides of the envelope on the first line, those of the card on the
second.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
30 40 50
50 36 27
```

Output:

```
YES
```

### Example 2

Input:

```
200 200 200
210 110 110
```

Output:

```
NO
```

## Solution

A triangle fits into another one exactly when it fits with one of its
sides lying on a side of the other. This is a known fact about two
triangles, and it was also confirmed here: a fine search over the turns
of the card, which tests each turn exactly (a translation exists when the
sum over the envelope's sides of length × the card's farthest reach
past that side's direction stays within twice the area), agreed with
this rule on about 600 random pairs, and so did an independent program.

So there are 3 · 3 · 2 placements to try: a side of the card on a side
of the envelope, the card flipped or not. With the envelope's side from
(0, 0) to (m, 0), its apex at (w, H), and the card's apex at (u, h)
above the start of its side of length ℓ, the card slides by t along the
side. It fits when ℓ ≤ m, h ≤ H and some t in [0, m − ℓ] puts its apex
between the envelope's other two sides:

h·w / H ≤ t + u ≤ m − h·(m − w) / H.

Both ends are linear in t, so this is an intersection of intervals.
Touching counts, so every comparison allows 10⁻⁹. A flat envelope, if
one is given, holds only a flat card that is no longer. All this takes
constant time.

Pitfalls:

- the card may be the envelope itself, touching it everywhere (test 03);
- a long side is not enough: a needle of length 999 with a 2 mm end is
  too wide at that end to reach into a 60° corner of a 1000 mm
  equilateral envelope (test 05);
- the card's apex may lie beyond the ends of its own side when it has an
  obtuse angle there, and so may the envelope's (test 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1566_geometry.cpp](1566_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 128 KB |
| [1566_geometry.go](1566_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1064 KB |
| [1566_geometry.java](1566_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1716 KB |
| [1566_geometry.py](1566_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 656 KB |
| [1566_geometry.rs](1566_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 232 KB |
