# 1403. Courier

[Timus 1403](https://acm.timus.ru/problem.aspx?space=1&num=1403) · difficulty 350 · greedy

Original problem by Nikita Rybak, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 1000 orders each take one day to deliver and have a deadline and a
reward; a late order earns nothing and must not be delivered. Choose the
orders and their order of delivery for the largest total reward.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the deadline and the reward of every order.

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

- deadlines can exceed 100 000 (the forum reports it for test 9), so
  nothing is sized by them (test 06);
- with all orders due on the first day only the largest reward is
  delivered (test 07).

The answers were compared with a search over all subsets on 400 random
small cases. The tests are judged by a checker that finds the best total
another way, placing the most rewarding orders on the latest free days.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1403_greedy.cpp](1403_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 228 KB |
| [1403_greedy.go](1403_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1348 KB |
| [1403_greedy.java](1403_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 2860 KB |
| [1403_greedy.py](1403_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 812 KB |
| [1403_greedy.rs](1403_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.046 s | 268 KB |
