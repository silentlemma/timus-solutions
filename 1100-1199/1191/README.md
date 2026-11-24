# 1191. Can a police officer catch a thief who keeps changing trams?

[Timus 1191](https://acm.timus.ru/problem.aspx?space=1&num=1191) · difficulty 249 · dp, math

Original problem by Leonid Volkov, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A thief runs `L` minutes ahead of a police officer at the same speed. At each
of `N` stops the thief waits for a tram of a route running every `Ki`
minutes, at an unknown phase, and rides it to the next stop; the
officer follows to the same stop and takes the next tram of the same
route, making an arrest if the thief is still waiting. All trams move
at the same speed. Decide whether the officer can possibly catch the
thief before the `N` rides are over.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`L` and `N`, then `K1 … KN`, all positive integers below 100.

## Output

`YES` if a catch is possible, otherwise `NO`.

## Checking

Exact answer tokens. Each new source has its own full target-runtime checks, independent mathematical comparisons and source-bound Accepted; retained simple versions keep their own metrics.

## Examples

### Example 1

Input:

```
8 3
6 4 3
```

Output:

```
NO
```

### Example 2

Input:

```
15 4
7 3 13 6
```

Output:

```
YES
```

## Solution

Let `g` be the officer's arrival delay at the next stop and `K`
the tram interval. The thief waits some `w` with `0≤w<K`. If `g<K`,
choose `g<w<K`: the thief is still waiting when the officer arrives,
so capture is possible. If `g≥K`, capture at this stop is impossible.

Otherwise the officer leaves an integer number of tram intervals after
the thief. Their departure delay is `K·ceil((g−w)/K)`. Write `g=qK+r`,
`0≤r<K`. Since `w<K`, this delay cannot be less than `qK`. Choose
`w=r+(K−r)/2`, strictly between `r` and `K`, to attain `qK` without
arrival/departure ties. Equal journey times preserve the departure delay
as the next stop's arrival delay.

Thus the best attainable next state is `g−g%K`, with zero denoting
possible capture. This map is nondecreasing in `g`, so keeping a smaller
attainable delay can never hurt at later stops. Induction over routes
proves that following these minimum states finds a capture exactly when
any admissible timetable does. Return YES on zero, otherwise NO after
all `N` trams. A delay equal to `K` stays `K`; it is not a capture.
Interval one never decreases a positive integer delay.

Time `O(N)`. Streaming C++/Go/Java use constant arithmetic storage;
the retained Python/Rust programs keep `O(N)` input tokens. All input
integers are in 1..99, divisors are positive and the minimum delay never
increases, so ordinary integer remainder is exact and safe.

## Optimized solutions

`1191_math_optimized.java`. Keep the forward recurrence gap-=gap%interval and its immediate YES when gap becomes zero. The current Java revision uses a bounded 1024-byte primitive integer parser, replacing StreamTokenizer and character decoding. Arithmetic, interval order and early return are unchanged. Worst-case O(N) time, O(1) auxiliary space plus the fixed buffer; this is not the reverse Python algorithm.

Exact-source Java 1.8 Accepted #11326955: 0.078 s / 340 KB. Saved current-Java comparison, 2026-11-20: time rank 2/25, memory rank 1/25. With memory below 1024 KB, strict admission uses time only.

- `1191_math_optimized.java`: 0.078 s / 340 KB; retained teaching base `1191_math.java`: 0.125 s / 1636 KB; time change -37.6%; memory change -79.2%.

**Python/PyPy.** Keep the direct forward tram simulation as the teaching solution. The new algorithm works backwards: the smallest positive final gap is 1. Before an interval k, a surviving gap must be at least ceil(needed/k)*k because the forward map is k*floor(gap/k). Replace needed by that threshold and continue in reverse order. The threshold never decreases, so needed>L already proves that no surviving final gap is possible and catching is possible. Otherwise L survives every stop, so catching is impossible. Consume the input integer list from its end without making a reversed slice. This is O(N) time and O(N) input storage; its measured advantage is memory, not time.

`1191_math_optimized.rs`. Keep only the current gap, rounding it down to a multiple of each next interval. Once the gap becomes zero, later operations cannot change it, so the answer can be emitted immediately. Worst-case time is O(N), auxiliary space O(1). Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1191_math.rs`: time 0.015 s → 0.015 s; memory 212 KB → 52 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1191_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1191_math.cpp](1191_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 124 KB | 11283443 |
| [1191_math.go](1191_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1060 KB | 11283445 |
| [1191_math.java](1191_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 1636 KB | 11283449 |
| [1191_math.py](1191_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 352 KB | 11283447 |
| [1191_math.rs](1191_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 212 KB | 11283451 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1191_math_optimized.java](1191_math_optimized.java) \* | Java 1.8 | math | O(N) | AC | 0.078 s | 340 KB | 11326955 |
| [1191_dp.py](1191_dp.py) | PyPy 3.10 x64 | dp | O(N) time, O(N) input integers | AC | 0.109 s | 236 KB | 11309781 |
| [1191_math_optimized.rs](1191_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 52 KB | 11325089 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
