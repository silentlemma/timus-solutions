# 1863. Peaceful Atom

[Timus 1863](https://acm.timus.ru/problem.aspx?space=1&num=1863) · difficulty 1084 · meet_in_middle

Original problem by Alexander Klepinin (prepared by Daniil Ayzenshteyn), from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The control rods of a reactor can stand at any depth from 0 to n mm and
started at depth s. A log lists k moves of the rods, but only their
lengths, not whether each went up or down; the rods never left the range
[0, n]. Find the smallest and the largest depth the rods can be at now.

## Input

n, s and k (0 ≤ s ≤ n ≤ 10⁹, n > 0, 1 ≤ k ≤ 40), then the k move
lengths. Some choice of directions keeps the rods within range.

## Output

The smallest and the largest possible final depth.

## Examples

### Example 1

Input:

```
10 3 3
4 5 1
```

Output:

```
1 3
```

## Solution

Trying all 2⁴⁰ directions is too slow, so split the log in the middle.
For the first half keep the set of depths it can reach without leaving
[0, n], growing it move by move and merging equal depths; it has at most
2²⁰ members.

For the second half go through every choice of directions by depth
first search and track three numbers: the total shift t and the lowest
and the highest running sums, low and high. Started at depth x the
second half stays in range exactly when x + low ≥ 0 and x + high ≤ n,
so x must lie in [−low, n − high], and it ends at x + t. Prune a choice
as soon as high − low exceeds n, since no x fits any more. At every
complete choice, binary search the sorted first-half depths for the
smallest and the largest x in that interval; they give the shallowest
and the deepest final depth for this choice. `O(2^(k/2)·k)`.

In the example the first move leads from 3 to 7 (−4 would go below 0),
and then 7 ± 5 gives 2 or 12, where only 2 stays in range; the last move
of 1 ends at 1 or 3.

Pitfalls:

- the range must hold after every move, not only at the end, which is
  why the second half needs its running extremes and not just its total;
- storing all 2²⁰ second-half choices with three 64-bit numbers each takes
  24 MiB; depth-first search avoids storing them all;
- the Python solution runs on PyPy, keeps first-half depths in sorted
  32-bit arrays instead of hash sets and searches the second half using
  feasible-depth intervals, arithmetic bounds and symmetry: 11 MB on the
  judge, where an earlier
  version with sets took 70 MB on test 10.

The answers agree with following the set of reachable depths through
the whole log on three hundred short logs and with an independent
accepted implementation on logs of 40 moves.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1863_meet_in_middle.cpp](1863_meet_in_middle.cpp) | G++ 13.2 x64 | meet_in_middle | O(2^(k/2) k) | AC | 0.203 s | 21256 KB |
| [1863_meet_in_middle.go](1863_meet_in_middle.go) | Go 1.14 x64 | meet_in_middle | O(2^(k/2) k) | AC | 0.593 s | 43488 KB |
| [1863_meet_in_middle.java](1863_meet_in_middle.java) | Java 1.8 | meet_in_middle | O(2^(k/2) k) | AC | 0.468 s | 20896 KB |
| [1863_meet_in_middle.py](1863_meet_in_middle.py) | PyPy 3.10 x64 | meet_in_middle | O(2^(k/2) k) | AC | 0.234 s | 11232 KB |
| [1863_meet_in_middle.rs](1863_meet_in_middle.rs) | Rust 1.75 x64 | meet_in_middle | O(2^(k/2) k) | AC | 0.234 s | 13384 KB |
