# 1232. Landing a probe inside a cone

[Timus 1232](https://acm.timus.ru/problem.aspx?space=1&num=1232) · difficulty 2375 · geometry

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A station hangs at height h above a flat asteroid, on the z axis. A probe
leaves the station and moves in straight pieces of exactly length d; each
piece must bring it lower, and the whole path must stay inside the cone of
apex angle α below the station, in which the station's signals reach. The
last piece must also have length d and end on the surface. Find a path with
the fewest pieces, or report that landing is impossible.

Limits: 0.5 ≤ h ≤ 99.9999, 1 ≤ d ≤ 5, 0.1 ≤ α ≤ 2 (radians), all with at
most four decimals.

Time limit: 1 second. Memory limit: 64 MB.

## Input

h, d and α.

## Output

The number of pieces n, or -1 if landing is impossible; then the n points
where the pieces end, as `x y z`, the last one on the surface. Coordinates
need 0.0001 precision.

## Checking

The path is not unique, so any valid path with the fewest pieces is
accepted. Our checker compares n with the expected answer and checks the
length of every piece, that it goes down, that every point is inside the
cone and that the last one is on the surface, all within 0.0001.

## Examples

### Example 1

Input:

```
11 5 2
```

Output:

```
3
0 3 7
3 3 3
3 -1 0
```

## Solution

**How many pieces.** A piece drops at most d, so at least `n = ⌈h/d⌉`
pieces are needed, and n is enough whenever landing is possible at all: if
a longer path lands, its first n pieces end strictly above the surface, and
since the depths n pieces can reach form an interval up to `n·d`, depth h
is reachable with n pieces too. So the answer is n or -1.

**Building the path.** All the work is in losing the extra height: with L
pieces left, `extra = z − (L−1)·d` lies in `(0, d]`, and once one piece
drops exactly `extra`, the rest go straight down. One piece can do that if
`extra` is at least the smallest drop available from the current point.
From a point on the cone wall at depth t below the station, where the cone
is `w = 2t·tan(α/2)` wide, that smallest drop is 0 if `w ≥ d` (the piece
can be almost level), and otherwise it comes from the piece that crosses
to the opposite wall:

```text
drop = (√(d²(1 + tan²) − w²) − w·tan) / (1 + tan²),  tan = tan(α/2)
```

While the extra height cannot be lost in one piece, the path, kept in
the plane y = 0, makes the piece that drops least, crossing to the
opposite wall, so the next piece starts from a wall again.

**When greed is wrong.** Crossing at full tilt is not always best. A
point deeper on the wall sees a wider cone, and while the cone there is
a little under d wide, a deeper start can give a shallower end after the
next crossing. So the program also tries paths whose first j pieces slide
straight down the wall before the zigzag starts, for j = 0, 1, …, n, and
prints the first that lands. j = 0 is the plain greedy zigzag; on test 05
(α = 0.496, d = 1, h = 2.01) it ends below the surface, while two slides
and a crossing land. `O(n²)` with n ≤ 100.

Pitfalls:

- the first piece leaves the apex of the cone, so even the most tilted one
  drops `d·cos(α/2)`; if h is less, nothing can land (tests 02, 06, 10);
- `⌈h/d⌉` needs a small tolerance, or h a multiple of d (test 04) gets
  one piece too many.

Our checker accepts these paths; separately, the answers (n or -1) were
compared with an exhaustive search over depth and distance from the axis
on a fine grid, for angles across the whole range, just above and just
below each threshold where landing becomes possible, and agreed
everywhere. That is a numerical check, not a proof that sliding then
zigzagging is always enough.

## Language notes

- All languages run the same simulation with the same tolerance and print
  six decimals.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1232_geometry.cpp](1232_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.015 s | 220 KB |
| [1232_geometry.go](1232_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.015 s | 1164 KB |
| [1232_geometry.java](1232_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.125 s | 1636 KB |
| [1232_geometry.py](1232_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.078 s | 688 KB |
| [1232_geometry.rs](1232_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.031 s | 256 KB |
