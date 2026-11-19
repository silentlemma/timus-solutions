# 1292. Mars Space Stations

[Timus 1292](https://acm.timus.ru/problem.aspx?space=1&num=1292) · difficulty 380 · math

Original problem by Denis Musin, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Let F(x) be the sum of the cubes of the decimal digits of x, so
F(12) = 9. Space bases stand along a route: the first at distance K
from the route's end, and if the gap before base i is x, the gap after
it is F(x). The key K is a multiple of 3.

A ship is between bases N − 1 and N, at distance L from base N − 1.
For each of T ≤ 33 333 queries with 2 ≤ N ≤ 33 333 and
3 ≤ K ≤ 33 333, print the distance from the ship to base N.

Time limit: 1 second. Memory limit: 64 MB.

## Input

T, then T lines with N, K and L.

## Output

T lines with the distances.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
2
4 6 123
7 93 49
```

Output:

```
18
104
```

## Solution

Counting the route's end as base 0, the gap before base N is F applied
N − 1 times to K, and the answer is that gap minus L. The sample
confirms it: 6 → 216 → 225 → 141, and 141 − 123 = 18.

Applying F up to 33 332 times per query would be too slow for 33 333
queries, but the chain settles almost at once. Since d³ ≡ d (mod 3),
F keeps the remainder of the digit sum mod 3, so multiples of 3 stay
multiples of 3. F(153) = 1 + 125 + 27 = 153, and checking every
multiple of 3 up to 33 333 shows that each one reaches 153 within at
most 14 steps (12 558 is the slowest). So F is applied until either
N − 1 steps are done or the value is 153. `O(T · 14 · digits)`.

Pitfalls:

- the gap before base N takes N − 1 steps, not N − 2: the first base
  is already K away from the end (test 01);
- a chain can be cut just before it reaches 153 (test 03);
- the gap can be much larger than K, for example F(99) = 1458
  (test 05).

The answers were compared with applying F all N − 1 times.

## Optimized solutions

`1292_math_optimized.py`. Retain repeated digit-cube sums until N-1 steps or the fixed point 153. Precompute ten digit cubes and read queries/output in 4096-byte chunks instead of retaining all queries and answers. For promised multiples of three K<=33333, the already checked finite convergence bound is fourteen steps, so the total is O(Q) under these fixed bounds and O(B) buffer storage. An unchanged intermediate value also stops the loop. Every digit-cube transformation uses exact integer arithmetic.

Compared with `1292_math.py`: time 0.265 s → 0.125 s; memory 7972 KB → 3 344 KB.

Both versions evaluate each query until the requested step or the fixed point 153 and write answers through a bounded buffer. Go looks up each digit's cube in a ten-entry table. C++ combines two precomputed cube sums for three-digit blocks and keeps the ship offset and subtraction in signed 64-bit integers. Go also uses signed 64-bit offsets and direct byte buffers for input and output, without allocating a string per number. Auxiliary space is constant.

The accepted base implementations [1292_math.java](1292_math.java), [1292_math.py](1292_math.py), [1292_math.rs](1292_math.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1292_math_optimized.py`: time place 1/19, memory place 5/19 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1292_math.cpp](1292_math.cpp) | G++ 13.2 x64 | math | O(T * 14 * digits) | AC | 0.046 s | 136 KB | 11284589 |
| [1292_math.go](1292_math.go) | Go 1.14 x64 | math | O(T * 14 * digits) | AC | 0.015 s | 1452 KB | 11284591 |
| [1292_math.java](1292_math.java) \* | Java 1.8 | math | O(T * 14 * digits) | AC | 0.109 s | 4740 KB | 11284593 |
| [1292_math.py](1292_math.py) \* | Python 3.12 x64 | math | O(T * 14 * digits) | AC | 0.265 s | 7972 KB | 11284592 |
| [1292_math.rs](1292_math.rs) \* | Rust 1.75 x64 | math | O(T * 14 * digits) | AC | 0.001 s | 2124 KB | 11284596 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1292_math_optimized.cpp](1292_math_optimized.cpp) | G++ 13.2 x64 | math | O(T · 14 · digits) | AC | 0.015 s | 84 KB | 11310876 |
| [1292_math_optimized.go](1292_math_optimized.go) \* | Go 1.14 x64 | math | O(T · 14 · digits) | AC | 0.001 s | 800 KB | 11311114 |
| [1292_math_optimized.py](1292_math_optimized.py) \* | PyPy 3.10 x64 | math | O(Q) under fixed K bounds; O(B) space | AC | 0.125 s | 3344 KB | 11325483 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
