# 1907. Equal Shares of Two Square Grids

[Timus 1907](https://acm.timus.ru/problem.aspx?space=1&num=1907) · difficulty 1326 · number_theory

Original problem by Ivan Burmistrov, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two square grids have integer side lengths a and b. Together they contain
a²+b² unit cells and 4(a+b) unit boundary segments. Both collections must
be split among the same c≥2 groups, so each group receives equally many
cells and equally many segments. There is no connectivity requirement.
Given a and an upper bound n, count the possible integers b with 1≤b≤n.
Limits: 1 second and 64 MB.

## Input

Two integers a and n, with 1≤a≤10¹² and 1≤n≤10¹⁸.

## Output

Print the number of admissible values of b.

## Checking

The answer is one exact integer, checked token by token.

## Examples

```
3 6
```

```
4
```

## Solution

A suitable group count c exists exactly when
gcd(a²+b²,4(a+b))>1. Equivalently, these totals have a common prime divisor.
When a and b have the same parity, both totals are even, so c=2 works.

For opposite parities, the cell total is odd. A common prime p must then
be odd and divide a+b. Substituting b≡−a modulo p gives
a²+b²≡2a². Since p is odd, this vanishes exactly when p divides a,
and consequently b as well. Conversely, an odd prime dividing both a
and b divides both totals. Thus the valid sizes are precisely those
with the same parity as a or with a shared odd prime factor.

Factor a by trial division and retain only its distinct odd prime factors.
Count the invalid sizes, which have opposite parity and avoid every factor.
If a is odd, write b=2t: count integers t≤floor(n/2) coprime to those primes.
If a is even, count odd b≤n coprime to those primes.

Let F(x,i) count the chosen type of integer up to x avoiding primes
with indices i,…,r−1. Without remaining primes, F(x,r)=x for all integers,
or F(x,r)=floor((x+1)/2) for odd integers. Otherwise,
F(x,i)=F(x,i+1)−F(floor(x/pᵢ),i+1). The second term removes multiples
of pᵢ; dividing by this odd prime preserves parity and divisibility by
every other prime. This proves the recurrence. Return n minus the
appropriate invalid count. For x=0, return zero immediately.

The prime list has at most ten elements: the product of the first eleven
odd primes is 3 710 369 067 405, already greater than 10¹². Trial division
takes O(√a) time, the recursion O(2ʳ), and storage is O(r).
For the sample, odd sizes 1,3,5 work, and size 6 shares the odd factor 3.

## Language notes

Use signed 64-bit values in C++, Go 1.14, Java 8 and Rust 1.75.
Never compute a²+b² for a candidate b: it can reach approximately 10³⁶.
Every recursive result is an actual subset count between zero and its
bound, so intermediate subtraction also fits signed 64 bits. The answer
is at most 10¹⁸. Trial-division squares are at most about 10¹², not n².
Python 3.12 needs no special arithmetic. Recursion depth is at most eleven.
Remove complete prime powers to avoid counting the same factor twice.

The answers agree with computing the gcd of the totals directly on
90 208 cases, and the large ones with a plain inclusion-exclusion sum in
arbitrary precision.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1907_number_theory.cpp](1907_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt(a) + 2^r) | AC | 0.015 s | 424 KB |
| [1907_number_theory.go](1907_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt(a) + 2^r) | AC | 0.046 s | 1088 KB |
| [1907_number_theory.java](1907_number_theory.java) | Java 1.8 | number_theory | O(sqrt(a) + 2^r) | AC | 0.140 s | 1660 KB |
| [1907_number_theory.py](1907_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt(a) + 2^r) | AC | 0.140 s | 500 KB |
| [1907_number_theory.rs](1907_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt(a) + 2^r) | AC | 0.046 s | 232 KB |
