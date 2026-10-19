# 1844. Warlord of the Army of Mages

[Timus 1844](https://acm.timus.ru/problem.aspx?space=1&num=1844) · difficulty 1557 · dp

Original problem by Evgeny Kurpilyansky, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two mentors, Sandro and Zagamius, interview mages in separate offices.
Each follows a fixed plan of steps "call mage a" and "release mage a".
A mage can be in only one office, so a call waits while the mage is
with the other mentor; when both can act, either one may go first. Tell
whether the mentors can end up waiting for each other forever.

## Input

t (1 ≤ t ≤ 10) tests. Each starts with n, m and k (1 ≤ n, m, k ≤ 1000):
the lengths of the plans of Sandro and Zagamius and the number of
mages. Then the n steps of Sandro and the m steps of Zagamius, each
"+ a" or "- a" (1 ≤ a ≤ k). Nobody calls a mage already in the same
office or releases one who is not there, and both offices end empty.

## Output

For every test ":-)" if both plans surely finish, and ":-(" if the
mentors can get stuck.

## Examples

### Example 1

Input:

```
2
4 4 2
+ 1
+ 2
- 2
- 1
+ 1
+ 2
- 2
- 1
4 4 2
+ 1
+ 2
- 1
- 2
+ 2
+ 1
- 2
- 1
```

Output:

```
:-)
:-(
```

## Solution

A moment is a cell (i, j): Sandro has done i steps and Zagamius j. Call
a cell taken when both offices hold one mage at once. A step is blocked
exactly when it would lead into a taken cell: a call is the only step
that can make two offices share a mage, and it does so precisely when
the other mentor holds that mage. So the moments that can happen are the
cells reachable from (0, 0) by steps down and right through free cells,
and the mentors can get stuck when such a cell, other than (n, m), has
both neighbours taken or missing. The last row and column never get
stuck, since there the finished mentor holds nobody.

Which cells are taken. For a fixed row the set of Sandro's mages is
fixed; walking along the row, count the mages in both offices, adding
or removing one when Zagamius calls or releases a mage Sandro holds.
With the taken cells known, one pass over the grid marks the reachable
ones and checks each for a dead end. `O(t·n·m)`.

The Python solution does the same with rows as bit masks over j. Every
mage gets the mask of the columns where Zagamius holds it; the taken
cells of a row are the union of those masks over Sandro's mages, put on
the stretches of rows where Sandro holds each mage with a segment tree
over the rows. Inside a row, Zagamius walks right from every cell
entered from above until the next taken cell; subtracting those seeds
from the mask of taken cells flips each free run from its first seed
onwards, which fills the row in a few big-integer operations.

In the second test of the example Sandro calls mage 1 while Zagamius
calls mage 2. Now Sandro waits for mage 2 and Zagamius for mage 1.

Pitfalls:

- only a call can wait, so a dead end needs both mentors to be about
  to call a mage the other one holds;
- the same mage may be called many times, so the holding stretches,
  not the mages, are what matter.

The answers agree with an independent accepted implementation on one
hundred and fifty random files of ten tests each.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1844_dp.cpp](1844_dp.cpp) | G++ 13.2 x64 | dp | O(t n m) | AC | 0.078 s | 2048 KB |
| [1844_dp.go](1844_dp.go) | Go 1.14 x64 | dp | O(t n m) | AC | 0.093 s | 7304 KB |
| [1844_dp.java](1844_dp.java) | Java 1.8 | dp | O(t n m) | AC | 0.171 s | 6816 KB |
| [1844_dp.py](1844_dp.py) | Python 3.12 x64 | dp | O(t n m) | AC | 0.140 s | 3536 KB |
| [1844_dp.rs](1844_dp.rs) | Rust 1.75 x64 | dp | O(t n m) | AC | 0.078 s | 2644 KB |
