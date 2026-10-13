# 1481. Winning Chances

[Timus 1481](https://acm.timus.ru/problem.aspx?space=1&num=1481) · difficulty 2282 · greedy

Original problem by Sergey Pupyrev, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N different weights (1 ≤ N ≤ 50, positive integers up to 1000) are put
one by one on a pan scale, each on the left or the right pan. After
each weight the heavier pan was written down as L or R; the scale was
never level. Given the weights and the record, print an order of the
weights with their pans that produces the record, or "I'm too stupid to
solve this problem" if there is none.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, the weights, then the record of N letters.

## Output

N lines: a weight and its pan, in the order they were put on.

## Examples

### Example 1

Input:

```
3
10 20 30
LRL
```

Output:

```
10 L
20 R
30 L
```

## Solution

An order always exists. Sort the weights and keep the ones already
used as a contiguous block of the sorted list in which neighbours stand
on opposite pans. Then the pan holding the largest weight is strictly
heavier: pairing the weights from the top, (a_k − a_(k−1)) +
(a_(k−2) − a_(k−3)) + … is positive.

Let c be the number of times the record changes letter. Start with the
weight that has exactly c heavier ones, on the pan of the first letter.
At each change, add the next larger weight on the pan opposite the
current largest, which is the new winner. At each repeat, add the next
smaller weight on the pan opposite the current smallest; the largest
weight, and so the winning pan, stays. The c changes use up exactly the
c heavier weights, and the repeats use the lighter ones. `O(N log N)`.

Pitfalls:

- the message is never printed: every record can be produced (all
  tests);
- always loading the lighter pan fails for close weights: 5, 6, 7 with
  LLL would end with R (test 05);
- a change at every step needs a chain of growing weights, so the start
  must leave exactly enough heavier ones (test 04, gen2).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1481_greedy.cpp](1481_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 200 KB |
| [1481_greedy.go](1481_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1108 KB |
| [1481_greedy.java](1481_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 1732 KB |
| [1481_greedy.py](1481_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.093 s | 552 KB |
| [1481_greedy.rs](1481_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.046 s | 260 KB |
