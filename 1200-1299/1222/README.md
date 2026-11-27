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
7
```

Output:

```
12
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

The result has O(N) digits/bits. Growing decimal vectors, big-integer values and decimal output require O(N) live value/output space plus library arithmetic workspace; the optimized C++ source instead reserves a fixed 1000-entry digit array. Repeated small multiplication has a conservative O(N²) digit-work bound. Library exponentiation uses larger multiplications; the common bound is not a claim that built-in power repeats N multiplications.

Pitfalls:

- `N = 1` gives 1, and `N = 4` gives 4;
- a remainder of 1 must not be kept as a factor of 1;
- the answer is far beyond 64 bits.

The answers were checked against a brute force over all splits for every
`N` up to 59, and compared with a separately written solution on every
test.

## Optimized solutions

`1222_math_optimized.java`. Keep the optimal split into threes, replacing a remainder one by a factor four; handle N<4 separately. Compute the same product in base-10^9 limbs with online multipliers up to 3^18, without BigInteger or precomputed answers. Each long intermediate is below 10^9*3^18<2^63. Decimal output pads lower limbs to nine digits. Conservative O(N²) arithmetic work and O(N) storage; the simple mathematical version remains.

Exact-source Java 1.8 Accepted #11327402 is 0.093 s / 348 KB. Saved 2026-11-20 comparison: time 12/136, memory 2/136. It qualifies by time only below 1024 KB, without a separate first-place target or asterisk. Earlier optimized #11304486 at 0.125 s / 484 KB is a distinct historical pair, not this current file receipt. The simple Java algorithm is preserved; its comment-only revision is tracked below.

- `1222_math_optimized.java`: 0.093 s / 348 KB; retained teaching base `1222_math.java`: 0.093 s / 1708 KB.

`1222_math_optimized.rs`. Keep the optimal decomposition into threes, using a four for remainder one. Pack nine decimal digits per u32 limb rather than one decimal digit per limb, and emit padded nine-digit groups directly without constructing a decimal String. Multiplication by three fits u32 because 3*(10^9-1)+2<2^32. Repeated small multiplications remain O(n²) limb work and O(n) output-digit storage; the gain is a smaller representation, not a new asymptotic algorithm. The simple decimal-limb version remains.

Compared with `1222_math.rs`: time 0.031 s → 0.015 s; memory 208 KB → 64 KB.

The optimized C++ solution multiplies a fixed global array of 1000
decimal digits instead of a `std::vector` that grows with the product,
so the program needs no dynamic memory; for `N ≤ 3000` the product has
at most 478 digits: {1222_math_optimized.cpp}.

### Measured gains

These are historical differences between paired Accepted values, not a universal 30%-gain admission rule. Simple versions remain. Negative reduction means increased cost; raw timing below one tick is not a portable speedup guarantee.

- `1222_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +45.83%; base: `1222_math.cpp`.

`1222_math_optimized.py` keeps the same exact maximum-product formula, using threes and replacing remainder one with four. It uses pow rather than ** and explicitly flushes stdout before os._exit(0). Its O(N)-bit result has a conservative schoolbook arithmetic/decimal-conversion bound O(N²), with O(N) value/output storage plus runtime workspace. The separate PyPy 0.109 s / 248 KB and base CPython 0.078 s / 396 KB pairs show different interpreter/run costs; they do not isolate a causal gain from exit or pow. The simple algorithm is preserved, with its proof-comment correction tracked below.

Compared with `1222_math.py`: time 0.078 s → 0.109 s; memory 396 KB → 248 KB.

## Language notes

Apply the shared [rating criteria](../../RATING_CRITERIA.md) to the cached source-bound receipts. Both C++, Go, base CPython, optimized Java and both Rust receipts qualify. Simple Java misses required memory; the PyPy alternative misses time and keeps its marker. Below1024 KB compare only time; Go at 1184 KB requires both metrics and its exact-compiler reference. Rust uses the same-language fallback: both 0.031 s / 208 KB and 0.015 s / 64 KB qualify numerically, not from an empty table or memory-gain exception. Old PyPy ranks 19/61 (time), 3/61 (memory) are historical, not a current first-place target.

This review corrects only the proof comment in `1222_math.cpp`, `1222_math_optimized.cpp`, `1222_math.go`, `1222_math.java`, `1222_math.py` and `1222_math.rs`: splitting a part above 4 strictly improves its product; 4=2+2 only ties. Executable text and every other comment are unchanged. Their table receipts and qualification above describe the historical exact bytes.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math.cpp](1222_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 176 KB | 11331135 |
| [1222_math.go](1222_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1216 KB | 11331004 |
| [1222_math.java](1222_math.java) | Java 1.8 | math | O(N²) | AC | 0.109 s | 1688 KB | 11331043 |
| [1222_math.py](1222_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.093 s | 420 KB | 11331062 |
| [1222_math.rs](1222_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.015 s | 204 KB | 11331100 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1222_math_optimized.cpp](1222_math_optimized.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 112 KB | 11331136 |
| [1222_math_optimized.java](1222_math_optimized.java) | Java 1.8 | math | O(N²) time; O(N) space | AC | 0.093 s | 348 KB | 11327402 |
| [1222_math_optimized.py](1222_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N²) | AC | 0.109 s | 248 KB | 11324929 |
| [1222_math_optimized.rs](1222_math_optimized.rs) | Rust 1.75 x64 | math | O(n²) limb work; O(n) digits | AC | 0.015 s | 64 KB | 11325523 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
