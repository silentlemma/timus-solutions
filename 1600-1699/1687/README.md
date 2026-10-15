# 1687. Numismatics for Fun

[Timus 1687](https://acm.timus.ru/problem.aspx?space=1&num=1687) · difficulty 1275 · greedy

Original problem prepared by Vladimir Yakovlev, with special thanks to Vladislav Isenbaev, for the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Boxes of coins cost 100 yen each after the discount, and a set of boxes
is worth 100 yen for every different wanted coin it contains. Find the
largest set of boxes, each holding at least one wanted coin, whose
price does not exceed its worth.

## Input

n (1 ≤ n ≤ 100) coin kinds and k (1 ≤ k ≤ 50) boxes, then each box as
its size and its distinct coins, then the m wanted coins.

## Output

The number of boxes and their numbers. Any largest set is accepted.

## Examples

### Example 1

Input:

```
10 4
5 2 7 6 1 3
6 6 7 10 2 9 4
5 1 8 3 9 2
5 4 3 7 6 1
4 8 5 4 9
```

Output:

```
3
2 3 4
```

## Solution

Call a box useful if it holds a wanted coin, and a wanted coin
coverable if some box holds it. A set S of useful boxes must have
|S| ≤ (wanted coins in S), so |S| is at most the number of coverable
coins, and of course at most the number of useful boxes.

The smaller of the two is reachable. For each coverable coin not yet
covered take any box holding it: this uses at most one box per coin
and covers every coverable coin. Then add further useful boxes while
the count stays within the number of coverable coins. The set is worth
all coverable coins, and it holds min(useful, coverable) boxes.
`O(k · n²)` with linear box searches.

Pitfalls:

- the answer can be larger than a maximum matching between boxes and
  coins: boxes {1, 2, 3}, {1}, {1}, {1} with wanted coins 1, 2, 3 allow
  three boxes, though only two can be matched (test 03);
- boxes without wanted coins never count (test 04);
- when no box holds a wanted coin the answer is 0 and an empty list.

The checker accepts any set of the expected size that pays off. The
answers match an exhaustive search over all sets of boxes on small
cases, and an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1687_greedy.cpp](1687_greedy.cpp) | G++ 13.2 x64 | greedy | O(k · n²) | AC | 0.015 s | 236 KB |
| [1687_greedy.go](1687_greedy.go) | Go 1.14 x64 | greedy | O(k · n²) | AC | 0.031 s | 1176 KB |
| [1687_greedy.java](1687_greedy.java) | Java 1.8 | greedy | O(k · n²) | AC | 0.109 s | 612 KB |
| [1687_greedy.py](1687_greedy.py) | Python 3.12 x64 | greedy | O(k · n²) | AC | 0.093 s | 964 KB |
| [1687_greedy.rs](1687_greedy.rs) | Rust 1.75 x64 | greedy | O(k · n²) | AC | 0.062 s | 296 KB |
