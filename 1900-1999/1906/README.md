# 1906. Recovering a Modular Recurrence

[Timus 1906](https://acm.timus.ru/problem.aspx?space=1&num=1906) · difficulty 6173 · number_theory

Original problem by Denis Dublennykh, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given n observations a₀,…,aₙ₋₁, recover the longest initial segment generated
by repeatedly multiplying by one integer k modulo one positive integer P.
Every retained observation must be a remainder: aᵢ < P, and
aᵢ₊₁ = k·aᵢ mod P. Limits: 1 second, 64 MB.

## Input

First n, with 1 ≤ n ≤ 10 000, then n integers 0 ≤ aᵢ ≤ 10⁹.
Whitespace and line breaks do not change their meaning.

## Output

Print L, P and k: the maximum possible prefix length and any parameters
producing that prefix, with 1 ≤ P ≤ 2·10¹⁸ and 0 ≤ k ≤ 2·10¹⁸.
The multiplier need not be smaller than P.

## Checking

The constructive checker compares L with the stored optimum, checks
all bounds, aᵢ < P and every recurrence equation using exact integers.
Different valid P and k are accepted, including noncanonical multipliers.

## Examples

```
5
1 2 4 8 0
```

```
5 16 2
```

```
3
4 2 1
```

```
3 5 3
```

## Solution

Each adjacent pair contributes a congruence aᵢ·k ≡ aᵢ₊₁ (mod P).
Maintain an equivalent system consisting of P dividing G and
d·k ≡ e (mod P), where d > 0. G = 0 imposes no restriction on P.
Initially d = a₀, e = a₁ and G = 0.

To add the row (a,b), find g = gcd(d,a) and integers x,y with xd+ya=g.
Replace the pivot and new row by (g,xe+yb) and
(0,(d/g)b−(a/g)e). This integer row transformation has determinant one,
so it is reversible modulo every P. Update d to g, e to xe+yb,
and G to gcd(G,(d_old/g)b−(a/g)e_old). When G > 0, reduce e modulo G.
If a is divisible by d, use x=1,y=0 directly. The row (0,0) changes
nothing; (0,b) with b>0 is impossible because P must exceed b.

For G>0, a divisor P of G permits a multiplier exactly when gcd(d,P)
divides e. We need the largest such divisor, without factoring G.
If gcd(d,G) divides e, take G. Otherwise set
U=gcd(G,e), Q=G/U and D=d/gcd(d,e). Repeatedly divide Q by gcd(Q,D)
until the gcd becomes one; the largest admissible modulus is UQ.

Why? For each prime p, if its exponent in e is at least its exponent
in d, every copy of p in G is allowed and p does not occur in D.
Otherwise P may retain at most the exponent in e. U already contains
that permitted power, and the loop removes all excess copies from Q.
Thus every admissible P divides UQ, and UQ itself is admissible.

A prefix is feasible exactly when this largest modulus exceeds its
largest observation. If G=0, choose P=d·10⁹+1: it exceeds all observations
and is coprime to d. Accept rows one at a time and stop at the first
infeasible one, preserving the previous state. Every longer prefix
contains the failed prefix, so stopping gives the maximum L.

For the final modulus, set h=gcd(d,P) and q=P/h. If q=1 take k=0;
otherwise k=(e/h)·inverse(d/h modulo q) mod q. This solves the pivot
congruence, hence all retained original rows. If a₀=0, take the initial
run of zeros with P=1,k=0. A lone positive observation uses P=a₀+1,k=0.

While G=0, proportional rows imply 0≤e≤10⁹. The first nonzero G is
at most 10¹⁸; subsequent gcd operations only decrease it. Therefore
the constructed P≤10¹⁸+1 and k<P satisfy the output bounds.
For example, 12,2,9 requires stripping excess factors: G=52, d=2,e=9,
and the largest valid modulus is 13, with multiplier 11.

One pass suffices. A conservative Euclidean-arithmetic bound is
O(n log² B), B=2·10¹⁸, with O(n) input storage and O(1) additional state.
Neither prime factorization nor binary search over prefix lengths is needed.

## Language notes

Stored values fit signed 64 bits, but intermediate determinants can
approach 10²⁷ and the final modular-inverse product can approach 10³⁶.
C++ and Rust use signed 128-bit arithmetic. Go uses math/big for wide
products and inverses; Java 8 uses BigInteger. Python 3.12 uses exact
integers. Signed remainders must be normalized before storing e.
Composite moduli and decreasing sequences must both be supported.

The answers agree with exhaustive search over small moduli and with
enumerating the divisors of the first 2 × 2 minors on 6441 cases;
another 10 000 cases check the divisor step alone. The checker accepts
four valid outputs and rejects 15 invalid ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1906_number_theory.cpp](1906_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log^2 B) | AC | 0.015 s | 524 KB |
| [1906_number_theory.go](1906_number_theory.go) | Go 1.14 x64 | number_theory | O(n log^2 B) | AC | 0.046 s | 4044 KB |
| [1906_number_theory.java](1906_number_theory.java) | Java 1.8 | number_theory | O(n log^2 B) | AC | 0.109 s | 5296 KB |
| [1906_number_theory.py](1906_number_theory.py) | Python 3.12 x64 | number_theory | O(n log^2 B) | AC | 0.093 s | 1888 KB |
| [1906_number_theory.rs](1906_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log^2 B) | AC | 0.046 s | 628 KB |
