# 1228. The bounds of an array from its index multipliers

[Timus 1228](https://acm.timus.ru/problem.aspx?space=1&num=1228) · difficulty 109 · math

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An `n`-dimensional array `array[0..k1, 0..k2, …, 0..kn]`, `n ≤ 20`, is
laid out with the last index changing fastest, so element
`X[i1, …, in]` has number `1 + D1·i1 + … + Dn·in` for some multipliers
`Di`. Given the multipliers and the total number of elements `s`, find
the upper bounds `k1, …, kn`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` (`1 ≤ n ≤ 20`) and `s` (`1 ≤ s < 2³¹ − 1`), then `D1, …, Dn`.

## Output

`k1, …, kn` (`0 < ki ≤ 1000`) separated by spaces or line breaks.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
3 24
8
4
1
```

Output:

```
2 1 3
```

## Solution

Stepping index `i` by one skips a whole block of the dimensions after
it, so `D(i−1) = Di · (ki + 1)`, and the whole array is one block of the
first dimension: `s = D1 · (k1 + 1)`. Reading the multipliers with `s` in
front, every bound is one less than the quotient of two neighbours:
`k1 = s/D1 − 1` and `ki = D(i−1)/Di − 1`. `O(n)`.

Pitfalls:

- the last multiplier is always 1, and the first bound comes from `s`,
  not from a multiplier;
- the products stay below `2³¹ − 1`, so signed 32-bit integers suffice
  for the arithmetic.

The bounds were checked by multiplying `ki + 1` back into `s` on 59 generated
arrays, and compared with a separately written solution on every test.

## Optimized solutions

The optimized C++ solution reads the multipliers one at a time and keeps
only the previous one, printing each bound as soon as its divisor
arrives, instead of storing `s` and all the multipliers in a
`std::vector`: {1228_math_optimized.cpp}.

The optimized Java solution parses the numbers digit by digit straight
from `System.in` instead of creating a `Scanner`, and keeps only the
previous multiplier instead of an array of all of them:
{1228_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1228_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +36.00%; base: `1228_math.cpp`.

- `1228_math_optimized.java`: time reduction +50.40%; memory reduction
  +78.22%; base: `1228_math.java`.

`1228_math_optimized.py`. Keep the same consecutive-ratio reconstruction: start with total size s and output previous/current-1 for each next multiplier. The final multiplier is processed in the same way; valid input supplies exact positive ratios. There are O(n) bounded-integer divisions. The 65536-byte chunk tokenizer carries only the unfinished token across reads, avoiding the complete decoded input and all input integers. It still builds the list of answer strings and joins it: O(n) output storage plus bounded parser storage under the token-size limits. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1228_math.py`: time 0.078 s → 0.109 s; memory 424 KB → 212 KB.

`1228_math_optimized.rs`. Keep the same consecutive-ratio reconstruction: start with total size s and output previous/current-1 for each next multiplier. The final multiplier is processed in the same way; valid input supplies exact positive ratios. There are O(n) bounded-integer divisions. Read and emit each ratio immediately, retaining only previous and current. No input vector, per-answer strings or joined output are needed: O(1) auxiliary state. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1228_math.rs`: time 0.015 s → 0.015 s; memory 216 KB → 52 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1228_math_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328526 (Go 1.14 x64): **0.015 s / 956 KB**. Archived comparison: `1228_math.go` (Go 1.14 x64) — 0.001 s / 1136 KB (#11283735).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1228_math_optimized.py`: time place 21/32, memory place 1/32 in this comparable sample.

`1228_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1228_math.cpp](1228_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 200 KB | 11283732 |
| [1228_math.go](1228_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.001 s | 1136 KB | 11283735 |
| [1228_math.java](1228_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1616 KB | 11283739 |
| [1228_math.py](1228_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 424 KB | 11283737 |
| [1228_math.rs](1228_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 216 KB | 11283740 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1228_math_optimized.cpp](1228_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.001 s | 128 KB | 11304270 |
| [1228_math_optimized.java](1228_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.062 s | 352 KB | 11304271 |
| [1228_math_optimized.py](1228_math_optimized.py) \* | PyPy 3.10 x64 | math | O(n) | AC | 0.109 s | 212 KB | 11325065 |
| [1228_math_optimized.rs](1228_math_optimized.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 52 KB | 11324870 |
| [1228_math_optimized.go](1228_math_optimized.go) | Go 1.14 x64 | math | O(n) | AC | 0.015 s | 956 KB | 11328526 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
