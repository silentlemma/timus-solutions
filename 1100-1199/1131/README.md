# 1131. Copying a program to N computers with K cables, one copy per cable per hour

[Timus 1131](https://acm.timus.ru/problem.aspx?space=1&num=1131) · difficulty 77 · math

Original problem by Stanislav Vasiliev and Alexander Mironenko, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A program is on one of `N` computers. In one hour a computer that has it
can copy it to one other computer over a cable, and there are `K` cables.
Find the least number of hours until all `N` computers have the program,
for `1 ≤ N, K ≤ 10⁹`.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`N` and `K` on one line.

## Output

The least number of hours.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
8 3
```

Output:

```
4
```

## Solution

In an hour, `min(have, K, N − have)` new computers get the program, where
`have` is the number of computers that already have it; copying as much
as possible every hour is clearly best. While `have < min(N, K)`, double
`have` and count one hour. If this reaches or exceeds `N`, all remaining
computers can receive the program in that hour, so stop; the counter may
overshoot `N` without changing the answer. This takes at most 30 hours.
Otherwise, once `have ≥ K`, each hour adds up to `K` computers, so the
remaining `N − have` computers need `⌈(N − have) / K⌉` more hours.
`O(log min(N, K))`.

Pitfalls:

- `N = 1` needs no hours;
- with `K = 1` and `N = 10⁹` the answer is almost `10⁹`, so the hours after
  the doubling must be computed by division, not one by one;
- the last hour can copy to fewer than `K` computers (test 11), so use
  ceiling division;
- the doubling counter can exceed `N` (test 05), but reaches at most
  `2³⁰`; 64-bit integers are safe, though signed 32-bit integers suffice.

The answers were compared with a binary search over the number of hours on
every test and with an hour-by-hour simulation for all `N < 200` and
`K < 70`.

## Optimized solutions

The optimized Java solution parses the two numbers byte by byte from
`System.in` instead of using `Scanner`: 0.093 s instead of 0.125 s and
344 KB instead of 1592 KB.

`1131_math_optimized.py`. Replace the doubling loop by d=(min(N,K)-1).bit_length(), the exact ceiling of log2(min(N,K)), including d=0 at one computer or cable. After 2^d computers are reached, add max(0,ceil((N-2^d)/K)) hours. This is the same two-phase model computed without floating logarithms. Raw-byte input and bounded integer arithmetic use O(1) time and state under N,K<=10^9. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1131_math.py`: time 0.078 s → 0.125 s; memory 424 KB → 196 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1131_math_implementation_optimized.rs`. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328944 (Rust 1.75 x64): **0.015 s / 180 KB**. Archived comparison: `1131_math.rs` (Rust 1.75 x64) — 0.046 s / 216 KB (#11279381).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1131_math_optimized.py`: time place 53/66, memory place 1/66 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1131_math.cpp](1131_math.cpp) | G++ 13.2 x64 | math | O(log min(N, K)) | AC | 0.015 s | 128 KB | 11279375 |
| [1131_math.go](1131_math.go) | Go 1.14 x64 | math | O(log min(N, K)) | AC | 0.015 s | 1076 KB | 11279376 |
| [1131_math.java](1131_math.java) | Java 1.8 | math | O(log min(N, K)) | AC | 0.125 s | 1592 KB | 11279379 |
| [1131_math.py](1131_math.py) | Python 3.12 x64 | math | O(log min(N, K)) | AC | 0.078 s | 424 KB | 11279378 |
| [1131_math.rs](1131_math.rs) | Rust 1.75 x64 | math | O(log min(N, K)) | AC | 0.046 s | 216 KB | 11279381 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1131_math_optimized.java](1131_math_optimized.java) | Java 1.8 | math | O(log min(N, K)) | AC | 0.093 s | 344 KB | 11303712 |
| [1131_math_optimized.py](1131_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 196 KB | 11324846 |
| [1131_math_implementation_optimized.rs](1131_math_implementation_optimized.rs) | Rust 1.75 x64 | math, implementation | O(log min(N, K)) | AC | 0.015 s | 180 KB | 11328944 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
