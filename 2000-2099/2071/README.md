# 2071. Order the cocktails for the fewest pourings

[Timus 2071](https://acm.timus.ru/problem.aspx?space=1&num=2071) · difficulty 640 · bitmask, dp

Original problem by Mikhail Rubinchik, prepared by Nickolai Permyakov and Alexey Danilyuk, from the Ural Regional School Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n guests each order a cocktail: a non-empty set of the juices A, B and P.
The glasses are put in a row in some order, and one pouring fills a
segment of consecutive glasses with one juice (apple first, then banana,
then pineapple, so the order of pourings is never a problem). Each glass
must get exactly the juices of its cocktail. Arrange the glasses to need
the fewest pourings. The limits are 1 second and 64 MB.

## Input

n, 1 ≤ n ≤ 10⁵, then n lines, each one of A, B, P, AB, AP, BP, ABP.

## Output

The smallest number of pourings, then the numbers of the glasses in the
row order. Any optimal arrangement is accepted.

## Checking

A checker compares the number of pourings and recounts the pourings that
the printed arrangement needs.

## Examples

### Example 1

Input:

```
3
A
B
ABP
```

Output:

```
3
1 3 2
```

## Solution

For a fixed row, each juice needs one pouring per maximal run of glasses
that contain it, so the cost is the number of places where a juice
appears in a glass but not in the glass before it (the first glass
counts all its juices). Moving a glass next to an equal one never adds
a run, so all glasses of one cocktail can stand together, and only the
order of at most seven distinct cocktails matters.

These are ordered by a DP over subsets: best[S][last] is the fewest
pourings for a row made of the cocktails in S that ends with last.
Appending cocktail k costs the number of juices of k missing in last,
that is popcount(k & ~last). The answer is the minimum over last for the
full set, and the stored predecessors give the order. With seven
cocktails this is 2⁷ · 7 · 7 steps, so the work is O(n) for reading and
printing.

In the example the order B, ABP, A needs three pourings: one run for
each juice.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2071_bitmask_dp.cpp](2071_bitmask_dp.cpp) | G++ 13.2 x64 | bitmask, dp | O(n) | AC | 0.078 s | 440 KB |
| [2071_bitmask_dp.go](2071_bitmask_dp.go) | Go 1.14 x64 | bitmask, dp | O(n) | AC | 0.046 s | 7572 KB |
| [2071_bitmask_dp.java](2071_bitmask_dp.java) | Java 1.8 | bitmask, dp | O(n) | AC | 0.125 s | 8848 KB |
| [2071_bitmask_dp.py](2071_bitmask_dp.py) | Python 3.12 x64 | bitmask, dp | O(n) | AC | 0.140 s | 17408 KB |
| [2071_bitmask_dp.rs](2071_bitmask_dp.rs) | Rust 1.75 x64 | bitmask, dp | O(n) | AC | 0.062 s | 7116 KB |
