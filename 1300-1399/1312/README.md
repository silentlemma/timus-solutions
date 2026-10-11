# 1312. Tray

[Timus 1312](https://acm.timus.ru/problem.aspx?space=1&num=1312) · difficulty 3032 · geometry

Original problem: idea by Alexander Petrov, prepared by Alexander Petrov and Alexander Mironenko, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place three round plates of radii R1, R2, R3 on a rectangular H × W
tray so that none sticks out and no two overlap (touching is allowed).
All numbers are positive integers up to 10⁶. Print the three centres
with four decimals, in the order of the radii, or `0` if they cannot be
placed.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

H, W, R1, R2 and R3.

## Output

Six coordinates, or `0`.

## Checking

Any valid placement is accepted. The checker verifies that every plate
lies on the tray and that no two overlap, allowing 10⁻³ for the
rounding to four decimals. When the expected answer is `0`, the output
must be `0` too.

## Examples

### Example 1

Input:

```
800 400 200 200 50
```

Output:

```
200.0000 200.0000 600.0000 200.0000 400.0000 50.0000
```

### Example 2

Input:

```
800 400 200 200 51
```

Output:

```
0
```

## Solution

Take any valid placement and push the plates down and to the left as
far as they go: among all valid placements take one with the smallest
total of x + y over the three centres. Such a placement exists, since
the set of placements is closed and bounded. In it every plate is
blocked, and a plate touching just one object could still roll around
it to a smaller x + y. So every plate touches two things that hold it,
the left or bottom wall or a plate lower and further left, and that
fixes its centre.

So it is enough to try every order of the plates and, for each plate in
turn, every centre where it touches two of: the walls (all four, to be
safe) and the plates already placed.

- touching two walls: the four corners (r, r), (H − r, r), …;
- touching a wall and a placed plate of radius s: on a line x = r or
  x = H − r (or y = …), at distance r + s from that plate's centre;
- touching two placed plates: the intersection of two circles around
  their centres, of radii r + s₁ and r + s₂.

Each candidate is kept only if the plate lies on the tray and does not
overlap the plates already placed. Six orders, at most a few dozen
candidates per plate: the whole search is tiny. The comparisons allow
10⁻⁹ of the tray size, so exact touching survives rounding.

Pitfalls:

- an answer often exists only with plates exactly touching, as in the
  example; one unit more and it is gone (tests 01 and 02);
- the gaps in the corners next to a plate that fills the tray take a
  radius of about (√2 − 1)/(√2 + 1) of it: 8 fits next to 50, 9 does
  not (tests 10 and 11);
- a plate wider than the tray is impossible at once (test 08).

Every placement printed on 250 small random trays was checked to be
valid, and for every tray answered with `0`, a penalty-descent search
from 60 random starts found no placement either.

## Language notes

- C++, Python and Rust try the orders in increasing order, Go and Java
  by Heap's algorithm, so the languages may print different valid
  placements.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1312_geometry.cpp](1312_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 212 KB |
| [1312_geometry.go](1312_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1204 KB |
| [1312_geometry.java](1312_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 2072 KB |
| [1312_geometry.py](1312_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 860 KB |
| [1312_geometry.rs](1312_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 292 KB |
