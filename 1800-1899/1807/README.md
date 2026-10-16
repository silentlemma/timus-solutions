# 1807. Cartridges for Maxim

[Timus 1807](https://acm.timus.ru/problem.aspx?space=1&num=1807) · difficulty 1479 · number_theory

Original problem by Daniil Ayzenshteyn (idea by Alex Samsonov), from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n cartridges came in at least two equal boxes of at least 100 each.
Split them among two or more pockets so that the gcd of the pocket
sizes is as large as possible, and among such splits the lcm is as
large as possible. Print any best split.

## Input

n (200 ≤ n ≤ 10⁹).

## Output

The pocket sizes.

## Examples

### Example 1

Input:

```
200
```

Output:

```
100 100
```

### Example 2

Input:

```
625
```

Output:

```
375 250
```

## Solution

Let p be the smallest prime factor of n; n is composite, so p ≤ 31622.
A gcd g of at least two pockets divides n and leaves n/g ≥ 2, so the
largest gcd is n/p. Every best split is then n/p times parts adding up
to p, and its lcm is n/p times the lcm of the parts. Among parts adding
up to p, the largest lcm comes from powers of distinct primes, padded
with ones, which is Landau's function. It is found by a knapsack: for
each prime q, choose at most one power of q below p, with weight the
power and value its logarithm, and maximize the value within weight p.
A choice table per prime gives back the parts. A full search over all
primes once showed that the best choice for any prime p < 31623 never
needs a prime above 700, so only primes below 1000 take part. Parts
are below p, so the split always has at least two pockets.
`O(p · π(1000))`.

In the second example p = 5 and n/p = 125; 5 = 2 + 3 has the lcm 6,
the most possible, so the pockets hold 250 and 375.

Pitfalls:

- an even n gives p = 2, and the only split is two halves;
- p itself may not be one part, since at least two pockets are needed;
- the lcm grows beyond any integer type, so its logarithm is compared.

The checker compares the exact lcm with that of the expected answer
and checks the sum, the gcd and the number of pockets. The answers
agree with an independent accepted implementation on the squares of
all primes from 11 to 400, on the square of the largest prime below
31623 and on random totals.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1807_number_theory.cpp](1807_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(p pi(1000)) | AC | 0.015 s | 5504 KB |
| [1807_number_theory.go](1807_number_theory.go) | Go 1.14 x64 | number_theory | O(p pi(1000)) | AC | 0.046 s | 14608 KB |
| [1807_number_theory.java](1807_number_theory.java) | Java 1.8 | number_theory | O(p pi(1000)) | AC | 0.171 s | 12444 KB |
| [1807_number_theory.py](1807_number_theory.py) | PyPy 3.10 x64 | number_theory | O(p pi(1000)) | AC | 0.187 s | 15384 KB |
| [1807_number_theory.rs](1807_number_theory.rs) | Rust 1.75 x64 | number_theory | O(p pi(1000)) | AC | 0.046 s | 5784 KB |
