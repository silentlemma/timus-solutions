# 1141. Decrypting small RSA messages by factoring the modulus

[Timus 1141](https://acm.timus.ru/problem.aspx?space=1&num=1141) · difficulty 363 · number_theory

Original problem by Mikhail Medvedev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For up to `K ≤ 2000` queries `e, n, c ≤ 32000`, where `n = p·q` for two
distinct odd primes and `e < (p − 1)(q − 1)` is coprime to `(p − 1)(q − 1)`,
find the message `m` with `m^e ≡ c (mod n)`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K`, then `K` lines with `e`, `n` and `c`.

## Output

One `m` per line.

## Examples

### Example 1

Input:

```
3
9 187 129
11 221 56
7 391 204
```

Output:

```
7
23
17
```

## Solution

This is RSA with a tiny modulus, so it can simply be broken. Trial
division by odd numbers from 3 finds `p` within `√n < 179` steps, and then
`φ = (p − 1)(q − 1)`. Since `e` is coprime to `φ`, it has an inverse
`d` modulo `φ`, found by the extended Euclidean algorithm. Then
`c^d ≡ m^(e·d) ≡ m (mod n)`: modulo each prime `r` dividing `n`,
`e·d = 1 + t·φ` is `1` plus a multiple of `r − 1`, so Fermat's little
theorem gives `m^(e·d) ≡ m (mod r)`, also when `r` divides `m`, and the
Chinese remainder theorem joins the two primes. So `m = c^d mod n`, found
by fast exponentiation. `O(√n + log n)` per query.

Pitfalls:

- `c` can be larger than `n`; the exponentiation reduces it first;
- the message may share a factor with `n`; decryption still works because
  `n` has no square factors;
- the inverse from the extended Euclidean algorithm may come out
  negative, so it is brought into `[0, φ)`;
- all products stay below `32000²`, which fits in 64-bit integers.

The answers were compared on every test with trying every `m` from `0` to
`n − 1`, which also confirmed that the answer is unique.

## Optimized solutions

Go and Rust sieve the odd primes up to 178 once and use only those primes to factor each modulus n ≤ 32000. They then compute the inverse exponent with extended Euclid and decrypt by binary exponentiation. Go uses fixed byte buffers and writes decimal digits directly; Rust processes input and output incrementally. The prime table uses fixed-size arrays.

The accepted base implementations [1141_number_theory.cpp](1141_number_theory.cpp), [1141_number_theory.java](1141_number_theory.java), [1141_number_theory.py](1141_number_theory.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- All languages factor, invert and exponentiate the same way; Python uses
  the built-in `pow(e, -1, phi)` for the inverse.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1141_number_theory.cpp](1141_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 216 KB | 11279444 |
| [1141_number_theory.go](1141_number_theory.go) | Go 1.14 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 1156 KB | 11279445 |
| [1141_number_theory.java](1141_number_theory.java) \* | Java 1.8 | number_theory | O(K (√n + log n)) | AC | 0.046 s | 596 KB | 11279448 |
| [1141_number_theory.py](1141_number_theory.py) \* | Python 3.12 x64 | number_theory | O(K (√n + log n)) | AC | 0.046 s | 992 KB | 11279446 |
| [1141_number_theory.rs](1141_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 352 KB | 11279449 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1141_number_theory_optimized.go](1141_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(K (√n + log n)) | AC | 0.015 s | 772 KB | 11311153 |
| [1141_number_theory_optimized.rs](1141_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 200 KB | 11311025 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
