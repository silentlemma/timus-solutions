# 1371. Cargo Agency

[Timus 1371](https://acm.timus.ru/problem.aspx?space=1&num=1371) · difficulty 520 · dp

Original problem: idea by Den Raskovalov, prepared by Alexander Klepinin, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 50 000 branches are joined by N − 1 roads into a tree, and every
road has a delivery time from 0 to 1000. Print the average delivery
time over all ordered pairs of different branches, the sum of all
distances divided by N(N − 1), to 4 decimal places.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N − 1 lines with the ends of a road and its time.

## Output

The average time.

## Examples

### Example 1

Input:

```
4
1 2 1
2 3 1
2 4 1
```

Output:

```
1.5
```

## Solution

Count each road once per pair that uses it. Removing a road splits the
tree into parts of s and N − s branches, and exactly the s · (N − s)
pairs with one end in each part go along it. So the sum over ordered
pairs is 2 · Σ c · s · (N − s).

Root the tree at branch 1 and list the branches parents first, by a
breadth-first walk. Read backwards, that list gives the subtree sizes:
each branch adds its size to its parent. `O(N)`.

Pitfalls:

- the sum reaches 4·10¹⁶ on a path of the dearest roads, so it needs
  64-bit integers (generated test 2);
- a path of 50 000 branches is too deep for recursion, hence the
  breadth-first order;
- free roads, with time 0, are allowed (test 03).

The answers were compared with summing all distances by a search from
every branch, on 300 random trees of up to 30 branches.

## Language notes

- Java keeps the tree in flat arrays; all languages print with a dot as
  the decimal point.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1371_dp.cpp](1371_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.078 s | 3976 KB |
| [1371_dp.go](1371_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.109 s | 10604 KB |
| [1371_dp.java](1371_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 3308 KB |
| [1371_dp.py](1371_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.218 s | 29648 KB |
| [1371_dp.rs](1371_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 9444 KB |
