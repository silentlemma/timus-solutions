# 1630. Talisman

[Timus 1630](https://acm.timus.ru/problem.aspx?space=1&num=1630) · difficulty 1004 · graphs

Original problem by Sergey Pupyrev (prepared by Daniil Ayzenshteyn), from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A talisman is a set of balls of radius 1 mm placed in space, some pairs
joined by rods 8 mm long, so neighbouring centres are exactly 1 cm apart.
Whenever one ball can be reached from another along rods, the smallest
number of rods on such a way must equal the distance in centimetres
between their centres. Given the scheme (which balls are joined), decide
whether such a talisman can be built.

## Input

The first line holds N and M (1 ≤ N ≤ 100, 0 ≤ M ≤ 10000), the numbers of
balls and rods. Each of the next M lines names two balls joined by a rod;
no pair is joined twice and no rod joins a ball to itself.

## Output

`Luck is possible` if the talisman can be built, otherwise
`Unlucky Petr`.

## Examples

### Example 1

Input:

```
3 3
1 2
1 3
2 3
```

Output:

```
Luck is possible
```

### Example 2

Input:

```
4 4
1 2
1 3
1 4
2 3
```

Output:

```
Unlucky Petr
```

## Solution

Different components can be put far apart, so each one is checked on its
own: its graph distances must be realised by points in space. That
leaves only two shapes.

Take a ball v with two neighbours u and w. They are 1 from v, so they
are either 1 apart or 2 apart; at 2 they are opposite ends of a diameter
through v. A third neighbour x would then have squared distances to u and
w adding up to 4, which no choice of 1 or 4 gives, so such a v has
exactly two neighbours.

- If the component has a triangle a, b, c, any other neighbour d of c
  must be 1 from a (otherwise c would sit between a and d and have three
  neighbours), and likewise 1 from b; repeating this, every ball is
  joined to every other one. Equidistant points in space number at most
  four, so it is a clique of at most 4 balls.
- Without a triangle, the neighbours of every ball are opposite each
  other, so every degree is at most 2 and each middle ball is the
  midpoint of its neighbours: the balls lie on a line, which a cycle
  cannot close. So it is a path.

Both shapes do work: a path along a line, and a point, segment,
equilateral triangle or regular tetrahedron with side 1. A union-find
collects for each component its number of balls k, of rods e and its
largest degree; it is fine when e = k − 1 with degrees at most 2, or
when e = k(k − 1)/2 with k ≤ 4. `O(N + M log N)`.

Pitfalls:

- a triangle with one more ball attached fails (the second example);
- a square or a hexagon is a cycle, not a path (tests 04, 09);
- five balls joined pairwise would need four dimensions (test 05).

The answers match an independent accepted implementation on all 1024
graphs with 5 balls and on 360 random schemes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1630_graphs.cpp](1630_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M log N) | AC | 0.015 s | 216 KB |
| [1630_graphs.go](1630_graphs.go) | Go 1.14 x64 | graphs | O(N + M log N) | AC | 0.031 s | 1248 KB |
| [1630_graphs.java](1630_graphs.java) | Java 1.8 | graphs | O(N + M log N) | AC | 0.093 s | 508 KB |
| [1630_graphs.py](1630_graphs.py) | Python 3.12 x64 | graphs | O(N + M log N) | AC | 0.093 s | 936 KB |
| [1630_graphs.rs](1630_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M log N) | AC | 0.031 s | 292 KB |
