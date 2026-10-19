# 2108. Closing a set of figures under wish rules

[Timus 2108](https://acm.timus.ru/problem.aspx?space=1&num=2108) · difficulty 453 · bitmask

Original problem by Kirill Borozdin, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n collectible figures. Each of m wishes says: once all figures
of a set A are owned, all figures of a set B are wanted too. Starting
from the figures already owned, find the smallest set that satisfies
every wish, that is, the set reached by granting wishes until nothing new
is wanted. The limits are 0.9 seconds and 64 MB.

## Input

n and m, 1 ≤ n ≤ 1000, 0 ≤ m ≤ 4000, then m lines with the sets A and B
as strings of n zeros and ones, and the owned set in the same format.

## Output

The final set in the same format.

## Examples

### Example 1

Input:

```
6 4
111000 101000
110000 111000
010000 100000
000010 000001
010100
```

Output:

```
111100
```

## Solution

A set that satisfies every wish and contains the owned figures has to
contain every figure that some chain of wishes leads to, and the set of
exactly those figures satisfies every wish. So repeat passes over the
wishes: a wish whose A is inside the owned set adds B. A pass that adds
nothing ends the process, and every other pass adds at least one figure,
so there are at most n + 1 passes.

The sets are bitsets of 64-bit words: "A inside the owned set" is
A AND NOT owned = 0, and adding B is an OR, both n / 64 word operations.
The total work is O(n · m · n / 64), about 6 · 10⁷ word operations.

In the example the owned figures 2 and 4 enable the third wish, which
adds 1; then the second wish adds 3, and the result is 111100.

## Language notes

The Python solution transposes the problem, because the passes are too
slow there when a chain of wishes is listed in reverse order. For every
figure it builds the set of wishes that need it as one big integer (a
column of the matrix of A strings). A segment tree over figures keeps the
union of these sets over the figures still missing, which is exactly the
set of wishes not yet enabled. Every round fires all newly enabled wishes
and clears the tree leaves of the newly owned figures, so the work is
O(n log n) big-integer operations plus one step per wish.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2108_bitmask.cpp](2108_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(n^2 m / 64) | AC | 0.046 s | 1808 KB |
| [2108_bitmask.go](2108_bitmask.go) | Go 1.14 x64 | bitmask | O(n^2 m / 64) | AC | 0.062 s | 18712 KB |
| [2108_bitmask.java](2108_bitmask.java) | Java 1.8 | bitmask | O(n^2 m / 64) | AC | 0.234 s | 1792 KB |
| [2108_bitmask.py](2108_bitmask.py) | Python 3.12 x64 | bitmask | O(n^2 m / 64) | AC | 0.171 s | 17336 KB |
| [2108_bitmask.rs](2108_bitmask.rs) | Rust 1.75 x64 | bitmask | O(n^2 m / 64) | AC | 0.062 s | 9312 KB |
