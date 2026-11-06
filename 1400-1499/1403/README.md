# 1403. Courier

[Timus 1403](https://acm.timus.ru/problem.aspx?space=1&num=1403) · difficulty 349 · greedy

Original problem by Nikita Rybak, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 1000 orders each take one day to deliver and have a deadline and a
reward; a late order earns nothing and must not be delivered. Choose the
orders and their order of delivery for the largest total reward.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N (1 ≤ N ≤ 1000), then the integer deadline and reward of every order,
both in 1..100000.

## Output

The number of orders delivered, then their numbers in the order of
delivery. Any best plan is accepted.

## Examples

### Example 1

Input:

```
4
1 17
5 15
2 10
2 11
```

Output:

```
3
1 4 2
```

## Solution

A set of orders can be delivered in time exactly when, sorted by
deadline, the k-th of them is due on day k or later. So go through the
orders by deadline and keep the chosen ones in a min-heap by reward:
add each order, and when the heap holds more orders than its deadline
allows, drop the cheapest one. Every step keeps the best feasible set
of the orders seen so far, because only the smallest reward ever has to
make room. The kept orders, sorted by deadline, are the plan.
`O(N log N)`.

Pitfalls:

- deadlines can be much larger than N, up to 100000; do not index an
  N-element day array directly by the deadline (test 06);
- with all orders due on the first day only the largest reward is
  delivered (test 07).

The answers were compared with a search over all subsets on 1000 random
small cases. The tests are judged by a checker that finds the best total
another way, placing the most rewarding orders on the latest free days.

## Optimized solutions

Go visits orders by decreasing reward and places each on the latest free day at or before its deadline. If an optimal schedule used an earlier day for that order, any order displaced from the later day can take the earlier one. If it omitted the current order, the current order can replace the occupant without lowering the reward. A predecessor array with path compression finds the free day and redirects it to its predecessor once occupied.

The accepted base implementations [1403_greedy.cpp](1403_greedy.cpp), [1403_greedy.java](1403_greedy.java), [1403_greedy.py](1403_greedy.py), [1403_greedy.rs](1403_greedy.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1403_greedy.cpp](1403_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 228 KB | 11286033 |
| [1403_greedy.go](1403_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1348 KB | 11286034 |
| [1403_greedy.java](1403_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 2860 KB | 11286036 |
| [1403_greedy.py](1403_greedy.py) \* | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 812 KB | 11286035 |
| [1403_greedy.rs](1403_greedy.rs) \* | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.046 s | 268 KB | 11286037 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1403_dsu_greedy.go](1403_dsu_greedy.go) \* | Go 1.14 x64 | dsu, greedy | O(N log N) | AC | 0.031 s | 936 KB | 11310421 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
