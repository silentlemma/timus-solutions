# 1283. Dwarf

[Timus 1283](https://acm.timus.ru/problem.aspx?space=1&num=1283) · difficulty 116 · math

Original problem by Leonid Volkov (prepared by Ivan Dashkevich), from the Ural State University Personal Contest 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dwarf has G units of gold, and every year a bank keeps p percent of
it as a fee (1 ≤ p ≤ 99), so the gold shrinks to (100 − p)/100 of
itself. Once the gold is at most L, the dwarf gives up. G and L are
integers not exceeding 2³¹ − 1. How many years are left?

Time limit: 1 second. Memory limit: 64 MB.

## Input

G, L and p.

## Output

The number of years.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
19 10 50
```

Output:

```
1
```

### Example 2

Input:

```
1000 1 1
```

Output:

```
688
```

## Solution

After k years the gold is exactly G · ((100 − p)/100)^k, and the answer
is the first k with that at most L. In whole numbers the test is

```text
G · (100 − p)^k ≤ L · 100^k
```

so both sides are multiplied each year, by 100 − p and by 100, until
the left one is no longer larger. The loop runs at most about 2140
times, for G = 2³¹ − 1, L = 1 and p = 1, and the numbers grow to a few
thousand digits. `O(Y²)` digit operations for Y years.

The bound on the loop assumes positive G and L, while the statement
gives no lower bounds for them: with G > 0 and L = 0, the gold stays
positive after every finite number of years, and there is no finite
answer.

Pitfalls:

- the gold can land exactly on the limit, and floating point then
  misses it: 300 · 0.81 comes out as 243.00000000000003, one year too
  many for L = 243 (test 05), and ln(9801/10000) / ln(0.99) rounds up to
  three years instead of two (test 06);
- if the gold is already at most L, the answer is 0 (tests 03, 04).

## Optimized solutions

`1283_binary_search_math.py`. Find the first year Y with G(100−p)^Y≤L100^Y by exponential bracketing and binary search on exact integer powers. No logarithm, gcd/math import or per-year big-integer multiplication loop is needed. Handle G≤L immediately, including zero; preserve exact equality boundaries. If D bounds operand bits and M(D) multiplication cost, conservative O(log²(Y+1)·M(D)) time and O(D) space. This search algorithm has a separate filename and the simple year-by-year version remains.

Compared with `1283_math.py`: time 0.078 s → 0.125 s; memory 480 KB → 264 KB.

The optimized Java solution keeps each side as an array of base-10⁹
digits that it multiplies in place, growing the array only when a new
digit appears, instead of creating two new `BigInteger` objects every
year; a digit times at most 100 plus the carry stays below 10¹¹ and fits
in `long`. It reads G, L and p digit by digit straight from `System.in`
into `int`, which holds them since they are at most 2³¹ − 1, instead of
creating a `Scanner`: {1283_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1283_math_optimized.java`: time reduction +0.00%; memory reduction
  +93.57%; base: `1283_math.java`.

`1283_math_optimized.rs`. Preserve exact comparison of G*(100-p)^Y and L*100^Y, but reduce G/L and (100-p)/100 by their gcds first. Keep both products in u128 while checked multiplication succeeds; on overflow promote both unchanged pre-multiplication values to base-10^9 u32 limbs and continue exactly. The guard G<=L returns zero before reduction. No logarithms, floating point or epsilon decide the stopping boundary. With Y years and at most D limbs, time O(Y·D), storage O(D); narrow limbs and the native-integer fast path reduce overhead. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1283_math.rs`: time 0.015 s → 0.031 s; memory 232 KB → 68 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1283_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1283_math.cpp](1283_math.cpp) | G++ 13.2 x64 | math | O(Y²) | AC | 0.015 s | 204 KB | 11284476 |
| [1283_math.go](1283_math.go) | Go 1.14 x64 | math | O(Y²) | AC | 0.031 s | 1276 KB | 11284478 |
| [1283_math.java](1283_math.java) | Java 1.8 | math | O(Y²) | AC | 0.109 s | 5600 KB | 11284490 |
| [1283_math.py](1283_math.py) | Python 3.12 x64 | math | O(Y²) | AC | 0.078 s | 480 KB | 11284484 |
| [1283_math.rs](1283_math.rs) | Rust 1.75 x64 | math | O(Y²) | AC | 0.015 s | 232 KB | 11284494 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1283_math_optimized.java](1283_math_optimized.java) | Java 1.8 | math | O(Y²) | AC | 0.109 s | 360 KB | 11304347 |
| [1283_math_optimized.rs](1283_math_optimized.rs) \* | Rust 1.75 x64 | math | O(Y·D) | AC | 0.031 s | 68 KB | 11325092 |
| [1283_binary_search_math.py](1283_binary_search_math.py) \* | PyPy 3.10 x64 | binary_search, math | O(log²(Y+1)·M(D)) time; O(D) space | AC | 0.125 s | 264 KB | 11325857 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
