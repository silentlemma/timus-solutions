# 1444. Elephpotamus

[Timus 1444](https://acm.timus.ru/problem.aspx?space=1&num=1444) · difficulty 262 · geometry

Original problem by Ekaterina Vasilyeva (idea and text) and Alexander Mironenko, Alexey Lakhtin and Den Raskovalov (programming), from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N pumpkins (3 ≤ N ≤ 30000) lie at distinct integer points with
coordinates from −1000 to 1000, not all on one line. An elephpotamus
starts at pumpkin 1 and eats it; after each pumpkin it can be sent in a
straight line to any remaining pumpkin. The animal stops for good as soon
as it steps on its own tracks, so the walk must never touch itself. Find
the largest number of pumpkins K it can eat and the order of the walk,
starting with 1.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then the coordinates of the pumpkins 1 to N.

## Output

K, then the numbers of the pumpkins in the order they are eaten, one per
line. Any valid walk is accepted.

## Checking

Accept any maximal visit order starting at the first point, with distinct point indices and no self-contact or self-intersection of the path.

## Examples

### Example 1

Input:

```
4
0 0
10 10
0 10
10 0
```

Output:

```
4
1
3
2
4
```

## Solution

All N pumpkins can always be eaten. Sort the others by the angle of the
direction from pumpkin 1, and on one ray by the distance, nearer first;
the comparisons use integer cross products, so they are exact. Walking
in this order sweeps around pumpkin 1 like a fan: every step either goes
further out along the same ray or moves into the next direction, so the
walk stays inside one narrow wedge at a time and never comes back.

The only danger is the start of the circle. If two neighbouring
directions are half a turn or more apart, the step between them could
pass through pumpkin 1 or cut across earlier steps, so the circle is cut
right after that gap; there can be at most one such gap, since not all
pumpkins lie on one line. Without such a gap, cut at any boundary between
distinct ray groups, starting with the nearest pumpkin of the next
group. Never split a ray group across the cut: returning to its nearer
pumpkins would touch the initial segment. The solutions' default cut at
the start of the angular sort already satisfies this rule.
`O(N log N)`.

The simple versions use O(N) auxiliary storage for point/direction records, sorted indices and any accumulated output, including sorting workspace. Whole-input readers additionally retain I input bytes; no pairwise intersection matrix is constructed.

Pitfalls:

- several pumpkins on one ray must be eaten from the nearest outwards
  (tests 03, 06, gen2);
- keep each ray group together when choosing the cut, even if every
  angular gap is below half a turn (test 06);
- a gap of exactly half a turn, with pumpkins on both sides of pumpkin
  1 along one line (tests 03, 09);
- pumpkin 1 in a corner leaves a gap of more than half a turn (tests
  04, gen3, gen4).

## Optimized solutions

`1444_geometry_optimized.py`. Keep the same exact packed angular ranks, Manhattan-distance and ID tie fields, sorting and half-turn gap selection. Move construction into main so hot-loop state uses local variables rather than module dictionary lookups. Coordinate bounds, integer rank separation and output order are unchanged; no floating angle approximation is added. O(N log N) time and O(N) storage. The new run is faster but uses 4100 KB versus the previous optimized 3976 KB; all teaching sources remain.

Exact-source CPython 3.12 Accepted #11326683: 0.14 s / 4100 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 2/74, memory rank 1/74. At least 1024 KB: both strict metrics are required and pass.

- `1444_geometry_optimized.py`: 0.14 s / 4100 KB; retained teaching base `1444_geometry.py` (Python 3.12 x64): 0.453 s / 11600 KB; time change -69.1%; memory change -64.7%.

Replace repeated cross-product comparisons during sorting with exact packed integer direction keys. A rational parameter based on Manhattan length is monotone around the origin. The coordinate bound gives a minimum separation between distinct fractions, so scaling and taking the floor cannot merge distinct directions. Pack the direction rank, Manhattan distance |dx|+|dy| and original index; same-ray points still appear nearest first. The angular gap identifies the same cyclic cut as the simple proof. No floating-point angle is used.

- `1444_geometry_optimized.cpp`: 0.015 s / 320 KB; base `1444_geometry.cpp`: 0.062 s / 444 KB; relative change: time -75.8%, memory -27.9%.
- `1444_geometry_optimized.go`: 0.031 s / 1188 KB; base `1444_geometry.go`: 0.078 s / 2336 KB; relative change: time -60.3%, memory -49.1%.
- `1444_geometry_optimized.java`: 0.093 s / 736 KB; base `1444_geometry.java`: 0.187 s / 6232 KB; relative change: time -50.3%, memory -88.2%.

- `1444_geometry_optimized.rs`: 0.046 s / 1244 KB; base `1444_geometry.rs`: 0.031 s / 2104 KB; relative change: time +48.4%, memory -40.9%.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1444_implementation_parsing_optimized.rs`. Keep the exact angular ordering and uint32 indices. Write the walk through a persistent bounded buffer instead of allocating a decimal string per vertex and retaining the full output. Specialize direct output to the answer types actually used, avoiding generic formatting dispatch and temporary answer strings. Fixed text uses native writes; numeric writers handle the required signed or unsigned magnitudes exactly. Mathematical decisions and archived simple versions are preserved.

Accepted #11329201 (Rust 1.75 x64): **0.015 s / 668 KB**. Archived comparison: `1444_geometry.rs` (Rust 1.75 x64) — 0.031 s / 2104 KB (#11286291).

## Language notes

The shared [criteria](../../RATING_CRITERIA.md) apply, with memory ignored only strictly below 1024 KB, no separate first-place or 30%-improvement rule. C++/Java/Python use ordinary top-ten or top-15% comparisons; exact-compiler samples of 1–10 rivals instead use the selected reference and jitter/tick limits.

Retain `1444_geometry.*` as the teaching bases. The covering C++/Go/Java/Python sources are `1444_geometry_optimized.*`; C++ time is 1/353 at 320 KB, Java time 1/260 at 736 KB, and Python time/memory 2/74 and 1/74 at 4100 KB. Go optimized 0.031 s / 1188 KB meets its five-rival limits 0.12535 s / 3459.20 KB.

Rust coverage comes from `1444_implementation_parsing_optimized.rs`, Accepted #11329201: 0.015 s / 668 KB, which passes the single-rival time limit 0.078 s with memory ignored. Older `1444_geometry_optimized.rs` is retained and marked: its 1244 KB exceeds the required memory limit 929.20 KB. Simple Rust at 2104 KB also fails that limit. The old rank 1/2 alone does not establish admission under the small-cohort override. Historical paired measurements above remain observations, not current alternative criteria.

Only lint-required constants in `1444_implementation_parsing_optimized.rs` were given names; their values, algorithm and comments are unchanged. Accepted #11329201 describes the preceding exact bytes and paired metrics.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1444_geometry.cpp](1444_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.062 s | 444 KB | 11286284 |
| [1444_geometry.go](1444_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.078 s | 2336 KB | 11286286 |
| [1444_geometry.java](1444_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.187 s | 6232 KB | 11286290 |
| [1444_geometry.py](1444_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.453 s | 11600 KB | 11286289 |
| [1444_geometry.rs](1444_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 2104 KB | 11286291 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1444_geometry_optimized.cpp](1444_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 320 KB | 11309261 |
| [1444_geometry_optimized.go](1444_geometry_optimized.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1188 KB | 11309263 |
| [1444_geometry_optimized.java](1444_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.093 s | 736 KB | 11309262 |
| [1444_geometry_optimized.py](1444_geometry_optimized.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.14 s | 4100 KB | 11326683 |
| [1444_geometry_optimized.rs](1444_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 1244 KB | 11309264 |
| [1444_implementation_parsing_optimized.rs](1444_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(N log N) | AC | 0.046 s | 656 KB | 11331111 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
