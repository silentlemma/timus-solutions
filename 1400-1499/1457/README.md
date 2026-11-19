# 1457. Heating Main

[Timus 1457](https://acm.timus.ru/problem.aspx?space=1&num=1457) · difficulty 69 · math

Original problem by Nikita Rybak, Dmitry Kovalioff and Ilya Grebnov, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A straight heating main passes under N places (1 ≤ N ≤ 1000) at
positions P[i] (0 ≤ P[i] ≤ 10⁶). The effort of walking a distance is
proportional to its square. Find the point of the main where the average
effort of reaching the places is smallest, with at least six digits
after the decimal point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N positions.

## Output

The best point.

## Checking

Repository tests compare numeric tokens with |actual-reference| <= 0.0000011·max(1,|reference|), reject nonfinite values, and compare nonnumeric tokens exactly.

## Examples

### Example 1

Input:

```
3
7 4 5
```

Output:

```
5.333333
```

## Solution

The average of (x − P[i])² is a parabola in x whose derivative
2 (x − mean) vanishes at the arithmetic mean of the positions, so the
answer is the sum divided by N. The sum is at most 10⁹ and fits in a signed
32-bit integer. `O(N)`.

Pitfalls:

- rounding to six digits may differ between languages when the mean
  ends exactly in a five, as 1/128 does (test 05); any answer within the
  required precision is accepted.

## Optimized solutions

`1457_math_optimized.py`. Keep the arithmetic mean that minimizes the sum of squared distances. Sum the N integer positions exactly, then perform only the final floating-point division and print six fractional digits. N<=1000 and positions<=10^6 bound the sum by 10^9, exactly representable in f64. Time O(N); numerical meaning and output precision are unchanged. Sum a map of byte-token integers instead of constructing the decoded input and a separate integer-position list. The byte tokens and sliced references still require O(N) storage. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1457_math.py`: time 0.078 s → 0.156 s; memory 504 KB → 248 KB.

`1457_math_optimized.rs`. Keep the arithmetic mean that minimizes the sum of squared distances. Sum the N integer positions exactly, then perform only the final floating-point division and print six fractional digits. N<=1000 and positions<=10^6 bound the sum by 10^9, exactly representable in f64. Time O(N); numerical meaning and output precision are unchanged. Accumulate positions as they arrive, so the input String and value vector disappear. Auxiliary state O(1); printf emits the one f64 mean. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1457_math.rs`: time 0.015 s → 0.031 s; memory 252 KB → 88 KB.

The optimized Java solution parses the numbers by hand instead of
`Scanner` and prints the mean without a formatter: it rounds the exact
value with integers, `(sum · 10⁶ + N / 2) / N`, and writes the integer
part and six digits of the fraction: 412 KB instead of 2612 KB, with
the same time.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1457_math_optimized.py`: time place 69/71, memory place 1/71 in this comparable sample.

`1457_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1457_math.cpp](1457_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 144 KB | 11286425 |
| [1457_math.go](1457_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1120 KB | 11286427 |
| [1457_math.java](1457_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 2612 KB | 11286431 |
| [1457_math.py](1457_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 504 KB | 11286429 |
| [1457_math.rs](1457_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 252 KB | 11286434 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1457_math_optimized.java](1457_math_optimized.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 412 KB | 11303608 |
| [1457_math_optimized.py](1457_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N) | AC | 0.156 s | 248 KB | 11324843 |
| [1457_math_optimized.rs](1457_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 88 KB | 11324854 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
