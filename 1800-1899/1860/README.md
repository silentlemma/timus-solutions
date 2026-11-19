# 1860. Fiborial

[Timus 1860](https://acm.timus.ru/problem.aspx?space=1&num=1860) · difficulty 469 · number_theory

Original problem by Denis Dublennykh (idea by Grigoriy Nazarov), from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Let F₀ = F₁ = 1 and Fᵢ = i·Fᵢ₋₁·Fᵢ₋₂. Find the number of divisors of
Fₙ modulo 10⁹ + 7.

## Input

n (1 ≤ n ≤ 10⁶).

## Output

The number of divisors of Fₙ modulo 10⁹ + 7.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
3
```

Output:

```
4
```

## Solution

Each step multiplies in i once and repeats the two previous products, so
the factor k enters Fₙ exactly fib(n − k + 1) times, with fib(1) =
fib(2) = 1: it appears once in F_k, once in F_{k+1}, twice in F_{k+2},
and so on by the Fibonacci rule. Hence Fₙ = Π k^fib(n−k+1) over
k = 1 … n.

The number of divisors is Π (e_p + 1) over the primes p, where e_p is
the exponent of p in Fₙ. A number k contributes v_p(k) times its weight
fib(n − k + 1), and v_p(k) counts how many of p, p², p³, … divide k, so
e_p is the sum of the weights of all multiples of p, of p², and so on.
Only e_p modulo 10⁹ + 7 matters, so the weights are kept reduced too.
Going over the multiples of every prime power takes about
n·ln ln n steps; the Python solution sums every progression with one
slice. `O(n log log n)`.

In the example F₃ = 3·F₂·F₁ = 3·2·1 = 6, which has the divisors 1, 2, 3
and 6.

Pitfalls:

- the exponents are huge, but the answer only needs them modulo
  10⁹ + 7;
- a prime power past n must stop the loop before it overflows;
- the Python solution runs on PyPy.

The answers agree with a direct factorisation of Fₙ for n up to 14 and
with an independent accepted implementation up to 10⁶.

## Optimized solutions

`1860_number_theory_optimized.java`. Keep the prime-exponent divisor formula modulo 10^9+7. Store Fibonacci residues in int[] rather than long[]: even their unreduced pair sum is below 2^31. Look up each weight as fib[n-multiple+1], eliminating the separate long[] weight copy. Keep accumulated prime exponents and the answer products in long; reduce exponents after each prime-power pass. Sieve primes and sum contributions over their powers as before. Time O(n log log n), storage O(n), with substantially fewer bytes per index. Input is one numeric byte token; n=1 still gives one divisor.

Compared with `1860_number_theory.java`: time 0.187 s → 0.125 s; memory 18 412 KB → 8 368 KB.

New C++, Go and Rust retain the prime-power exponent sum, but store only one uint32 Fibonacci array. Read weight(k) directly at fib[n−k+1], avoiding the duplicate 64-bit weight array. Two reduced terms sum to less than 2·MOD, so conditional subtraction replaces Fibonacci modulo. An odd-only bit sieve uses roughly n/16 bytes; handle prime2 separately. For each prime, the number of summed terms is at most n, so their unreduced uint64 sum is below n·MOD≤10¹⁵. Reduce once per prime; the final modular product also fits uint64. Check power>n/p before multiplying. Time stays O(n log log n), storage O(n), with about4n bytes of weights instead of two8n arrays. All bases remain; Java/Python reuse admitted bases.

The accepted base implementations [1860_number_theory.java](1860_number_theory.java), [1860_number_theory.py](1860_number_theory.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`1860_number_theory_optimized.java`: time place 3/16, memory place 5/16 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1860_number_theory.cpp](1860_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log log n) | AC | 0.031 s | 15492 KB | 11325590 |
| [1860_number_theory.go](1860_number_theory.go) | Go 1.14 x64 | number_theory | O(n log log n) | AC | 0.046 s | 18860 KB | 11290853 |
| [1860_number_theory.java](1860_number_theory.java) \* | Java 1.8 | number_theory | O(n log log n) | AC | 0.187 s | 18412 KB | 11325560 |
| [1860_number_theory.py](1860_number_theory.py) \* | PyPy 3.10 x64 | number_theory | O(n log log n) | AC | 0.171 s | 34140 KB | 11325600 |
| [1860_number_theory.rs](1860_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log log n) | AC | 0.046 s | 16684 KB | 11325614 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1860_number_theory_optimized.cpp](1860_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(n log log n) | AC | 0.031 s | 3700 KB | 11315295 |
| [1860_number_theory_optimized.go](1860_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(n log log n) | AC | 0.031 s | 4800 KB | 11315297 |
| [1860_number_theory_optimized.rs](1860_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(n log log n) | AC | 0.046 s | 3888 KB | 11315298 |
| [1860_number_theory_optimized.java](1860_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(n log log n) | AC | 0.125 s | 8368 KB | 11325040 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
