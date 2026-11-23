# 1032. Choosing numbers whose sum is a multiple of N

[Timus 1032](https://acm.timus.ru/problem.aspx?space=1&num=1032) · difficulty 302 · prefix_sums, math

Original problem from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `N` positive integers (`1 ≤ N ≤ 10 000`, each at most 15 000, repeats
allowed), choose one or more of them whose sum is divisible by `N`. If there
is no such choice, print 0.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `N` numbers, one per line.

## Output

The number of chosen numbers, then the chosen numbers one per line, in any
order; or 0.

## Checking

Any valid choice is accepted. The checker verifies that every number is
used at most as many times as it is given, that at least one number is
chosen and that the sum is a multiple of `N`.

## Examples

### Example 1

Input:

```
4
3
8
6
1
```

Output:

```
1
8
```

### Example 2

Input:

```
1
15000
```

Output:

```
1
15000
```

## Solution

**A choice always exists**, and it can even be a block of consecutive
numbers. Look at the `N + 1` prefix sums `S_0 = 0, S_1, ..., S_N` modulo
`N`. They take at most `N` different values, so by the **pigeonhole
principle** two of them are equal, `S_i ≡ S_j (mod N)` with `i < j`; then
`a_{i+1} + ... + a_j = S_j - S_i` is a multiple of `N`.

Walk through the numbers keeping the prefix sum modulo `N` and the first
position where each remainder appeared (remainder 0 at position 0). The
first repeated remainder gives the block. `O(N)`.

So the answer 0 is never needed.

Pitfalls:

- the remainder 0 must be "seen" at position 0, so that a prefix that is
  itself a multiple of `N` is found;
- the numbers in the output are the values, not their positions;
- `N = 1`: any single number works.

## Optimized solutions

`1032_prefix_sums_optimized.py`. Python keeps the first repeated prefix remainder modulo N. Store both first positions and read values in unsigned-short arrays; N<=10000, values<=15000 and the offset positions fit 16 bits. Zero marks unseen, and the empty prefix is pre-recorded. Equal remainders identify a contiguous witness whose sum is divisible by N. Print its length and values in chunks of at most 512, limiting temporary joined strings instead of building one complete witness string. Flush stdout before exiting inside main with both arrays still live. Time O(N), storage O(N) plus a bounded output chunk. The teaching solution remains unchanged.

Exact-source Python 3.12 x64 Accepted #11327433: 0.078 s / 820 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/51, memory 1/51. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. Both metrics rank first, so the separate language target also passes; no asterisk. The previously documented optimized run #11310314 (Python 3.12 x64) was 0.109 s / 1068 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1032_prefix_sums_optimized.py`: 0.078 s / 820 KB; retained teaching base `1032_prefix_sums.py`: 0.093 s / 2608 KB.

The accepted base implementations [1032_prefix_sums.cpp](1032_prefix_sums.cpp), [1032_prefix_sums.go](1032_prefix_sums.go), [1032_prefix_sums.java](1032_prefix_sums.java), [1032_prefix_sums.rs](1032_prefix_sums.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

`1032_prefix_sums_optimized.java`. Java updates the prefix residue as values arrive. Zero means unseen in the first-position array; real positions are offset by one, with the empty prefix recorded initially. On the first repeated residue, output the intervening saved values directly through a bounded buffer. Equal residues make that segment sum divisible by N. This removes the array fill and the complete output builder while retaining O(N) time and O(N) storage.

Compared with `1032_prefix_sums.java`: time 0.156 s → 0.109 s; memory 944 KB → 592 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1032_prefix_sums_optimized.rs`. Retain the archived algorithm and its integer types. Convert decimal integer tokens directly instead of calling the general string parser; negative values are accumulated with their sign so the minimum signed value remains representable. Existing input storage and algorithmic bounds are unchanged.

Accepted #11328489 (Rust 1.75 x64): **0.031 s / 456 KB**. Archived comparison: `1032_prefix_sums.rs` (Rust 1.75 x64) — 0.046 s / 464 KB (#11278437).

## Language notes

These notes describe the simple implementations.

The same pass everywhere.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1032_prefix_sums.cpp](1032_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 232 KB | 11278431 |
| [1032_prefix_sums.go](1032_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 1368 KB | 11278432 |
| [1032_prefix_sums.java](1032_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.156 s | 944 KB | 11278435 |
| [1032_prefix_sums.py](1032_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.093 s | 2608 KB | 11278433 |
| [1032_prefix_sums.rs](1032_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 464 KB | 11278437 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1032_prefix_sums_optimized.py](1032_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(N) time; O(N) storage + bounded output chunk | AC | 0.078 s | 820 KB | 11327433 |
| [1032_prefix_sums_optimized.java](1032_prefix_sums_optimized.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 592 KB | 11325005 |
| [1032_prefix_sums_optimized.rs](1032_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.031 s | 456 KB | 11328489 |
