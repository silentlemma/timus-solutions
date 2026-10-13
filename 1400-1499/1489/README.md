# 1489. Points on a Parallelepiped

[Timus 1489](https://acm.timus.ru/problem.aspx?space=1&num=1489) · difficulty 384 · geometry

Original problem by Vladislav Isenbaev and Alexander Toropov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A box A × B × C (1 ≤ A, B, C ≤ 1000) is cut out as a cross-shaped net:
a column of width A at x from C to C + A holding, from the bottom up,
faces of heights B, C, B and C, and two C × B flaps on either side of
the third face. Two different points of the net, with two decimals,
are marked. Find the distance between them once the box is folded,
within 10⁻⁶.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A, B and C, then the two points as x y.

## Output

The distance.

## Examples

### Example 1

Input:

```
2 2 2
3.00 3.00
5.00 5.00
```

Output:

```
1.4142135623730950
```

## Solution

Put the third face of the column on the floor: its corner (C, B + C)
goes to the origin, and a point (x, y) of it to (x − C, y − B − C, 0).
Every other face folds up from it along a shared edge, so a point keeps
its distance from that edge as its height:

- the left flap gives (0, y − B − C, C − x), the right flap
  (A, y − B − C, x − C − A);
- the face below the floor gives (x − C, 0, B + C − y), the one above it
  (x − C, B, y − 2B − C);
- the bottom face of the column becomes the lid: (x − C, B − y, C).

Points on a shared edge get the same position from either face. The
answer is the straight-line distance between the two positions.
Reading the coordinates in hundredths keeps the faces exact. `O(1)`.

Pitfalls:

- the distance is straight through the box, not along its surface
  (tests 01, 03);
- two different points of the net can be glued into one point of the
  box, and the answer is then 0 (tests 02, 05);
- the far ends of the column and of the flaps all become edges of the
  lid or of the side faces (tests 04, 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1489_geometry.cpp](1489_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 208 KB |
| [1489_geometry.go](1489_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1120 KB |
| [1489_geometry.java](1489_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1892 KB |
| [1489_geometry.py](1489_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 572 KB |
| [1489_geometry.rs](1489_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 256 KB |
