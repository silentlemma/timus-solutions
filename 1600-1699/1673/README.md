# 1673. Admission to Exam

[Timus 1673](https://acm.timus.ru/problem.aspx?space=1&num=1673) · difficulty 1220 · number_theory

Original problem by Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N teachers run N² labs: teacher t runs labs t, N + t, 2N + t, …. Student
j of N attends exactly the labs whose numbers are multiples of j, and a
student is admitted to the exam after attending at least one lab of
every teacher. Exactly K students were admitted; print the smallest
possible N, or 0 if there is none.

## Input

K (1 ≤ K ≤ 2·10⁹).

## Output

The smallest N, or 0.

## Examples

### Example 1

Input:

```
8
```

Output:

```
15
```

### Example 2

Input:

```
3
```

Output:

```
0
```

## Solution

Teacher t runs the labs whose numbers leave remainder t modulo N.
Student j attends j, 2j, …, Nj, which run through all the multiples of
gcd(j, N) modulo N; that is every remainder exactly when gcd(j, N) = 1.
So K = φ(N), Euler's totient, and the task is the smallest N with
φ(N) = K.

With N = p₁^e₁ ⋯ p_r^e_r, φ(N) = ∏ (pᵢ − 1) pᵢ^(eᵢ − 1). Every pᵢ − 1
divides K, so the only primes worth trying are d + 1 for the divisors d
of K. K ≤ 2·10⁹ has at most 1536 divisors; each d + 1 is tested with
Miller–Rabin on the bases 2, 3, 5, 7, which is exact below 3.2·10⁹.

A memoised search takes the candidate primes in increasing order:
least(rest, i) is the smallest product of powers of primes from the i-th
on with totient rest. For each prime p from i on with (p − 1) | rest it
tries p¹, p², … while the powers still divide what is left, recurses on
the rest with the later primes, and keeps the smallest product. Every
state is a divisor of K and a prime index, and the answer is
least(K, 0). For D divisors and P candidate primes that is at most
`O(D · P²)` steps, far fewer in practice.

Pitfalls:

- K = 1 gives N = 1: with one teacher and one lab, the only student is
  admitted (test 03);
- odd K above 1 is never a totient (test 02), and some even ones are not
  either, 14 being the smallest (test 08);
- the answer may exceed 2³¹: φ(2 500 015 625) = 2·10⁹ (test 06).

The answers match the smallest N found by a totient sieve for every K up
to 300 and every seventh K up to 3000, and an independent accepted
implementation on large K.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1673_number_theory.cpp](1673_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(D P^2) | AC | 0.062 s | 1848 KB |
| [1673_number_theory.go](1673_number_theory.go) | Go 1.14 x64 | number_theory | O(D P^2) | AC | 0.078 s | 5620 KB |
| [1673_number_theory.java](1673_number_theory.java) | Java 1.8 | number_theory | O(D P^2) | AC | 0.203 s | 8080 KB |
| [1673_number_theory.py](1673_number_theory.py) | Python 3.12 x64 | number_theory | O(D P^2) | AC | 0.375 s | 5048 KB |
| [1673_number_theory.rs](1673_number_theory.rs) | Rust 1.75 x64 | number_theory | O(D P^2) | AC | 0.046 s | 3292 KB |
