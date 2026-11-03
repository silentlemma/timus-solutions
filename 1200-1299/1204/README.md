# 1204. Idempotents modulo a product of two primes

[Timus 1204](https://acm.timus.ru/problem.aspx?space=1&num=1204) · difficulty 230 · number_theory

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

## Checking

Compare output tokens; extra whitespace does not matter.

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

## Optimized solutions

CRT reconstruction is unchanged. Java uses a primitive prime array, integer trial divisions and bounded ASCII output instead of boxed primes and per-answer strings. Python uses a prime-product tree: a GCD tests an entire block, and nontrivial factors are routed down to smaller blocks. At a leaf, ordinary trial division finishes the split. Every returned divisor is verified exactly; there is no probabilistic factorization assumption. Product-tree construction and big-integer GCD/multiplication costs must be counted, rather than treating each large-number operation as constant time.

- `1204_number_theory_optimized.java`: 0.109 s / 484 KB; base `1204_number_theory.java`: 0.171 s / 1088 KB; relative change: time -36.3%, memory -55.5%.
- `1204_number_theory_trees.py`: 0.093 s / 1084 KB; base `1204_number_theory.py`: 0.312 s / 1016 KB; relative change: time -70.2%, memory +6.7%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1204_number_theory.cpp`; covering source `1204_number_theory.cpp`; time/memory places 3/7, other-author entries 75/75.

- Go: preferred teaching base `1204_number_theory.go`; covering source `1204_number_theory.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1204_number_theory.java`; covering source `1204_number_theory_optimized.java`; time/memory places 2/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1204_number_theory.py`; covering source `1204_number_theory_trees.py`; time/memory places 1/2, other-author entries 13/13.

- Rust: preferred teaching base `1204_number_theory.rs`; covering source `1204_number_theory.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1204_number_theory.cpp](1204_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 228 KB | 11283581 |
| [1204_number_theory.go](1204_number_theory.go) | Go 1.14 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 1320 KB | 11283582 |
| [1204_number_theory.java](1204_number_theory.java) | Java 1.8 | number_theory | O(k·π(√n)) | AC | 0.171 s | 1088 KB | 11283585 |
| [1204_number_theory.py](1204_number_theory.py) | Python 3.12 x64 | number_theory | O(k·π(√n)) | AC | 0.312 s | 1016 KB | 11283583 |
| [1204_number_theory.rs](1204_number_theory.rs) | Rust 1.75 x64 | number_theory | O(k·π(√n)) | AC | 0.015 s | 268 KB | 11283586 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1204_number_theory_optimized.java](1204_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(K sqrt N) | AC | 0.109 s | 484 KB | 11309381 |
| [1204_number_theory_trees.py](1204_number_theory_trees.py) \* | Python 3.12 x64 | number_theory, trees | O(log P) bigint gcds per query | AC | 0.093 s | 1084 KB | 11309380 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
