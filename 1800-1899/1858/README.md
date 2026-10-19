# 1858. Magic Cube

[Timus 1858](https://acm.timus.ru/problem.aspx?space=1&num=1858) · difficulty 3556 · bfs

Original problem by Mikhail Rubinchik (prepared by Denis Mukhametianov), from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cube of side n·l was built from n³ cubic crystals of side l. Two
touching faces carry the same rune, a face on the outside carries none,
and every rune appears on exactly two faces. The crystals are given
separately, each in some unknown turn, as the runes on their six faces.
For several pairs of crystals find the distance between their centres in
the assembled cube.

## Input

l and n (1 ≤ l ≤ 100, 2 ≤ n ≤ 30), then n³ lines of six runes from 0 to
10⁹ (0 for no rune), then m (1 ≤ m ≤ 10 000) and m pairs of crystal
numbers.

## Output

The distance for every pair, with absolute or relative error at most
10⁻⁶.

## Examples

### Example 1

Input:

```
1 2
0 8 73 0 0 16
0 9 0 73 0 1000
0 146 4 0 16 0
0 15 0 4 1000 0
146 0 1 0 6 0
15 0 0 1 2 0
8 0 17 0 0 6
9 0 0 17 0 2
2
1 5
2 8
```

Output:

```
1.4142135
1
```

## Solution

The turns of the crystals do not matter at all. Joining every two
crystals that share a rune gives the grid graph of the cube, n × n × n,
and in a grid graph the shortest path between two cells has length equal
to the sum of their absolute coordinate differences. That is enough to
recover the coordinates.

A crystal with the fewest neighbours is a corner c; call it the origin.
A breadth-first search from it gives every crystal its x + y + z. The
other corners are n − 1, 2(n − 1) or 3(n − 1) steps away, so the
corners exactly n − 1 steps from c are its three neighbours along the
edges of the cube, say at (n − 1, 0, 0), (0, n − 1, 0) and
(0, 0, n − 1). A search from the first of them gives
(n − 1 − x) + y + z, so
x = (d(c, v) − d(cₓ, v) + n − 1)/2, and the same for y and z. Four
searches over n³ ≤ 27 000 crystals place them all, up to a symmetry of
the cube that keeps every distance. Each answer is then
l·√(Δx² + Δy² + Δz²). `O(n³ + m)`.

In the example the cube has side 2. Crystal 1 shares runes with crystals
2, 3 and 7, and crystal 5 shares none of them with it but two neighbours,
so they sit on a diagonal of a face: √2. Crystals 2 and 8 share rune 9,
so they touch: 1.

Pitfalls:

- the turns of the crystals are a distraction: only the contact graph
  counts;
- for n = 2 every crystal is a corner and the corners next to c are its
  direct neighbours, which the same rule finds;
- the runes go up to 10⁹, so they need a hash table, not an array.

The distances agree with an independent accepted implementation on
sixty small cubes and on cubes of side 30 with ten thousand questions.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1858_bfs.cpp](1858_bfs.cpp) | G++ 13.2 x64 | bfs | O(n^3 + m) | AC | 0.156 s | 6512 KB |
| [1858_bfs.go](1858_bfs.go) | Go 1.14 x64 | bfs | O(n^3 + m) | AC | 0.062 s | 17504 KB |
| [1858_bfs.java](1858_bfs.java) | Java 1.8 | bfs | O(n^3 + m) | AC | 0.281 s | 15404 KB |
| [1858_bfs.py](1858_bfs.py) | Python 3.12 x64 | bfs | O(n^3 + m) | AC | 0.250 s | 21964 KB |
| [1858_bfs.rs](1858_bfs.rs) | Rust 1.75 x64 | bfs | O(n^3 + m) | AC | 0.031 s | 11632 KB |
