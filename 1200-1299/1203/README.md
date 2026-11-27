# 1203. The most talks one person can attend

[Timus 1203](https://acm.timus.ru/problem.aspx?space=1&num=1203) · difficulty 78 · greedy

Original problem by Magaz Asanov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A conference has `N ≤ 10⁵` interesting talks, each running from minute
`Ts` to minute `Te`, `1 ≤ Ts < Te ≤ 30000`. Two attended talks may not
overlap, and there must be at least one minute between them: after a
talk ending at 15 the next one can start at 16 at the earliest. Find the
largest number of talks one person can attend.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains integer N, 1 ≤ N ≤ 100000. Each of the next N lines contains integer start/end times Ts Te with 1 ≤ Ts < Te ≤ 30000.

## Output

The largest number of talks.

## Checking

Repository tests compare the integer answer token exactly, ignoring whitespace and line separators.

## Examples

### Example 1

Input:

```
7
8 10
1 2
5 8
3 5
6 7
10 11
12 14
```

Output:

```
5
```

## Solution

The classic greedy for interval scheduling: repeatedly take the talk that
ends first among those starting after the last chosen one ended. Any
optimal schedule can swap its first talk for that one without losing
anything, and the same argument repeats.

Times are small, so no sorting is needed: for each minute `e` keep the
latest start among the talks ending at `e`. Sweep the minutes in order;
when the latest start at `e` is after the last chosen end, a talk ending
at `e` can be taken, and it is the earliest ending one available.
`O(N + T)` for `T = 30000`.

The latest-start array uses O(T) storage. C++/Go/Java bases read talks incrementally with fixed input buffering, so their space is O(T + B), where B is the bounded buffer size. Simple Python additionally retains O(I) input/tokens and O(N) slice references; simple Rust retains the O(I) input String and O(N) parsed values: total O(T + I + N). Optimized Go also retains the whole input bytes, using O(T + I). Buffered optimized C++/Rust and the chunked Python array need O(T + B + L) space, L the longest token length. Their 16-bit latest-start entries reduce constants without changing the O(T) table size. These bounds include input storage; all algorithms still do O(N + T) bucket work.

Pitfalls:

- a talk starting the very minute the previous one ends is not allowed,
  so the test is a strict "start > last end";
- repeated identical talks count once at most.

The answers were compared with a separately written solution on 300
random inputs and on every test.

## Optimized solutions

The optimized solutions (C++, Rust) parse the numbers by hand straight
from the input buffer instead of `scanf` or reading the whole input into
a string, and keep the latest starts as 16-bit numbers, since all times
are at most 30 000. C++ needs 0.001 s instead of 0.109 s and 164 KB
instead of 304 KB; Rust needs 276 KB instead of 4176 KB, while its paired time increases from 0.015 s to 0.031 s.

The optimized Python solution reads the input in 16 KB blocks and parses
it lazily, and keeps the latest starts in an `array` of 16-bit numbers
instead of a list: 980 KB instead of 14476 KB, although the time grows
from 0.109 s to 0.140 s.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1203_greedy_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328521 (Go 1.14 x64): **0.031 s / 6052 KB**. Archived comparison: `1203_greedy.go` (Go 1.14 x64) — 0.125 s / 4420 KB (#11303282).

## Language notes

This review only names the existing 64-bit integer/float conversion parameters in `1203_greedy_optimized.go`; expanding the constants reproduces the original executable text. The simple Go version and all meaningful comments remain unchanged.

No language needs anything special.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1203_greedy.cpp](1203_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + T) | AC | 0.109 s | 304 KB | 11283566 |
| [1203_greedy.go](1203_greedy.go) | Go 1.14 x64 | greedy | O(N + T) | AC | 0.125 s | 4420 KB | 11303282 |
| [1203_greedy.java](1203_greedy.java) | Java 1.8 | greedy | O(N + T) | AC | 0.109 s | 620 KB | 11303457 |
| [1203_greedy.py](1203_greedy.py) | Python 3.12 x64 | greedy | O(N + T) | AC | 0.109 s | 14476 KB | 11283574 |
| [1203_greedy.rs](1203_greedy.rs) | Rust 1.75 x64 | greedy | O(N + T) | AC | 0.015 s | 4176 KB | 11283580 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1203_greedy_optimized.cpp](1203_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N + T) | AC | 0.001 s | 164 KB | 11303579 |
| [1203_greedy_optimized.py](1203_greedy_optimized.py) | Python 3.12 x64 | greedy | O(N + T) | AC | 0.14 s | 980 KB | 11303723 |
| [1203_greedy_optimized.rs](1203_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(N + T) | AC | 0.031 s | 276 KB | 11303580 |
| [1203_greedy_optimized.go](1203_greedy_optimized.go) | Go 1.14 x64 | greedy | O(N + T) | AC | 0.015 s | 6228 KB | 11330991 |
