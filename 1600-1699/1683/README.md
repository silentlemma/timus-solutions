# 1683. Fridge

[Timus 1683](https://acm.timus.ru/problem.aspx?space=1&num=1683) · difficulty 137 · greedy

Original problem by Stanislav Vasilyev, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A paper strip 1 cm wide and n cm long is folded into a 1 × 1 cm square
of n layers. Each fold measures a whole number of centimetres from the
left end and folds that part over to the right, so the left end moves
by that amount. Find the fewest folds and the lengths measured.

## Input

n (1 ≤ n ≤ 10⁹).

## Output

The number of folds, then the measured lengths in order. Any shortest
sequence is accepted.

## Checking

The repository uses a semantic checker and accepts any output satisfying these conditions. The repository checker requires the optimal fold count from the reference and exactly that many integer lengths. Each length x must satisfy1<=x<=current-x, then current decreases by x; the final strip length must be one. Any shortest valid sequence is accepted.

## Examples

### Example 1

Input:

```
12
```

Output:

```
4
5 3 2 1
```

## Solution

Folding x cm of a strip of length L is possible only if the flap fits on
the rest, x ≤ L − x, and leaves a strip of L − x ≥ ⌈L / 2⌉. So no fold
more than halves the strip, rounding up, and folding ⌊L / 2⌋ every time
achieves exactly that: the number of folds is the least m with
2ᵐ ≥ n. `O(log n)`.

Pitfalls:

- n = 1 needs no folds: print 0 and an empty list;
- the example's 5 3 2 1 is one of many answers, so a checker compares
  the count and replays the folds.

The checker replays every fold and compares the count with the
greedy one.

## Optimized solutions

`1683_greedy_optimized.java`. Keep optimal repeated half-folds. For 1≤N≤10^9, ceil(log2 N) is 32−numberOfLeadingZeros(N−1); N=1 gives zero folds. All fold lengths fit int, and at most thirty values fit a 384-byte complete answer buffer. Encode digits in place, write once and flush before System.exit(0), instead of building strings or using a generic long-output buffer. O(log N) folds and bounded auxiliary storage. The current 0.078 s/452 KB receipt is separate from the old 0.093 s/452 KB receipt; one timer tick alone is not a 30% gain. Teaching sources and Python runtime-selection evidence remain unchanged.

Exact-source Java 1.8 Accepted #11327867: 0.078 s / 452 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/62, memory 5/62. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11304448 was 0.093 s / 452 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1683_greedy_optimized.java`: 0.078 s / 452 KB; retained teaching base `1683_greedy.java`: 0.125 s / 1664 KB.

`1683_greedy_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327033 measures 0.062 s / 620 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 1/21, memory rank 21/21. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11324922, 0.125 s / 208 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`1683_greedy_optimized.py`. Keep folding floor(length/2) from the left, leaving ceil(length/2). No legal fold can shrink the strip faster, so the minimum count is ceil(log2 n), including zero folds for n=1. There are O(log n) bounded-integer steps under n<=10^9. Compute the count with (n-1).bit_length() before constructing the lengths. The code still stores strings for all folds and joins them, so auxiliary output storage remains O(log n). The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1683_greedy.py`: time 0.125 s → 0.125 s; memory 372 KB → 208 KB.

`1683_greedy_optimized.rs`. Keep folding floor(length/2) from the left, leaving ceil(length/2). No legal fold can shrink the strip faster, so the minimum count is ceil(log2 n), including zero folds for n=1. There are O(log n) bounded-integer steps under n<=10^9. Use a first halving pass to count, then repeat the same deterministic steps while emitting lengths. This avoids Vec<String> and joined output: O(1) auxiliary state, two O(log n) passes. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1683_greedy.rs`: time 0.015 s → 0.062 s; memory 244 KB → 52 KB.

The optimized C++ solution keeps the folds in a fixed array of
30 numbers on the stack instead of a growing `std::vector`. Since
n ≤ 10⁹ < 2³⁰, at most 30 halvings bring the strip down to 1 cm, so the
array always suffices and the program itself allocates nothing on the
heap: {1683_greedy_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1683_greedy_optimized.cpp`: time reduction +0.00%; memory reduction
  +47.92%; base: `1683_greedy.cpp`.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1683_greedy_parsing_optimized.go`. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments.

Accepted #11328881 (Go 1.14 x64): **0.015 s / 916 KB**. Archived comparison: `1683_greedy.go` (Go 1.14 x64) — 0.031 s / 1096 KB (#11288848).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

Earlier PyPy comparison: `1683_greedy_optimized.py`: time place 18/21, memory place 1/21 in this comparable sample.

`1683_greedy_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy.cpp](1683_greedy.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 192 KB | 11288846 |
| [1683_greedy.go](1683_greedy.go) | Go 1.14 x64 | greedy | O(log n) | AC | 0.031 s | 1096 KB | 11288848 |
| [1683_greedy.java](1683_greedy.java) | Java 1.8 | greedy | O(log n) | AC | 0.125 s | 1664 KB | 11288850 |
| [1683_greedy.py](1683_greedy.py) | Python 3.12 x64 | greedy | O(log n) | AC | 0.125 s | 372 KB | 11288849 |
| [1683_greedy.rs](1683_greedy.rs) | Rust 1.75 x64 | greedy | O(log n) | AC | 0.015 s | 244 KB | 11288851 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy_optimized.cpp](1683_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 100 KB | 11304447 |
| [1683_greedy_optimized.java](1683_greedy_optimized.java) | Java 1.8 | greedy | O(log N) time; bounded 384-byte answer | AC | 0.078 s | 452 KB | 11327867 |
| [1683_greedy_optimized.py](1683_greedy_optimized.py) | Python 3.12 x64 | greedy | O(log n) | AC | 0.062 s | 620 KB | 11327033 |
| [1683_greedy_optimized.rs](1683_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(log n) | AC | 0.062 s | 52 KB | 11325142 |
| [1683_greedy_parsing_optimized.go](1683_greedy_parsing_optimized.go) | Go 1.14 x64 | greedy, parsing | O(log n) | AC | 0.015 s | 916 KB | 11328881 |
