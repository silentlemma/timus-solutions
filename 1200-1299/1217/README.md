# 1217. Tickets that are lucky both in Moscow and in St. Petersburg

[Timus 1217](https://acm.timus.ru/problem.aspx?space=1&num=1217) · difficulty 408 · combinatorics

Original problem by Leonid Volkov, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A ticket number has `N` digits, `N` even and at most 20, leading zeros
allowed. It is lucky in Moscow when its two halves have equal digit sums,
and lucky in St. Petersburg when the digits in odd positions sum like the
digits in even positions. Count the tickets lucky in both senses.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The number of such tickets.

## Examples

### Example 1

Input:

```
4
```

Output:

```
100
```

## Solution

Split the positions into four groups by half and by parity: `A` and `B`
are the odd and even positions of the first half, `C` and `D` those of
the second half, and let each letter also stand for the digit sum of its
group. The two conditions read `A + B = C + D` and `A + C = B + D`.
Adding them gives `A = D`, and subtracting gives `B = C`; conversely
those two equalities give back both conditions. The groups are
independent, so the answer is

(pairs of fillings of `A` and `D` with equal sums) × (pairs of fillings
of `B` and `C` with equal sums).

The number of ways to write a sum `s` with `k` digits comes from a small
table built one digit at a time, and each factor is the sum over `s` of
the products of two such counts. `O(N²)` with tiny constants.

Pitfalls:

- the group sizes depend on whether `N/2` is odd; counting them position
  by position avoids getting that wrong;
- the answer for `N = 20` is about `1.9·10¹⁷`, beyond 32 bits but within
  64.

The formula was checked by brute force over all six-digit tickets, and
every even `N` from 2 to 20 was compared with a separately written
solution.

## Language notes

- All languages build the digit-sum tables the same way and use 64-bit
  integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1217_combinatorics.cpp](1217_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N²) | AC | 0.001 s | 192 KB |
| [1217_combinatorics.go](1217_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N²) | AC | 0.031 s | 1072 KB |
| [1217_combinatorics.java](1217_combinatorics.java) | Java 1.8 | combinatorics | O(N²) | AC | 0.109 s | 1592 KB |
| [1217_combinatorics.py](1217_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N²) | AC | 0.078 s | 436 KB |
| [1217_combinatorics.rs](1217_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N²) | AC | 0.031 s | 224 KB |
