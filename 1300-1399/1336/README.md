# 1336. Problem of Ben Betsalel

[Timus 1336](https://acm.timus.ru/problem.aspx?space=1&num=1336) · difficulty 123 · math

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Write a whole number n, 1 ≤ n ≤ 10⁹, as the ratio of a square to a cube:
find whole numbers m and k from 1 to 10¹⁰⁰ with m² = k³ · n. Any such
pair is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number n.

## Output

m on the first line and k on the second.

## Checking

The checker accepts any m and k from 1 to 10¹⁰⁰ with m² = k³ · n.

## Examples

### Example 1

Input:

```
18
```

Output:

```
12
2
```

### Example 2

Input:

```
1
```

Output:

```
1
1
```

## Solution

Take k = n and m = n². Then m² = n⁴ = n³ · n. So a pair always exists,
which is also why the problem always has a solution. `O(1)`.

Pitfalls:

- m reaches 10¹⁸, which needs a 64-bit integer (test 03);
- the first sample shows a smaller pair; any correct one is accepted.

## Optimized solutions

The optimized Java solution reads n byte by byte from `System.in`
instead of creating a `Scanner`, whose regular expressions and locale
data are the main cost of a program that does one multiplication; n²
still fits in `long`, since it is at most 10¹⁸:
{1336_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1336_math_optimized.java`: time reduction +0.00%; memory reduction
  +77.24%; base: `1336_math.java`.

`1336_math_optimized.py`. Keep the exact construction m=n², k=n, because m²=n⁴=k³*n. It satisfies the allowed output bounds without factoring n. At n<=10^9 the largest emitted value is 10^18, safe even in signed i64. O(1) bounded arithmetic and storage. Use one print call with a newline separator instead of two calls; all calculations remain integer. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1336_math.py`: time 0.062 s → 0.109 s; memory 352 KB → 196 KB.

`1336_math_optimized.rs`. Keep the exact construction m=n², k=n, because m²=n⁴=k³*n. It satisfies the allowed output bounds without factoring n. At n<=10^9 the largest emitted value is 10^18, safe even in signed i64. O(1) bounded arithmetic and storage. Emit the two integers directly on separate lines, avoiding Rust formatting and the decoded input String. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1336_math.rs`: time 0.015 s → 0.031 s; memory 240 KB → 60 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1336_math_optimized.py`: time place 25/45, memory place 1/45 in this comparable sample.

`1336_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math.cpp](1336_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11285033 |
| [1336_math.go](1336_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11285034 |
| [1336_math.java](1336_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB | 11285036 |
| [1336_math.py](1336_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 352 KB | 11285035 |
| [1336_math.rs](1336_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB | 11285038 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1336_math_optimized.java](1336_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 356 KB | 11304378 |
| [1336_math_optimized.py](1336_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 196 KB | 11324908 |
| [1336_math_optimized.rs](1336_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 60 KB | 11324871 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
