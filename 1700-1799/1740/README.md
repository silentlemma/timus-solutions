# 1740. Deer is Better!

[Timus 1740](https://acm.timus.ru/problem.aspx?space=1&num=1740) · difficulty 138 · math

Original problem by Sergey Pupyrev (prepared by Daniil Ayzenshteyn), from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The way to the polling station is l km long. The deer may run any way
they like, as long as every stretch of k km takes exactly h hours. Find
the shortest and the longest possible time for the whole way.

## Input

Integers l, k and h (1 ≤ k ≤ l ≤ 1000, 1 ≤ h ≤ 1000).

## Output

The shortest and the longest time, with an error of at most 10⁻⁵.

## Checking

Repository tests compare numeric tokens with |actual-reference| <= 1e-5·max(1,|reference|), reject nonfinite values, and compare nonnumeric tokens exactly.

## Examples

### Example 1

Input:

```
30 10 1
```

Output:

```
3.00000000 3.00000000
```

## Solution

Let t(x) be the time to reach kilometre x. Every stretch of k km takes h
hours, so t(x + k) = t(x) + h: t grows by h per k km plus a part that
repeats every k km. With l = nk + r, the whole way takes nh + t(r), and
t(r) lies between t(0) = 0 and t(k) = h. The deer can spend almost no
time on the first r km of every stretch, or almost all of it, so the
answers are nh and, if r > 0, (n + 1)h. `O(1)`.

In the example 30 km is three stretches of 10 km, 3 hours either way.

Pitfalls:

- when k divides l both answers are the same;
- the times are whole numbers; the code prints eight decimal
  places.

## Optimized solutions

`1740_math_optimized.java`. Keep l=qk+r and the exact integer bounds qh and (q+[r>0])h. Parse the three integers through a bounded 1024-byte buffer instead of StreamTokenizer/character decoding. Output appends eight literal decimal zeros, avoiding floating conversion while preserving the required numeric values. O(1) arithmetic and auxiliary space; the teaching implementation remains.

Exact-source Java 1.8 Accepted #11326958: 0.093 s / 368 KB. Saved current-Java comparison, 2026-11-20: time rank 4/90, memory rank 1/90. With memory below 1024 KB, strict admission uses time only.

- `1740_math_optimized.java`: 0.093 s / 368 KB; retained teaching base `1740_math.java`: 0.14 s / 1792 KB; time change -33.6%; memory change -79.5%.

The optimized C++ solution reads the three numbers with `scanf` instead
of `std::cin`, so the program does not carry the `iostream` machinery at
all; the computation and the output are the same:
{1740_math_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1740_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +72.28%; base: `1740_math.cpp`.

`1740_math_optimized.py`. Keep the period decomposition l=q*k+r. The shortest time is q*h and the longest is (q+[r!=0])*h. Both extrema are integers; emit integer tokens directly instead of converting them to floats and formatting eight decimals. Numeric judging accepts these equivalent values. Under the statement limits products are at most 10^6, with O(1) time and state. Reuse divmod for quotient and remainder and avoid the decimal-formatting operation. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1740_math.py`: time 0.078 s → 0.125 s; memory 384 KB → 188 KB.

`1740_math_optimized.rs`. Keep the period decomposition l=q*k+r. The shortest time is q*h and the longest is (q+[r!=0])*h. Both extrema are integers; emit integer tokens directly instead of converting them to floats and formatting eight decimals. Numeric judging accepts these equivalent values. Under the statement limits products are at most 10^6, with O(1) time and state. Use i64 quotient/remainder and the manual integer writer rather than f64 values and Rust floating-point formatting. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1740_math.rs`: time 0.046 s → 0.015 s; memory 252 KB → 48 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1740_math_optimized.py`: time place 22/29, memory place 1/29 in this comparable sample.

`1740_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math.cpp](1740_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB | 11289483 |
| [1740_math.go](1740_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1092 KB | 11289484 |
| [1740_math.java](1740_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1792 KB | 11304069 |
| [1740_math.py](1740_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 384 KB | 11328291 |
| [1740_math.rs](1740_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 252 KB | 11304070 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1740_math_optimized.cpp](1740_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 112 KB | 11304455 |
| [1740_math_optimized.java](1740_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 368 KB | 11326958 |
| [1740_math_optimized.py](1740_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 188 KB | 11324913 |
| [1740_math_optimized.rs](1740_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 48 KB | 11325145 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
