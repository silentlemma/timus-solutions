# 2035. Splitting a total under two upper bounds

[Timus 2035](https://acm.timus.ru/problem.aspx?space=1&num=2035) · difficulty 78 · math

Original problem by Kirill Borozdin, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given integers `X,Y,C` with `0 ≤ X,Y,C ≤ 1000000000`, find any integers
`A,B` satisfying `0 ≤ A ≤ X`, `0 ≤ B ≤ Y` and `A+B=C`.
Time limit: 0.5 seconds; memory limit: 64 MB.

## Input

One line with `X Y C`. There is one instance and no test-count prefix.

## Output

Any valid pair `A B`, or the exact word `Impossible` if no pair exists.
The pair `0 0` is valid when `C=0`.

## Checking

A checker verifies both bounds and the sum; `Impossible` is accepted
only when no pair exists. Any valid pair is accepted.

## Examples

```
2 7 5
```

```
2 3
```

```
9 15 100
```

```
Impossible
```

## Solution

Take A as large as possible, A = min(X, C), and B = C − A. If B ≤ Y,
the pair works; otherwise no pair does, because any other A is smaller
and only makes B larger. `O(1)`.

Pitfalls:

- A = X alone may exceed C and make B negative;
- zero summands are allowed, and any valid pair is accepted.

## Optimized solutions

`2035_math_optimized.py`. Keep the bounded-summand construction A=min(X,C), B=C-A. These values are nonnegative and A<=X; if B>Y no feasible pair exists, otherwise emit it. C=0 correctly gives 0 0. This uses only the three input values and a few bounded integers, O(1) time and state. Inline the former solve/main wrappers and parse raw byte tokens; there is no new feasibility algorithm. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `2035_math.py`: time 0.078 s → 0.14 s; memory 436 KB → 200 KB.

`2035_math_optimized.rs`. Keep the bounded-summand construction A=min(X,C), B=C-A. These values are nonnegative and A<=X; if B>Y no feasible pair exists, otherwise emit it. C=0 correctly gives 0 0. This uses only the three input values and a few bounded integers, O(1) time and state. Read the three signed i64 values directly and emit numbers without the input String and formatted output. The nonnegative statement domain keeps every subtraction safe. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `2035_math.rs`: time 0.031 s → 0.046 s; memory 228 KB → 68 KB.

The optimized C++ solution parses the three numbers by hand with
`getchar` instead of `iostream`: 100 KB instead of 400 KB, with the same
time.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2035_math_optimized.py`: time place 47/54, memory place 1/54 in this comparable sample.

`2035_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2035_math.cpp](2035_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 400 KB | 11293165 |
| [2035_math.go](2035_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1088 KB | 11293168 |
| [2035_math.java](2035_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 492 KB | 11303531 |
| [2035_math.py](2035_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB | 11293171 |
| [2035_math.rs](2035_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11293174 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2035_math_optimized.cpp](2035_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 100 KB | 11303670 |
| [2035_math_optimized.py](2035_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.14 s | 200 KB | 11324848 |
| [2035_math_optimized.rs](2035_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 68 KB | 11324857 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
