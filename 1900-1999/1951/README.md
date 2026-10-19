# 1951. Counting Compatible Complex Roots

[Timus 1951](https://acm.timus.ru/problem.aspx?space=1&num=1951) · difficulty 1789 · number_theory

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Olga Soboleva).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count complex numbers x satisfying both xⁿ=A=a+bi and xᵐ=C=c+di,
where i²=−1. All four coefficients are integers, both right-hand sides
are nonzero, and the exponents are positive. Limits: 1 second, 64 MB.

## Input

First line: a,b,n. Second line: c,d,m.
−10¹⁸≤a,b,c,d≤10¹⁸, including the endpoints; 1≤n,m≤100.
At least one of a,b and at least one of c,d is nonzero.

## Output

One integer, the number of common complex roots.

## Checking

Outputs are compared token by token.

## Examples

```
0 1 2
1 0 2
```

```
0
```

```
1 0 2
1 0 4
```

```
2
```

## Solution

Let g=gcd(n,m), p=n/g, q=m/g, so gcd(p,q)=1. The answer is g if
A^q=C^p and zero otherwise. Necessity follows by raising the two equations
to q and p. For sufficiency choose integers u,v with up+vq=1 and set
Y=A^u C^v; negative powers exist because A,C are nonzero. The compatibility
identity gives Y^p=A and Y^q=C. Every solution of x^g=Y solves both original
equations, and every common root obeys x^g=A^u C^v. A nonzero complex Y
has exactly g distinct g-th roots, proving the count.

Compare the two Gaussian-integer powers exactly by modular multiplication.
Sieve primes up to L=10000 and take the first K=510 at least 5000. There
are 560 primes in this interval; the selected list starts at 5003 and ends
at 9521. Reduce both coordinates, use binary exponentiation, and compare
both output coordinates for each modulus. Any mismatch means zero roots.
If all match, return g.

This comparison is deterministic. Each coordinate of Z^e has magnitude
at most (|Re Z|+|Im Z|)^e. Here each input sum is at most 2·10¹⁸<2⁶¹,
and p,q≤100. Therefore either coordinate difference D between A^q and C^p
satisfies |D|<2·(2·10¹⁸)^100<2⁶¹⁰¹. Each chosen prime exceeds
4096=2¹², so their product P>2^(510·12)=2⁶¹²⁰>|D|. Matching residues
make every distinct prime divide D, hence P divides D. The only such
integer with |D|<P is zero. Apply this to both coordinates. This is an
exact bounded-integer argument, not a collision probability estimate.

Complex multiplication modulo a prime is the pair operation
(r₁r₂−i₁i₂, r₁i₂+i₁r₂), reducing each result. It is a ring homomorphism;
the Gaussian residue ring need not be a field, because no division or
modular inverse is used.

O(L log log L + K log E) time and O(L) space, where E=max(n,m), L=10000
and K=510. Build the sieve once. With the fixed L,K from the input bounds,
the comparison takes O(log E) time and fixed auxiliary storage.

Reduce exponents by g: Aᵐ=Cⁿ alone can hold with no common root. Both
coordinates matter, including phase and negative values. Floating magnitudes
or angles cannot prove equality. A handful of primes is insufficient;
the full product bound is the correctness argument. Do not assume each
Gaussian residue ring is a field or forget the nonzero input guarantee.

## Language notes

Read coefficients as signed 64-bit integers in native languages. Normalize
negative remainders into 0..prime−1 before any multiplication. The normalized
products have absolute intermediate values below 2·9999²<2³¹−1; the native
versions still use 64 bits throughout. Never multiply raw 10¹⁸ coefficients.
All versions use only the standard library. Python/C++/Go/Java cache the
moduli once; Rust builds one list and passes it into the comparison.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1951_number_theory.cpp](1951_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(n,m)) | AC | 0.015 s | 412 KB |
| [1951_number_theory.go](1951_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(n,m)) | AC | 0.046 s | 1096 KB |
| [1951_number_theory.java](1951_number_theory.java) | Java 1.8 | number_theory | O(log max(n,m)) | AC | 0.156 s | 708 KB |
| [1951_number_theory.py](1951_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(n,m)) | AC | 0.093 s | 688 KB |
| [1951_number_theory.rs](1951_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(n,m)) | AC | 0.046 s | 244 KB |
