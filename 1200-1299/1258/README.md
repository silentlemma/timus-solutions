# 1258. Billiards in an office

[Timus 1258](https://acm.timus.ru/problem.aspx?space=1&num=1258) · difficulty 417 · geometry

Original problem by Pavel Egorov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A programmer walks in straight lines through a W × D room
(2 ≤ W, D ≤ 1000), bouncing off the walls like a billiard ball. The
start and the end are integer points strictly inside the room, and the
walls hit are listed in order: L, R, F, B for the left (x = 0), right
(x = W), front (y = 0) and back (y = D) walls, at most 1000 hits, never
in a corner. Find the length of the walk, rounded to four digits after
the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

W and D, then x0 y0, then x1 y1, then the string of hits (possibly
empty).

## Output

The length of the walk.

## Examples

### Example 1

Input:

```
10 20
9 1
1 19
FLRLRB
```

Output:

```
52.8015
```

## Solution

Mirror the room at every hit instead of turning the walker: the walk
becomes one straight segment, whose horizontal and vertical extents add
up separately.

Along x, only the L and R hits matter, and they must alternate. With
none, the extent is |x1 − x0|. Otherwise the walker first goes to the
first side wall (x0 for L, W − x0 for R), crosses the room W wide
between each two consecutive side hits, and goes from the last side wall
to the end (x1 for L, W − x1 for R):

```text
dx = first + (k − 1) · W + last
```

The same with F, B and D gives dy, and the answer is √(dx² + dy²).
The order in which side and front/back hits interleave does not change
the length. `O(K)` for K hits.

Pitfalls:

- even in the smallest room, a valid path must avoid corners; a single
  wall hit is possible (test 07);
- the line of hits may be empty or missing altogether (test 02);
- the first hit on an axis may be either wall (tests 03, 06);
- dx and dy reach about 10⁶, so dx² + dy² needs 64 bits (test 08).

The answers were compared with the length of the straight segment from
which each random test was built (its crossings of the mirrored grid
give the hits) on 200 cases.

## Optimized solutions

The new Python implementation unfolds the path by reflecting its endpoint through the walls in reverse hit order: L maps x to −x, R to 2W−x, F maps y to −y and B to 2D−y. Each reflection undoes one bounce and preserves length, leaving one straight segment from the start. This removes the separate lists of horizontal and vertical hits and the math import; the square root uses exponent 0.5 and prints four decimals. Time is O(K), and the tokenized input occupies O(K) space. The ordinary Python implementation and all other language bases are preserved; the other four bases already cover the fast set.

The accepted base implementations [1258_geometry.cpp](1258_geometry.cpp), [1258_geometry.go](1258_geometry.go), [1258_geometry.java](1258_geometry.java), [1258_geometry.rs](1258_geometry.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1258_geometry_implementation_optimized.py`. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328529 (Python 3.12 x64): **0.062 s / 760 KB**. Archived comparison: `1258_geometry_optimized.py` (Python 3.12 x64) — 0.093 s / 396 KB (#11314897).

`1258_geometry_optimized.rs`. Count the hits and remember the first/last wall for each axis during one pass. This replaces the combined wall list and its two filtered copies with constant state; the unfolded-distance formula is unchanged.

Accepted #11328695 (Rust 1.75 x64): **0.015 s / 244 KB**. Archived comparison: `1258_geometry.rs` (Rust 1.75 x64) — 0.046 s / 264 KB (#11284107).

## Language notes

These notes describe the simple implementations.

- All languages count the hits per axis and use the same formula.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1258_geometry.cpp](1258_geometry.cpp) | G++ 13.2 x64 | geometry | O(K) | AC | 0.001 s | 220 KB | 11284098 |
| [1258_geometry.go](1258_geometry.go) | Go 1.14 x64 | geometry | O(K) | AC | 0.031 s | 1120 KB | 11284100 |
| [1258_geometry.java](1258_geometry.java) | Java 1.8 | geometry | O(K) | AC | 0.109 s | 1532 KB | 11284105 |
| [1258_geometry.py](1258_geometry.py) | Python 3.12 x64 | geometry | O(K) | AC | 0.125 s | 504 KB | 11284104 |
| [1258_geometry.rs](1258_geometry.rs) | Rust 1.75 x64 | geometry | O(K) | AC | 0.046 s | 264 KB | 11284107 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1258_geometry_optimized.py](1258_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(K) | AC | 0.093 s | 396 KB | 11314897 |
| [1258_geometry_implementation_optimized.py](1258_geometry_implementation_optimized.py) | Python 3.12 x64 | geometry, implementation | O(K) | AC | 0.062 s | 760 KB | 11328529 |
| [1258_geometry_optimized.rs](1258_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(K) | AC | 0.015 s | 244 KB | 11328695 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
