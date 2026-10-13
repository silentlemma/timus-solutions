# 1478. Spy Satellites

[Timus 1478](https://acm.timus.ru/problem.aspx?space=1&num=1478) · difficulty 3896 · dsu

Original problem by Dmitry Ivankov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N objects lie in the plane at integer points (coordinates up to 10⁴ in
absolute value). They are split into bases so that inside every base
any two objects are strictly closer than any object of that base is to
any object of another base. For each test print a string of N digits
whose k-th digit is 1 if a split into exactly k bases exists. The
tests end with 0; the sum of N is at most 5000, of N² at most 400 000
and of N³ at most 2.5·10⁸.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Tests: N, then N lines x y; tests are separated by empty lines; 0 ends
the input.

## Output

A string of N zeros and ones per test.

## Examples

### Example 1

Input:

```
4
-1 -1
1 1
1 -1
-1 1

4
1 0
2 4
1 1
0 1

0
```

Output:

```
1001
1101
```

## Solution

Call a set C good if its diameter is less than its distance to the
rest; a split is a partition into good sets. Two good sets never cross:
if x lies in both, a only in A and b only in B, then
d(x, b) > diam A ≥ d(x, a) and d(x, a) > diam B ≥ d(x, b). Moreover, if
C is good and t is its distance to the rest, C is a connected component
of the graph joining the objects closer than t; and conversely such a
component is good exactly when its diameter is below t. So the good
sets are nodes of the single-linkage tree: run Kruskal on all pairs by
length, adding all pairs of equal length together, and each component
that appears after a group is a node whose children are the components
it swallowed. A node is good when its diameter, kept up to date with
the cross distances at every merge, is less than the length of the
group that later swallows it; the last node is always good.

Any good set inside a node lies inside one of its children, so the
possible counts of a node are {1} if it is good, together with every
sum of one possible count from each child. These sets are kept as bit
masks and combined child by child. `O(N² log N)` for the sort; the
merges and the sums cost `O(N²)` and about N³/64 bit operations.

Pitfalls:

- pairs of equal length must join in one group: halfway through a tie a
  component is not a component of any graph above, so a 25 × 25 grid
  allows only 1 or 625 bases (gen4, gen2);
- the inequality is strict: three objects with equal gaps split only
  into 1 or 3 bases (test 02);
- a node that is not good still splits through its children: the five
  objects (0, 0), (2, 0), (4, 0), (0, 1), (4, 1) allow every count but 2
  (test 02).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1478_dsu.cpp](1478_dsu.cpp) | G++ 13.2 x64 | dsu | O(N^2 log N) | AC | 0.031 s | 2600 KB |
| [1478_dsu.go](1478_dsu.go) | Go 1.14 x64 | dsu | O(N^2 log N) | AC | 0.093 s | 9804 KB |
| [1478_dsu.java](1478_dsu.java) | Java 1.8 | dsu | O(N^2 log N) | AC | 0.156 s | 7008 KB |
| [1478_dsu.py](1478_dsu.py) | Python 3.12 x64 | dsu | O(N^2 log N) | AC | 0.640 s | 25816 KB |
| [1478_dsu.rs](1478_dsu.rs) | Rust 1.75 x64 | dsu | O(N^2 log N) | AC | 0.031 s | 2012 KB |
