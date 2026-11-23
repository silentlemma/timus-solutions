# 1327. Fuses

[Timus 1327](https://acm.timus.ru/problem.aspx?space=1&num=1327) · difficulty 47 · math

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A computer loses a fuse on every odd working day: on day 1, then on day
3, on day 5 and so on. Count the fuses lost from day A to day B
inclusive, 1 ≤ A ≤ B ≤ 10 000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A on the first line and B on the second.

## Output

The number of fuses.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
1
5
```

Output:

```
3
```

### Example 2

Input:

```
100
200
```

Output:

```
50
```

## Solution

Days 1 to x hold ⌊(x + 1) / 2⌋ odd days. The odd days from A to B are
those up to B minus those up to A − 1, which gives
⌊(B + 1) / 2⌋ − ⌊A / 2⌋. `O(1)`.

Pitfalls:

- a range of a single day gives 1 for an odd day and 0 for an even one
  (tests 03 and 04);
- both ends count when they are odd (tests 01 and 07).

## Optimized solutions

The optimized Java solution parses the two numbers byte by byte from
`System.in` instead of using `Scanner`: 0.078 s instead of 0.109 s and
304 KB instead of 1624 KB.

`1327_math_optimized.py`. Keep the difference of odd-day prefix counts, (B+1)//2-A//2. Parse both bounded endpoints from byte tokens instead of two text input calls. The arithmetic uses O(1) time and auxiliary storage. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1327_math.py`: time 0.062 s → 0.125 s; memory 404 KB → 208 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1327_parsing_optimized.go`. Use direct typed conversion over a 256-byte refill buffer and compact output with complete writes. Signed integer conversion accumulates negative values directly, including the signed minimum; no reflection-based input or generic output dispatch is needed. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments.

Accepted #11329104 (Go 1.14 x64): **0.015 s / 796 KB**. Archived comparison: `1327_math.go` (Go 1.14 x64) — 0.031 s / 1060 KB (#11284982).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1327_math_optimized.py`: time place 90/102, memory place 1/102 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1327_math.cpp](1327_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11284981 |
| [1327_math.go](1327_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB | 11284982 |
| [1327_math.java](1327_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1624 KB | 11284984 |
| [1327_math.py](1327_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 404 KB | 11284983 |
| [1327_math.rs](1327_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 236 KB | 11284985 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1327_math_optimized.java](1327_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 304 KB | 11303741 |
| [1327_math_optimized.py](1327_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 208 KB | 11324836 |
| [1327_parsing_optimized.go](1327_parsing_optimized.go) | Go 1.14 x64 | parsing | O(1) | AC | 0.015 s | 796 KB | 11329104 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
