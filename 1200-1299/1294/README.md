# 1294. Mars Satellites

[Timus 1294](https://acm.timus.ru/problem.aspx?space=1&num=1294) · difficulty 317 · geometry

Original problem by Vladimir Yakovlev, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Four satellites A, B, C and D lie on one circular orbit in this order.
The distances AD, AC, BD and BC are known, in thousands of kilometres
(whole numbers from 1 to 10 000); the radius of the orbit is not. Find
the distance CD in kilometres, rounded to an integer, or report that it
cannot be determined uniquely.

Time limit: 1 second. Memory limit: 64 MB.

## Input

AD, AC, BD and BC.

## Output

`Distance is X km.` or `Impossible.`

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
50 40 40 14
```

Output:

```
Distance is 30000 km.
```

## Acceptance update

The Python whitespace-input correction has exact-source Accepted #11330228
(`0.093 s / 424 KB`) in the table. Earlier measurements remain historical.
Saved numerical coverage is established for C++, Go, Java and Python;
Rust has Accepted code but no comparable rating reference. Teaching
sources and distinct optimized implementations remain available.

## Solution

Write a = AD, b = AC, c = BD, d = BC and x = CD. The points A and B lie
on the same arc cut off by the chord CD, so they see it at the same
inscribed angle t. The law of cosines in triangles ACD and BCD gives

x² = a² + b² − 2ab cos t = c² + d² − 2cd cos t,

two equations in x² and cos t. Hence

cos t = (a² + b² − c² − d²) / (2 (ab − cd)),

x² = (ab (c² + d²) − cd (a² + b²)) / (ab − cd).

- If ab = cd, the equations either contradict each other or say
  nothing about t. In the second case, for example a symmetric
  trapezoid, CD really can take many values (test 02). Either way the
  answer is `Impossible.` (tests 02 and 03).
- If |a² + b² − c² − d²| ≥ 2 |ab − cd|, no nondegenerate triangle
  exists: equality also fails because three distinct points on a circle
  cannot be collinear (tests 04 and 07).
- Ptolemy’s theorem requires AB · CD = bc − ad > 0 for the stated cyclic
  order. Reject bc ≤ ad as `Impossible.` (tests 05 and 07). With a strict
  cosine bound, this check also ensures the reconstructed points have
  the required order.
- Otherwise x = 1000 · √x² kilometres, rounded.

All feasibility checks use exact 64-bit integers (the original products
stay below 2 · 10¹⁶). Normalize the numerator and denominator to positive
values. Use a floating-point square root to estimate the integer part m
of the distance in kilometres, then round up exactly when
(2m + 1)² ≤ floor(4 · 1000² · num / den). Compute this bound as
s · (num div den) + (s · (num mod den)) div den, where s = 4 · 1000²,
to avoid overflow. All new intermediates are below 2 · 10¹⁵.
Time and auxiliary space are both `O(1)`.

The corrected feasibility checks and rounded answers are verified
by reconstructing AB first, checking exact triangle inequalities and
cyclic point order, then verifying all four given chords and the common
circumcircle in rational coordinates. Ptolemy and exact rounding provide
further certificates. The unchanged Python main also agrees on all
20736 four-tuples in `[1, 12]` and 1000 seeded full-bound inputs.

Pitfalls:

- the inputs are in thousands of kilometres, the answer in kilometres
  (test 01);
- AD · AC = BD · BC does not always mean the data contradict each
  other: sometimes it means many answers (tests 02 and 03);
- a cosine in [−1, 1] alone does not ensure a valid orbit: exclude
  degenerate triangles and enforce the cyclic order (test 07).

## Optimized solutions

`1294_geometry_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1294_geometry.java`: time 0.109 s → 0.093 s; memory 1 600 KB → 452 KB.

Rust factors the squared chord length into an integer numerator and denominator after checking whether the geometry determines a unique answer. Scale the rational square to obtain twice the distance in kilometres, splitting quotient and remainder before multiplication. Correct the floating-point square-root estimate with integer square comparisons. Its integer part decides the final rounding without floating-point formatting. Input and the complete response use fixed byte buffers. Rust reads and writes through the C runtime.

The accepted Rust 1.75 x64 run takes 0.031 s versus 0.015 s for the base and uses 56 KB versus 220 KB.

The source-bound saved audit admits simple C++ and Python without duplicate
fast files. Simple Go #11325573 (`0.015 s / 1080 KB`) misses the
1016.60 KB sparse memory limit; optimized Go #11328935 (`0.015 s /
804 KB`) passes its time-only comparison. Simple Java #11325554
misses the required memory ranking; optimized Java #11325015 passes
ordinary time ranking at 452 KB. These simple files remain for teaching.
Both Rust files have verified Accepted sources but no eligible rival
reference in the saved audit: their numerical rating is unknown, not
a proven failure. The old blanket base-coverage claim is superseded.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1294_geometry_parsing_implementation_optimized.go`. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments. Use an 8192-byte refillable input buffer instead of retaining the entire input. Tokens and partial/EOF reads retain their original meaning.

Accepted #11328935 (Go 1.14 x64): **0.015 s / 804 KB**. Archived comparison: `1294_geometry.go` (Go 1.14 x64) — 0.015 s / 1080 KB (#11325573).

## Language notes

The shared [rating criteria](../../RATING_CRITERIA.md) apply to all languages:
ordinary top ten or top 15% for required metrics, replaced by the
reference rule for 1–10 eligible rivals on the exact compiler. Below
1024 KB only time is required. Rival times below `0.015 s` are excluded;
only our own time uses that comparison floor. Raw Accepted measurements,
including C++ `0.001 s`, remain unchanged. There is no ID/date cutoff,
separate first-place requirement or admission merely for a 30% gain.

The 18 November 2026 ranks of optimized Java (time 5/20, memory 2/20)
are historical; its saved ordinary time ranking still admits it. Python
passes the nine-rival exact-compiler time limit `0.093 s`. Rust’s
retained star denotes unknown numerical ranking, pending a comparable
reference or separately bound qualitative review. The Rust star denotes an unknown numerical rank. A source-bound qualitative review already approves the optimized Rust implementation against the C++ reference.

The current fast Go revision corrects a comment: `fastFormatted`
supports only `%d`, converted from int/int64 with optional padding. The program uses the fixed format `Distance is %d km.\n`; character,
string and decimal conversions are absent. The strict linter also requires extracting the inline token capacity
128 into `inlineTokenBytes`; after substituting that constant, executable
tokens and algorithm are unchanged.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1294_geometry.cpp](1294_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.001 s | 112 KB | 11325577 |
| [1294_geometry.go](1294_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1080 KB | 11325573 |
| [1294_geometry.java](1294_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1600 KB | 11325554 |
| [1294_geometry.py](1294_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 424 KB | 11330228 |
| [1294_geometry.rs](1294_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 220 KB | 11325604 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1294_geometry_optimized.rs](1294_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 56 KB | 11311233 |
| [1294_geometry_optimized.java](1294_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 452 KB | 11325015 |
| [1294_geometry_parsing_implementation_optimized.go](1294_geometry_parsing_implementation_optimized.go) | Go 1.14 x64 | geometry, parsing, implementation | O(1) | AC | 0.015 s | 804 KB | 11331022 |

\* Accepted; numerical ranking is unknown because there are no eligible peers. The private auditor records a source-bound qualitative approval against the C++ reference; no numerical rank is assigned.
