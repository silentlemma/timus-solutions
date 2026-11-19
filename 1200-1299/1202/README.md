# 1202. The shortest walk through a chain of rectangles

[Timus 1202](https://acm.timus.ru/problem.aspx?space=1&num=1202) · difficulty 442 · greedy

Original problem by Leonid Volkov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Fewer than `10⁵` rectangles on squared paper form a chain from left to right:
the first has its lower left corner at `(0, 0)`, each one starts where
the previous one ends horizontally, and every side is from 2 to 100
cells long. Where two neighbours touch, their shared border disappears. A
traveller walks along grid lines from `(1, 1)` to one cell inside the
upper right corner of the last rectangle, may not walk along any
rectangle border, and can only pass from one rectangle to the next
through the vanished part of their border. Find the length of the
shortest walk, or `-1` if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n`, then each rectangle as `x1 y1 x2 y2`, lower left and upper right
corners.

## Output

The length of the shortest walk, or `-1`.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
2
0 0 3 5
3 1 5 7
```

Output:

```
8
```

## Solution

The walk has to get from `x = 1` to `x = x2 − 1` of the last rectangle,
and it can always do so without ever stepping left, so the horizontal
part is fixed. Between rectangles `i` and `i + 1` the walk crosses the
line `x = x2ᵢ` at a whole height strictly inside both rectangles, that is
in `[max(y1) + 1, min(y2) − 1]`; if that range is empty there is no walk.
Inside a rectangle any change of height is possible on an inner vertical
line, so the vertical length is the total change of height between the
start, the chosen crossing heights and the goal.

To minimise that, move only when forced: keep the current height and, at
each border, clamp it into the allowed range. By induction the cheapest
way to stand at height `h` after border `i` costs the greedy total so far
plus `|h − greedy height|`, so the greedy choice is never worse. `O(n)`.

Pitfalls:

- rectangles that touch along fewer than two units, or only at a corner,
  leave no crossing at all;
- rectangles may extend below zero;
- with a single rectangle the answer is just the distance from `(1, 1)`
  to the goal, and 0 for a 2×2 rectangle.

The answers were compared with a separately written solution on 400
random chains and on every test.

## Optimized solutions

`1202_greedy_optimized.py`. Keep the same shortest-path greedy clamping into each consecutive rectangle overlap. Stream four coordinates per rectangle in 4096-byte chunks, retaining only the previous vertical interval, current height and accumulated vertical motion. This removes both the integer input list and the copied rectangle list. Empty overlap returns -1 immediately; otherwise use the final rectangle’s right/top boundary exactly as before. Time O(n), auxiliary space O(B) for bounded coordinate tokens and chunk B. Flush the complete answer before the standalone interpreter exit.

Compared with `1202_greedy.py`: time 0.328 s → 0.203 s; memory 39384 KB → 6 920 KB.

The new C++ and Go versions preserve the same projection onto each shared-border interval. They already need only the previous rectangle, current height and accumulated vertical distance; no rectangle list is introduced. C++ replaces repeated scanf parsing with an 8192-byte reader. Go replaces bufio/fmt with bounded standard-handle input and output. Negative coordinates are parsed explicitly, and 64-bit arithmetic is retained for coordinates and path totals on the target platforms. An empty crossing interval returns −1 immediately. Time remains O(n), auxiliary storage is bounded. All ordinary sources remain; Java, Python and Rust reuse admitted bases in the fast set.

The accepted base implementations [1202_greedy.java](1202_greedy.java), [1202_greedy.py](1202_greedy.py), [1202_greedy.rs](1202_greedy.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1202_greedy_optimized.py`: time place 3/15, memory place 8/15 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1202_greedy.cpp](1202_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.234 s | 132 KB | 11283557 |
| [1202_greedy.go](1202_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.046 s | 1088 KB | 11283561 |
| [1202_greedy.java](1202_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 540 KB | 11283564 |
| [1202_greedy.py](1202_greedy.py) \* | Python 3.12 x64 | greedy | O(n) | AC | 0.328 s | 39384 KB | 11283563 |
| [1202_greedy.rs](1202_greedy.rs) \* | Rust 1.75 x64 | greedy | O(n) | AC | 0.031 s | 8696 KB | 11283565 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1202_greedy_optimized.cpp](1202_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 88 KB | 11315050 |
| [1202_greedy_optimized.go](1202_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(n) | AC | 0.046 s | 312 KB | 11315069 |
| [1202_greedy_optimized.py](1202_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(n) time; O(B) space | AC | 0.203 s | 6920 KB | 11325482 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
