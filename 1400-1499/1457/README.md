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

`1457_math_optimized.py`. Read all integer tokens from the binary input stream into one list. Its first element is the count N. Starting the sum at −N cancels that header, so the remaining sum is exactly the sum of the positions. This lets the built-in sum traverse the integer list without slicing it. Divide once by N and print six decimal places. Time and temporary storage are both O(N).

The simple CPython run #11286429 used 0.078 s / 504 KB. The earlier PyPy implementation #11324843 used 0.156 s / 248 KB. The new CPython run #11328147 used 0.062 s / 432 KB.

`1457_math_optimized.rs`. Keep the arithmetic mean that minimizes the sum of squared distances. Sum the N integer positions exactly, then perform only the final floating-point division and print six fractional digits. N<=1000 and positions<=10^6 bound the sum by 10^9, exactly representable in f64. Time O(N); numerical meaning and output precision are unchanged. Accumulate positions as they arrive, so the input String and value vector disappear. Auxiliary state O(1); printf emits the one f64 mean. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1457_math.rs`: time 0.015 s → 0.031 s; memory 252 KB → 88 KB.

The optimized Java solution parses the numbers by hand instead of
`Scanner` and prints the mean without a formatter: it rounds the exact
value with integers, `(sum · 10⁶ + N / 2) / N`, and writes the integer
part and six digits of the fraction: 412 KB instead of 2612 KB, with
the same time.

## Language notes

The Rust comparison below uses the 18 November 2026 snapshot. Both comparisons use other authors on current judge compilers and count ties at the same rank.

`1457_math_optimized.py`. The CPython run ranked 3/71 by time and 23/71 by memory in the 18 November 2026 comparison. Its 432 KB footprint makes the time rank sufficient for strict admission. The asterisk marks the separate goal of first place in both metrics.

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
| [1457_math_optimized.py](1457_math_optimized.py) \* | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 432 KB | 11328147 |
| [1457_math_optimized.rs](1457_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 88 KB | 11324854 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
