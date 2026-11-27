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
For each of 2 ≤ T ≤ 33 333 queries with 2 ≤ N ≤ 33 333 and
3 ≤ K ≤ 33 333, print the distance from the ship to base N.

Time limit: 1 second. Memory limit: 64 MB.

## Input

T, then T lines with N, K and L, where `L ≥ 1`. The ship lies between
the two named bases; L is its offset within that gap.

## Output

T lines with the distances.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
2
3 12 100
16 12558 152
```

Output:

```
629
1
```

## Solution

Counting the route's end as base 0, the gap before base N is F applied
N − 1 times to K, and the answer is that gap minus L. Our example
confirms it: 12 → 9 → 729, and 729 − 100 = 629.

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

All fixed/generated answers are checked by independent function
composition (binary lifting), without stopping at 153. Exhaustive
inspection of all 11111 valid keys separately certifies the fourteen-step bound.

## Optimized solutions

`1292_math_optimized.py`. Retain repeated digit-cube sums until N-1 steps or the fixed point 153. Precompute ten digit cubes and read queries/output in 4096-byte chunks instead of retaining all queries and answers. For promised multiples of three K<=33333, the already checked finite convergence bound is fourteen steps, so the total is O(Q) under these fixed bounds and O(B) buffer storage. An unchanged intermediate value also stops the loop. Every digit-cube transformation uses exact integer arithmetic.

Compared with `1292_math.py`: time 0.265 s → 0.125 s; memory 7972 KB → 3 344 KB.

Optimized C++ and Go evaluate each query until the requested step or the fixed point 153 and write answers through a bounded buffer. Go looks up each digit's cube in a ten-entry table. C++ combines two precomputed cube sums for three-digit blocks and keeps the ship offset and subtraction in signed 64-bit integers. Go also uses signed 64-bit offsets and direct byte buffers for input and output, without allocating a string per number. Auxiliary space is constant.

Simple Java already meets the saved ordinary comparison on time and
memory and can be reused as a fast solution without a duplicate file.
Simple Python and Rust remain teaching implementations: Python misses
the sparse time limit, and Rust misses the sparse memory limit. Their
separate optimized files supply qualifying results. Both Go versions
and optimized C++ also qualify; simple C++ remains for clarity.
The earlier universal admission claim for all base files is superseded.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1292_math_implementation_optimized.rs`. Read tokens through a bounded native byte buffer; short tokens stay inline and only long tokens allocate spill storage. Decimal conversion retains the signed bounds without keeping the full command input. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328962 (Rust 1.75 x64): **0.015 s / 144 KB**. Archived comparison: `1292_math.rs` (Rust 1.75 x64) — 0.001 s / 2124 KB (#11284596).

The current Rust fast file only extracts the inline token capacity 32 into
`INLINE_TOKEN_BYTES` to satisfy strict lint; its algorithm and comments
are unchanged. #11328962 and its measurements describe the preceding
exact bytes.

## Language notes

Use the shared [rating criteria](../../RATING_CRITERIA.md), without a
language-specific first-place rule or separate 30%-improvement admission.
Ordinary comparisons require top ten or top 15% for the required metrics.
With 1–10 eligible rivals on the same compiler, the sparse reference
comparison replaces rank admission. Below 1024 KB only time is required.
Foreign times below `0.015 s` are excluded; only our own time uses that
floor. Raw Accepted pairs, including `0.001 s`, remain unchanged.
There is no date or submission-ID cutoff.

The 18 November 2026 PyPy ranks (time 1/19, memory 5/19) are historical.
The source-bound frozen audit admits optimized PyPy #11325483 by the
nine-rival exact-compiler reference: `0.125 s / 3344 KB` versus limits
`0.19665 s / 7672.80 KB`. Base CPython #11284592 has `0.265 s`, above
its `0.21505 s` limit. Base Rust #11284596 uses 2124 KB, above its
1904.40 KB limit; optimized Rust #11328962 uses 144 KB and passes time.

Let `I` and `Z` be input/output bytes and `B` fixed buffers. Simple C++
and Go stream queries and use `O(B)` auxiliary space. Java retains
the output (`O(Z+B)`), simple Python retains input tokens and answers
(`O(I+T+Z)`), and simple Rust retains input (`O(I+B)`). Fast C++/Go
use fixed lookup tables/buffers; fast Rust uses bounded input/output
and inline tokens for the promised short numbers: `O(B)` space.
Fast Python keeps at most a block of tokens and an output block; under
the promised bounded number lengths it is also `O(B)`. Here `Q = T`
in the earlier fast-Python discussion. With arbitrary token length S,
its pending token and Rust spill storage would add `O(S)` space.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1292_math.cpp](1292_math.cpp) | G++ 13.2 x64 | math | O(T * 14 * digits) | AC | 0.046 s | 136 KB | 11284589 |
| [1292_math.go](1292_math.go) | Go 1.14 x64 | math | O(T * 14 * digits) | AC | 0.015 s | 1452 KB | 11284591 |
| [1292_math.java](1292_math.java) | Java 1.8 | math | O(T * 14 * digits) | AC | 0.109 s | 4740 KB | 11284593 |
| [1292_math.py](1292_math.py) | Python 3.12 x64 | math | O(T * 14 * digits) | AC | 0.265 s | 7972 KB | 11284592 |
| [1292_math.rs](1292_math.rs) | Rust 1.75 x64 | math | O(T * 14 * digits) | AC | 0.001 s | 2124 KB | 11284596 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1292_math_optimized.cpp](1292_math_optimized.cpp) | G++ 13.2 x64 | math | O(T · 14 · digits) | AC | 0.015 s | 84 KB | 11310876 |
| [1292_math_optimized.go](1292_math_optimized.go) | Go 1.14 x64 | math | O(T · 14 · digits) | AC | 0.001 s | 800 KB | 11311114 |
| [1292_math_optimized.py](1292_math_optimized.py) | PyPy 3.10 x64 | math | O(Q) under fixed K bounds; O(B) space | AC | 0.125 s | 3344 KB | 11325483 |
| [1292_math_implementation_optimized.rs](1292_math_implementation_optimized.rs) | Rust 1.75 x64 | math, implementation | O(T * 14 * digits) | AC | 0.015 s | 144 KB | 11331118 |
