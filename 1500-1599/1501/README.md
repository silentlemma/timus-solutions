# 1501. Sense of Beauty

[Timus 1501](https://acm.timus.ru/problem.aspx?space=1&num=1501) · difficulty 268 · dp

Original problem by Leonid Volkov and Stanislav Vasiliev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two piles of N cards each (4 ≤ N ≤ 1000) hold N red and N black cards in
total. The croupier repeatedly takes the top card of either pile and
puts it on a red or a black pile, until all cards are moved. At every
moment the red and the black piles may differ by at most one card. Print
the piles the cards are taken from, as 2N digits 1 and 2, or
"Impossible".

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then the two piles from top to bottom, 1 for red and 0 for black.

## Output

The 2N digits, or "Impossible". Any fitting order is accepted.

## Examples

### Example 1

Input:

```
4
0011
0110
```

Output:

```
22121112
```

### Example 2

Input:

```
4
1100
1100
```

Output:

```
Impossible
```

## Solution

A moment is described by the numbers i and j of cards taken from the
two piles. With d = 2 · (red cards) − (cards) counted over each pile's
taken part, the red and black piles differ by d1[i] + d2[j], so the
state is allowed when that is −1, 0 or 1. A state is reachable when it
is allowed and the state above or to the left of it is reachable;
(0, 0) starts. If (N, N) is reachable, walk back from it, taking any
reachable predecessor, and read the moves backwards. `O(N²)`.

Pitfalls:

- the condition applies after every single move, not only at the end
  (test 02, gen4);
- many orders can be right, so the tests use a checker (all tests);
- with the 0.5-second limit the table of N² states must be cheap; the
  Python solution keeps each row as one integer mask and spreads
  reachability along runs of allowed states with one addition.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1501_dp.cpp](1501_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 856 KB |
| [1501_dp.go](1501_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 2216 KB |
| [1501_dp.java](1501_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.109 s | 2704 KB |
| [1501_dp.py](1501_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 836 KB |
| [1501_dp.rs](1501_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.031 s | 1164 KB |
