# 1823. Ideal Gas

[Timus 1823](https://acm.timus.ru/problem.aspx?space=1&num=1823) · difficulty 348 · math

Original problem credited to Benoît Paul Émile Clapeyron and Dmitri Mendeleev, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The ideal gas law pV = nRT links pressure p, amount of gas n, volume V
and temperature T, with R = 8.314. Three of the four values are given;
find the fourth. Volume and temperature must be positive. Print
"error" if the data contradict each other and "undefined" if the value
is not determined uniquely.

## Input

Three lines "X = value" for three different quantities X among p, n, V
and T, each value a non-negative integer up to 1000. The given V and T
are positive.

## Output

"X = value" with absolute or relative error at most 10⁻⁶, or "error",
or "undefined".

## Checking

Repository tests compare numeric tokens with |actual-reference| <= 1e-6·max(1,|reference|), reject nonfinite values, and compare nonnumeric tokens exactly.

## Examples

### Example 1

Input:

```
p = 1
n = 1
V = 1
```

Output:

```
T = 0.120279
```

## Solution

Solve pV = nRT for the missing value; the given values are integers,
so every zero test is exact.

- p = nRT/V and n = pV/(RT): V and T are given and positive, so the
  result is always defined, possibly 0.
- V = nRT/p: if p = 0 the equation reads 0 = nRT, which holds for every
  V when n = 0 ("undefined") and for none when n > 0 ("error"). If
  p > 0 and n = 0, V would be 0, which is not allowed ("error").
- T = pV/(nR) works the same way with n in place of p.

Use R = 8314/1000 to keep each result as an exact integer fraction a/b.
Round a/b to six decimal places using integer arithmetic, rounding ties
up, then print the integer and six-digit fractional parts with a literal
decimal point. Java uses `Locale.ROOT` for the digits. The absolute
rounding error is at most 0.0000005, and all intermediate values fit in
signed 64-bit integers under the input bounds.

`O(1)`.

In the example T = 1·1/(1·8.314) ≈ 0.120279.

Pitfalls:

- zero pressure or zero gas is allowed and is a valid answer when p or
  n is the unknown;
- a computed volume or temperature of zero is an error, not an answer;
- the lines may come in any order;
- numeric output must be independent of the system locale: test 15
  exposes Java's default formatting, which can print `0,000000` instead
  of `0.000000`.

## Optimized solutions

`1823_math_optimized.java`. Keep the exact scaled-integer ideal-gas calculation with R=8314/1000 and six decimal output places. Four scalar long values with -1 for the missing nonnegative quantity replace the HashMap. For unknown V or T, distinguish 0=0 (undefined) from a single zero factor (error) before dividing; known V,T are positive. Round the rational value half up at scale 10^6 and emit digits directly, including six zero-padded fractional positions, without printf/locale machinery. The largest scaled numerator is at most 8.314·10^15, safely within long. Time and arithmetic state O(1), plus fixed byte buffers.

Compared with `1823_math.java`: time 0.093 s → 0.078 s; memory 1736 KB → 504 KB.

`1823_math_optimized.py`. Keep the ideal-gas equation and all zero/undefined/error branches exactly as in the simple source. Preserve R=8314/1000 and integer half-up rounding to six decimal places; no floating approximation is introduced. Only raw input, ASCII decoding and standalone interpreter lifetime differ. Input storage/work is O(I), with a fixed number of bounded arithmetic operations. Flush the final answer before os._exit(0). Admission is the own runtime’s measured memory improvement, not a new gas-equation algorithm.

Compared with `1823_math.py`: time 0.078 s → 0.125 s; memory 572 KB → 284 KB.

Go and Rust index p, V, n and T in four fixed slots and use 1000pV = 8314nT to isolate the missing value with integer arithmetic. A zero numerator and denominator give undefined. A zero denominator, or a forced zero volume or temperature, gives error. Otherwise round the rational value to six decimal places using 64-bit integers.

The accepted base implementations [1823_math.cpp](1823_math.cpp), [1823_math.java](1823_math.java), [1823_math.py](1823_math.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`1823_math_optimized.java`: time place 1/18, memory place 1/18 in this comparable sample.

`1823_math_optimized.py`: time place 11/17, memory place 1/17 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1823_math.cpp](1823_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 384 KB | 11325589 |
| [1823_math.go](1823_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1116 KB | 11298046 |
| [1823_math.java](1823_math.java) \* | Java 1.8 | math | O(1) | AC | 0.093 s | 1736 KB | 11298047 |
| [1823_math.py](1823_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 572 KB | 11298048 |
| [1823_math.rs](1823_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 424 KB | 11325613 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1823_math_optimized.go](1823_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 776 KB | 11311181 |
| [1823_math_optimized.rs](1823_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 208 KB | 11310736 |
| [1823_math_optimized.java](1823_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 504 KB | 11325039 |
| [1823_math_optimized.py](1823_math_optimized.py) \* | PyPy 3.10 x64 | math | O(I) input work; exact bounded arithmetic | AC | 0.125 s | 284 KB | 11325491 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
