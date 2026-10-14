# 1529. Game of Squares

[Timus 1529](https://acm.timus.ru/problem.aspx?space=1&num=1529) · difficulty 3540 · games

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players take turns with a k-dimensional box of n1 × … × nk unit
cubes (1 ≤ k ≤ 8, (n1 + 1)·…·(nk + 1) ≤ 10000), and later with the boxes
left over. A move picks a box and a unit cube in it and cuts through
that cube with the k planes parallel to the faces: the cut cubes vanish
and up to 2^k smaller boxes remain. A cut is allowed if one of the new
boxes has every edge coprime with the matching edge of the box being
cut, or if nothing remains. The player who cannot move loses. Say who
wins, and if it is Alice, who moves first, her lexicographically
smallest winning cut.

Time limit: 5 seconds. Memory limit: 64 MB.

## Input

k, then n1 … nk.

## Output

1 or 2 for the winner, and for 1 the 1-based coordinates of the cut.

## Examples

### Example 1

Input:

```
2
2 2
```

Output:

```
2
```

### Example 2

Input:

```
3
3 4 5
```

Output:

```
1
1 1 3
```

## Solution

The boxes left over are independent games, so by the Sprague–Grundy
theorem every box has a value and a move is worth the XOR of the values
of the parts it leaves; an empty part is worth 0. A cut at position c of
an edge d leaves the pieces c − 1 and d − c along it, and the parts are
all combinations of the pieces of the k edges. A part has every edge
coprime exactly when each of its pieces is, so a cut is allowed when
every edge has a nonempty piece coprime with it; as gcd(d − c, d) =
gcd(c, d), a middle cut fails only when both c − 1 and c share a factor
with d. A box with an edge of 1 vanishes under any cut and is worth 1.
In one dimension the two pieces always total d − 1, which makes the
value d mod 2.

The value of a box does not depend on the order of its edges, so the
values are computed for sorted edge lists in order of growing size and
stored under every ordering. For a box, take the table of its parts'
values indexed by piece lengths, and replace one axis at a time by its
legal cuts, each cut XORing the slices at c − 1 and d − c: after all axes
the table holds the value of every move, and the mex of those is the
box's value. This costs about 2k operations per entry of the table
rather than 2^k. Alice wins when the whole box is worth more than 0,
and her first move is the first zero in the table of moves of the whole
box, in the input's order of edges.

Pitfalls:

- "the original parallelepiped" in the rule is the box being cut at
  that move; this reading is the one the judge accepts;
- a box with an edge of 1 can always be cut away, so Alice wins with
  the cut (1, …, 1) (test 05);
- one dimension needs no search: odd lengths win (tests 03, 04, 10);
- the rectangle 6 × 5 has some cuts that are not allowed (test 06);
- both square boxes such as 99 × 99 and long thin ones such as
  1046 × 2 are heavy (test 07, gen1).

## Language notes

The Python solution packs each row of values along the last axis into
one big integer with 16-bit lanes. A cut on the last axis joins lane
c − 1 with lane d − c, which is lane c − 1 of the reversed row, so whole
rows are XORed at once, and the other axes XOR whole rows too. Even the
plain computation of the legal cuts is done with byte masks.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1529_games.cpp](1529_games.cpp) | G++ 13.2 x64 | games | O(k * prod(n_i)^2) | AC | 0.125 s | 3768 KB |
| [1529_games.go](1529_games.go) | Go 1.14 x64 | games | O(k * prod(n_i)^2) | AC | 0.375 s | 12336 KB |
| [1529_games.java](1529_games.java) | Java 1.8 | games | O(k * prod(n_i)^2) | AC | 0.296 s | 7560 KB |
| [1529_games.py](1529_games.py) | Python 3.12 x64 | games | O(k * prod(n_i)^2) | AC | 1.375 s | 2148 KB |
| [1529_games.rs](1529_games.rs) | Rust 1.75 x64 | games | O(k * prod(n_i)^2) | AC | 0.125 s | 4892 KB |
