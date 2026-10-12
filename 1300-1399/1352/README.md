# 1352. Mersenne Primes

[Timus 1352](https://acm.timus.ru/problem.aspx?space=1&num=1352) · difficulty 132 · number_theory

Original problem by Vladimir Yakovlev, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A Mersenne prime is a prime of the form 2^p − 1. Given T queries, each
a number N ≤ 38, print the exponent p of the N-th Mersenne prime in
increasing order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

T, then T lines with N.

## Output

T lines with the exponents.

## Examples

### Example 1

Input:

```
13
18
32
24
21
19
34
27
33
20
30
28
29
22
```

Output:

```
3217
756839
19937
9689
4253
1257787
44497
859433
4423
132049
86243
110503
9941
```

## Solution

No program can find these primes in a second: the 38th exponent is
6 972 593, and checking even one number of that size takes a lot of
computation. The order of the first 38 Mersenne primes was settled long
ago, so the solutions keep the list of their exponents as a constant
table and answer each query by indexing it. `O(T)`.

Pitfalls:

- N counts from 1: the first Mersenne prime is 2² − 1 = 3, exponent 2
  (test 03);
- all exponents fit in 32-bit integers.

The first 22 entries were checked by running the Lucas–Lehmer test on
every prime exponent up to 10 000; the rest come from the published list
and agree with the example and the entries named in the statement.

## Language notes

- Python keeps the table as one string split into words, so the answers
  are printed without converting them back to numbers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1352_number_theory.cpp](1352_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T) | AC | 0.001 s | 128 KB |
| [1352_number_theory.go](1352_number_theory.go) | Go 1.14 x64 | number_theory | O(T) | AC | 0.031 s | 1084 KB |
| [1352_number_theory.java](1352_number_theory.java) | Java 1.8 | number_theory | O(T) | AC | 0.078 s | 444 KB |
| [1352_number_theory.py](1352_number_theory.py) | Python 3.12 x64 | number_theory | O(T) | AC | 0.062 s | 324 KB |
| [1352_number_theory.rs](1352_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T) | AC | 0.001 s | 216 KB |
