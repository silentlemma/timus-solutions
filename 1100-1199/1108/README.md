# 1108. Unit fractions that leave the smallest positive remainder

[Timus 1108](https://acm.timus.ru/problem.aspx?space=1&num=1108) · difficulty 252 · math

Original problem by Pavlin Peev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose positive integers `a_1 ≤ a_2 ≤ … ≤ a_N` (`1 ≤ N ≤ 18`) so that
`1 − (1/a_1 + … + 1/a_N)` is positive and as small as possible. Print
them in that order, one per line.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`.

## Output

`a_1`, …, `a_N`, each on its own line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2
```

Output:

```
2
3
```

## Solution

Take every fraction greedily: the largest unit fraction that still leaves
something. This gives Sylvester's sequence `a_1 = 2`,
`a_{k+1} = a_k (a_k − 1) + 1`, and by induction the remainder after `k`
terms is exactly `1 / (a_{k+1} − 1)`, so the next largest admissible
fraction is `1/a_{k+1}`. That the greedy choice is also the best one for
every `N` is a classical result on Egyptian fractions (Curtiss, 1922).

The terms square at every step: `a_18` has about 26 700 digits and the
whole output about 53 000 characters, so big integers are needed. One
multiplication per term, `O(D²)` with the schoolbook method for `D`
digits, is fast enough.

Pitfalls:

- 64-bit integers overflow already at `a_8`;
- Python refuses by default to convert integers longer than 4300 digits
  to text, which `a_16` already exceeds;
- the denominators must be printed in full, without scientific notation
  or rounding.

The answers were checked against a search over all non-decreasing
denominators with exact fractions for `N ≤ 4`, and for every `N` by
verifying with exact fractions that the remainder is `1 / (a_1 ⋯ a_N)`,
the value the greedy argument gives.

## Language notes

- Go and Java use `math/big` and `BigInteger`; Python's own integers
  need `sys.set_int_max_str_digits(0)` before printing.
- C++ and Rust keep the number in base `10^9` digits and compute
  `a · (a − 1) + 1` by schoolbook multiplication.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1108_math.cpp](1108_math.cpp) | G++ 13.2 x64 | math | O(D²) per term | AC | 0.015 s | 232 KB |
| [1108_math.go](1108_math.go) | Go 1.14 x64 | math | O(D²) per term | AC | 0.015 s | 1920 KB |
| [1108_math.java](1108_math.java) | Java 1.8 | math | O(D²) per term | AC | 0.187 s | 6508 KB |
| [1108_math.py](1108_math.py) | Python 3.12 x64 | math | O(D²) per term | AC | 0.031 s | 1144 KB |
| [1108_math.rs](1108_math.rs) | Rust 1.75 x64 | math | O(D²) per term | AC | 0.015 s | 356 KB |
