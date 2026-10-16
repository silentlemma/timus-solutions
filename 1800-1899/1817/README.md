# 1817. Merry-go-round

[Timus 1817](https://acm.timus.ru/problem.aspx?space=1&num=1817) · difficulty 1008 · probability

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A merry-go-round has n horses and turns one horse per second. A kid
walks up to a random horse; if it is taken, the kid waits for the next
horse to come by, and so on, until a free one arrives. Nobody leaves.
For every number of riders from 0 to n − 1, find the expected wait of
the next kid, with error at most 10⁻⁶.

## Input

n (2 ≤ n ≤ 20).

## Output

n lines: the expected wait in seconds when 0, 1, …, n − 1 kids ride.

## Examples

### Example 1

Input:

```
4
```

Output:

```
0.000000
0.250000
0.687500
1.500000
```

## Solution

A kid takes the first free horse at or after a random position, which
is exactly an insertion into a circular hash table with linear
probing, and the wait is the number of taken horses passed. Knuth's
analysis of linear probing on a table of n slots holding k keys gives
the average number of probes of an unsuccessful search as
(1 + Q)/2 with Q = Σⱼ (j + 1)·k(k − 1)…(k − j + 1)/nʲ, the sum over
j = 0 … k. The wait is one probe fewer: (Q − 1)/2. Each line takes a
short sum. `O(n²)`.

For n = 4 and two riders, Q = 1 + 2·(2/4) + 3·(2·1/16) = 2.375, so the
wait is 0.6875.

Pitfalls:

- the expectation is over how the earlier kids sat down, not over
  uniformly random occupied horses: runs of taken horses grow faster;
- with k kids riding the sum stops at j = k;
- a direct simulation over all 2²⁰ seatings is fine in a compiled
  language but needs care elsewhere; the formula avoids it.

The answers agree, for every n from 2 to 20, with an independent
accepted implementation that follows the probability of every set of
taken horses, up to the last digit where the exact value 0.3419875 is
rounded differently.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1817_probability.cpp](1817_probability.cpp) | G++ 13.2 x64 | probability | O(n^2) | AC | 0.015 s | 140 KB |
| [1817_probability.go](1817_probability.go) | Go 1.14 x64 | probability | O(n^2) | AC | 0.046 s | 1088 KB |
| [1817_probability.java](1817_probability.java) | Java 1.8 | probability | O(n^2) | AC | 0.140 s | 1792 KB |
| [1817_probability.py](1817_probability.py) | Python 3.12 x64 | probability | O(n^2) | AC | 0.093 s | 452 KB |
| [1817_probability.rs](1817_probability.rs) | Rust 1.75 x64 | probability | O(n^2) | AC | 0.015 s | 276 KB |
