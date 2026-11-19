# 1293. Eniya

[Timus 1293](https://acm.timus.ru/problem.aspx?space=1&num=1293) · difficulty 14 · math

Original problem by Den Raskovalov, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N rectangular panels of A by B metres must be coated on both sides,
and one square metre takes one nanogram of coating
(1 ≤ N, A, B ≤ 100). How many nanograms are needed?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, A and B on one line.

## Output

The number of nanograms.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
5 2 3
```

Output:

```
60
```

## Solution

Each panel has two sides of A · B square metres, so the answer is
2 · N · A · B. `O(1)`.

Pitfalls:

- both sides count: forgetting the factor 2 gives 30 instead of 60 on
  the example (test 01);
- the largest answer is 2 000 000, which fits easily in 32 bits
  (test 03).

## Optimized solutions

`1293_math_optimized.go`. Keep the two-sided panel area 2*N*A*B. All three inputs are at most 100, so the result is at most 2000000; no floating-point conversion is needed. The new code reads the three numbers directly rather than invoking formatted scanners or retaining decoded input and, in Rust, a value vector. Time and bounded arithmetic state O(1); the teaching formula sources remain unchanged. Portable os.Stdin.Read/os.Stdout.Write and direct integer conversion use fixed 4096-byte input and output buffers. Partial writes are handled before reusing the output buffer. The original simple Accepted source is preserved.

Compared with `1293_math.go`: time 0.031 s → 0.031 s; memory 1152 KB → 796 KB.

`1293_math_optimized.py`. Keep the two-sided panel area 2*N*A*B. All three inputs are at most 100, so the result is at most 2000000; no floating-point conversion is needed. The new code reads the three numbers directly rather than invoking formatted scanners or retaining decoded input and, in Rust, a value vector. Time and bounded arithmetic state O(1); the teaching formula sources remain unchanged. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1293_math.py`: time 0.078 s → 0.109 s; memory 344 KB → 188 KB.

`1293_math_optimized.rs`. Keep the two-sided panel area 2*N*A*B. All three inputs are at most 100, so the result is at most 2000000; no floating-point conversion is needed. The new code reads the three numbers directly rather than invoking formatted scanners or retaining decoded input and, in Rust, a value vector. Time and bounded arithmetic state O(1); the teaching formula sources remain unchanged. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1293_math.rs`: time 0.031 s → 0.015 s; memory 224 KB → 48 KB.

The optimized Java solution parses the three numbers byte by byte from
`System.in` instead of using `Scanner`: 312 KB instead of 1596 KB, with
the same time.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1293_math_optimized.go`: time place 22/32, memory place 1/32 in this comparable sample.

`1293_math_optimized.py`: time place 935/1017, memory place 3/1017 in this comparable sample.

`1293_math_optimized.rs`: time place 1/12, memory place 1/12 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1293_math.cpp](1293_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11303289 |
| [1293_math.go](1293_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1152 KB | 11284602 |
| [1293_math.java](1293_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1596 KB | 11284606 |
| [1293_math.py](1293_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 344 KB | 11284604 |
| [1293_math.rs](1293_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 224 KB | 11284608 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1293_math_optimized.java](1293_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 312 KB | 11303733 |
| [1293_math_optimized.go](1293_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 796 KB | 11325047 |
| [1293_math_optimized.py](1293_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 188 KB | 11324826 |
| [1293_math_optimized.rs](1293_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 48 KB | 11324850 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
