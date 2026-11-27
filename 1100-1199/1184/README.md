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
3 7
4.17
3.08
2.54
```

Output:

```
1.27
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

Only the C++, Java, Python and Rust optimized sources use the
tighter bounds and early piece-count exit described next. The Go
I/O variant keeps low=0 and high=M, sums every cable at each probe,
and stores int64 lengths; it does not compute S or stop at K.
Its changes are token input and fixed integer output. Both search
forms are correct and have worst-case O(N log C) time/O(N) cable
storage; the Go reader has an 8192-byte refill buffer and retains
only the current token rather than all input.

Those four optimized implementations retain the same exact integer binary search,
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

Exact-source Accepted memory: C++ 168 versus 280 KB (40.0% less),
Java 448 versus 6284 KB (92.9% less), Python 516 versus 1580 KB
(67.3% less), Rust 220 versus 420 KB (47.6% less). C++ times
0.031→0.015 s differ by one tick, which alone is not proof of
algorithmic acceleration. Java is 0.125→0.093 s; Python stays
0.078 s and Rust stays 0.015 s. These are measured tradeoffs,
not an independent memory-gain admission requirement; qualification
uses the shared ranking policy.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1184_binary_search_parsing_implementation_optimized.go`. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments. Use an 8192-byte refillable input buffer instead of retaining the entire input. Tokens and partial/EOF reads retain their original meaning.

Accepted #11328934 (Go 1.14 x64): **0.031 s / 1332 KB**. Archived comparison: `1184_binary_search.go` (Go 1.14 x64) — 0.031 s / 1688 KB (#11283358).

The current Go I/O revision corrects the formatter comment and
names the unchanged 128-byte inline token capacity for structural lint:
it supports the integer %d verb with optional width and zero
padding; dot and newline are literal output, not floating formats. Accepted #11328934 (0.031 s / 1332 KB), the table and its cache
comparison describe preceding bytes.

## Language notes

Use the shared [rating criteria](../../RATING_CRITERIA.md), not
the former first-place/30%-gain profile. The source-bound cache
confirms C++/Java/Python optimized versions by time only below
1024 KB. Python has no failure marker; its qualifying CPython
base also covers the family, with both metrics at 1580 KB. Go
has two exact-version rivals, not an empty sample: its Accepted
I/O variant passes both limits 0.078 s / 1499.60 KB; the 1688 KB
base misses memory and remains an unstarred teaching version.
Rust base/optimized pass the exact-version one-rival comparison
using time only. C++/Java bases also remain for teaching despite
missing their metrics. Other compilers are used only when no
current-compiler rivals exist. No fresh standings were fetched;
all raw paired metrics and simple sources are preserved.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

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
| [1184_binary_search_optimized.py](1184_binary_search_optimized.py) | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 516 KB | 11308745 |
| [1184_binary_search_optimized.rs](1184_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 220 KB | 11308751 |
| [1184_binary_search_parsing_implementation_optimized.go](1184_binary_search_parsing_implementation_optimized.go) | Go 1.14 x64 | binary_search, parsing, implementation | O(N log C) | AC | 0.031 s | 1332 KB | 11331018 |
