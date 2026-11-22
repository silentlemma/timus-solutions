# 1385. Interesting Number

[Timus 1385](https://acm.timus.ru/problem.aspx?space=1&num=1385) · difficulty 247 · math

Original problem by Alexander Ipatov, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A number with 2N digits and no leading zero is interesting if it is
divisible both by the number made of its first N digits and by the
number made of its last N digits. Count the interesting numbers with
2N digits, 1 ≤ N ≤ 10 000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

The count.

## Checking

Compare one integer token. Five added sources have 13 repository tests and 67 additional saved target executions each, including N=1,2,3,4,4300,4301,9999,10000. Python alone was additionally executed for every N=1..10000. Small counts were checked from the original divisibility definition through N=3 and by explicit multiples for N=4. These are separate proof counts, not 10000 runs of every language.

## Examples

### Example 1

Input:

```
1
```

Output:

```
14
```

The fourteen numbers are 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77,
88 and 99.

## Solution

Write the number as `A*M+B`, where `M=10^N`, `M/10≤A<M` and `0≤B<M`.
The second block can have leading zeroes but must be nonzero to divide the
whole number. Divisibility by A implies `B=k*A`, with `1≤k≤9`. Then
`k*A | A*M+B` is equivalent to `k | M`. For each such k, the possible A
are `M/10..M/k−1`, giving `M/k−M/10` choices. These k values are disjoint,
so add their counts.

The teaching Go, Java and Python directly compute M using their standard
big-integer facilities, test k=1..9 and perform exact divisions. This uses
`O(N)` decimal digits of storage, with a conservative `O(N²)` bound for
arithmetic and decimal conversion. Python disables the default integer-to-
decimal digit limit, which would reject legal large N. No fixed-width
integer holds the result. All earlier formula sources are retained;
C++ and Rust use the proved closed form because their standard libraries
do not supply a corresponding arbitrary-precision integer type.

## Optimized solutions

`1385_math_optimized.go`. Keep the derived divisibility coefficient using only 10^min(N,3), then stream the zero suffix. Raw Go 1.14 syscall.Read/Write with fixed 256-byte buffers replaces os.File initialization and the previous 4096-byte buffers, retrying EINTR and partial writes and recognizing zero-byte EOF. No answer table or arbitrary-precision allocation is added. O(N) output time and O(1) auxiliary space. Our exact Accepted uses 280 KB, 74.9% less than the short 1116 KB formula baseline; preserve both simple formula and big-integer teaching sources.

Compared with `1385_math.go`: time 0.031 s → 0.015 s; memory 1116 KB → 280 KB.

`1385_math_optimized.rs`. Keep the proved divisibility count Σ(10^N/d-10^(N-1)) over d=1..9 dividing 10^N, but compute its coefficient using only 10^min(N,3). The admissible d stabilize at 1,2,4,5,8 from N=3, so this yields 14,155 or 1575 and then exactly N-3 zero bytes when needed. These values are derived by the small divisor loop, not stored answers. Both variants emit the zero suffix directly instead of constructing Repeat/repeat strings or a concatenated answer. The output has N+1 digits: O(N) time, O(1) auxiliary state plus bounded I/O, no arbitrary-precision integer or N-sized buffer. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1385_math.rs`: time 0.015 s → 0.015 s; memory 224 KB → 56 KB.

Among k=1..9, only prime factors 2 and 5 can divide `10^N`.
For N=1 the valid k are 1,2,5, giving 9+4+1=14. For N=2 they are 1,2,4,5,
giving 90+40+15+10=155. For N≥3 the set stabilizes at 1,2,4,5,8.
Factoring out `10^(N−3)` leaves
`(1000−100)+(500−100)+(250−100)+(200−100)+(125−100)=1575`.
Thus emit `1575` followed by N−3 zeroes. These constants follow from the
divisibility count, not stored answers to selected inputs. Output has N+1
digits and needs `O(N)` time. The original formula versions build the
result string, using `O(N)` space; new C++/Java emit bounded zero blocks,
using `O(1)` auxiliary storage with respect to N.

Compare Python's retained formula with the direct big-integer teaching
version: the measured memory saving is 35.5%, with the same 0.078 s time.
New Java is slower than its big-integer base but saves memory; both facts
are recorded. A formula implementation below the ranking goal still
qualifies by its actual memory reduction and is marked with a star.

- `1385_math.py`: 0.078 s / 392 KB; base `1385_math_number_theory.py`: 0.078 s / 608 KB; relative change: time -0.0%, memory -35.5%.
- `1385_math_optimized.cpp`: 0.015 s / 120 KB; base `1385_math.cpp`: 0.015 s / 372 KB; relative change: time -0.0%, memory -67.7%.
- `1385_math_optimized.java`: 0.093 s / 432 KB; base `1385_math_number_theory.java`: 0.078 s / 1388 KB; relative change: time +19.2%, memory -68.9%.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1385_math_optimized.go`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

`1385_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1385_math.cpp](1385_math.cpp) | G++ 13.2 x64 | math | O(N) output time; O(N) string space | AC | 0.015 s | 372 KB | 11285827 |
| [1385_math_number_theory.go](1385_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(N^2) conservative arithmetic/conversion; O(N) digits | AC | 0.031 s | 1428 KB | 11308776 |
| [1385_math_number_theory.java](1385_math_number_theory.java) | Java 1.8 | math, number_theory | O(N^2) conservative arithmetic/conversion; O(N) digits | AC | 0.078 s | 1388 KB | 11308767 |
| [1385_math_number_theory.py](1385_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(N^2) conservative arithmetic/conversion; O(N) digits | AC | 0.078 s | 608 KB | 11308764 |
| [1385_math.rs](1385_math.rs) | Rust 1.75 x64 | math | O(N) output time; O(N) string space | AC | 0.015 s | 224 KB | 11285843 |

### Other Accepted approaches

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1385_math.go](1385_math.go) | Go 1.14 x64 | math | O(N) output time; O(N) string space | AC | 0.031 s | 1116 KB | 11285831 |
| [1385_math.java](1385_math.java) | Java 1.8 | math | O(N) output time; O(N) string space | AC | 0.109 s | 1648 KB | 11285839 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1385_math.py](1385_math.py) \* | Python 3.12 x64 | math | O(N) output time; O(N) string space | AC | 0.078 s | 392 KB | 11285836 |
| [1385_math_optimized.cpp](1385_math_optimized.cpp) | G++ 13.2 x64 | math | O(N) output time; O(1) auxiliary space | AC | 0.015 s | 120 KB | 11308752 |
| [1385_math_optimized.java](1385_math_optimized.java) | Java 1.8 | math | O(N) output time; O(1) auxiliary space | AC | 0.093 s | 432 KB | 11308759 |
| [1385_math_optimized.go](1385_math_optimized.go) \* | Go 1.14 x64 | math | O(N) time; O(1) space | AC | 0.015 s | 280 KB | 11328274 |
| [1385_math_optimized.rs](1385_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 56 KB | 11325098 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
