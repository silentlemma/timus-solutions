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

`1049_number_theory_optimized.java` (Java 1.8): 59 real-process fixtures, including all 14 repository cases; 11007 additional independent whole-main probes.

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

`1049_number_theory_optimized.java`. Store the ten values as residual factors. For each trial divisor, remove all its powers from all ten residuals before multiplying the finalized exponent+1 modulo ten. Recompute the largest remaining residual during that same pass; once the next divisor squared exceeds it, every residual above one is prime and equal residuals are grouped. Already removed smaller primes make composite trial divisors harmless. If the product modulo ten becomes zero after a complete divisor pass, later independent factors cannot change it, so factorization can stop. This is safe only after collecting the full exponent across all inputs. No 10001-entry exponent table is allocated. For C=10 and initial maximum V≤10000: O(C sqrt(V)+C²) time and O(C) state, with fewer passes as values shrink. Tiny input is parsed directly, and the two answer bytes are written and flushed normally. The exact source passed 59 process fixtures and 11007 independent whole-main probes, including all 10000 single-value divisor counts and repeated-prime boundaries. Preserve the teaching factorization and other languages.

Exact-source Java 1.8 Accepted #11328052: 0.062 s / 316 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/77, memory 1/77. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. Both metrics rank first, so the separate language target also passes; no asterisk. The previously documented optimized run #11308799 was 0.109 s / 368 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1049_number_theory_optimized.java`: 0.062 s / 316 KB; retained teaching base `1049_number_theory.java`: 0.14 s / 3880 KB.

`1049_number_theory_optimized.py`. Keep exact prime exponents and product(e+1) modulo ten. Extract the exponent of two using the lowest set bit: (value & −value).bit_length()−1, then shift it away. Strip threes and use the 6k±1 trial wheel for the remainder; a final value above one is prime. A local dictionary avoids module-global working variables. Write the two answer bytes directly through an unbuffered file, without imports or explicit early exit. C=10 values, V≤10000: O(C sqrt(V)) trial work and O(C log V) prime records. New CPython uses 572 KB versus the historical PyPy 296 KB; preserve the paired runtime measurements and the readable factorization.

Exact-source Python 3.12 x64 Accepted #11327877: 0.062 s / 572 KB. Saved 2026-11-20 compiler-cohort ranks, time then memory: 1/70; 34/70. Strict admission uses time only below 1024 KB: top ten or top 15%, ties share rank and percentage cutoff rounds up. An asterisk remains for the separate first-place-in-both language target. The preserved previous variant has its own paired receipt #11309728 (PyPy 3.10 x64): 0.109 s / 296 KB; do not mix measurements or runtimes. All teaching sources remain unchanged.

- `1049_number_theory_optimized.py`: 0.062 s / 572 KB; retained teaching base `1049_number_theory.py`: 0.078 s / 456 KB.

The divisor formula is unchanged: factor each of the ten values, add exponents of equal primes, and multiply exponent+1 modulo ten. Remove powers of two together, then test odd factors only; a remaining value greater than one is prime. Go uses byte exponents and a list of touched primes; Java instead keeps ten residual values and one shared factor scan, as described above. The largest exponent is 10*floor(log2(10000))=130, which fits Go uint8; Java accumulates it in int. Six distinct primes already have product 30030, so at most five are contributed by one input. The Go arrays indexed through 10000 cost O(V) initialization/storage; its ten trial factorizations cost O(C sqrt(V)). Python keeps a small exponent dictionary and native bit operations; its memory/runtime tradeoff is measured separately.

- `1049_number_theory_optimized.go`: 0.015 s / 308 KB; base `1049_number_theory.go`: 0.031 s / 1108 KB; relative change: time -51.6%, memory -72.2%.

`1049_number_theory_optimized.rs`. Factor the ten numbers as they arrive and accumulate prime exponents in a fixed byte array. Each exponent is at most 130 because a value is at most 10000, so a byte suffices. Multiply exponent+1 modulo ten over the array. Factoring costs O(10√M) and the final array scan O(M), with M=10000; storage is M+1 bytes plus constant state. Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1049_number_theory.rs`: time 0.015 s → 0.015 s; memory 416 KB → 52 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1049_number_theory_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [1049_number_theory_optimized.go](1049_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(C sqrt(V)+V) time; O(V) space | AC | 0.015 s | 308 KB | 11328262 |
| [1049_number_theory_optimized.java](1049_number_theory_optimized.java) | Java 1.8 | number_theory | O(C sqrt(V)+C^2) time; O(C) space | AC | 0.062 s | 316 KB | 11328052 |
| [1049_number_theory_optimized.py](1049_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(C sqrt(V)) time; O(C log V) prime records | AC | 0.062 s | 572 KB | 11327877 |
| [1049_number_theory_optimized.rs](1049_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(10√M+M), M=10000 | AC | 0.015 s | 52 KB | 11325082 |
