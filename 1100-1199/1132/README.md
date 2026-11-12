# 1132. All square roots of a modulo a prime n, for up to 100000 queries

[Timus 1132](https://acm.timus.ru/problem.aspx?space=1&num=1132) · difficulty 545 · number_theory

Original problem by Mikhail Medvedev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For up to `K ≤ 100000` queries `a, n` with a prime `n ≤ 32767` and
`1 ≤ a ≤ 32767` not divisible by `n`, print all `x` from `1` to `n − 1`
with `x² ≡ a (mod n)` in increasing order, or `No root` if there are none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K`, then `K` lines with `a` and `n`.

## Output

One line per query: the roots separated by spaces, or `No root`.

## Examples

### Example 1

Input:

```
5
4 17
3 7
2 7
14 31
10007 20011
```

Output:

```
2 15
No root
3 4
13 18
5382 14629
```

## Solution

Reduce `a` modulo `n`. For `n = 2` the only root is `1`. For an odd prime,
Euler's criterion decides whether a root exists: `a^((n−1)/2)` is `1` for a
quadratic residue and `n − 1` otherwise. If a root `r` exists, the other
one is `n − r`, and they differ because `n` is odd and `a` is not zero.

The root itself comes from the Tonelli–Shanks algorithm. Write
`n − 1 = q·2^s` with odd `q` and take any non-residue `z`. Start with
`r = a^((q+1)/2)`, `t = a^q` and `c = z^q`; then `r² = a·t` always holds.
While `t ≠ 1`, find the least `i` with `t^(2^i) = 1`, set
`b = c^(2^(s−i−1))`, and update `r ← r·b`, `t ← t·b²`, `c ← b²`, `s ← i`.
Each step lowers the order of `t`, so after at most `s` steps `t = 1` and
`r² = a`. The smallest non-residue of each prime is found once and kept.
For `n ≡ 3 (mod 4)` the loop does not run at all and `r = a^((n+1)/4)`.
`O(log² n)` per query.

Pitfalls:

- `a` can be larger than `n`, so reduce it first;
- `n = 2` has a single root, `1`, and Euler's criterion does not apply;
- the two roots are printed smaller first;
- with up to 100000 queries, input and output are buffered.

The answers were compared on every test with a table of all squares
modulo each prime that occurs.

The teaching C++ version sorts the queries by prime and builds one square table for each group. For an odd prime p, the two roots are x and p − x, so testing 1 through floor(p/2) finds the smaller one. Successive squares differ by 2x − 1, so each table entry needs one addition and at most one subtraction of p. A zero entry means the nonzero residue has no root. For p = 2, the two roots coincide and the code prints 1 once. The stored query indices restore input order. Time is O(K log K + Σp), summing over distinct input primes. Space is O(K + P), where P is the largest input prime.

## Optimized solutions

The new C++/Go/Rust versions keep Tonelli–Shanks but specialize p≡3 mod4: compute a^((p+1)/4) and verify the square, avoiding a separate Euler test. For p≡5 mod8 try a^((p+3)/8), multiply by 2^((p−1)/4) if needed and verify again; that correction is cached. For the remaining primes write p−1=q2^s with q odd. A single b=a^((q−1)/2) gives r=ab and t=rb, so r²=at. If the order of t is2^s there is no root; otherwise ordinary Tonelli–Shanks corrections reduce that order. Powers of two in the correction are evaluated by repeated squaring. Cache the initial c=z^q, not the modified loop value, in one uint16 entry per modulus. Products below32767² fit 32-bit unsigned integers. Stream both input and output through fixed buffers (Rust uses C character I/O); do not store all queries or answers. Query work is O(log²P), O(log P) in the special classes, plus a once-per-needed-prime nonresidue search: if Z_p trial bases are inspected, its cost is O((Z_p+1)log p). For K queries and Z = Σ(Z_p+1) over these primes, total time including cache initialization is O(P + K log² P + Z log P). Extra space is O(P) for P=32768 plus fixed buffers. The unchanged simple programs remain; Java/Python reuse admitted bases.

The accepted Rust 1.75 x64 run takes 0.062 s versus 0.015 s for the base and uses 108 KB versus 4068 KB.

The accepted base implementations [1132_number_theory.java](1132_number_theory.java), [1132_number_theory.py](1132_number_theory.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The original files cache a quadratic nonresidue per prime. Optimized C++, Go and Rust cache the starting power or the correction used by their branch. The p≡3 mod4 branch computes the root directly.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1132_number_theory.cpp](1132_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log² n) | AC | 0.203 s | 2196 KB | 11279382 |
| [1132_number_theory.go](1132_number_theory.go) | Go 1.14 x64 | number_theory | O(K log² n) | AC | 0.093 s | 1668 KB | 11279383 |
| [1132_number_theory.java](1132_number_theory.java) \* | Java 1.8 | number_theory | O(K log² n) | AC | 0.281 s | 5908 KB | 11279386 |
| [1132_number_theory.py](1132_number_theory.py) \* | Python 3.12 x64 | number_theory | O(K log² n) | AC | 0.468 s | 19404 KB | 11279385 |
| [1132_number_theory.rs](1132_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log² n) | AC | 0.015 s | 4068 KB | 11279388 |
| [1132_math.cpp](1132_math.cpp) | G++ 13.2 x64 | math | O(K log K + Σp) | AC | 0.171 s | 6056 KB | 11315928 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1132_number_theory_optimized.cpp](1132_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(P + K log² P + Z log P) | AC | 0.031 s | 140 KB | 11315759 |
| [1132_number_theory_optimized.go](1132_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(P + K log² P + Z log P) | AC | 0.015 s | 992 KB | 11315760 |
| [1132_number_theory_optimized.rs](1132_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(P + K log² P + Z log P) | AC | 0.062 s | 108 KB | 11315763 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
