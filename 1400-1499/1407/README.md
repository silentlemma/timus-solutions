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

Historically every N from 1 to 100 was checked for an N-digit divisible construction. Current tests use the semantic checker in Checking: any 1..10000-digit answer of ones/twos divisible by 2^N is valid, including shorter answers such as 112 for N=4. Exact equality with the unique N-digit construction is not required.

## Optimized solutions

`1407_constructive_optimized.java`. Java keeps the same right-to-left constructive rule: after k digits, bit k of the current value chooses digit 2 when zero and digit 1 otherwise. Unlike the teaching BigInteger version, this file stores the current value and power of ten as pairs of long words modulo 2^128. For N<=100 every queried bit is retained; unsigned carry and split-32-bit multiplication by ten implement exact modular arithmetic despite signed Java words. Digits go directly into an N+1 byte answer. For this bounded domain, time O(N), answer storage O(N) and arithmetic state O(1); this does not claim constant-width arithmetic for unbounded N. Teaching sources remain available.

Exact-source Java 1.8 Accepted #11327478: 0.093 s / 312 KB. Saved 2026-11-20 compiler-cohort comparison: time 5/44, memory 1/44. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. Time rank 5/44 passes the shared time-only criterion; the unstarred row is correct, without a separate first-place target. The previously documented optimized run #11324811 was 0.125 s / 524 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1407_constructive_optimized.java`: 0.093 s / 312 KB; retained teaching base `1407_constructive.java`: 0.109 s / 1668 KB.

`1407_constructive_optimized.py`. Keep constructing digits from least significant to most significant. After k positions the value is divisible by 2^k; bit k decides between digit 1 and 2 because 10^k/2^k is odd. This removes the two trial remainder operations. Store the answer in a bytearray and reverse once. Integers grow to O(n) bits, so the loop has O(n²) bit work and O(n) bit/digit storage; this is not a fixed-word linear-time claim. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `1407_constructive.py`: time 0.078 s → 0.125 s; memory 416 KB → 244 KB.

Go and Rust build the answer from right to left, keeping the partial value and the next power of ten modulo 2¹²⁸. After k digits the lowest k bits are zero, so bit k decides whether the next digit is one or two. Only the lowest N ≤ 100 bits matter. Go implements the 128-bit arithmetic with two 64-bit words and Rust uses wrapping u128 operations. Go reads the exponent directly from a small reusable byte buffer and writes the constructed digits without string conversion.

The accepted Go 1.14 x64 run takes 0.031 s versus 0.015 s for the base and uses 784 KB versus 1140 KB.

The fast set reuses qualifying simple C++ and Python sources and uses optimized Java. Simple Java is retained for teaching, not claimed to qualify: its time 15/44 and memory 19/44 fail. Optimized Java's preceding Accepted #11327478 is 0.093 s / 312 KB with time 5/44, which passes under time-only comparison. No identical source copies are needed. Simple teaching rows are not separate optimization targets.

## Language notes

Use the shared [criteria](../../RATING_CRITERIA.md): memory is ignored only strictly below 1024 KB; rivals below 0.015 s are excluded, and only our time is floored. Ordinary cohorts use top ten or top 15%, ties shared and percentile rounded up. There is no first-place or 30%-improvement exception. Cached C++ passes time 1/19. Simple Python passes time 4/27, while optimized PyPy time 22/27 fails and keeps its star. Go has no current-compiler rivals and uses two eligible Go 1.3 results as same-language fallback; both versions pass. Rust similarly uses three older-compiler rivals, with simple/optimized time 4/4 and 1/4 passing. Existing historical paired measurements remain separate observations.

Only explanatory comments are added in `1407_constructive_optimized.java`: XOR-based unsigned carry comparison, split-32-bit multiplication and why bit k chooses the digit modulo 2^128. Executable code is unchanged.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1407_constructive.cpp](1407_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 188 KB | 11286054 |
| [1407_constructive.go](1407_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.015 s | 1140 KB | 11286055 |
| [1407_constructive.java](1407_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 1668 KB | 11286057 |
| [1407_constructive.py](1407_constructive.py) | Python 3.12 x64 | constructive | O(N^3) | AC | 0.078 s | 416 KB | 11286056 |
| [1407_constructive.rs](1407_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 216 KB | 11286058 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1407_constructive_optimized.go](1407_constructive_optimized.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 784 KB | 11311119 |
| [1407_constructive_optimized.rs](1407_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 188 KB | 11310807 |
| [1407_constructive_optimized.java](1407_constructive_optimized.java) | Java 1.8 | constructive | O(N) time; O(N) answer space | AC | 0.078 s | 324 KB | 11331218 |
| [1407_constructive_optimized.py](1407_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(n²) bit work; O(n) bits | AC | 0.125 s | 244 KB | 11325484 |

\* Accepted; this distinct optimized PyPy version fails the current time criterion. Python is covered by the simple source.
