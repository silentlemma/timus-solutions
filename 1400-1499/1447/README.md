# 1447. Portkey Network

[Timus 1447](https://acm.timus.ru/problem.aspx?space=1&num=1447) · difficulty 971 · graphs

Original problem by Den Raskovalov (author) and Stanislav Vasiliev (text), from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A firm has N branches (1 ≤ N ≤ 1000) and M possible portkey links
(1 ≤ M ≤ 500000), each joining two different branches and having a
length and a cost, integers from 1 to 10⁶; no pair of branches has two
links. The network must connect all branches with no redundant link,
that is, it must be a spanning tree, and some such tree exists. The firm
pays by the metre, so Lucius Malfoy wants the tree with the smallest
ratio of total cost to total length. Print that ratio with precision
10⁻⁸.

Time limit: 4 seconds. Memory limit: 64 MB.

## Input

N, M, then M lines with two branches, the length and the cost of a link.

## Output

The smallest average cost of a metre.

## Examples

### Example 1

Input:

```
3
3
1 2 50 60
1 3 100 100
2 3 100 100
```

Output:

```
1
```

### Example 2

Input:

```
3
3
1 2 1000 3000
1 3 1 5
2 3 1000 1997
```

Output:

```
2
```

## Solution

A tree T has ratio at most λ exactly when the sum of c − λ d over its
links is at most 0, so the question "is there a tree with ratio below
λ" is a minimum spanning tree with the weights c − λ d. Dinkelbach's
method turns this into a fast iteration: take any tree, set λ to its
ratio, find the minimum tree for the weights c − λ d, and if its weight
is negative, its own ratio is smaller, so it becomes the new λ; once the
minimum weight is 0, no tree beats λ. The ratio drops quickly and only a
handful of rounds are needed in practice.

Keeping λ as a fraction p / q makes everything exact: the weights
c q − d p are integers that fit in 64 bits, so the stopping test does not
depend on rounding. With up to 500000 links on 1000 branches the graph can be
nearly complete, so each tree is built by Prim's algorithm on an N × N
matrix in `O(N²)`, and the whole run takes `O(N²)` per round.

Pitfalls:

- the cheapest tree is not the one with the best ratio (example 1);
- a network that is already a tree leaves no choice (tests 05, gen4);
- ratios can be tiny, so print enough digits after the decimal point
  (tests 04, 07).

## Language notes

- Python reads the links line by line into rows of `array`: half a
  million links split into one list of words take over 64 MB. On the
  judge it takes 2.25 s and 9 MB, within the 4-second limit.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1447_graphs.cpp](1447_graphs.cpp) | G++ 13.2 x64 | graphs | O(N^2) per round | AC | 0.078 s | 7656 KB |
| [1447_graphs.go](1447_graphs.go) | Go 1.14 x64 | graphs | O(N^2) per round | AC | 0.140 s | 17924 KB |
| [1447_graphs.java](1447_graphs.java) | Java 1.8 | graphs | O(N^2) per round | AC | 0.281 s | 9224 KB |
| [1447_graphs.py](1447_graphs.py) | Python 3.12 x64 | graphs | O(N^2) per round | AC | 2.250 s | 9136 KB |
| [1447_graphs.rs](1447_graphs.rs) | Rust 1.75 x64 | graphs | O(N^2) per round | AC | 0.093 s | 33148 KB |
