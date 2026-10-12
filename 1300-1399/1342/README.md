# 1342. Enterprise

[Timus 1342](https://acm.timus.ru/problem.aspx?space=1&num=1342) · difficulty 729 · dp

Original problem by Magaz Asanov and Pavel Egorov, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A firm has N ≤ 1000 factories and needs M ≤ 1000 brooms. Factory i can
make from 0 to K_i ≤ 100 brooms a day; its first broom costs P_i, its
K_i-th costs Q_i, and the price of the j-th broom changes linearly in
between. Find the least total cost of M brooms, with two digits after
the point. If the factories cannot make M brooms together, first print
the largest amount V they can make and then the least cost of V brooms.

Time limit: 2.5 seconds. Memory limit: 64 MB.

## Input

N and M, then N lines with K_i, P_i and Q_i.

## Output

`Maximum possible amount: V` if M cannot be reached, then
`Minimum possible cost: C`.

## Examples

### Example 1

Input:

```
2 10
6 20 15
100 100 100
```

Output:

```
Minimum possible cost: 505.00
```

### Example 2

Input:

```
2 10
5 30 14
1 20 20
```

Output:

```
Maximum possible amount: 6
Minimum possible cost: 130.00
```

## Solution

The j-th broom of a factory costs P + (j − 1) · (Q − P) / (K − 1), so x
brooms from it cost x · P + (Q − P) / (K − 1) · x (x − 1) / 2. The target
is T = min(M, ΣK). When prices fall along the way, a factory pays off
only when it makes many brooms, and when they rise, only its first ones
are cheap. With both kinds mixed, no greedy order works, so it is a
knapsack: best[j] is the least cost of exactly j brooms from the
factories seen so far. A new factory updates it by trying every amount x
from 0 to K for every j up to T. That is at most N · T · K = 10⁸ simple
steps. `O(N · M · K)`.

Pitfalls:

- a factory with falling prices may beat a cheaper-looking one only
  when used fully (test 04);
- when the total capacity is short, both lines are printed and the cost
  is for V brooms (tests 02 and 06);
- a factory with K = 1 has a single broom priced P.

The costs were compared with trying every split of the order among up
to 3 factories on 400 random cases.

## Language notes

- CPython needs about 4 seconds for the largest case, over the
  2.5-second limit, so the Python solution is submitted under PyPy 3.10,
  where it takes about 0.1 seconds.
- Java compares doubles directly in the inner loop: `Math.min` on doubles
  also handles NaN and −0 and made the solution several times slower.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1342_dp.cpp](1342_dp.cpp) | G++ 13.2 x64 | dp | O(N·M·K) | AC | 0.078 s | 244 KB |
| [1342_dp.go](1342_dp.go) | Go 1.14 x64 | dp | O(N·M·K) | AC | 0.171 s | 2088 KB |
| [1342_dp.java](1342_dp.java) | Java 1.8 | dp | O(N·M·K) | AC | 0.250 s | 5520 KB |
| [1342_dp.py](1342_dp.py) | PyPy 3.10 x64 | dp | O(N·M·K) | AC | 0.375 s | 6840 KB |
| [1342_dp.rs](1342_dp.rs) | Rust 1.75 x64 | dp | O(N·M·K) | AC | 0.218 s | 308 KB |
