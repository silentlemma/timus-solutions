# 1284. Space poker

[Timus 1284](https://acm.timus.ru/problem.aspx?space=1&num=1284) · difficulty 2247 · bruteforce

Original problem by Leonid Volkov, from the Ural State University Personal Contest 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A hand of N ≤ 20 distinct cards lies in a row; each card has a value
from 1 to 100 and a suit from 1 to 10. Odd suits are blue, even suits
yellow, and the numbers of blue and yellow suits in the hand differ by
at most one. One move takes a card and puts it anywhere in the row.
Find the fewest moves after which every suit lies together, blue and
yellow suits alternate, and inside every suit the values are sorted,
all suits the same way (all ascending or all descending).

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N cards as value and suit, from left to right.

## Output

The fewest moves.

## Examples

### Example 1

Input:

```
5
10 1
12 2
8 2
4 4
7 4
```

Output:

```
2
```

## Solution

Cards that are never moved keep their relative order, and every moved
card can be dropped straight into its final place. So for a fixed
target arrangement the answer is N minus the longest subsequence of the
hand that already comes in target order: give every card its rank in
the target and take the longest increasing subsequence of ranks.

The targets differ only in the order of the blue suits, the order of
the yellow suits, which colour comes first (forced when one colour has
more suits) and the direction of sorting. With at most five suits of
each colour that is at most 5! · 5! · 2 · 2 = 57 600 targets, each
checked with an `O(N log N)` longest increasing subsequence.

Pitfalls:

- the direction is shared: one suit ascending and another descending is
  not allowed;
- when one colour has more suits, it must start and end the row
  (test 08);
- a hand already in order needs no moves (tests 04, 06).

The answers were compared with a breadth-first search over all
arrangements reachable by single moves on 200 random hands of up to six
cards.

## Language notes

- C++ walks the suit orders with `next_permutation`; Python uses
  `itertools.permutations`; Go, Java and Rust swap elements recursively.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1284_bruteforce.cpp](1284_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(5!² · N log N) | AC | 0.031 s | 208 KB |
| [1284_bruteforce.go](1284_bruteforce.go) | Go 1.14 x64 | bruteforce | O(5!² · N log N) | AC | 0.046 s | 5948 KB |
| [1284_bruteforce.java](1284_bruteforce.java) | Java 1.8 | bruteforce | O(5!² · N log N) | AC | 0.156 s | 5880 KB |
| [1284_bruteforce.py](1284_bruteforce.py) | Python 3.12 x64 | bruteforce | O(5!² · N log N) | AC | 0.531 s | 608 KB |
| [1284_bruteforce.rs](1284_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(5!² · N log N) | AC | 0.046 s | 228 KB |
