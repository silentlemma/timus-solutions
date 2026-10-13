# 1456. Jedi Riddle 2

[Timus 1456](https://acm.timus.ru/problem.aspx?space=1&num=1456) · difficulty 748 · number_theory

Original problem by Ilya Grebnov, Dmitry Kovalioff and Nikita Rybak, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given A and N (2 ≤ A < N ≤ 10⁹), the remainders Z[1] = A mod N,
Z[i + 1] = Z[i] · A mod N are computed one by one. Find the smallest
positive X with Z[X] = 1, that is, the smallest X with A^X ≡ 1 (mod N),
or print 0 if there is none.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

A and N.

## Output

X, or 0.

## Examples

### Example 1

Input:

```
7 20
```

Output:

```
4
```

The remainders are 7, 9, 3 and 1.

## Solution

If A and N share a factor, every remainder keeps it and never becomes 1,
so the answer is 0. Otherwise X is the multiplicative order of A modulo
N, and by Euler's theorem it divides φ(N). Factor N by trial division up
to √N to get φ(N), then factor φ(N) the same way, and start from
x = φ(N): for each prime p of φ(N), divide x by p as long as
A^(x / p) is still 1 modulo N. What remains is the order, since a power
that equals 1 stays a multiple of the order. All products are below
10¹⁸, so 64-bit arithmetic with fast exponentiation is enough.
`O(√N + log² N)`.

Pitfalls:

- a common factor of A and N, including even A with even N (tests 02,
  08, 11);
- simulating the remainders one by one is far too slow when the order
  is close to N (test 13);
- A = N − 1 has order 2 (tests 04, 10).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1456_number_theory.cpp](1456_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.031 s | 192 KB |
| [1456_number_theory.go](1456_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.031 s | 1072 KB |
| [1456_number_theory.java](1456_number_theory.java) | Java 1.8 | number_theory | O(sqrt N + log^2 N) | AC | 0.140 s | 1628 KB |
| [1456_number_theory.py](1456_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.078 s | 472 KB |
| [1456_number_theory.rs](1456_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt N + log^2 N) | AC | 0.015 s | 232 KB |
