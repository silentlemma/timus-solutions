# 1124. Sorting coloured pieces back into their boxes with the fewest hand moves

[Timus 1124](https://acm.timus.ru/problem.aspx?space=1&num=1124) · difficulty 299 · dsu

Original problem by Stanislav Vasiliev, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `M` colours (`2 ≤ M ≤ 500`), `N` pieces of each (`2 ≤ N ≤ 50`)
and `M` boxes, box `i` meant for colour `i`; each box now holds `N`
pieces of arbitrary colours. One hand move either carries one piece from
the box where the hand is to another box (the hand ends there) or moves
the empty hand to another box. The hand may start at any box for free.
Find the fewest moves that put every piece in its own box.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`M N`, then `M` lines of `N` colours: the pieces in each box.

## Output

The fewest hand moves.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4 3
1 3 1
2 3 3
1 2 2
4 4 4
```

Output:

```
6
```

## Solution

Draw a directed edge from box `b` to box `c` for every piece of colour
`c` lying in box `b ≠ c`. Each misplaced piece needs at least one carrying
move, and each carrying move fixes at most one piece. Every box holds `N`
pieces and must end with `N`, so every box has as many edges in as out,
and every connected group of boxes has an Euler circuit: the hand can
follow it, carrying one piece along each edge and ending each carry where
the next one starts. Between two groups the hand needs one empty move.
So with `E` misplaced pieces in `G` groups the answer is `E + G − 1`, and
0 if nothing is misplaced. A disjoint-set union over the boxes finds the
groups. `O(M·N)`.

Pitfalls:

- boxes that are already correct are not a group and need no visit;
- the first placement of the hand is free, hence the `− 1`;
- with no misplaced piece the answer is 0, not `−1`.

The formula was checked against a breadth-first search over the full
state (the contents of every box and the position of the hand) on 150
tiny mosaics; the hand-made tests come from that search and the large
ones were checked against the formula computed separately.

## Language notes

- All languages run the same union-find with path halving.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1124_dsu.cpp](1124_dsu.cpp) | G++ 13.2 x64 | dsu | O(M·N) | AC | 0.015 s | 208 KB |
| [1124_dsu.go](1124_dsu.go) | Go 1.14 x64 | dsu | O(M·N) | AC | 0.046 s | 1520 KB |
| [1124_dsu.java](1124_dsu.java) | Java 1.8 | dsu | O(M·N) | AC | 0.125 s | 480 KB |
| [1124_dsu.py](1124_dsu.py) | Python 3.12 x64 | dsu | O(M·N) | AC | 0.078 s | 1860 KB |
| [1124_dsu.rs](1124_dsu.rs) | Rust 1.75 x64 | dsu | O(M·N) | AC | 0.015 s | 652 KB |
