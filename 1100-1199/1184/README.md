# 1184. The longest equal pieces that cables can be cut into

[Timus 1184](https://acm.timus.ru/problem.aspx?space=1&num=1184) · difficulty 244 · binary_search

Original problem by Vladimir Pinaev and Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given N cables, choose a common piece length, in whole centimetres,
and cut at least K pieces of that length. A piece must come from one cable;
leftovers cannot be joined. Maximize the length. `1≤N,K≤10000`. Every
cable is between 1 m and 100 km, inclusive, specified exactly to a
centimetre. Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains N and K. Each of the next N lines contains
one cable length in metres with exactly two digits after the decimal point.

## Output

Print the largest feasible length in metres with exactly two fractional
digits. If no positive whole-centimetre length can give K pieces, print `0.00`.

## Checking

Compare the single decimal token, retaining exactly two fractional
digits. Every new program passed 13 repository inputs and 39 independent
extra inputs in its actual target compiler/interpreter. All 156 extra
outputs and exit codes were re-read against an exact rational oracle:
merge the decreasing sequences `c/1,c/2,...` for all cables, take the Kth
largest value and floor it to centimetres. This enumerates critical piece
lengths without a feasibility binary search. The Python candidate also
ran on 2889 host stocks; small cases independently tried every integer
length. Coverage includes 1.13 m, 0.00 output, N/K=10000, total length
10¹¹, maximum cable length, explicit plus signs, and narrowing only after
the 64-bit minimum. The 2889 count is Python, not native executions.
All four published sources have their own exact-byte Accepted.

## Examples

### Example 1

Input:

```
4 11
8.02
7.43
4.57
5.39
```

Output:

```
2.00
```

## Solution

Parse each cable as an integer number c of centimetres. With exactly
two fractional digits, removing the decimal point is exact; do not parse
binary floating point and multiply it by 100. The range is `100≤c≤10⁷`.

For a positive trial length L, one cable gives `floor(c/L)` pieces.
Let `F(L)=Σ floor(c/L)`. Every term is nonincreasing, so `F(L)≥K` is
a monotone predicate. The simple versions binary-search the largest
feasible integer L between zero and the longest cable. Zero is a sentinel
for no positive answer, never a divisor. An upper midpoint gives positive
L whenever the loop actually probes from a zero lower bound.

If L is feasible, all smaller positive lengths are feasible. If L fails,
all greater lengths fail. Keeping the feasible lower side and discarding
the impossible side therefore leaves the maximum at termination. Return
centimetres as `L/100` and the two-digit remainder, including leading zero.
Time is `O(N log C)` and space `O(N)`, with `C=max(c)≤10⁷`. Any stored
input tokens must also be counted. The zero-answer case is possible even
though each input cable is at least one metre.

## Optimized solutions

The `_optimized` files retain the same exact integer binary search,
with tighter proved bounds and smaller input/storage representations.
Let M be the longest cable and S the total length. A single longest cable
can provide K pieces of length `floor(M/K)`, so `low=M/K` is a valid lower
bound whenever positive; zero keeps the sentinel interpretation. Any
feasible L satisfies both `L≤M` and `K·L≤S`, hence
`high=min(M,floor(S/K))`. These bounds cannot discard the optimum.

Search while low<high using `mid=(low+high+1)/2`. It is positive, even
when low=0. Count pieces only until reaching K: all remaining summands are
nonnegative, so early exit preserves the predicate. This often reduces
work but leaves worst-case `O(N log C)`. All individual lengths and search
bounds fit 32 bits. S can reach `10¹¹` and is accumulated in 64 bits in
native code; piece counts also use wide accumulators. In particular,
`S/K` must be minimized with M in 64 bits before narrowing to 32 bits.
The regression `S/K=2³²+100` would otherwise corrupt the high bound.

C++ and Java parse bounded byte streams directly into 32-bit arrays,
skipping the decimal dot of each length token. Java avoids whole-input
strings, long arrays and locale-formatting machinery. Rust uses a bounded
reader and Vec of u32, without a full input string or per-token replacement.
CPython reads each prescribed cable line into `array('I')`, without
retaining a full token list or boxed-integer list. Auxiliary I/O buffers
are bounded; cable storage remains linear. All five readable bases remain
byte for byte unchanged.

Exact-source Accepted memory: C++ 168 versus 280 KB (40.0% less), Java
448 versus 6284 KB (92.9% less), Python 516 versus 1580 KB (67.3% less),
Rust 220 versus 420 KB (47.6% less). C++ times 0.031→0.015 s differ by
only one judge tick, so time alone is not used for admission. Java is
0.125→0.093 s; Python stays 0.078 s and Rust stays 0.015 s. All four
qualify independently by measured memory, not by timing noise.

## Language notes

The original five implementations retain their straightforward search.
The new Python source was accepted in CPython 3.12; no PyPy metrics are
substituted. C++, Java and Rust meet the current rating profile. Python
is second by time and first by memory in the filtered snapshot, so its
admitted row keeps a star and room for improvement. Go has no eligible
competing authors here: its base gives formal coverage, not evidence of
superiority. The C++ target is top 15% or first ten places in both metrics;
other families require first in both. Each memory gain uses its own
unchanged same-language simple Accepted base.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1184_binary_search.cpp](1184_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N log C) | AC | 0.031 s | 280 KB | 11283357 |
| [1184_binary_search.go](1184_binary_search.go) | Go 1.14 x64 | binary_search | O(N log C) | AC | 0.031 s | 1688 KB | 11283358 |
| [1184_binary_search.java](1184_binary_search.java) | Java 1.8 | binary_search | O(N log C) | AC | 0.125 s | 6284 KB | 11283361 |
| [1184_binary_search.py](1184_binary_search.py) | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 1580 KB | 11283360 |
| [1184_binary_search.rs](1184_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 420 KB | 11283363 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1184_binary_search_optimized.cpp](1184_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O(N log C) | AC | 0.015 s | 168 KB | 11308739 |
| [1184_binary_search_optimized.java](1184_binary_search_optimized.java) | Java 1.8 | binary_search | O(N log C) | AC | 0.093 s | 448 KB | 11308743 |
| [1184_binary_search_optimized.py](1184_binary_search_optimized.py) \* | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 516 KB | 11308745 |
| [1184_binary_search_optimized.rs](1184_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 220 KB | 11308751 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
