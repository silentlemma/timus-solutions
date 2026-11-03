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

**Java.** The added Java keeps exactly the same arithmetic and early return.
It replaces `Scanner` with `StreamTokenizer` over `InputStreamReader`;
no pattern-based token parser is needed for at most 101 integer tokens.
The tokenizer's numeric values represent these small integers exactly.
This is an implementation of the same algorithm, hence `_optimized`.

**Python/PyPy.** Keep the direct forward tram simulation as the teaching solution. The new algorithm works backwards: the smallest positive final gap is 1. Before an interval k, a surviving gap must be at least ceil(needed/k)*k because the forward map is k*floor(gap/k). Replace needed by that threshold and continue in reverse order. The threshold never decreases, so needed>L already proves that no surviving final gap is possible and catching is possible. Otherwise L survives every stop, so catching is impossible. Consume the input integer list from its end without making a reversed slice. This is O(N) time and O(N) input storage; its measured advantage is memory, not time.

- `1191_math_optimized.java`: 0.125 s / 408 KB; base `1191_math.java`: 0.125 s / 1636 KB; relative change: time -0.0%, memory -75.1%.
- `1191_dp.py`: 0.109 s / 236 KB; base `1191_math.py`: 0.062 s / 352 KB; relative change: time +75.8%, memory -33.0%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1191_math.cpp`; covering source `1191_math.cpp`; time/memory places 1/1, other-author entries 38/38.

- Go: preferred teaching base `1191_math.go`; covering source `1191_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1191_math.java`; covering source `1191_math_optimized.java`; time/memory places 2/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1191_math.py`; covering source `1191_dp.py`; time/memory places 8/1, other-author entries 12/12.

- Rust: preferred teaching base `1191_math.rs`; covering source `1191_math.rs`; time/memory places 1/1, other-author entries 0/0.

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
| [1191_math_optimized.java](1191_math_optimized.java) \* | Java 1.8 | math | O(N) | AC | 0.125 s | 408 KB | 11308408 |
| [1191_dp.py](1191_dp.py) \* | PyPy 3.10 x64 | dp | O(N) time, O(N) input integers | AC | 0.109 s | 236 KB | 11309781 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
