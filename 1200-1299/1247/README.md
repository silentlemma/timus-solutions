# 1247. No segment heavier than its length plus N

[Timus 1247](https://acm.timus.ru/problem.aspx?space=1&num=1247) · difficulty 240 · bitmask, dp, prefix_sums

Original problem by Alexander Mironenko, from the Ural State University Personal Contest, March 1, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given positive `S, N ≤ 30000` and `S` integers `0 ≤ A_i ≤ 100`, with the PROMISE `sum(A_i) = S + N`, decide whether every nonempty contiguous segment satisfies `A_i + … + A_j ≤ (j − i + 1) + N`. Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`S N`, followed by `S` lines, one sequence value per line.

## Output

Print uppercase `YES` if all segments satisfy the bound, otherwise `NO`.

## Checking

Exact answer tokens. Each new source has its own full target-runtime checks, independent mathematical comparisons and source-bound Accepted; retained simple versions keep their own metrics.

## Examples

### Example 1

Input:

```
4 3
2
3
0
2
```

Output:

```
YES
```

### Example 2

Input:

```
4 5
1
0
5
3
```

Output:

```
NO
```

## Solution

Subtract one from each value and write `p_0 = 0`,
`p_i = sum(A_1 − 1, …, A_i − 1)`. The given total says `p_S = N`.
The condition for a segment is `p_j − p_(i−1) ≤ N`.

Necessity: each prefix is a segment, so `p_i ≤ N`; each suffix after a
prefix is a segment, so `N − p_i ≤ N` and therefore `p_i ≥ 0`.
Sufficiency: if every prefix lies in `[0, N]`, every segment difference
is at most `N − 0 = N`. Thus check just `0 ≤ p_i ≤ N` while streaming
the input. A prefix above `N` is already a violating segment; a negative
prefix makes the remaining suffix too heavy. The program may stop with
`NO` immediately. This equivalence uses the promised total and is not
claimed for arbitrary inputs without it.

These five `prefix_sums` programs are the preferred simple versions:
`O(S)` time and one running prefix, `O(1)` algorithm state. Rust retains
its input text; that input buffer is additional to the scan state.
All earlier Accepted sources remain byte for byte. Their general Kadane
DP keeps the largest sum ending at each position,
`ending = max(0, ending + A_i − 1)`, and compares the maximum with `N`.
It also takes `O(S)` time and works without needing the total-sum promise.

## Optimized solutions

Keep the older dynamic-programming alternatives and all five simpler streaming prefix bases; compare with the latter. The promised total S+N makes the condition equivalent to every adjusted prefix p_i=sum(A_1..A_i)-i lying in[0,N]. Native C++ retains that algorithm with a bounded 4096 byte read buffer and direct output. Python uses C-backed iterators: accumulate raw sums, subtract increasing positions, then apply floor division by N+1. Since N>0, an integer p has p//(N+1)==0 exactly when 0<=p<=N, including negative p. any detects the first nonzero quotient without a Python loop or retained sequence. O(S)time, O(1)working storage; Python is compared with the current 0.109 s/328 KB streaming base, not the older 1312 KB DP.

- `1247_prefix_sums_optimized.cpp`: 0.015 s / 64 KB; base `1247_prefix_sums.cpp`: 0.031 s / 104 KB; relative change: time -51.6%, memory -38.5%.
- `1247_prefix_sums_optimized.py`: 0.078 s / 416 KB; base `1247_prefix_sums.py`: 0.109 s / 328 KB; relative change: time -28.4%, memory +26.8%.

## Language notes

The saved snapshots are from 2 and 4 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1247_prefix_sums.cpp`; covering source `1247_prefix_sums_optimized.cpp`; time/memory places 1/1, other-author entries 75/75.

- Go: preferred teaching base `1247_prefix_sums.go`; covering source `1247_prefix_sums.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1247_prefix_sums.java`; covering source `1247_prefix_sums.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1247_prefix_sums.py`; covering source `1247_prefix_sums_optimized.py`; time/memory places 1/1, other-author entries 17/17.

- Rust: preferred teaching base `1247_prefix_sums.rs`; covering source `1247_prefix_sums.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1247_prefix_sums.cpp](1247_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(S) | AC | 0.031 s | 104 KB | 11308243 |
| [1247_prefix_sums.go](1247_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(S) | AC | 0.046 s | 1316 KB | 11308245 |
| [1247_prefix_sums.java](1247_prefix_sums.java) | Java 1.8 | prefix_sums | O(S) | AC | 0.109 s | 444 KB | 11308247 |
| [1247_prefix_sums.py](1247_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(S) | AC | 0.109 s | 328 KB | 11308241 |
| [1247_prefix_sums.rs](1247_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(S) | AC | 0.031 s | 468 KB | 11308248 |

### Other Accepted approaches

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1247_dp.cpp](1247_dp.cpp) | G++ 13.2 x64 | dp | O(S) | AC | 0.031 s | 124 KB | 11283945 |
| [1247_dp.go](1247_dp.go) | Go 1.14 x64 | dp | O(S) | AC | 0.031 s | 1348 KB | 11283948 |
| [1247_dp.java](1247_dp.java) | Java 1.8 | dp | O(S) | AC | 0.109 s | 528 KB | 11283951 |
| [1247_dp.py](1247_dp.py) | Python 3.12 x64 | dp | O(S) | AC | 0.093 s | 1312 KB | 11283950 |
| [1247_dp.rs](1247_dp.rs) | Rust 1.75 x64 | dp | O(S) | AC | 0.062 s | 840 KB | 11283953 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1247_prefix_sums_optimized.cpp](1247_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(S) time; O(1) working storage | AC | 0.015 s | 64 KB | 11309382 |
| [1247_prefix_sums_optimized.py](1247_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(S) time; O(1) working storage | AC | 0.078 s | 416 KB | 11309921 |
