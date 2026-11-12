# 1343. Fairy Tale

[Timus 1343](https://acm.timus.ru/problem.aspx?space=1&num=1343) · difficulty 417 · number_theory

Original problem by Pavel Atnashev, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The first k of 12 digits are given, 0 ≤ k ≤ 12. Print any 12-digit
number that starts with them and has no divisors other than 1 and
itself. An answer is guaranteed to exist.

Time limit: 1 second. Memory limit: 64 MB.

## Input

k on the first line, the k digits on the second.

## Output

The 12-digit number.

## Checking

The checker accepts any 12 digits that start with the given ones and
make a number with no other divisors.

## Examples

### Example 1

Input:

```
5
64631
```

Output:

```
646310554187
```

## Solution

The preferred teaching version is C++ trial division. Fill the remaining digits with zeros, test 2 separately and then try odd candidates. A candidate is prime exactly when it has no divisor up to its integer square root. Test 2 and 3 first; every larger prime is 6q−1 or 6q+1, so the loop checks these pairs. All products fit 64 bits because N<10¹². For G candidates this is O(G·sqrt(N)) time and O(1) auxiliary space, without modular exponentiation or a prime table. The answer guarantee ensures that a prime is found before leaving the given prefix. Print exactly twelve digits with leading zeros. If all twelve digits are supplied, echo the guaranteed-valid value directly, including 000000000001. This elementary algorithm is retained on C++; the more advanced accepted implementations remain available separately.

## Optimized solutions

Miller–Rabin uses the six bases 2,3,5,7,11,13. After small-prime checks, write N−1=2ˢd with d odd. For each base, compute x=aᵈ mod N; accept that base if x is 1 or N−1, or if one of its next s−1 modular squares is N−1. Otherwise reject the candidate. [Jaeschke’s six-base bound](https://doi.org/10.1090/S0025-5718-1993-1192971-8) is 3474749660383, above every value here, so the test is deterministic in this task. It takes O(G log N) word operations for G candidates. The new Go and Rust sources use bounded I/O; Go multiplies via bits.Mul64/bits.Rem64 and Rust via u128. Java and Python reuse their already-admitted original files. C++ fast coverage shares the elementary [trial-division file](1343_bruteforce.cpp) listed under Simple: its exact Accepted receipt meets the inclusion rule, without a duplicate optimized copy. That measured admission does not claim better asymptotic complexity than Miller–Rabin. Original C++/Go/Rust Miller–Rabin bases are retained under Other Accepted approaches.

The accepted base implementations [1343_number_theory.java](1343_number_theory.java), [1343_number_theory.py](1343_number_theory.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The elementary base needs no wide modular products. Miller–Rabin C++/Rust use 128-bit products, Go uses math/bits and Java splits a product into 20-bit halves. Python retains its actual accepted CPython interpreter. Original files and their source-bound measurements remain unchanged. Stars apply only to selected fast sources below their language rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1343_bruteforce.cpp](1343_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(G sqrt N) | AC | 0.015 s | 112 KB | 11314926 |

### Other Accepted approaches

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1343_number_theory.cpp](1343_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(G·log N) | AC | 0.015 s | 392 KB | 11285094 |
| [1343_number_theory.go](1343_number_theory.go) | Go 1.14 x64 | number_theory | O(G·log N) | AC | 0.031 s | 1024 KB | 11285096 |
| [1343_number_theory.rs](1343_number_theory.rs) | Rust 1.75 x64 | number_theory | O(G·log N) | AC | 0.046 s | 216 KB | 11285099 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1343_number_theory_optimized.go](1343_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(G log N) | AC | 0.015 s | 312 KB | 11314932 |
| [1343_number_theory.java](1343_number_theory.java) \* | Java 1.8 | number_theory | O(G·log N) | AC | 0.125 s | 1752 KB | 11285098 |
| [1343_number_theory.py](1343_number_theory.py) \* | Python 3.12 x64 | number_theory | O(G·log N) | AC | 0.078 s | 524 KB | 11285097 |
| [1343_number_theory_optimized.rs](1343_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(G log N) | AC | 0.046 s | 56 KB | 11314929 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
