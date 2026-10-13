# 1491. Unreal Story

[Timus 1491](https://acm.timus.ru/problem.aspx?space=1&num=1491) · difficulty 205 · prefix_sums

Original problem by Alexander Toropov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N knights (2 ≤ N ≤ 100000) are numbered 1 to N. The king names a, b and
c, and every knight from a to b receives c coins; then each knight names
a further triple a_i, b_i, c_i with the same effect (1 ≤ a ≤ b ≤ N,
1 ≤ c ≤ 10000). Print how many coins each knight receives.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, the king's triple, then N triples of the knights.

## Output

N totals separated by spaces.

## Examples

### Example 1

Input:

```
4
2 3 2
2 4 1
3 4 1
1 2 1
1 1 1
```

Output:

```
2 4 4 2
```

### Example 2

Input:

```
7
1 7 1
2 3 4
3 5 3
1 2 1
5 7 4
2 4 10
3 4 2
1 6 3
```

Output:

```
5 19 23 19 11 8 5
```

## Solution

N + 1 range additions, each up to 10⁵ long, are too slow one by one. A
difference array records a gift of c to the knights a..b as +c at
position a and −c at position b + 1; a running sum over the array then
gives every knight's total. `O(N)`.

Pitfalls:

- the king's triple is one more gift, so there are N + 1 of them
  (tests 01, 02);
- a total can reach 100001 · 10000 ≈ 10⁹, close to the 32-bit limit, so
  the sums are kept in 64 bits (gen2);
- the conditions about the knights' own seats change nothing in the
  arithmetic (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1491_prefix_sums.cpp](1491_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.187 s | 980 KB |
| [1491_prefix_sums.go](1491_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 4540 KB |
| [1491_prefix_sums.java](1491_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 8872 KB |
| [1491_prefix_sums.py](1491_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.328 s | 35944 KB |
| [1491_prefix_sums.rs](1491_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 9428 KB |
