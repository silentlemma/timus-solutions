# 1082. Input that makes a quicksort count a given number of steps

[Timus 1082](https://acm.timus.ru/problem.aspx?space=1&num=1082) · difficulty 127 · constructive

Original problem by Nikita Shamgunov, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A given program reads `N` integers (`1 ≤ N ≤ 1000`) and sorts them with
a quicksort: the first element of a range is the pivot, and two indices
move towards each other, `j` from the right while elements are greater
than the pivot and `i` from the left while they are smaller, swapping
when they have not crossed (Hoare's partition). The program counts every
single move of `i` and `j` over all calls and wins if the total is
exactly `(N² + 3N − 4)/2`. Print `N` integers within `10^9` in absolute
value that make it win.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

`N` integers separated by spaces.

## Checking

Any suitable numbers are accepted. The checker runs the same partition on
the output and compares the count with `(N² + 3N − 4)/2`.

## Examples

### Example 1

Input:

```
3
```

Output:

```
1 2 3
```

## Solution

Print the sorted numbers `1, 2, …, N`. On a sorted range of length `k`
with the pivot at its left end, `j` walks from the right end all the way
to the pivot, `k` moves, and `i` makes one move onto the pivot; they meet
at once, so the range splits into the pivot alone and the other `k − 1`
elements, still sorted. The count is `k + 1` for every `k` from `N` down
to 2:

`(N + 1) + N + … + 3 = (N² + 3N − 4)/2`,

which is exactly the target. `O(N)`.

Pitfalls:

- other orders give other counts: for `3 2 1` the program counts 8
  moves instead of 7, because the swap changes how the ranges split;
- for `N = 1` the program counts nothing, and the target is 0 too.

The checker simulates the partition with an explicit stack and compares
the count.

## Optimized solutions

`1082_constructive_optimized.java`. Keep the ascending 1..N construction that produces the required quicksort worst case. Emit each integer through a reusable digit array and a 4096-byte output buffer rather than building the complete StringBuilder. Work is proportional to the number of emitted digits, O(N log N); auxiliary output storage is fixed. The constructive argument and teaching source remain.

Exact-source Java 1.8 Accepted #11327337: 0.078 s / 336 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/165, memory 1/165. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. Both metrics rank first, so the separate language target also passes; no asterisk. The previously documented optimized run #11304423 was 0.109 s / 364 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1082_constructive_optimized.java`: 0.078 s / 336 KB; retained teaching base `1082_constructive.java`: 0.093 s / 1592 KB.

The Python version writes the same sorted sequence in batches of at most 128 numbers, limiting the size of each temporary string.

### Measured gains

Each optimized version has Accepted and qualifies by ranking or by a reduction of at least 30% in time or memory against the base version. The base sources are retained. The asterisk concerns the rating target only.

- `1082_constructive_optimized.py` uses 440 KB versus 452 KB for the base, and takes 0.078 s instead of 0.062 s. In the 2026-11-16 ranking for current Python/PyPy interpreters it places 4th by time and 12th by memory out of 45. It qualifies by top 30% on both metrics and improves the base's 15th place in memory.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1082_constructive_optimized.rs`. Retain the archived algorithm and its integer types. Convert decimal integer tokens directly instead of calling the general string parser; negative values are accumulated with their sign so the minimum signed value remains representable. Existing input storage and algorithmic bounds are unchanged.

Accepted #11328494 (Rust 1.75 x64): **0.031 s / 288 KB**. Archived comparison: `1082_constructive.rs` (Rust 1.75 x64) — 0.046 s / 252 KB (#11279020).

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1082_constructive_parsing_optimized.go`. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments.

Accepted #11328879 (Go 1.14 x64): **0.015 s / 924 KB**. Archived comparison: `1082_constructive.go` (Go 1.14 x64) — 0.031 s / 1116 KB (#11279017).

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1082_constructive.cpp](1082_constructive.cpp).

- All languages print `1 … N` joined by spaces.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1082_constructive.cpp](1082_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 128 KB | 11279016 |
| [1082_constructive.go](1082_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1116 KB | 11279017 |
| [1082_constructive.java](1082_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.093 s | 1592 KB | 11279019 |
| [1082_constructive.py](1082_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.062 s | 452 KB | 11279018 |
| [1082_constructive.rs](1082_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 252 KB | 11279020 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1082_constructive_optimized.java](1082_constructive_optimized.java) | Java 1.8 | constructive | O(N log N) time; O(1) auxiliary space | AC | 0.078 s | 336 KB | 11327337 |
| [1082_constructive_optimized.py](1082_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 440 KB | 11307455 |
| [1082_constructive_optimized.rs](1082_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 288 KB | 11328494 |
| [1082_constructive_parsing_optimized.go](1082_constructive_parsing_optimized.go) | Go 1.14 x64 | constructive, parsing | O(N) | AC | 0.015 s | 924 KB | 11328879 |
