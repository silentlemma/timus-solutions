# 1239. One ray through as many spheres as possible

[Timus 1239](https://acm.timus.ru/problem.aspx?space=1&num=1239) · difficulty 3015 · geometry

Original problem by Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A gun at the origin fires one ray into the octant x, y, z ≥ 0. There are
N ghosts (0 ≤ N ≤ 100), balls with integer centres (X, Y, Z), 1 ≤ X, Y,
Z ≤ 10 000, and integer radius 1 ≤ R ≤ min(X, Y, Z); the ray kills every
ghost it touches, even at one point. Find the most ghosts one ray can
kill, and which ones.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then each ghost as `X Y Z R`.

## Output

The maximum number of ghosts, then their numbers in any order.

## Checking

Several groups can be best, so the checker accepts any: the count must
equal the maximum count, the numbers must be distinct, and a ray
touching all the listed ghosts must exist. The checker looks for that
ray with 50-digit decimals.

## Examples

### Example 1

Input:

```
2
1200 1200 3900 300
160 160 820 60
```

Output:

```
2
1 2
```

### Example 2

Input:

```
13
1200 1200 3900 300
160 160 820 60
100 10 10 10
10 100 10 10
10 10 100 10
10 10 10 10
50 50 50 10
100 100 75 20
100 75 100 20
75 100 100 20
3000 4000 7000 2600
100 1000 1000 50
1000 100 1000 100
```

Output:

```
5
6 7 9 10 11
```

## Solution

Seen from the gun, a ghost with centre C is a circular cone: a ray along
d touches it exactly when `d·C ≥ L·|d|`, where `L = √(|C|² − R²)` is the
length of a tangent from the origin. On the sphere of directions each
ghost is a cap, and the task asks for a point covered by the most caps.

The caps a best point lies in meet in a convex region. Either that region
is a single cap, and then that cap's centre is in all of them, or it has a
corner where the outlines of two caps cross or touch. So it is enough to
try the direction to each centre and the points where two outlines meet,
`O(N²)` candidates, and count the caps holding each one. `O(N³)`.

For det > 0, the outlines of caps i and j meet at the unit vectors
`d = (a·C_i + b·C_j ± c·C_i×C_j)` with `d·C_i = L_i` and `d·C_j = L_j`.
Writing `g = C_i·C_j` and `det = |C_i|²|C_j|² − g²`,

```text
a·det = L_i|C_j|² − L_j·g,   b·det = L_j|C_i|² − L_i·g,   c² = Q / det²,
Q = det − L_i²|C_j|² − L_j²|C_i|² + 2g·L_i·L_j
```

The whole difficulty is precision: the first example only works because
the two cones touch exactly, and a touch is enough. So every decision
that can be made in integers is:

- the centre of cap i lies in cap k when `(C_i·C_k)² ≥ L_k²·|C_i|²`, all
  integers;
- the outlines meet when Q ≥ 0, where Q is an integer plus `2g·√(L_i²L_j²)`;
  its sign comes from comparing squares in 128-bit integers, so a touch
  gives exactly Q = 0 and a single point;
- when Q, `a·det` and `b·det` are differences of nearly equal numbers,
  they are computed through the conjugate, `x − y = (x² − y²)/(x + y)`,
  with the numerator exact.

Only the last test, whether a third cap holds the candidate point, uses a
relative tolerance of 10⁻⁹.

Pitfalls:

- equal cones from scaled ghosts, like `(1200, 1200, 3900, 300)` and
  `(2400, 2400, 7800, 600)`, have coincident outlines (det = 0), so their
  pair is skipped; points with other caps still count both (test 09);
- a slightly thinner copy must miss the touching point (test 08);
- with no ghosts the answer is 0 and an empty list.

The answers were compared with the same search done in 80-digit decimals
on 600 random small cases, many of them made of scaled and mirrored
copies.

## Language notes

- C++ and Rust use 128-bit integers for the exact signs, Go `math/big` and
  Java `BigInteger`; Python's integers are exact already.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1239_geometry.cpp](1239_geometry.cpp) | G++ 13.2 x64 | geometry | O(N³) | AC | 0.031 s | 252 KB |
| [1239_geometry.go](1239_geometry.go) | Go 1.14 x64 | geometry | O(N³) | AC | 0.031 s | 3908 KB |
| [1239_geometry.java](1239_geometry.java) | Java 1.8 | geometry | O(N³) | AC | 0.125 s | 3728 KB |
| [1239_geometry.py](1239_geometry.py) | Python 3.12 x64 | geometry | O(N³) | AC | 0.187 s | 1132 KB |
| [1239_geometry.rs](1239_geometry.rs) | Rust 1.75 x64 | geometry | O(N³) | AC | 0.015 s | 296 KB |
