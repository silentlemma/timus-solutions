# 1260. The fussy photographer

[Timus 1260](https://acm.timus.ru/problem.aspx?space=1&num=1260) · difficulty 112 · dp

Original problem by Alexander Ipatov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N students aged 1, 2, …, N years (1 ≤ N ≤ 55) sit in a row. The one
aged 1 sits at the left end, and the ages of any two neighbours differ by
at most 2. How many such rows are there?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The number of rows.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
4
```

Output:

```
4
```

## Solution

Let a(k) be the number of rows for the ages 1..k. Look at who sits
second:

- age 2: the rest is a row of 2..k starting with 2, the same problem
  shifted by one, a(k − 1) ways;
- age 3, then age 2: the next must be 4, and the rest is a row of 4..k
  starting with 4, a(k − 3) ways;
- age 3, but 2 later: the neighbours of 2 can only be 1, 3 and 4, and 1
  and 3 are already taken next to each other, so 2 sits at the right end
  next to 4. This forces the zigzag 1, 3, 5, … up the odd ages and back
  down the even ones to 4, 2: exactly one row.

So a(k) = a(k − 1) + a(k − 3) + 1, with a(1) = a(2) = 1 and a(3) = 2.
Running the rule backwards gives a(0) = 0 and a(−1) = −1, which lets the
loop start from k = 1 with no special cases. a(55) = 1 388 937 263
still fits in 32 bits, but C++, Go, Java and Rust use 64-bit integers,
and Python uses its arbitrary-precision integers. `O(N)`.

Pitfalls:

- the third case is easy to miss: for N = 5 it is the row 1, 3, 5, 4, 2
  (test 05);
- N = 1 and N = 2 both have a single row (tests 02, 03).

The recurrence was compared with listing all permutations for N up to
10.

## Optimized solutions

`1260_dp_optimized.java`. Java retains the same recurrence and three long counters: starting from (-1,0,1), each step replaces them by (old,current,current+older+1). For N from 1 to 55 it needs at most 54 steps, O(N) time and O(1) auxiliary space. Fixed 1024-byte input/output buffers and a 20-digit scratch buffer replace per-character stream input and general number formatting. Every allowed N was checked against an independent array recurrence; small permutation enumeration also checks the counting interpretation.

Exact-source Java 1.8 Accepted #11327453: 0.093 s / 340 KB. Saved 2026-11-20 compiler-cohort comparison: time 9/96, memory 4/96. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11304342 was 0.109 s / 320 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1260_dp_optimized.java`: 0.093 s / 340 KB; retained teaching base `1260_dp.java`: 0.093 s / 1568 KB.

`1260_dp_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327021 measures 0.078 s / 564 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 6/44, memory rank 26/44. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11324915, 0.125 s / 200 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`1260_dp_optimized.py`. Keep a(k)=a(k-1)+a(k-3)+1 and the same rolling initial state (-1,0,1). Three accumulators replace no additional table: each iteration simultaneously advances all three old values. Time O(N), three bounded integer slots. With N<=55 the counts fit signed 64 bits; a conservative bound a(N)<2^N suffices. Read one byte token and keep the recurrence at module scope, avoiding the wrapper call. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1260_dp.py`: time 0.109 s → 0.125 s; memory 404 KB → 200 KB.

`1260_dp_optimized.rs`. Keep a(k)=a(k-1)+a(k-3)+1 and the same rolling initial state (-1,0,1). Three accumulators replace no additional table: each iteration simultaneously advances all three old values. Time O(N), three bounded integer slots. With N<=55 the counts fit signed 64 bits; a conservative bound a(N)<2^N suffices. Keep i64 accumulators and emit the final number directly; no decoded input or Rust output formatting is retained. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1260_dp.rs`: time 0.015 s → 0.031 s; memory 232 KB → 56 KB.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1260_dp_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328530 (Go 1.14 x64): **0.031 s / 936 KB**. Archived comparison: `1260_dp.go` (Go 1.14 x64) — 0.046 s / 1076 KB (#11284124).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

Earlier PyPy comparison: `1260_dp_optimized.py`: time place 37/44, memory place 1/44 in this comparable sample.

`1260_dp_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1260_dp.cpp](1260_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB | 11284122 |
| [1260_dp.go](1260_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.046 s | 1076 KB | 11284124 |
| [1260_dp.java](1260_dp.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 1568 KB | 11284130 |
| [1260_dp.py](1260_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.109 s | 404 KB | 11284128 |
| [1260_dp.rs](1260_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 232 KB | 11284131 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1260_dp_optimized.java](1260_dp_optimized.java) | Java 1.8 | dp | O(N) time; O(1) auxiliary space | AC | 0.093 s | 340 KB | 11327453 |
| [1260_dp_optimized.py](1260_dp_optimized.py) | Python 3.12 x64 | dp | O(N) | AC | 0.078 s | 564 KB | 11327021 |
| [1260_dp_optimized.rs](1260_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 56 KB | 11325091 |
| [1260_dp_optimized.go](1260_dp_optimized.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 936 KB | 11328530 |
