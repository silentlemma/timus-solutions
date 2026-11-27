# 1346. Intervals of Monotonicity

[Timus 1346](https://acm.timus.ru/problem.aspx?space=1&num=1346) · difficulty 297 · greedy

Original problem by Alexander Klepinin, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A function F is given on the integer grid A, A + 1, …, B, with
0 ≤ A < B ≤ 100 000 and integer values from −100 000 to 100 000. Split the grid
into the fewest intervals on each of which F does not decrease or does
not increase, and print how many there are.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A and B, then the integer values F(A), …, F(B), separated by spaces or line
breaks.

## Output

The smallest number of intervals.

## Checking

Token comparison (`judging: tokens`): one integer, the minimum number
of disjoint monotone intervals of grid points. Endpoints or the actual
partition are not required; whitespace is ignored.

## Examples

### Example 1

Input:

```
1 10
1 2 3 4 2 1 -1 3 6 7
```

Output:

```
3
```

## Solution

The intervals split the points of the grid, so the step between the
last point of one interval and the first point of the next one is free.
Any part of a monotone interval is monotone again. So it never hurts to
make the first interval as long as possible, and the same holds for
every next one: the greedy count is the smallest.

An interval is stretched while it stays monotone. Its direction is set
by its first step that is not flat, and flat steps fit either
direction. The first step against that direction ends the interval, and
the next one starts at the following point. `O(B − A)`.

Pitfalls:

- the step between two intervals is free: 1 3 2 4 needs only 2
  intervals, 1 3 and 2 4 (test 02);
- flat steps belong to the interval whichever way it goes, and a
  constant function is a single interval (tests 03, 05 and 06);
- the values may come on several lines.

The counts were compared with a dynamic program over all splits on 500
random functions of up to 12 points.

## Optimized solutions

`1346_greedy_optimized.cpp`. Keep the greedy monotonicity scan. On a nonzero direction reversal, start a new interval and reset its direction: the crossing step belongs to neither interval. Equal values do not set a direction. Only the previous value, direction and count are retained, giving O(B-A+1) time and O(1) auxiliary storage. Replace formatted input with a 16384-byte fread buffer plus one sentinel byte; carry signs and partial digits across refills, checking EOF without a retry loop on empty input. Write the single count as raw decimal bytes. The shared scanner was checked at both buffer sizes with AddressSanitizer/UndefinedBehaviorSanitizer and 100019 values per size. The clearer teaching implementation remains.

C++ #11327408 `0.015 s / 92 KB` passes time rank 1/71 under the
shared [criteria](../../RATING_CRITERIA.md): below 1024 KB only time
counts, with no separate C++ goal. The earlier #11310334
`0.031 s / 84 KB` remains a distinct historical pair.

- `1346_greedy_optimized.cpp`: 0.015 s / 92 KB; retained teaching base `1346_greedy.cpp`: 0.062 s / 588 KB.

Historical previous-revision comparison: The C++ and Go versions keep the greedy scan and process each value as it arrives. They retain the previous value, the direction of the current interval and the interval count. The input buffer has fixed size, so the scan takes O(B − A + 1) time and O(1) additional space. The Accepted C++ run took 0.031 s and used 84 KB, compared with 0.062 s and 588 KB for the baseline. Go used 1588 KB instead of 2512 KB, with 0.031 s in both versions.

Java reuses its base: 900 KB activates time-only ranking, place 2/28.
Python qualifies through its streaming file `0.109 s / 724 KB`, not
the base `0.140 s / 11140 KB`: six exact CPython rivals give the third
reference limit 0.12535 s. Rust qualifies through the native file
`0.015 s / 56 KB`, not the 2632 KB base, which exceeds its 2047 KB
memory limit. One exact Rust rival gives a time limit of 0.031 s.
Qualifying bases need no identical optimized copies; teaching versions remain.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1346_greedy_optimized.py`. Stream the sequence, retaining only its previous value, current monotone direction and interval count. Equal values do not set a direction; a direction reversal starts the next interval. This gives linear time and constant algorithmic state. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328773 (Python 3.12 x64): **0.109 s / 724 KB**. Archived comparison: `1346_greedy.py` (Python 3.12 x64) — 0.14 s / 11140 KB (#11285126).

`1346_implementation_parsing_optimized.rs` retains the streaming
greedy scan. NativeNumbers parses signed i64 values across refills
in a 4096-byte buffer. NativeOutput writes the unsigned interval
count with a 20-byte digit scratch and 256-byte output buffer, then
flushes the newline with complete-write loops. Windows uses C-runtime
_read/_write and binary mode; other platforms use read/write. No
signed output routine or generic formatting dispatch is used.
Time O(B-A+1), fixed algorithmic state and bounded I/O storage.

This exact source has its own Accepted and meets the shared [rating criteria](../../RATING_CRITERIA.md). Time and memory below come from the same run; repeated runs can differ because of judge timing. Existing simple and distinct optimized implementations are preserved.

Accepted #11329367 (Rust 1.75 x64): **0.015 s / 56 KB**.

## Language notes

These notes describe the simple implementations.

- All five solutions make the same single pass.

Only lint-required constants in `1346_greedy_optimized.py` were given names; their values, algorithm and comments are unchanged. Accepted #11328773 describes the preceding exact bytes and paired metrics.

Only lint-required constants in `1346_implementation_parsing_optimized.rs` were given names; their values, algorithm and comments are unchanged. Accepted #11329367 describes the preceding exact bytes and paired metrics.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1346_greedy.cpp](1346_greedy.cpp) | G++ 13.2 x64 | greedy | O(B - A) | AC | 0.062 s | 588 KB | 11285122 |
| [1346_greedy.go](1346_greedy.go) | Go 1.14 x64 | greedy | O(B - A) | AC | 0.031 s | 2512 KB | 11285125 |
| [1346_greedy.java](1346_greedy.java) | Java 1.8 | greedy | O(B - A) | AC | 0.109 s | 900 KB | 11285127 |
| [1346_greedy.py](1346_greedy.py) | Python 3.12 x64 | greedy | O(B - A) | AC | 0.14 s | 11140 KB | 11285126 |
| [1346_greedy.rs](1346_greedy.rs) | Rust 1.75 x64 | greedy | O(B - A) | AC | 0.015 s | 2632 KB | 11285128 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1346_greedy_optimized.cpp](1346_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(B-A+1) time; O(1) auxiliary storage | AC | 0.015 s | 92 KB | 11327408 |
| [1346_greedy_optimized.go](1346_greedy_optimized.go) | Go 1.14 x64 | greedy | O(B - A + 1) | AC | 0.031 s | 1588 KB | 11310367 |
| [1346_greedy_optimized.py](1346_greedy_optimized.py) | Python 3.12 x64 | greedy | O(B-A+1) time; O(1) state + bounded input buffer | AC | 0.093 s | 792 KB | 11331069 |
| [1346_implementation_parsing_optimized.rs](1346_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(B-A+1) time; O(1) state + bounded input buffer | AC | 0.031 s | 60 KB | 11331112 |
