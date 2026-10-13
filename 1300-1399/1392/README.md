# 1392. Dreaming of Stars

[Timus 1392](https://acm.timus.ru/problem.aspx?space=1&num=1392) · difficulty 763 · graphs

Original problem by Fedor Fominykh, from the First Collegiate Programming Contest for High School Pupils of Novouralsk, April 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

K ≤ 1000 planets are balls with integer centres and radii up to 1000 in
absolute value. Two planets are stuck together if they share at least
two points, and an archipelago is a group of planets joined by chains
of stuck pairs that no other planet is stuck to. Print the
archipelagos.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

K, then K lines with x, y, z and R.

## Output

One line per archipelago with its planet numbers from 0, in increasing
order and separated by a comma and a space; the archipelagos are ordered
by their smallest planet.

## Examples

### Example 1

Input:

```
2
1 1 1 1
1 3 1 1
```

Output:

```
0
1
```

### Example 2

Input:

```
3
1 1 1 1
1 3 1 1
1 4 1 1
```

Output:

```
0
1, 2
```

### Example 3

Input:

```
3
1000 1000 1000 1
 999 1000 1000 1
   1    1    1 1
```

Output:

```
0, 1
2
```

## Solution

Two solid balls share more than one point exactly when they overlap,
which happens when the distance between the centres is less than
r₁ + r₂; when it is equal they only touch. In integers that is
dx² + dy² + dz² < (r₁ + r₂)², with no rounding at all. The archipelagos
are the connected components of this relation: check all pairs and join
the overlapping ones in a disjoint-set union. Then gather the planets by
their root in increasing order and sort the groups by their first
planet. `O(K²)`.

Pitfalls:

- balls that touch at one point are not stuck (examples 1 and 2, test
  06);
- a ball inside another one, even touching it from inside, is stuck to
  it (test 05);
- a chain given out of order still forms one archipelago (test 04);
- the separator is a comma and a space, with none after the last
  planet.

The tests are judged by exact comparison.

## Language notes

- Python runs under PyPy: CPython exceeds the 0.5 s limit on the judge's
  test 10, and PyPy takes about 0.2 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1392_graphs.cpp](1392_graphs.cpp) | G++ 13.2 x64 | graphs | O(K^2) | AC | 0.015 s | 264 KB |
| [1392_graphs.go](1392_graphs.go) | Go 1.14 x64 | graphs | O(K^2) | AC | 0.031 s | 1224 KB |
| [1392_graphs.java](1392_graphs.java) | Java 1.8 | graphs | O(K^2) | AC | 0.171 s | 2964 KB |
| [1392_graphs.py](1392_graphs.py) | PyPy 3.10 x64 | graphs | O(K^2) | AC | 0.203 s | 5736 KB |
| [1392_graphs.rs](1392_graphs.rs) | Rust 1.75 x64 | graphs | O(K^2) | AC | 0.031 s | 320 KB |
