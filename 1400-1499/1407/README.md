# 1407. One-two, One-two

[Timus 1407](https://acm.timus.ru/problem.aspx?space=1&num=1407) · difficulty 388 · constructive

Original problem by Sergey Pupyrev, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For 1 ≤ N ≤ 100, print a number of at most 10 000 digits, all 1 or 2, that
is divisible by 2ᴺ, or "No solution" if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

Such a number; any one is accepted.

## Checking

The checker accepts any number of 1 to 10000 digits, all 1 or 2, whose remainder modulo `2^N` is zero. Extra output is rejected.

## Examples

### Example 1

Input:

```
2
```

Output:

```
12
```

## Solution

There is always one with exactly N digits, built from the right. Let aₖ
have k digits 1 and 2 and be divisible by 2ᵏ; put the digit d in front:
d·10ᵏ + aₖ = 2ᵏ·(d·5ᵏ + aₖ / 2ᵏ). As 5ᵏ is odd, exactly one of d = 1 and
d = 2 makes the bracket even, which gives aₖ₊₁ divisible by 2ᵏ⁺¹. Start
from nothing and repeat N times. `O(N²)` in Go/Java, `O(N³)` in Python.

Only the lowest N + 1 bits decide the choice, so C++ and Rust keep the
number in 128 bits and let the sums wrap around; Go and Java use big
integers and look at the lowest set bit.

Pitfalls:

- the answer is never "No solution";
- 2¹⁰⁰ is far past 64 bits (tests 07 to 09).

Every N from 1 to 100 was checked: the number has N digits 1 and 2 and
2ᴺ divides it. The tests are judged by exact comparison, as the N-digit
answer is unique.

## Optimized solutions

`1407_constructive_optimized.java`. Java keeps the same right-to-left constructive rule: after k digits, bit k of the current value chooses digit 2 when zero and digit 1 otherwise. Unlike the teaching BigInteger version, this file stores the current value and power of ten as pairs of long words modulo 2^128. For N<=100 every queried bit is retained; unsigned carry and split-32-bit multiplication by ten implement exact modular arithmetic despite signed Java words. Digits go directly into an N+1 byte answer. For this bounded domain, time O(N), answer storage O(N) and arithmetic state O(1); this does not claim constant-width arithmetic for unbounded N. Teaching sources remain available.

Exact-source Java 1.8 Accepted #11327478: 0.093 s / 312 KB. Saved 2026-11-20 compiler-cohort comparison: time 5/44, memory 1/44. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11324811 was 0.125 s / 524 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1407_constructive_optimized.java`: 0.093 s / 312 KB; retained teaching base `1407_constructive.java`: 0.109 s / 1668 KB.

`1407_constructive_optimized.py`. Keep constructing digits from least significant to most significant. After k positions the value is divisible by 2^k; bit k decides between digit 1 and 2 because 10^k/2^k is odd. This removes the two trial remainder operations. Store the answer in a bytearray and reverse once. Integers grow to O(n) bits, so the loop has O(n²) bit work and O(n) bit/digit storage; this is not a fixed-word linear-time claim. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `1407_constructive.py`: time 0.078 s → 0.125 s; memory 416 KB → 244 KB.

Go and Rust build the answer from right to left, keeping the partial value and the next power of ten modulo 2¹²⁸. After k digits the lowest k bits are zero, so bit k decides whether the next digit is one or two. Only the lowest N ≤ 100 bits matter. Go implements the 128-bit arithmetic with two 64-bit words and Rust uses wrapping u128 operations. Go reads the exponent directly from a small reusable byte buffer and writes the constructed digits without string conversion.

The accepted Go 1.14 x64 run takes 0.031 s versus 0.015 s for the base and uses 784 KB versus 1140 KB.

The accepted base implementations [1407_constructive.cpp](1407_constructive.cpp), [1407_constructive.java](1407_constructive.java), [1407_constructive.py](1407_constructive.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1407_constructive_optimized.py`: time place 22/27, memory place 1/27 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1407_constructive.cpp](1407_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 188 KB | 11286054 |
| [1407_constructive.go](1407_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.015 s | 1140 KB | 11286055 |
| [1407_constructive.java](1407_constructive.java) \* | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 1668 KB | 11286057 |
| [1407_constructive.py](1407_constructive.py) \* | Python 3.12 x64 | constructive | O(N^3) | AC | 0.078 s | 416 KB | 11286056 |
| [1407_constructive.rs](1407_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 216 KB | 11286058 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1407_constructive_optimized.go](1407_constructive_optimized.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 784 KB | 11311119 |
| [1407_constructive_optimized.rs](1407_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 188 KB | 11310807 |
| [1407_constructive_optimized.java](1407_constructive_optimized.java) | Java 1.8 | constructive | O(N) time; O(N) answer space | AC | 0.093 s | 312 KB | 11327478 |
| [1407_constructive_optimized.py](1407_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(n²) bit work; O(n) bits | AC | 0.125 s | 244 KB | 11325484 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
