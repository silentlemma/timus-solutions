# 2070. Prime powers with a prime number of divisors

[Timus 2070](https://acm.timus.ru/problem.aspx?space=1&num=2070) · difficulty 235 · number_theory

Original problem by Alexey Danilyuk, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

One person calls an integer interesting when it is prime, another when
its number of positive divisors is prime. An integer is satisfying when
both agree, either way. Count the satisfying integers in [L; R]. The
limits are 2 seconds and 64 MB.

## Input

L and R, 2 ≤ L ≤ R ≤ 10¹².

## Output

The number of satisfying integers in [L; R].

## Examples

### Example 1

Input:

```
3 7
```

Output:

```
4
```

### Example 2

Input:

```
2 2
```

Output:

```
1
```

### Example 3

Input:

```
77 1010
```

Output:

```
924
```

## Solution

A prime has 2 divisors, and 2 is prime, so both call every prime
interesting. A composite number is satisfying unless its number of
divisors is prime. For x = p₁^a₁ · … · pₛ^aₛ that number is
(a₁ + 1) · … · (aₛ + 1), and a product is prime only when it has a
single factor. So the unsatisfying numbers are exactly the powers p^k
of a prime with k ≥ 2 and k + 1 prime, and the answer is
R − L + 1 minus their count in [L; R].

Since p^k ≤ 10¹² with k ≥ 2, every such p is at most 10⁶. A sieve up to
10⁶ gives the primes, and for each prime p with p² ≤ R the powers
p², p³, … up to R are walked, counting those at least L whose exponent
plus one is prime. Primes above 10⁴ only have the square, so the walk
is short; the total work is dominated by the sieve, O(N log log N) with
N = 10⁶.

In the first example 4 = 2² has 3 divisors, so it is the only
unsatisfying number among 3 … 7 and the answer is 4.

## Language notes

C++, Go, Java and Rust compare powers with R / p before multiplying,
so they never exceed 10¹² · 10⁶ and stay within 64 bits. The Python solution counts the
squares as the primes between √L and √R with one slice of the sieve and
walks only the primes up to ∛R, which keeps it fast on CPython.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2070_number_theory.cpp](2070_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.031 s | 304 KB |
| [2070_number_theory.go](2070_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.031 s | 2136 KB |
| [2070_number_theory.java](2070_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.140 s | 2632 KB |
| [2070_number_theory.py](2070_number_theory.py) | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.109 s | 2816 KB |
| [2070_number_theory.rs](2070_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.062 s | 1212 KB |
