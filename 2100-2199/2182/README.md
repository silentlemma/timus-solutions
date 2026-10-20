# 2182. Bottles that multiply by the number of ones in their box number

[Timus 2182](https://acm.timus.ru/problem.aspx?space=1&num=2182) · difficulty 663 · dp, combinatorics

Original problem by Artyom Kutuzov, from the Ural Team Programming Contest 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Bottles numbered 1 … 2ⁿ − 1 go into the boxes with the same numbers.
Putting a bottle into box k creates a new bottle numbered popcount(k),
the number of ones in the binary form of k, unless that equals k; the
new bottle goes into its box and does the same. For q boxes print how
many bottles end up in them. The limits are 1 second and 256 MB.

## Input

n, 1 ≤ n ≤ 60, q, 1 ≤ q ≤ 10⁵, then the box numbers, 1 ≤ aᵢ ≤ 2ⁿ − 1.

## Output

The number of bottles in each asked box.

## Examples

### Example 1

Input:

```
5
2
8 4
```

Output:

```
1 6
```

## Solution

Every bottle that lands in box j sends one bottle on to box popcount(j)
when that differs from j. So with c(k) the final count of box k,

c(k) = 1 + Σ c(j) over the boxes j ≠ k with popcount(j) = k.

No box above 60 receives anything, since a number below 2⁶⁰ has at most
60 ones, so those boxes hold one bottle. For k ≤ 60 the boxes j with
popcount(j) = k are C(n, k) numbers; all but the few that are at most
60 hold one bottle each, so c(k) is C(n, k) plus 1 plus the extra
bottles of the small boxes k < j ≤ 60 with popcount(j) = k, minus one for
j = k when k = 1. Since popcount(j) < j for j > 1, filling c from 60 down
to 1 uses only finished values. The largest count, about 2⁶⁰, still fits
in 64 bits, and each query is a lookup.

In the example box 4 gets its own bottle and one from each of the
C(5, 4) = 5 boxes 15, 23, 27, 29 and 30.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2182_dp_combinatorics.cpp](2182_dp_combinatorics.cpp) | G++ 13.2 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.140 s | 692 KB |
| [2182_dp_combinatorics.go](2182_dp_combinatorics.go) | Go 1.14 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.031 s | 4308 KB |
| [2182_dp_combinatorics.java](2182_dp_combinatorics.java) | Java 1.8 | dp, combinatorics | O(60^2 + q) | AC | 0.187 s | 24904 KB |
| [2182_dp_combinatorics.py](2182_dp_combinatorics.py) | Python 3.12 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.109 s | 13712 KB |
| [2182_dp_combinatorics.rs](2182_dp_combinatorics.rs) | Rust 1.75 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.046 s | 6904 KB |
