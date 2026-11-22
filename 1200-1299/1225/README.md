# 1225. Rows of white, blue and red stripes

[Timus 1225](https://acm.timus.ru/problem.aspx?space=1&num=1225) · difficulty 35 · dp

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A row of `N ≤ 45` stripes is made of white, blue and red ones. No two
neighbouring stripes share a colour, and a blue stripe must stand between
a white and a red one. Count the possible rows.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The number of rows.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
1
```

Output:

```
2
```

## Solution

A blue stripe needs neighbours on both sides, so a row never ends in
blue; it ends in white or red. Let `f(n)` count the valid rows of length
`n`. Before a last white stripe there is either red, which closes a valid
row of length `n − 1` ending in red, or blue preceded by red, which
closes a valid row of length `n − 2` ending in red; the same holds for
red with the colours swapped. By symmetry half of the rows of each length
end in red, so `f(n) = f(n − 1) + f(n − 2)` with `f(1) = f(2) = 2`:
twice the Fibonacci numbers. `O(N)`.

Pitfalls:

- a single stripe can be white or red but not blue, so `f(1) = 2`;
- for `N = 45` the count is 2,269,806,340, beyond 32-bit signed integers.

The formula was checked by brute force over all colourings up to 12
stripes, and every `N` from 1 to 45 was compared with a separately
written solution.

## Optimized solutions

`1225_math.py`. Alternative exact generating-function algorithm: valid flags number 2·Fib(N). With B=2^64, extract coefficient N−1 of 1/(1−x−x²) as floor(B^(N+1)/(B²−B−1)) mod B, then double it. For 1≤N≤45 the coefficients fit a base-B digit and the remaining positive tail is below one, so there is no carry. No floating point or embedded answers. One division on O(N)-bit integers (at most 2945-bit numerator), not constant-cost arithmetic for unbounded N. Keep the readable recurrence.

Exact-source Python 3.12 x64 Accepted #11327782: 0.062 s / 644 KB. Saved 2026-11-20 compiler-cohort ranks, time then memory: 5/366; 329/366. Strict admission uses time only below 1024 KB: top ten or top 15%, ties share rank and percentage cutoff rounds up. An asterisk remains for the separate first-place-in-both language target. The preserved previous variant has its own paired receipt #11324831 (PyPy 3.10 x64): 0.14 s / 224 KB; do not mix measurements or runtimes. All teaching sources remain unchanged.

- `1225_math.py`: 0.062 s / 644 KB; retained teaching base `1225_dp.py` (Python 3.12 x64): 0.093 s / 372 KB.

The optimized Java solution parses the number byte by byte from
`System.in` instead of using `Scanner`: 0.093 s instead of 0.125 s and
316 KB instead of 1576 KB.

`1225_dp_optimized.py`. Keep the two-accumulator recurrence starting at (2,2); each extra stripe replaces the pair by (current,previous+current). No table is introduced. Raw-byte input and flushed immediate termination reduce runtime overhead. There are O(N) additions and two integer accumulators, bounded by N<=45. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1225_dp.py`: time 0.093 s → 0.14 s; memory 372 KB → 224 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1225_dp_optimized.py`: time place 363/366, memory place 2/366 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1225_dp.cpp](1225_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB | 11283710 |
| [1225_dp.go](1225_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1072 KB | 11283711 |
| [1225_dp.java](1225_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1576 KB | 11283713 |
| [1225_dp.py](1225_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 372 KB | 11283712 |
| [1225_dp.rs](1225_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 216 KB | 11283714 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1225_dp_optimized.java](1225_dp_optimized.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 316 KB | 11303728 |
| [1225_dp_optimized.py](1225_dp_optimized.py) \* | PyPy 3.10 x64 | dp | O(N) | AC | 0.14 s | 224 KB | 11324831 |
| [1225_math.py](1225_math.py) \* | Python 3.12 x64 | math | One O(N)-bit integer division; O(N) bits | AC | 0.062 s | 644 KB | 11327782 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
