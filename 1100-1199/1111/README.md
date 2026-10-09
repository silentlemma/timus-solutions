# 1111. Sorting squares by their distance to a point

[Timus 1111](https://acm.timus.ru/problem.aspx?space=1&num=1111) · difficulty 386 · geometry

Original problem on Timus; its author and source are not given.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `n` filled squares (`1 ≤ n ≤ 50`), each given by two opposite
corners with integer coordinates in `(−9999, 9999)`; the squares may be
turned at any angle, and a square may shrink to a single point. The
distance from a point `P` to a square is the length of the shortest
segment from `P` to a point of the square, so it is 0 when `P` lies
inside. Print the square numbers sorted by distance, the smaller number
first on ties.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`n`, then `n` lines `x1 y1 x2 y2` with two opposite corners, then the
line `x y` of `P`.

## Output

The square numbers (1-based) in sorted order, separated by spaces.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2
0 0 1 1
0 3 1 4
0 0
```

Output:

```
1 2
```

## Solution

Look at each square from its centre `C`, with `D = (x2 − x1, y2 − y1)`
the diagonal. Its sides run along `D` turned by `±45°`, that is along
`D ± D⊥`, where `D⊥` is `D` turned by `90°`. With the doubled offset
`q = 2P − (x1 + x2, y1 + y2)`, all integer, the projections of `q` on the
two side directions are `s1 = |q · (D + D⊥)|` and `s2 = |q · (D − D⊥)|`,
and `P` is inside exactly when both are at most `h = |D|²`. Outside, the
excess `a = max(0, s1 − h)` and `b = max(0, s2 − h)` give the squared
distance `(a² + b²) / (8h)`, and a point square has `|q|² / 4`.

Every squared distance is thus an exact fraction of integers, and two of
them are compared by cross-multiplying; a stable sort keeps equal
distances in input order. `O(n log n)`.

Pitfalls:

- ties are common, from symmetric squares and from `P` inside several of
  them, so the comparison must be exact: floating point can order two
  equal distances either way;
- the numerators reach about `5 · 10^18` and the cross products about
  `10^28`, beyond 64 bits;
- the given corners are opposite, not adjacent, and either diagonal in
  either direction describes the same square.

The answers were checked against a separate exact computation with
fractions: the four corners are built explicitly, containment is tested
by cross products, and the distance is the least distance to the four
sides as segments. Hundreds of random sets, many with ties, agreed.

## Language notes

- C++ and Rust compare in 128-bit integers, Go with `bits.Mul64`, Java
  with `BigInteger`, Python with its own integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1111_geometry.cpp](1111_geometry.cpp) | G++ 13.2 x64 | geometry | O(n log n) | AC | 0.015 s | 192 KB |
| [1111_geometry.go](1111_geometry.go) | Go 1.14 x64 | geometry | O(n log n) | AC | 0.031 s | 1124 KB |
| [1111_geometry.java](1111_geometry.java) | Java 1.8 | geometry | O(n log n) | AC | 0.171 s | 3984 KB |
| [1111_geometry.py](1111_geometry.py) | Python 3.12 x64 | geometry | O(n log n) | AC | 0.062 s | 492 KB |
| [1111_geometry.rs](1111_geometry.rs) | Rust 1.75 x64 | geometry | O(n log n) | AC | 0.015 s | 252 KB |
