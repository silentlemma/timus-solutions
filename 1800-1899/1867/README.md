# 1867. Nanotechnologies

[Timus 1867](https://acm.timus.ru/problem.aspx?space=1&num=1867) · difficulty 2568 · geometry

Original problem by Sergey Pupyrev (prepared by Ivan Burmistrov), from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given the squared distances between every two of n atoms, place the
atoms at points with integer coordinates of absolute value at most 10⁶
so that all the squared distances are as given, or say that this is
impossible. Several atoms may share a point.

## Input

n (2 ≤ n ≤ 100), then the symmetric n × n matrix of integers aᵢⱼ
(0 ≤ aᵢⱼ ≤ 10⁹, aᵢᵢ = 0).

## Output

n lines with the coordinates of the atoms, or "Impossible". Any valid
placement is accepted.

## Examples

### Example 1

Input:

```
3
0 1 4
1 0 1
4 1 0
```

Output:

```
0 0
1 0
2 0
```

### Example 2

Input:

```
3
0 1 5
1 0 1
5 1 0
```

Output:

```
Impossible
```

### Example 3

Input:

```
3
0 1 0
1 0 1
0 1 0
```

Output:

```
5 -5
5 -4
5 -5
```

## Solution

Shifts keep the grid, so atom 1 can sit at the origin. Let p be the
first atom at a positive distance D from it. Quarter turns and
reflections in the axes and the diagonals also keep the grid, so p can
be taken to be at (a, b) with 0 ≤ a ≤ b and a² + b² = D. These pairs
are found by trying every a up to √(D/2), and each of them is tried.

With atoms 1 and p fixed, another atom (x, y) at squared distances d₁
and dₚ from them has the dot product ax + by = (d₁ − dₚ + D)/2. Its
cross product bx − ay is ±√(D·d₁ − dot²), because
dot² + cross² = D·(x² + y²). Then x = (a·dot + b·cross)/D and
y = (b·dot − a·cross)/D, and all of these must be integers. Atoms on
the line through 1 and p have cross 0. The first atom off that line may
go to either side, and both sides are tried: the mirror image of an
integer point in a slanted line is usually not an integer point. After
that only one sign agrees with the distance to that atom. Every atom is
checked against all atoms placed before it, so a placement that gets
through is an answer. Its coordinates stay within √10⁹ of the origin,
far inside the limit. `O(√D + r·n²)`, where r, the number of ways to
write D as a² + b², is a few dozen at most.

For the first example this gives (0, 0), (0, 1), (0, 2) and for the
third (0, 0), (0, 1), (0, 0); both are as good as the sample answers.

Pitfalls:

- different ways to write D are not the same: 25 = 0² + 5² = 3² + 4²,
  and atoms at (0, 0), (3, 4) and (4, 3) fit only the second;
- both sides of the first slanted line must be tried for the same
  reason;
- atoms may share a point, also with atom 1, and all distances may be
  0;
- products reach 10¹⁸, so 64-bit integers are needed.

The answers pass a checker on every matrix of 3 atoms with entries up
to 13 and of 4 atoms with entries up to 5, compared against all small
placements, and on large random ones. The "Impossible" answers agree
with an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1867_geometry.cpp](1867_geometry.cpp) | G++ 13.2 x64 | geometry | O(sqrt(D) + r n^2) | AC | 0.015 s | 280 KB |
| [1867_geometry.go](1867_geometry.go) | Go 1.14 x64 | geometry | O(sqrt(D) + r n^2) | AC | 0.031 s | 1340 KB |
| [1867_geometry.java](1867_geometry.java) | Java 1.8 | geometry | O(sqrt(D) + r n^2) | AC | 0.140 s | 636 KB |
| [1867_geometry.py](1867_geometry.py) | Python 3.12 x64 | geometry | O(sqrt(D) + r n^2) | AC | 0.093 s | 1676 KB |
| [1867_geometry.rs](1867_geometry.rs) | Rust 1.75 x64 | geometry | O(sqrt(D) + r n^2) | AC | 0.046 s | 440 KB |
