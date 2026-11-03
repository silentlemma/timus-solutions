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

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1385_math.cpp`; covering source `1385_math_optimized.cpp`; time/memory places 1/1, other-author entries 39/39.

- Go: preferred teaching base `1385_math_number_theory.go`; covering source `1385_math_number_theory.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1385_math_number_theory.java`; covering source `1385_math_optimized.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1385_math_number_theory.py`; covering source `1385_math.py`; time/memory places 2/7, other-author entries 20/20.

- Rust: preferred teaching base `1385_math.rs`; covering source `1385_math.rs`; time/memory places 1/1, other-author entries 0/0.

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

\* Accepted; the rating target is not yet met. This version may be optimized further.
