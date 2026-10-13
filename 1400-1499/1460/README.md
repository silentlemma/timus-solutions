# 1460. Wires

[Timus 1460](https://acm.timus.ru/problem.aspx?space=1&num=1460) · difficulty 3928 · geometry

Original problem by Dmitry Ivankov, from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Four pins on a board, with integer coordinates from −200 to 200, must
all be connected by straight pieces of wire; up to three extra pins may
be added anywhere. Find the smallest total length of wire, with at least
four digits after the point, for each of N sets (1 ≤ N ≤ 100).

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N sets of four points, the sets separated by empty lines.

## Output

The smallest length for each set, one per line.

## Examples

### Example 1

Input:

```
2
0 0
2 0
2 1
3 0

0 0
0 1
1 0
1 1
```

Output:

```
3.9093
2.7321
```

## Solution

This is the Euclidean Steiner tree for four points. In an optimal tree
every extra point joins exactly three wires at 120°, so it has at most
two extra points, and every tree is a degenerate case of one of the
three full shapes where pins {a, b} hang on one extra point, {c, d}
on the other, and the two extra points are joined. For such a shape,
Melzak's construction gives the extra points: replace a and b by the
apex e of an equilateral triangle on ab; the second extra point is then
the Fermat point of e, c and d, and the first is the Fermat point of a,
b and the second (Fermat points as in problem 1451). Both sides of ab
are tried for the apex, and both ways round for each pairing.

When the shape does not really fit, the construction may give odd
points, so the length counted is always the real length of the tree
built from them, never the formula |e e'|; then every candidate is an
actual tree and none can undershoot. The degenerate shapes are added
directly: the minimum spanning tree, and one extra point at the Fermat
point of three pins with the fourth pin wired to the nearest of the
four points. The answer is the smallest candidate. `O(1)` per set.

Pitfalls:

- the optimal tree may have no extra point (pins on a line), one, or
  two (tests 01, 02);
- a square needs two extra points, not its diagonals (example 2);
- a construction that does not apply must never give a length below the
  real optimum, which is why real tree lengths are measured.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1460_geometry.cpp](1460_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) per set | AC | 0.015 s | 220 KB |
| [1460_geometry.go](1460_geometry.go) | Go 1.14 x64 | geometry | O(1) per set | AC | 0.031 s | 1184 KB |
| [1460_geometry.java](1460_geometry.java) | Java 1.8 | geometry | O(1) per set | AC | 0.218 s | 5264 KB |
| [1460_geometry.py](1460_geometry.py) | Python 3.12 x64 | geometry | O(1) per set | AC | 0.109 s | 1200 KB |
| [1460_geometry.rs](1460_geometry.rs) | Rust 1.75 x64 | geometry | O(1) per set | AC | 0.015 s | 284 KB |
