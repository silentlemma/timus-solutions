# 1624. Go out of here!

[Timus 1624](https://acm.timus.ru/problem.aspx?space=1&num=1624) · difficulty 4804 · implementation

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A prison is a W × H grid of cells (2 ≤ W · H ≤ 150) with walls or doors
between neighbouring cells and walls all around. Two blind scouts start
in unknown cells (maybe the same one) and take turns trying to move
north, south, east or west, reporting the direction and whether the move
succeeded; odd reports belong to the first scout. Given K reports
(1 ≤ K ≤ 10⁵), print the first report after which both positions are certain,
or that there is not enough data, or the first report that contradicts
the earlier ones (this takes priority).

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

W, H and K, then K reports such as `E+` or `N-`.

## Output

One of three messages; no report number for insufficient data.

## Examples

### Example 1

Input:

```
2 1 4
E+
W-
N-
S-
```

Output:

```
The scouts are safe at step number 2
```

### Example 2

Input:

```
2 1 4
N-
W-
N-
S-
```

Output:

```
There is not enough data
```

### Example 3

Input:

```
2 1 4
N-
W-
N-
S+
```

Output:

```
A mistake has been made at step number 4
```

## Solution

Each scout keeps its position relative to its own unknown start, the
range of positions it has visited, and what it has seen at each edge
relative to its start: a door or a wall. The unknowns are the two
starts. The first scout's start must keep its visited range inside the
prison, which gives an interval for each coordinate; the same for the
second.

The two scouts meet the same walls only through the shift between their
starts. If the first scout saw a door at relative edge e and the second
a wall at relative edge f of the same kind (or vice versa), then a shift
of e − f is impossible. These shifts are marked in a table of
(2H − 1) · (2W − 1) entries. The number of start pairs left is a sum over
the shifts that are not marked, each giving a rectangle of first starts;
counting stops at 2.
A count of 1 means the scouts are located, 0 means a mistake, and so does
a scout reporting a door and a wall at the same edge.

Recount only after a new cross-scout conflict or a wider range. E counts
reports discovering a new edge or widening a range; `E = O(W · H)`.

Pitfalls:

- a mistake must be reported even after the scouts are already located;
- a scout's visited column and row spans must be below W and H (test 05);
- the scouts may stand in one cell without noticing each other.

The answers match an independent accepted implementation on 132 random
prisons, with true and falsified reports.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1624_implementation.cpp](1624_implementation.cpp) | G++ 13.2 x64 | implementation | O(K · log(W · H) + E · W · H) | AC | 0.046 s | 412 KB |
| [1624_implementation.go](1624_implementation.go) | Go 1.14 x64 | implementation | O(K + E · W · H) | AC | 0.046 s | 3004 KB |
| [1624_implementation.java](1624_implementation.java) | Java 1.8 | implementation | O(K + E · W · H) | AC | 0.109 s | 4636 KB |
| [1624_implementation.py](1624_implementation.py) | Python 3.12 x64 | implementation | O(K + E · W · H) | AC | 0.156 s | 8036 KB |
| [1624_implementation.rs](1624_implementation.rs) | Rust 1.75 x64 | implementation | O(K + E · W · H) | AC | 0.031 s | 1436 KB |
