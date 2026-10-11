# 1310. ACM Diagnostics

[Timus 1310](https://acm.timus.ru/problem.aspx?space=1&num=1310) · difficulty 1066 · dp

Original problem: idea by Alexander Klepinin, prepared by Alexander Klepinin and Pavel Egorov, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A state is a vector of L ≤ 100 integers, each from 1 to M ≤ 50, whose
sum is divisible by K ≤ 50. List all states in increasing
lexicographic order, numbered from 0. Given a number N from that list,
print the state.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

L, M and K, then N.

## Output

The L values of the state.

## Examples

### Example 1

Input:

```
3 10 4
213
```

Output:

```
9 6 1
```

## Solution

Count first, then pick the values one by one.

Let ways[i][r] be the number of ways to fill i registers with values
1..M so that their sum leaves remainder r modulo K. Then ways[0][0] = 1
and

ways[i][(r + v) mod K] += ways[i − 1][r] for every v in 1..M.

To read off the state, walk through the positions keeping the sum s
of the values chosen so far. At a position with `left` registers after
it, value v starts a block of ways[left][(−(s + v)) mod K] states. Try
v = 1, 2, …: while N is at least the block, skip the block (N −= block),
otherwise take v and move on.

The counts reach about 50¹⁰⁰, a 170-digit number, so N and the table
need big integers. The table has 101 · K entries and is filled with
L · M · K big additions. `O(L · M · K)` big operations.

Pitfalls:

- the remainder of a negative number must be taken into 0..K − 1
  ((−(s + v)) mod K);
- with K = 1 the states are all of M^L vectors, and the last one is
  all M (test 06);
- one register: only the values divisible by K exist (tests 02 and 03).

The answers were compared with listing all the states directly on 150
small random cases.

## Language notes

- Python, Go and Java use their built-in big integers; C++ and Rust use
  a small number type stored in base 10⁹ with only the operations
  needed: reading, adding, comparing and subtracting.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1310_dp.cpp](1310_dp.cpp) | G++ 13.2 x64 | dp | O(L * M * K) | AC | 0.031 s | 800 KB |
| [1310_dp.go](1310_dp.go) | Go 1.14 x64 | dp | O(L * M * K) | AC | 0.015 s | 1752 KB |
| [1310_dp.java](1310_dp.java) | Java 1.8 | dp | O(L * M * K) | AC | 0.109 s | 6596 KB |
| [1310_dp.py](1310_dp.py) | Python 3.12 x64 | dp | O(L * M * K) | AC | 0.109 s | 884 KB |
| [1310_dp.rs](1310_dp.rs) | Rust 1.75 x64 | dp | O(L * M * K) | AC | 0.046 s | 820 KB |
