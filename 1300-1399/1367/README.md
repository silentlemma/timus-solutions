# 1367. Top Secret

[Timus 1367](https://acm.timus.ru/problem.aspx?space=1&num=1367) · difficulty 2783 · dsu

Original problem by Pavel Egorov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A picture of at most 1000 × 1000 cells shows walls: `-` is a horizontal
wall through the middle of its cell, `|` a vertical one, `+` a cross of
both, and `.` is open ground. A secret `#` is a cross with an object in
its centre that can be reached from any of the four sides. Agents move
anywhere except through walls and never leave the picture. Two of the at
most 100 secrets are joined when an agent can get from one to the other.
Print the adjacency matrix, with the secrets numbered from top to bottom
and from right to left within a row.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

H lines of W characters each.

## Output

The matrix of 0s and 1s, one row per line.

## Examples

### Example 1

Input:

```
+------+
|#+-+--|
-++#|..|
##..|#.|
-+--+--+
```

Output:

```
10100
01010
10100
01011
00011
```

## Solution

Every wall runs along a middle line of its cell, so the four quarters
of the cells around a corner of the grid always touch one another: the
places an agent can be are the corners of the grid, (H + 1) × (W + 1) of
them. Each cell joins some of its four corners:

- `.` joins all four;
- `-` joins the two upper corners and the two lower ones;
- `|` joins the two left corners and the two right ones;
- `+` and `#` join none.

A disjoint-set union over the corners gives the open regions. A secret
touches the regions of its four corners. The example shows that the
relation is not transitive: secret 4 is joined to 2 and to 5, but 2 and
5 are not. So an agent may not walk through a secret from one of its
sides to another, and two secrets are joined exactly when some corner
of one lies in the same region as some corner of the other.
`O(H · W · log(H · W) + K²)` for K secrets.

Pitfalls:

- the order is right to left within a row, as stated in the output
  specification;
- a wall ending at the edge of a cell does not meet a wall that runs
  through the middle of the next cell: the gap lets agents through
  (test 02), and a cross closes it (test 03);
- a secret is a cross too, so it blocks the way between its own
  neighbours (test 07);
- every secret is joined to itself;
- with no secrets there are no matrix rows (test 09).

The six small pictures from the statement are tests 02 to 07, and the
corner model was compared on 1 500 random pictures of up to 7 × 7 with
a search over the four quarters of every cell.

## Language notes

- Python also runs under CPython.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1367_dsu.cpp](1367_dsu.cpp) | G++ 13.2 x64 | dsu | O(H·W·log(H·W) + K²) | AC | 0.140 s | 4976 KB |
| [1367_dsu.go](1367_dsu.go) | Go 1.14 x64 | dsu | O(H·W·log(H·W) + K²) | AC | 0.062 s | 10736 KB |
| [1367_dsu.java](1367_dsu.java) | Java 1.8 | dsu | O(H·W·log(H·W) + K²) | AC | 0.140 s | 6380 KB |
| [1367_dsu.py](1367_dsu.py) | PyPy 3.10 x64 | dsu | O(H·W·log(H·W) + K²) | AC | 0.453 s | 14008 KB |
| [1367_dsu.rs](1367_dsu.rs) | Rust 1.75 x64 | dsu | O(H·W·log(H·W) + K²) | AC | 0.015 s | 9948 KB |
