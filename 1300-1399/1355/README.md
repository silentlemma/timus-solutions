# 1355. Bald Spot Revisited

[Timus 1355](https://acm.timus.ru/problem.aspx?space=1&num=1355) · difficulty 212 · number_theory

Original problem by Aleksandr Bikbaev, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Taverns are numbered by positive integers, and from tavern n one may go
only to a tavern whose number is a multiple of n. A walk starts at
tavern a and must end at tavern b, with a mug of ale in every tavern on
the way, a and b included. For each of T ≤ 20 pairs with
1 ≤ a, b ≤ 10⁹, print the largest number of mugs, or 0 if b cannot be
reached.

Time limit: 1 second. Memory limit: 64 MB.

## Input

T, then T lines with a and b.

## Output

T lines with the answers.

## Checking

Exact answer tokens. Each new source has its own full target-runtime checks, independent mathematical comparisons and source-bound Accepted; retained simple versions keep their own metrics.

## Examples

### Example 1

Input:

```
5
30 89
2 16
3 243
1 1
2 2
```

Output:

```
0
4
5
1
1
```

## Solution

Every number on the walk divides the next one, so b is reachable only
when a divides b. Then each step multiplies the number by some factor
greater than 1, and the product of all the factors is q = b / a. To
visit as many taverns as possible, each factor should be a single
prime, so the number of steps is Ω(q), the count of prime factors of q
with repetition. The answer is 1 + Ω(q), counting tavern a itself.

Trial division up to √q ≤ 31 623 finds Ω(q). `O(T · √(b / a))`.

Pitfalls:

- a = b gives one mug, not zero (example);
- b smaller than a, or not a multiple of it, gives 0 (test 04);
- T can be 0, and then no answers are printed (test 02);
- q = 2²⁹ gives the most steps, 30 mugs (test 03).

## Optimized solutions

Trial division remains the teaching version. The faster Python source computes the gcd of the quotient with a fixed product of all primes up to 1000. This square-free gcd identifies the small prime divisors. Divide each of them out of the quotient with its full multiplicity. The remaining factors exceed 1000, so a quotient bounded by 10^9 can contain at most two. A second fixed product covers the primes from 1001 through 31623. A remaining composite must have a factor in that range, while a remaining prime above 10^6 has gcd 1 with the product. Count one or two factors accordingly. The products are generated once from a sieve and stored as hexadecimal constants.

- `1355_number_theory_math.py`: 0.062 s / 584 KB; base `1355_number_theory.py`: 0.109 s / 392 KB; relative change: time -43.1%, memory +49.0%.

## Language notes

The saved snapshots are from 2 and 4 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1355_number_theory.cpp`; covering source `1355_number_theory.cpp`; time/memory places 1/2, other-author entries 61/61.

- Go: preferred teaching base `1355_number_theory.go`; covering source `1355_number_theory.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1355_number_theory.java`; covering source `1355_number_theory.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1355_number_theory.py`; covering source `1355_number_theory_math.py`; time/memory places 1/4, other-author entries 13/13.

- Rust: preferred teaching base `1355_number_theory.rs`; covering source `1355_number_theory.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1355_number_theory.cpp](1355_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 132 KB | 11285268 |
| [1355_number_theory.go](1355_number_theory.go) | Go 1.14 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 1100 KB | 11285270 |
| [1355_number_theory.java](1355_number_theory.java) | Java 1.8 | number_theory | O(T·√(b/a)) | AC | 0.078 s | 448 KB | 11285272 |
| [1355_number_theory.py](1355_number_theory.py) | Python 3.12 x64 | number_theory | O(T·√(b/a)) | AC | 0.109 s | 392 KB | 11285271 |
| [1355_number_theory.rs](1355_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 212 KB | 11285273 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1355_number_theory_math.py](1355_number_theory_math.py) \* | Python 3.12 x64 | number_theory, math | O(T*(P+log Q)) bounded arithmetic, P=1000 | AC | 0.062 s | 584 KB | 11310243 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
