# 1264. Workdays

[Timus 1264](https://acm.timus.ru/problem.aspx?space=1&num=1264) · difficulty 21 · math

Original problem by Den Raskovalov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A function counts how many times each value from 0 to M occurs in an
array of N elements, written as one `if` line for every element and
every value (0 ≤ N, M ≤ 40 000). One line takes one second to write.
How many seconds does the whole function take?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M.

## Output

The number of seconds.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
3 1
```

Output:

```
6
```

## Solution

There are N elements and M + 1 values, so the answer is N · (M + 1).
`O(1)`.

Pitfalls:

- the values run from 0 to M, so there are M + 1 of them, not M;
- the answer reaches 40 000 · 40 001 = 1 600 040 000, close to the
  32-bit signed limit; C++, Go, Java and Rust use 64 bits (test 05);
- N = 0 gives 0 whatever M is (tests 02, 03).

## Optimized solutions

`1264_math_optimized.java`. Keep the direct product N*(M+1), including either zero boundary. N,M<=40000 bound the result by 1600040000, so int arithmetic is exact. Fixed 256-byte input and 128-byte output buffers plus reusable digits reduce input/formatting overhead. O(1) arithmetic and auxiliary space; no array simulation or changed counting algorithm, and the simple source is preserved.

Exact-source Java 1.8 Accepted #11327465: 0.093 s / 340 KB. Saved 2026-11-20 compiler-cohort comparison: time 42/1224, memory 11/1224. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303732 was 0.14 s / 296 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1264_math_optimized.java`: 0.093 s / 340 KB; retained teaching base `1264_math.java`: 0.109 s / 1552 KB.

`1264_math_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327022 measures 0.046 s / 596 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 1/597, memory rank 524/597. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11324828, 0.109 s / 208 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`1264_math_optimized.go`. Keep the direct count N*(M+1), including zero elements and the value zero among the M+1 possibilities. No array simulation is introduced. With N,M<=40000 the product is at most 1600040000; Go retains int64 arithmetic and Python uses exact integers. Byte-number input and direct output reduce runtime overhead, while time and auxiliary state remain O(1). Portable os.Stdin.Read/os.Stdout.Write and direct integer conversion use fixed 4096-byte input and output buffers. Partial writes are handled before reusing the output buffer. The original simple Accepted source is preserved.

Compared with `1264_math.go`: time 0.031 s → 0.031 s; memory 1060 KB → 820 KB.

`1264_math_optimized.py`. Keep the direct count N*(M+1), including zero elements and the value zero among the M+1 possibilities. No array simulation is introduced. With N,M<=40000 the product is at most 1600040000; Go retains int64 arithmetic and Python uses exact integers. Byte-number input and direct output reduce runtime overhead, while time and auxiliary state remain O(1). The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1264_math.py`: time 0.093 s → 0.109 s; memory 320 KB → 208 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1264_math_optimized.go`: time place 1/16, memory place 1/16 in this comparable sample.

Earlier PyPy comparison: `1264_math_optimized.py`: time place 539/597, memory place 1/597 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1264_math.cpp](1264_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11284168 |
| [1264_math.go](1264_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB | 11284172 |
| [1264_math.java](1264_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1552 KB | 11284181 |
| [1264_math.py](1264_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 320 KB | 11284180 |
| [1264_math.rs](1264_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB | 11284182 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1264_math_optimized.java](1264_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 340 KB | 11327465 |
| [1264_math_optimized.go](1264_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 820 KB | 11328270 |
| [1264_math_optimized.py](1264_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.046 s | 596 KB | 11327022 |
