# 1204. Idempotents modulo a product of two primes

[Timus 1204](https://acm.timus.ru/problem.aspx?space=1&num=1204) · difficulty 229 · number_theory

Original problem by Pavel Atnashev, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A number `x` is an idempotent modulo `n` if `x·x ≡ x (mod n)`. For up to
1000 values `n < 10⁹`, each the product of two different primes `p` and
`q`, list all idempotents from `0` to `n − 1` in increasing order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number of tests `k`, then `n` for each test.

## Output

For each test, its idempotents on one line in increasing order.

## Examples

### Example 1

Input:

```
3
6
15
910186311
```

Output:

```
0 1 3 4
0 1 6 10
0 1 303395437 606790875
```

## Solution

`x(x − 1) ≡ 0 (mod pq)` means each of `p` and `q` divides `x` or
`x − 1`, so modulo each prime `x` is 0 or 1. By the Chinese remainder
theorem that gives exactly four idempotents: 0, 1, the number that is 1
modulo `p` and 0 modulo `q`, and the number that is 0 modulo `p` and 1
modulo `q`. The third is `x = q·(q⁻¹ mod p)`, the inverse coming from the
extended Euclidean algorithm, and the fourth is `n + 1 − x`, since the
two add up to 1 modulo both primes.

To split `n`, try the primes up to `√10⁹ < 31623`, found once with a
sieve; the smaller factor is among them. About 3400 divisions per test
at most. `O(k·π(√n))`.

Pitfalls:

- the two nontrivial idempotents must be printed in increasing order,
  and either may be the smaller;
- only the smaller factor has to be found by trial division; the larger
  one, up to `5·10⁸`, is just `n / p`;
- `p` can be as small as 2.

The answers were compared with a separately written solution on 3000
generated products of all three kinds.

## Language notes

- Python takes the inverse with `pow(q, -1, p)`; the other languages use
  the extended Euclidean algorithm.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1204_number_theory.cpp](1204_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 228 KB |
| [1204_number_theory.go](1204_number_theory.go) | Go 1.14 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 1320 KB |
| [1204_number_theory.java](1204_number_theory.java) | Java 1.8 | number_theory | O(k·π(√n)) | AC | 0.171 s | 1088 KB |
| [1204_number_theory.py](1204_number_theory.py) | Python 3.12 x64 | number_theory | O(k·π(√n)) | AC | 0.312 s | 1016 KB |
| [1204_number_theory.rs](1204_number_theory.rs) | Rust 1.75 x64 | number_theory | O(k·π(√n)) | AC | 0.015 s | 268 KB |
