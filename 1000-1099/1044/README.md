# 1044. Counting balanced tickets of N digits

[Timus 1044](https://acm.timus.ru/problem.aspx?space=1&num=1044) · difficulty 122 · bruteforce

Original problem by Stanislav Vasiliev, from the Fifth Ural State University Team Programming Championship, October 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A ticket number has `N` digits (`N` is even, `2 ≤ N ≤ 8`; leading zeros
are allowed). It is balanced when the first half of the digits and the
second half have equal sums. Count the balanced tickets.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`.

## Output

The number of balanced tickets.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
```

Output:

```
670
```

### Example 2

Input:

```
2
```

Output:

```
10
```

## Solution

The halves are independent. Count, for every sum `s`, how many numbers
below `10^(N/2)` have digit sum `s`: at most 10000 numbers to look at.
A balanced ticket is a pair of halves with the same sum, so the answer is
the sum of `ways[s]^2` over all `s`. `O(10^(N/2) · N)`.

For `N = 8` the answer is 4816030, which fits in 32 bits, but the
squares are summed in 64-bit integers anyway.

Pitfalls:

- leading zeros count: `0000` is a ticket;
- the halves have `N / 2` digits each, not `N`.

[Problem 1036](../1036/README.md) asks the same for up to 100 digits and
a fixed total sum; there the counts come from a DP and need big integers.

## Language notes

- All languages run the same count; Python takes digit sums of
  `str(x)`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1044_bruteforce.cpp](1044_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 196 KB |
| [1044_bruteforce.go](1044_bruteforce.go) | Go 1.14 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.046 s | 1080 KB |
| [1044_bruteforce.java](1044_bruteforce.java) | Java 1.8 | bruteforce | O(10^(N/2) · N) | AC | 0.093 s | 1552 KB |
| [1044_bruteforce.py](1044_bruteforce.py) | Python 3.12 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.078 s | 288 KB |
| [1044_bruteforce.rs](1044_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(10^(N/2) · N) | AC | 0.015 s | 216 KB |
