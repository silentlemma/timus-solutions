# 1031. The cheapest set of railway tickets with three fare bands

[Timus 1031](https://acm.timus.ru/problem.aspx?space=1&num=1031) · difficulty 392 · dp, two_pointers

Original problem from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` stations (`2 ≤ N ≤ 10 000`) lie on a line; station 1 is at distance 0
and the others at given increasing distances (at most `10^9`, neighbouring
stations at most `L3` apart). A ticket covers one ride between two stations
at distance `X`: it costs `C1` if `X ≤ L1`, `C2` if `L1 < X ≤ L2`, `C3` if
`L2 < X ≤ L3`, and longer rides need several tickets, changing at stations
(`1 ≤ L1 < L2 < L3 ≤ 10^9`, `1 ≤ C1 < C2 < C3 ≤ 10^9`). Find the cheapest
way between two given stations; the answer does not exceed `10^9`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`L1 L2 L3 C1 C2 C3`, then `N`, then two distinct station numbers in
`1..N` (in either order). The next `N - 1` lines contain distinct positive
integer distances from station 1 to stations 2..`N`, in increasing order.

## Output

The smallest total price.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 6 8 20 30 40
7
2 6
3
5
9
12
17
19
```

Output:

```
70
```

### Example 2

Input:

```
1 2 3 1 2 3
2
2 1
1
```

Output:

```
1
```

## Solution

Swap the stations so that `a < b`; going backwards never helps. Let
`cost[i]` be the cheapest way from `a` to station `i`, with `cost[a] = 0`;
the last ticket goes from some station `j` to `i` and costs the price of the
band of `x[i] - x[j]`.

**Quadratic DP.** Try every `j` with `x[i] - x[j] ≤ L3`. That is up to
`N^2 / 2 = 5·10^7` steps when one ticket reaches far — enough in C++, not in
Python.

**Three pointers.** `cost` never decreases along the line: a way to station
`i + 1` ends with a ticket from some `j`, and the ticket from `j` to `i` is
not longer, so not more expensive. Therefore, for a ticket of band `k`, the
best start is the **farthest** station `j` with `x[i] - x[j] ≤ Lk` — it has
the smallest `cost` among all starts that band reaches. As `i` grows, these
farthest starts only move forward, so keep one pointer per band and advance
it while the distance exceeds `Lk`. Each step tries three candidates:
`O(N)` in total.

Both DP approaches store `O(N)` positions and costs; the three pointers
add only constant state. Whole-input Python and Rust bases also retain
`O(I)` input storage, where `I` is the input length. Optimized Python uses
`O(N)` packed arrays and bounded input blocks. Optimized Rust stores only
`K = b - a + 1` positions/costs, using `O(K)` space; optimized Go reserves
fixed arrays for the limit of 10000 stations. These are linear capacities
in the station limit, not constant space independent of that limit.

Pitfalls:

- the stations may be given in decreasing order;
- a ticket of a cheaper band is used for any shorter ride, so a ride of
  length `X ≤ L1` costs `C1`, not `C3`;
- the answer fits in 32 bits, but use 64-bit integers for sums anyway.

## Optimized solutions

Go and Rust keep one moving pointer per fare, to the earliest station still within its range. The minimum cost of reaching a station is nondecreasing, so that pointer gives the cheapest predecessor for the fare. Both versions read positions in order and keep only the interval between the two endpoints. The bound on the answer allows positions and costs to use 32-bit integers. Go uses fixed arrays for at most 10000 stations and direct byte input and output.

The base three-pointer C++ and Java programs also cover their fast set
without duplicate files. The shared [rating criteria](../../RATING_CRITERIA.md)
compare time alone for their sub-1-MiB measurements. Simple Python remains
a teaching version: its 1684 KB exceeds the cached small-cohort memory
limit, while optimized Python at 896 KB qualifies by time alone. The
separate optimized Python source therefore supplies Python's fast set.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1031_dp_two_pointers_optimized.py`. Store positions and costs in unsigned 64-bit arrays instead of Python integer lists. The same ticket DP and moving pointers are retained; The 64-bit elements provide arithmetic headroom; valid coordinates remain at most `10^9`. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328768 (Python 3.12 x64): **0.078 s / 896 KB**. Archived comparison: `1031_dp_two_pointers.py` (Python 3.12 x64) — 0.078 s / 1684 KB (#11278428).

`1031_dp_two_pointers_optimized.py`: the current revision names the unchanged ASCII-space threshold.

## Language notes

These notes describe the simple implementations.

- **C++**, **Go**, **Python**, **Java**, **Rust**: three pointers.
- **C++** also has the quadratic DP.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1031_dp.cpp](1031_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.078 s | 284 KB | 11278426 |
| [1031_dp_two_pointers.cpp](1031_dp_two_pointers.cpp) | G++ 13.2 x64 | dp, two_pointers | O(N) | AC | 0.015 s | 280 KB | 11278425 |
| [1031_dp_two_pointers.go](1031_dp_two_pointers.go) | Go 1.14 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 1440 KB | 11278427 |
| [1031_dp_two_pointers.java](1031_dp_two_pointers.java) | Java 1.8 | dp, two_pointers | O(N) | AC | 0.093 s | 668 KB | 11278429 |
| [1031_dp_two_pointers.py](1031_dp_two_pointers.py) | Python 3.12 x64 | dp, two_pointers | O(N) | AC | 0.078 s | 1684 KB | 11278428 |
| [1031_dp_two_pointers.rs](1031_dp_two_pointers.rs) | Rust 1.75 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 516 KB | 11278430 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1031_dp_two_pointers_optimized.go](1031_dp_two_pointers_optimized.go) | Go 1.14 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 884 KB | 11311110 |
| [1031_dp_two_pointers_optimized.rs](1031_dp_two_pointers_optimized.rs) | Rust 1.75 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 276 KB | 11310607 |
| [1031_dp_two_pointers_optimized.py](1031_dp_two_pointers_optimized.py) | Python 3.12 x64 | dp, two_pointers | O(N) | AC | 0.093 s | 928 KB | 11331076 |
