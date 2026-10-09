# 1086. The n-th prime number

[Timus 1086](https://acm.timus.ru/problem.aspx?space=1&num=1086) · difficulty 106 · number_theory

Original problem: folklore, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each of `k` numbers `n` (`1 ≤ n ≤ 15000`) print the `n`-th prime
number. 1 is not a prime.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`k`, then `k` lines with `n`.

## Output

The `n`-th prime for each `n`, one per line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
3
2
5
7
```

Output:

```
5
3
11
17
```

## Solution

The 15000th prime is 163 841, so one sieve of Eratosthenes up to that
number lists every prime that can be asked for, and each query is an
index into the list. `O(L log log L)` for the sieve with `L = 163 842`,
`O(1)` per query.

Pitfalls:

- the first prime is 2, not 1;
- the sieve bound must cover the 15000th prime itself; it can be found
  once with any method and written into the program;
- the number of queries is not limited, so the primes are computed once,
  not for every query.

The answers were checked against primes found one by one by trial
division.

## Language notes

- Python crosses out multiples with slice assignment on a `bytearray`.
- C++, Go, Java and Rust start crossing out at `p²`; C++ and Java compute
  it in 64 bits to stay safe from overflow.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1086_number_theory.cpp](1086_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L) | AC | 0.031 s | 212 KB |
| [1086_number_theory.go](1086_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L) | AC | 0.001 s | 2308 KB |
| [1086_number_theory.java](1086_number_theory.java) | Java 1.8 | number_theory | O(L log log L) | AC | 0.093 s | 2132 KB |
| [1086_number_theory.py](1086_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L) | AC | 0.093 s | 2764 KB |
| [1086_number_theory.rs](1086_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L) | AC | 0.001 s | 1268 KB |
