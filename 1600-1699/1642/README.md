# 1642. 1D Maze

[Timus 1642](https://acm.timus.ru/problem.aspx?space=1&num=1642) · difficulty 96 · implementation

Original problem by Daniil Ayzenshteyn, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A person stands at 0 on a line with obstacles and an exit at x. They
walk in a chosen direction, leave as soon as they reach the exit, and
turn around at every obstacle. For both starting directions, forward
(increasing) and backward, find the distance walked before leaving, or
report that the exit cannot be reached.

## Input

n and x (0 ≤ n ≤ 100), then n distinct obstacle coordinates. All
coordinates are non-zero, at most 1000 in absolute value, and no
obstacle is at the exit. Whatever the direction, the walk meets the
exit or an obstacle.

## Output

Two distances, forward first, or `Impossible`.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
3 -2
-10 -4 2
```

Output:

```
6 2
```

### Example 2

Input:

```
3 -2
10 -1 2
```

Output:

```
Impossible
```

## Solution

Only the nearest obstacles matter: left, the largest one below 0 (or −∞
if absent), and right, the smallest one above 0 (or +∞ if absent). The
exit is reachable exactly when left < x < right; otherwise
`Impossible`. In both directions the walk is then direct, or one detour:

- x > 0: forward x; backward to left and back, 2 · |left| + x;
- x < 0: forward to right and back, 2 · right + |x|; backward |x|.

The obstacle needed for the detour exists by the promise in the
statement. `O(n)`.

Pitfalls:

- an obstacle between the start and the exit blocks both directions,
  so one answer covers both (the second example, test 06);
- there may be no obstacles at all on the side of the exit.

The answers match an independent accepted implementation on 300 random
lines.

## Optimized solutions

`1642_implementation_optimized.py`. Keep the nearest walls and the same exit distances. A wall strictly between zero and the exit makes escape impossible, permitting immediate termination. Otherwise only the nearest opposite wall is needed for the one-turn route; the promised obstacle guarantees it exists. Read/split the bounded input at once, then use os.write and os._exit(0). O(N) time and O(I) token storage plus constant geometric state; unlike the previous revision this is not a bounded-buffer streaming parser.

Exact-source Python 3.12 x64 Accepted #11327790: 0.078 s / 744 KB. Saved 2026-11-20 compiler-cohort comparison: time 20/243, memory 225/243. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11325697 was 0.156 s / 252 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1642_implementation_optimized.py`: 0.078 s / 744 KB; retained teaching base `1642_implementation.py`: 0.093 s / 504 KB.

`1642_implementation_optimized.java`. Java retains the nearest obstacle on each side of zero and the same two travel distances. Any obstacle strictly between zero and the exit makes escape impossible permanently, so the file prints Impossible and returns immediately. Otherwise, for exit x>0 the distances are x and x-2*left; for x<0 they are 2*right-x and -x. The promised obstacle on the opposite side makes the detour finite. Signed byte parsing and raw numeric/text output replace Scanner and concatenation. Worst-case time O(N), auxiliary space O(1); no obstacle list is stored.

Exact-source Java 1.8 Accepted #11327458: 0.093 s / 416 KB. Saved 2026-11-20 compiler-cohort comparison: time 4/83, memory 6/83. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303629 was 0.125 s / 436 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1642_implementation_optimized.java`: 0.093 s / 416 KB; retained teaching base `1642_implementation.java`: 0.14 s / 1688 KB.

`1642_implementation_optimized.cpp`. Keep the nearest barrier on each side in one input pass, then apply the same reachability and two travel-distance formulas. Manual C byte parsing/printing replaces formatted integer conversion, using signed 64-bit intermediates. No obstacle list is retained: O(n) time and O(1) explicit working state.

Compared with `1642_implementation.cpp`: time 0.031 s → 0.015 s; memory 124 KB → 72 KB.

`1642_implementation_optimized.rs`. Update both nearest-barrier bounds as each obstacle arrives instead of collecting the input and scanning its vector twice. The distance formulas remain unchanged. C-runtime numeric input/output and two bound variables give O(n) time and O(1) auxiliary space.

Compared with `1642_implementation.rs`: time 0.031 s → 0.015 s; memory 228 KB → 48 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1642_implementation.cpp](1642_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 124 KB | 11303497 |
| [1642_implementation.go](1642_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB | 11288477 |
| [1642_implementation.java](1642_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1688 KB | 11288479 |
| [1642_implementation.py](1642_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 504 KB | 11288478 |
| [1642_implementation.rs](1642_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 228 KB | 11303498 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1642_implementation_optimized.java](1642_implementation_optimized.java) | Java 1.8 | implementation | O(N) time; O(1) auxiliary space | AC | 0.093 s | 416 KB | 11327458 |
| [1642_implementation_optimized.cpp](1642_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 72 KB | 11325060 |
| [1642_implementation_optimized.rs](1642_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 48 KB | 11324980 |
| [1642_implementation_optimized.py](1642_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N) time; O(I) token storage | AC | 0.078 s | 744 KB | 11327790 |
