# 1717. Eligibility Rules

[Timus 1717](https://acm.timus.ru/problem.aspx?space=1&num=1717) · difficulty 2166 · segment_tree

Original problem by Sergey Pupyrev, prepared by Alex Samsonov, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n teams has an average age a, a number of contests f and a
satisfaction s. Choose a range of ages and a range of contests so that
at least two teams fall into both, and the total satisfaction of those
teams is as large as possible.

## Input

n (2 ≤ n ≤ 1500), then n lines a f s with 4·10⁸ ≤ a ≤ 10⁹,
0 ≤ f ≤ 10⁹ and |s| ≤ 10⁹.

## Output

The age range on the first line and the contests range on the second,
integers from 0 to 10⁹. Any optimal pair of ranges is accepted.

## Examples

### Example 1

Input:

```
4
500000000 1 1
510000000 3 -10
600000000 3 2
700000000 4 3
```

Output:

```
550000000 750000000
2 5
```

## Solution

This is a rectangle of largest weight over points in the plane, with at
least two points inside. Only the distinct values of a and f matter.
Fix the lowest age in turn and raise the highest age step by step,
adding the teams of each new age to a segment tree over the distinct
values of f.

A node keeps its total, its number of teams capped at 2, and the best
prefix and best suffix for each exact count 0, 1 and "2 or more", plus
its best range with two or more teams. Prefixes and suffixes here are
never empty. Two children combine as usual for the largest subarray,
with the counts added and capped. A range crossing the middle joins a
suffix of the left child and a prefix of the right one whose counts
add up to at least 2. After each new age the root gives the best range
of contests for these ages. That is `O(n² log n)` in total.

The tree finds only the best value and its pair of ages. The contests
range is then found again for that pair with prefix sums, in one pass.
For each right end, the best left end has the least prefix sum among
those that leave at least two teams inside.

Pitfalls:

- a single team can never be the answer, even when all others make it
  worse (test 02);
- teams with the same age must all be added before the root is read,
  and teams with the same f share a leaf;
- the totals reach 1.5 · 10¹², so they need 64 bits;
- the Python solution runs on PyPy with the tree in four flat arrays:
  instead of the three exact counts it keeps only the best prefix and
  suffix that hold at least one team, so a range crossing a node's
  middle holds two teams by itself, and only leaves tell one team from
  two. CPython needs about 5 s on 1500 teams. On PyPy it takes 0.75 s on
  the judge; an earlier version with nine count arrays ran out of time
  on the judge's test 5.

A checker accepts any optimal pair of ranges. It checks the bounds,
that at least two teams are admitted, and the total. The answers match
an independent accepted implementation on 300 small random cases and on
large ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1717_segment_tree.cpp](1717_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(n² log n) | AC | 0.578 s | 308 KB |
| [1717_segment_tree.go](1717_segment_tree.go) | Go 1.14 x64 | segment_tree | O(n² log n) | AC | 0.828 s | 1656 KB |
| [1717_segment_tree.java](1717_segment_tree.java) | Java 1.8 | segment_tree | O(n² log n) | AC | 1.718 s | 5904 KB |
| [1717_segment_tree.py](1717_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(n² log n) | AC | 0.750 s | 9680 KB |
| [1717_segment_tree.rs](1717_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(n² log n) | AC | 0.781 s | 952 KB |
