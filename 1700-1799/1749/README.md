# 1749. Periodic Sum

[Timus 1749](https://acm.timus.ru/problem.aspx?space=1&num=1749) · difficulty 2053 · matrix

Original problem by Petr Lezhankin, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

S(t) is the sum of all substrings of the decimal form of t, read as
numbers with leading zeros allowed, and F(t, k) is t written k times in
a row. Given p, k and m, find S(F(p, k)) modulo m.

## Input

p (1 ≤ p < 10¹⁰⁰⁰⁰⁰), then k and m (1 ≤ k, m ≤ 10⁹).

## Output

S(F(p, k)) modulo m.

## Examples

### Example 1

Input:

```
1205
3 999999999
```

Output:

```
847123538
```

## Solution

Read the digits left to right and let E be the sum of the substrings
that end at the current digit. A new digit d at position j extends each
of them by one digit and starts a new one, so E becomes 10·E + d·j, and
S adds up E after every digit.

Over one copy of p this is linear in the state (S, E, J, 1), where J is
the number of digits before the copy: the position of its i-th digit is
J + i. One pass over p finds the 4 × 4 matrix of one copy: E becomes
10ⁿ·E + v·J + w, with v the value of p and w the sum of its digits
weighted by their positions and powers of ten; S gains the running sums
of those three quantities; J grows by the length n of p. The k-th power
of this matrix, by repeated squaring modulo m, applied to the starting
state S = E = J = 0 gives the answer. `O(n + log k)`.

For the example, S(1205) alone is 1575, and the three copies give
847123538 modulo 999999999.

Pitfalls:

- p has up to 100 000 digits, so it is read as a string;
- substrings with leading zeros count with their value, so a zero digit
  still adds to the positions;
- m = 1 makes every answer 0.

The answers match a direct sum over all substrings with exact integers
on 300 random cases, and an independent accepted implementation on the
large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1749_matrix.cpp](1749_matrix.cpp) | G++ 13.2 x64 | matrix | O(n + log k) | AC | 0.015 s | 640 KB |
| [1749_matrix.go](1749_matrix.go) | Go 1.14 x64 | matrix | O(n + log k) | AC | 0.031 s | 1764 KB |
| [1749_matrix.java](1749_matrix.java) | Java 1.8 | matrix | O(n + log k) | AC | 0.125 s | 1196 KB |
| [1749_matrix.py](1749_matrix.py) | Python 3.12 x64 | matrix | O(n + log k) | AC | 0.156 s | 936 KB |
| [1749_matrix.rs](1749_matrix.rs) | Rust 1.75 x64 | matrix | O(n + log k) | AC | 0.015 s | 480 KB |
