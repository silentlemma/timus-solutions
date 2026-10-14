# 1598. Attack on DSA

[Timus 1598](https://acm.timus.ru/problem.aspx?space=1&num=1598) · difficulty 3852 · math

Original problem prepared by Vladimir Yakovlev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A DSA public key (q, p, g, y) has an N-bit prime q (3 ≤ N ≤ 36), an
L-bit prime p (L ≤ 60) with q dividing p − 1, g of order q modulo p and
y = gˣ mod p for a secret 0 < x < q. Given the key and a hash H, print
any valid signature (r, s): 0 < r, s < q and, with w = s⁻¹, u₁ = H·w and
u₂ = r·w modulo q, ((g^u₁·y^u₂) mod p) mod q = r.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, L, q, p, g, y and H.

## Output

r and s.

## Examples

### Example 1

Input:

```
3 6 5 41 10 16 2
```

Output:

```
3 3
```

## Solution

The hash is fixed, so the usual tricks that forge a signature for some
message do not help: the solution finds the secret key. Since g has
order q, x is the discrete logarithm of y in a group of at most 2³⁶
elements, and the baby-step giant-step method finds it in about
√q ≈ 2.6·10⁵ steps: store gʲ for j < m = ⌈√q⌉ in a hash table, then
multiply y by g⁻ᵐ = g^(q − m) until the value appears in the table; if
it is gʲ after i steps, x = i·m + j.

With x known the signature is made as the statement describes, with
k = 1, 2, … until r = (gᵏ mod p) mod q and s = k⁻¹(H + x·r) mod q are
both nonzero. q is prime, so k⁻¹ = k^(q − 2) mod q. The check then holds:
u₁ + x·u₂ = (H + x·r)·w = k, so g^u₁·y^u₂ = gᵏ. In total
`O(√q)` time and memory.

The tests use a checker that verifies the signature as the statement
does. It accepted the output on keys made exactly as described, with
every size from tiny to N = 36, L = 60.

Pitfalls:

- p has up to 60 bits, so products need 128 bits: C++ and Rust use
  128-bit integers, Go uses bits.Mul64 with bits.Rem64, and Java 8,
  which has neither, multiplies two bits at a time so that every sum
  stays below 2⁶³;
- k = 1 can give r = g mod q = 0 (it does in the example), so k has to
  move on;
- H has N bits and can be larger than q; it is used modulo q.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1598_math.cpp](1598_math.cpp) | G++ 13.2 x64 | math | O(√q) | AC | 0.109 s | 12456 KB |
| [1598_math.go](1598_math.go) | Go 1.14 x64 | math | O(√q) | AC | 0.093 s | 20784 KB |
| [1598_math.java](1598_math.java) | Java 1.8 | math | O(√q) | AC | 0.312 s | 9832 KB |
| [1598_math.py](1598_math.py) | Python 3.12 x64 | math | O(√q) | AC | 0.265 s | 26936 KB |
| [1598_math.rs](1598_math.rs) | Rust 1.75 x64 | math | O(√q) | AC | 0.046 s | 17656 KB |
