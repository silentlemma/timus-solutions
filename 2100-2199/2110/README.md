# 2110. Largest OR after deleting exactly k numbers

[Timus 2110](https://acm.timus.ru/problem.aspx?space=1&num=2110) · difficulty 1032 · bitmask, dp, backtracking

Original problem by Alexey Danilyuk, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Delete exactly k of n non-negative integers so that the bitwise OR of the
remaining ones is as large as possible. Every test has k ≤ 7 or all
numbers at most 10⁵. The limits are 2 seconds and 64 MB.

## Input

n and k, 0 ≤ k ≤ 100, k + 1 ≤ n ≤ 10⁵, then the n numbers, each at most
10⁹.

## Output

The largest OR.

## Examples

### Example 1

Input:

```
4 1
32 16 8 7
```

Output:

```
56
```

### Example 2

Input:

```
4 1
98765432 98765432 98765432 1
```

Output:

```
98765433
```

## Solution

Let F be the OR of all numbers and r = n − k the number kept. Every set
bit of F has a witness, a number containing it, so at most popcount(F)
numbers already give F, and the remaining places can be filled with
anything. Hence if r ≥ popcount(F) the answer is F.

Otherwise r < popcount(F) ≤ 30, which leaves two small cases.

- k ≤ 7: then n = r + k ≤ 36. A depth-first search sorted by decreasing
  value chooses which numbers to keep. It stops a branch when the current
  OR together with all later numbers cannot beat the best result, and
  takes that upper bound at once when the remaining places are enough to
  pick one witness for every still missing bit.
- Numbers at most 10⁵: then F < 2¹⁷, r ≤ 16 and n ≤ 116. A knapsack over
  OR masks stores, for every mask, the fewest distinct numbers that
  produce it; a mask reached with at most r numbers is achievable, since
  duplicates and other numbers fill the other places without lowering the
  OR. The masks are processed in decreasing order so each number is used
  once, and the loop stops as soon as F is reached.

In the second example all copies of 98765432 give the same bits, so
deleting one copy keeps the 1 and the answer is 98765433.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2110_bitmask_dp_backtracking.cpp](2110_bitmask_dp_backtracking.cpp) | G++ 13.2 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.031 s | 936 KB |
| [2110_bitmask_dp_backtracking.go](2110_bitmask_dp_backtracking.go) | Go 1.14 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.031 s | 2168 KB |
| [2110_bitmask_dp_backtracking.java](2110_bitmask_dp_backtracking.java) | Java 1.8 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.125 s | 1036 KB |
| [2110_bitmask_dp_backtracking.py](2110_bitmask_dp_backtracking.py) | Python 3.12 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.781 s | 11344 KB |
| [2110_bitmask_dp_backtracking.rs](2110_bitmask_dp_backtracking.rs) | Rust 1.75 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.031 s | 2148 KB |
