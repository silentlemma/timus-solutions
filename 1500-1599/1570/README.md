# 1570. Eating High

[Timus 1570](https://acm.timus.ru/problem.aspx?space=1&num=1570) · difficulty 895 · dp

Original problem by Vladimir Yakovlev, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A menu lists N ≤ 100 dishes, each with a price of 1 … 10000 roubles and
a satiety from 0.1 to 10 (with at most three digits after the point),
the number of people it feeds. Order any number of plates of any dishes
so that the satieties add up to at least M ≤ 20 at the least cost, and
among such orders take one with the most different dishes. Print the
cost and the dishes with their numbers of plates.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then each dish as a name, a price and a satiety.

## Output

The cost, then one dish and its number of plates per line. Any best
order is accepted.

## Examples

### Example 1

Input:

```
4 6
pizza 320 2.4
turkey 1050 3.5
lasagna 150 0.9
pasta 75 0.45
```

Output:

```
865
pizza 2
lasagna 1
pasta 1
```

## Solution

Satiety is read exactly in thousandths, so the goal is T = 1000·M, and
any total of T or more counts as T. An unbounded knapsack over these
totals keeps for each total the least cost and, on a tie, the most
different dishes, packed into one number cost·128 − dishes, where
smaller is better.

The number of different dishes is not additive over plates, so the
dishes are added one at a time. For each dish, the orders that take it
start with a first plate on top of an order without it, which counts one
more dish, and then grow by further plates of it, which count none; the
best of these and of the orders without the dish is kept. Each step
also notes where it came from, so the order can be walked back dish by
dish from the total T. This takes O(N·T) time, about 2·10⁶ states. The
results were checked against trying all numbers of plates on 300 random
small menus.

Pitfalls:

- a cheaper order may overshoot M, so totals above T must stay possible
  (test 07: two 0.501 plates);
- the tie on cost is broken by the number of different dishes, not by
  the number of plates (the example and tests 04, 05);
- satiety may be written without a point (test 04);
- Python runs under PyPy: the largest tests take about 0.8 s with
  CPython against a limit of 1 s, and about 0.1 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1570_dp.cpp](1570_dp.cpp) | G++ 13.2 x64 | dp | O(N M) | AC | 0.031 s | 12116 KB |
| [1570_dp.go](1570_dp.go) | Go 1.14 x64 | dp | O(N M) | AC | 0.031 s | 14396 KB |
| [1570_dp.java](1570_dp.java) | Java 1.8 | dp | O(N M) | AC | 0.140 s | 13196 KB |
| [1570_dp.py](1570_dp.py) | PyPy 3.10 x64 | dp | O(N M) | AC | 0.312 s | 18672 KB |
| [1570_dp.rs](1570_dp.rs) | Rust 1.75 x64 | dp | O(N M) | AC | 0.062 s | 12176 KB |
