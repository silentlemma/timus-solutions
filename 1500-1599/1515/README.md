# 1515. Cashmaster

[Timus 1515](https://acm.timus.ru/problem.aspx?space=1&num=1515) · difficulty 215 · greedy

Original problem by Ilya Grebnov, Nikita Rybak and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There is one banknote of each of N values (1 ≤ N ≤ 100), given in
increasing order, each from 1 to 10⁶. Find the smallest positive value
that is not the sum of some of these banknotes; a single banknote
counts as a sum.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N values in increasing order.

## Output

The smallest value that no set of banknotes adds up to.

## Examples

### Example 1

Input:

```
5
1 2 4 9 100
```

Output:

```
8
```

## Solution

Go through the values in increasing order and keep reach, the largest
number such that every sum from 1 to reach can be paid. If the next
value d is at most reach + 1, then every sum up to reach + d can be paid
too: the sums up to reach as before, and the larger ones as d plus a
sum up to reach. If d > reach + 1, then reach + 1 cannot be paid: the
values taken so far add up to only reach, and every other value is
larger than reach + 1 by itself. The answer is reach + 1. The scan takes
`O(N)` time. All five implementations sort first, giving an overall
`O(N log N)` time upper bound and `O(N)` storage.

Pitfalls:

- the input is already increasing, but the implementations still sort it;
  include that step when bounding the total time (tests 05, 06 have N = 100);
- without a banknote of 1 the answer is 1 (tests 03, 06);
- the answer can be larger than every value, up to the sum of all of
  them plus one (tests 04, 05, gen2);
- the first gap ends the scan, and no later value can fill it: with 1
  and 3 the sum 2 is missing (test 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1515_greedy.cpp](1515_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 196 KB |
| [1515_greedy.go](1515_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1096 KB |
| [1515_greedy.java](1515_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.109 s | 500 KB |
| [1515_greedy.py](1515_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 428 KB |
| [1515_greedy.rs](1515_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 228 KB |
