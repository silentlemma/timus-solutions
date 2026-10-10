# 1188. Rearranging bookcase shelves to fit one big tome

[Timus 1188](https://acm.timus.ru/problem.aspx?space=1&num=1188) · difficulty 2174 · geometry

Original problem by Elena Kryuchkova and Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A niche of width `XN` and height `YN` holds `N ≤ 100` horizontal planks at
different heights, each resting on two pegs with the plank's middle
between them. A tome of width `XT` and height `YT` must stand on one
shelf, fully on it, without any other shelf or peg entering its inside.
Each shelf may be left alone, slid, shortened by whole inches, have one
peg moved to another place at the same height (with sliding and cutting
allowed too), or be removed with both its pegs; every shelf left must
still rest properly on its pegs inside the niche. Minimise first the
number of pegs moved (a removal moves two), then the inches cut (a
removal cuts the whole plank).

Time limit: 1 second. Memory limit: 64 MB.

## Input

`XN YN XT YT`, `N`, then for each shelf its height, left end, length and
the offsets of its two pegs from the left end. Everything is in whole
inches up to 1000.

## Output

The fewest pegs moved and then the fewest inches cut.

## Examples

### Example 1

Input:

```
11 8 3 4
4
1 1 7 1 4
4 3 7 1 6
7 2 6 3 4
2 0 3 0 3
```

Output:

```
0 0
```

### Example 2

Input:

```
11 8 4 6
4
1 1 7 1 4
4 3 7 1 6
7 2 6 3 4
2 0 3 0 3
```

Output:

```
1 3
```

## Solution

Try the tome on every shelf `i` at every whole position `x`. The cost
splits into the cost of making shelf `i` carry the tome and, for each
shelf strictly between the tome's bottom and top, the cost of getting it
out of the strip `(x, x + XT)`. These parts are independent.

Getting a shelf out of the strip means putting its plank wholly into
`[0, x]` or into `[x + XT, XN]`; call that room `[F, G]`. If no peg
moves, both pegs `a < b` must be in the room, and a plank of length `t`
can be placed over them with its middle between them exactly when
`b − a ≤ t ≤ min(2(b − F), G − F, 2(G − a))`. So the cut is the plank
length minus the largest allowed `t`, if that is at least `b − a`. If one
peg may move, the new peg can always balance the plank, so only the peg
that stays has to be in the room, and the cut is whatever does not fit:
cost one peg plus `max(0, length − (G − F))`. Removal costs two pegs and
the whole length. The best of these is the shelf's cost.

The carrying shelf never needs a cut, since a shorter plank covers less.
With its pegs fixed, the possible left ends of the plank form an
interval, which is checked with doubled coordinates to keep the middle an
integer. Otherwise moving one peg works whenever the plank is long enough
to reach over the tome and the peg that stays.

The clearing cost of each shelf depends only on `x`, so with the shelves
sorted by height, prefix sums over shelves give the total for the shelves
above shelf `i` at once. A cost is stored as pegs times a million plus
inches, which orders them correctly. `O(N·XN)`.

Pitfalls:

- shelves exactly at the tome's top or at its own height may touch it and
  cost nothing;
- a moved plank must stay inside the niche, which is what forces cuts
  near the walls;
- a tome as wide as the niche leaves no room on one side, so a shelf in
  the way can only go to the other side or be removed.

The answers were compared with a separately written solution on 667
random bookcases and on every test.

## Language notes

- All languages use the same closed-form costs and the same prefix sums
  over the sorted shelves.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1188_geometry.cpp](1188_geometry.cpp) | G++ 13.2 x64 | geometry | O(N·XN) | AC | 0.015 s | 604 KB |
| [1188_geometry.go](1188_geometry.go) | Go 1.14 x64 | geometry | O(N·XN) | AC | 0.031 s | 1960 KB |
| [1188_geometry.java](1188_geometry.java) | Java 1.8 | geometry | O(N·XN) | AC | 0.171 s | 7384 KB |
| [1188_geometry.py](1188_geometry.py) | Python 3.12 x64 | geometry | O(N·XN) | AC | 0.281 s | 4880 KB |
| [1188_geometry.rs](1188_geometry.rs) | Rust 1.75 x64 | geometry | O(N·XN) | AC | 0.015 s | 900 KB |
