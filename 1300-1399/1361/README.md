# 1361. Spaceology vs. Chronistics

[Timus 1361](https://acm.timus.ru/problem.aspx?space=1&num=1361) · difficulty 1894 · graphs

Original problem: idea by Alexander Klepinin, prepared by Evgeny Krokhalev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city has N ≤ 100 000 crossroads, and each crossroad lists its outgoing
roads from left to right. Two professors start driving at the same
moment from crossroads A and B. At every crossroad the first one always
takes the leftmost road and the second one the rightmost; every road
takes one minute. They can meet only at a crossroad, at the same
moment. Print the minute of the first meeting, or −1 if they never
meet.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines, each a list of crossroads ending with 0, from the
leftmost road to the rightmost. The last line holds A and B.

## Output

The minute of the meeting, or −1.

## Examples

### Example 1

Input:

```
7
2 4 0
3 1 0
4 2 0
5 1 6 3 0
6 4 0
2 5 4 0
6 0
1 7
```

Output:

```
7
```

## Solution

Each driver has exactly one way out of every crossroad, so each walk is
a tail followed by a cycle. Walk each one until a crossroad repeats.
Then every crossroad v on a walk is visited either once, at moment r, or
at the moments r, r + L, r + 2L, … if it lies on the cycle of length L.

For every crossroad that both walks visit, intersect the two sets of
moments:

- two single moments meet only if they are equal;
- a single moment t lies in r + kL when t ≥ r and L divides t − r;
- two cycles need t ≡ r₁ (mod L₁) and t ≡ r₂ (mod L₂). By the Chinese
  remainder theorem there is a solution only if gcd(L₁, L₂) divides
  r₂ − r₁. Its least value is at least r₁; when it is still below r₂, add
  whole multiples of lcm(L₁, L₂).

The answer is the least moment over all crossroads. `O(N log N)`.

Pitfalls:

- simulating step by step is too slow: two cycles of 49 999 and 50 001
  crossroads that share one crossroad meet only after 2 499 999 998
  minutes (generated test 2), more than 32-bit integers hold;
- cycles of equal even length entered out of step never meet
  (generated test 3);
- both may start at the same crossroad, which gives 0 (test 02);
- only the first and last road of each list matter, but all of them
  must be read.

The answers were compared with step-by-step simulation, long enough to
cover the tails and both cycles, on 3 000 random cities of up to 9
crossroads, 985 of them without a meeting.

## Language notes

- Python uses `pow(x, -1, m)` for the modular inverse; the other
  languages use the extended Euclidean algorithm.
- Go and Java read the input byte by byte.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1361_graphs.cpp](1361_graphs.cpp) | G++ 13.2 x64 | graphs | O(N log N) | AC | 0.187 s | 4608 KB |
| [1361_graphs.go](1361_graphs.go) | Go 1.14 x64 | graphs | O(N log N) | AC | 0.062 s | 12740 KB |
| [1361_graphs.java](1361_graphs.java) | Java 1.8 | graphs | O(N log N) | AC | 0.109 s | 7420 KB |
| [1361_graphs.py](1361_graphs.py) | Python 3.12 x64 | graphs | O(N log N) | AC | 0.343 s | 49584 KB |
| [1361_graphs.rs](1361_graphs.rs) | Rust 1.75 x64 | graphs | O(N log N) | AC | 0.046 s | 7588 KB |
