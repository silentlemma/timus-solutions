# 1049. The last digit of the number of divisors of a product

[Timus 1049](https://acm.timus.ru/problem.aspx?space=1&num=1049) · difficulty 249 · number_theory

Original problem by Stanislav Vasiliev, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Ten integers `a1 … a10` are given, each from 1 to 10000. Find the last
digit of the number of positive divisors of the product `a1 · … · a10`.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Ten integers, one per line.

## Output

One digit: the last digit of the number of divisors.

## Checking

Compare the exact answer tokens; whitespace formatting is immaterial.

- `1049_number_theory_optimized.go` (Go 1.14 x64): 14 repository cases; 14 additional source-bound comparisons.

- `1049_number_theory_optimized.java` (Java 1.8): 14 repository cases; 172 additional source-bound comparisons.

- `1049_number_theory_optimized.py` (PyPy 3.10 x64): 14 repository cases.

## Examples

### Example 1

Input:

```
1
2
6
1
3
1
1
1
1
1
```

Output:

```
9
```

### Example 2

Input:

```
1
1
1
1
1
1
1
1
1
1
```

Output:

```
1
```

## Solution

If `P = p1^e1 · p2^e2 · … · pk^ek`, a divisor of `P` chooses each
exponent independently from `0` to `ei`, so `P` has
`(e1 + 1)(e2 + 1)…(ek + 1)` divisors.

The product itself can have 40 digits, but it is never needed: factor
each number by trial division up to its square root (at most 100 steps),
add the exponents of equal primes, and multiply the `(e + 1)` modulo 10.
`O(10 · √10000)`.

Pitfalls:

- the exponents must be added over all ten numbers before the `+ 1`:
  `2 · 2` has 3 divisors, not `2 · 2`;
- a prime factor larger than the square root remains after the trial
  division and still counts;
- the last digit may be 0 (48 = `2^4 · 3` has 10 divisors).

## Optimized solutions

The divisor formula is unchanged: factor each of the ten values, add exponents of equal primes, and multiply exponent+1 modulo ten. Remove powers of two together, then test odd factors only; a remaining value greater than one is prime. Go uses byte exponents and a list of touched primes; Java uses unsigned 16-bit char exponents rather than boxed maps. The largest exponent is 10*floor(log2(10000))=130, which fits Go uint8 but not signed Java byte. Six distinct primes already have product 30030, so at most five are contributed by one input. Arrays indexed through 10000 cost O(V) initialization/storage; the ten trial factorizations cost O(C sqrt(V)). Python keeps a small exponent dictionary and native bit operations; its memory/runtime tradeoff is measured separately.

- `1049_number_theory_optimized.go`: 0.015 s / 292 KB; base `1049_number_theory.go`: 0.031 s / 1108 KB; relative change: time -51.6%, memory -73.6%.
- `1049_number_theory_optimized.java`: 0.109 s / 368 KB; base `1049_number_theory.java`: 0.140 s / 3880 KB; relative change: time -22.1%, memory -90.5%.
- `1049_number_theory_optimized.py`: 0.109 s / 296 KB; base `1049_number_theory.py`: 0.078 s / 456 KB; relative change: time +39.7%, memory -35.1%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1049_number_theory.cpp`; covering source `1049_number_theory.cpp`; time/memory places 1/1, other-author entries 121/121.

- Go: preferred teaching base `1049_number_theory.go`; covering source `1049_number_theory_optimized.go`; time/memory places 1/1, other-author entries 2/2.

- Java: preferred teaching base `1049_number_theory.java`; covering source `1049_number_theory_optimized.java`; time/memory places 3/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `1049_number_theory.py`; covering source `1049_number_theory_optimized.py`; time/memory places 44/1, other-author entries 54/54.

- Rust: preferred teaching base `1049_number_theory.rs`; covering source `1049_number_theory.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1049_number_theory.cpp](1049_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 184 KB | 11278665 |
| [1049_number_theory.go](1049_number_theory.go) | Go 1.14 x64 | number_theory | O(10 · √10000) | AC | 0.031 s | 1108 KB | 11278667 |
| [1049_number_theory.java](1049_number_theory.java) | Java 1.8 | number_theory | O(10 · √10000) | AC | 0.140 s | 3880 KB | 11278675 |
| [1049_number_theory.py](1049_number_theory.py) | Python 3.12 x64 | number_theory | O(10 · √10000) | AC | 0.078 s | 456 KB | 11278673 |
| [1049_number_theory.rs](1049_number_theory.rs) | Rust 1.75 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 416 KB | 11278679 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1049_number_theory_optimized.go](1049_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(C sqrt(V)+V) time; O(V) space | AC | 0.015 s | 292 KB | 11309757 |
| [1049_number_theory_optimized.java](1049_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(C sqrt(V)+V) time; O(V) space | AC | 0.109 s | 368 KB | 11308799 |
| [1049_number_theory_optimized.py](1049_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(C sqrt(V)) time; O(C log V) prime records | AC | 0.109 s | 296 KB | 11309728 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
