# 1535. The Hobbit or There and Back Again

[Timus 1535](https://acm.timus.ru/problem.aspx?space=1&num=1535) · difficulty 496 · constructive

Original problem by Alexander Ipatov, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Bilbo leaves city 1, visits each of the cities 2 … N once and returns to
city 1 (2 ≤ N ≤ 50000). Entering city P from city Q costs P·Q gold.
Print a visiting order of minimal total cost and one of maximal total
cost.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

Two lines with N numbers each, starting with 1: the cheapest order and
the dearest one. Any optimal orders are accepted.

## Examples

### Example 1

Input:

```
4
```

Output:

```
1 4 2 3
1 3 4 2
```

## Solution

The cost is the sum of products of neighbours around a cycle through all
numbers 1 … N, so both lines are cyclic arrangements.

The dearest puts every number next to the two numbers closest in size:
1, 3, 5, … up to N and back down through the even numbers to 2. This is
the classical organ-pipe arrangement that maximises such a cyclic sum.

The cheapest pairs large numbers with small ones. Read as a cycle from
N, one side goes 2, N − 2, 4, N − 4, 6, … and the other 1, N − 1, 3,
N − 3, 5, …; at step k the two sides take k + 1 and k for odd k and
N − k and N − k + 1 for even k, until a pair would reuse a number. If
one number is left, it sits where the two sides meet. Exhaustive search
for N ≤ 10 shows this is the only cheapest cycle up to reflection, and
the judge accepts it for all N; we do not have a proof. Rotating the
cycle to start at 1 gives the first line. `O(N)`.

Pitfalls:

- simple alternation 1, N, 2, N − 1, … is not optimal: for N = 5 it costs
  38, and 1, 5, 2, 3, 4 costs 37 (test 04);
- the two sides may meet with one city left over (test 05) or with none
  (test 06);
- both lines must start with city 1 (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1535_constructive.cpp](1535_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1700 KB |
| [1535_constructive.go](1535_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 7060 KB |
| [1535_constructive.java](1535_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.140 s | 11176 KB |
| [1535_constructive.py](1535_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.109 s | 8752 KB |
| [1535_constructive.rs](1535_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 4376 KB |
