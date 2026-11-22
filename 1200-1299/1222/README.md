# 1222. The highest product of numbers with a given sum

[Timus 1222](https://acm.timus.ru/problem.aspx?space=1&num=1222) · difficulty 144 · math

Original problem: folklore, proposed by Leonid Volkov, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A group of eagles with `1 ≤ N ≤ 3000` heads in total has an IQ equal to
the product of the head counts of its eagles. Find the largest possible
IQ; in other words, the largest product of positive integers that add up
to `N`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The largest product.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
5
```

Output:

```
6
```

## Solution

A part of 4 or more can be split into 2 and the rest without lowering the
product, and a part of 5 or more raises it that way (`2(k − 2) > k` for
`k > 4`), while a part of 1 only wastes a head. So an optimal split uses
only 2s, 3s and 4s, and a 4 is the same as 2 + 2. Three 2s are worse than
two 3s (`8 < 9`), so there are at most two 2s. That leaves: all 3s when
`3` divides `N`, one 2 more when the remainder is 2, and two 2s (or one
4) instead of a 3 when the remainder is 1. For `N` up to 3 the eagle
alone is best. The product has up to 478 digits. `O(N²)` digit
operations for the repeated multiplication by 3.

Pitfalls:

- `N = 1` gives 1, and `N = 4` gives 4;
- a remainder of 1 must not be kept as a factor of 1;
- the answer is far beyond 64 bits.

The answers were checked against a brute force over all splits for every
`N` up to 59, and compared with a separately written solution on every
test.

## Optimized solutions

`1222_math_optimized.java`. Keep the optimal split into threes, replacing a remainder one by a factor four; handle N<4 separately. Compute the same product in base-10^9 limbs with online multipliers up to 3^18, without BigInteger or precomputed answers. Each long intermediate is below 10^9*3^18<2^63. Decimal output pads lower limbs to nine digits. Conservative O(N²) arithmetic work and O(N) storage; the simple mathematical version remains.

Exact-source Java 1.8 Accepted #11327402: 0.093 s / 348 KB. Saved 2026-11-20 compiler-cohort comparison: time 12/136, memory 2/136. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11304486 was 0.125 s / 484 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1222_math_optimized.java`: 0.093 s / 348 KB; retained teaching base `1222_math.java`: 0.093 s / 1708 KB.

`1222_math_optimized.rs`. Keep the optimal decomposition into threes, using a four for remainder one. Pack nine decimal digits per u32 limb rather than one decimal digit per limb, and emit padded nine-digit groups directly without constructing a decimal String. Multiplication by three fits u32 because 3*(10^9-1)+2<2^32. Repeated small multiplications remain O(n²) limb work and O(n) output-digit storage; the gain is a smaller representation, not a new asymptotic algorithm. The simple decimal-limb version remains.

Compared with `1222_math.rs`: time 0.031 s → 0.015 s; memory 208 KB → 64 KB.

The optimized C++ solution multiplies a fixed global array of 1000
decimal digits instead of a `std::vector` that grows with the product,
so the program needs no dynamic memory; for `N ≤ 3000` the product has
at most 478 digits: {1222_math_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1222_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +45.83%; base: `1222_math.cpp`.

`1222_math_optimized.py`. Keep the maximum-product partition into threes, with N<4 handled directly and a remainder one replaced by a four. The exact result is unchanged; pow and the basic ** are equivalent integer exponentiation. With an O(N)-bit result, a conservative schoolbook arithmetic and decimal-output bound is O(N²) time and O(N) bits. The measured gain comes from the standalone runtime implementation. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1222_math.py`: time 0.078 s → 0.109 s; memory 396 KB → 248 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1222_math_optimized.py`: time place 19/61, memory place 3/61 in this comparable sample.

`1222_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math.cpp](1222_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 192 KB | 11283695 |
| [1222_math.go](1222_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1184 KB | 11283696 |
| [1222_math.java](1222_math.java) | Java 1.8 | math | O(N²) | AC | 0.093 s | 1708 KB | 11283698 |
| [1222_math.py](1222_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.078 s | 396 KB | 11283697 |
| [1222_math.rs](1222_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.031 s | 208 KB | 11283699 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math_optimized.cpp](1222_math_optimized.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.001 s | 104 KB | 11304484 |
| [1222_math_optimized.java](1222_math_optimized.java) \* | Java 1.8 | math | O(N²) time; O(N) space | AC | 0.093 s | 348 KB | 11327402 |
| [1222_math_optimized.py](1222_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N²) | AC | 0.109 s | 248 KB | 11324929 |
| [1222_math_optimized.rs](1222_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n²) limb work; O(n) digits | AC | 0.015 s | 64 KB | 11325523 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
