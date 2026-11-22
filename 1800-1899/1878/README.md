# 1878. Rubinchik's Cube

[Timus 1878](https://acm.timus.ru/problem.aspx?space=1&num=1878) · difficulty 219 · implementation

Original problem by Denis Mukhametianov, from the Ural Regional School Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A puzzle is made of four transparent 4 × 4 layers on a common axis.
Each layer has four coloured squares, one of each of four colours,
placed so that a quarter turn of the layer moves each of them into the
next quadrant. Each layer's four squares form an orbit under this turn,
and all layers have the same clockwise cyclic colour order, up to
rotation, as in the [original layer diagram](https://acm.timus.ru/image/get.aspx/a394d0eb-f9d5-4bc2-846a-74ef972e9e4b).
Seen from above the layers fill the 4 × 4 grid. The
puzzle is solved when every 2 × 2 quadrant has a single colour. One
move turns one layer by 90° either way. Given the view from above, find
the fewest moves that solve the puzzle.

## Input

Four lines of four colours from 1 to 4: the view from above.

## Output

The least number of moves.

## Checking

Compare output tokens; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2 1 2 3
1 1 2 2
4 4 3 3
1 4 3 4
```

Output:

```
1
```

## Solution

All layers share the same cyclic colour order, so aligning their colour 1
squares also aligns every other colour. Every layer has exactly one square
of colour 1, and that square tells
the layer's orientation: its quadrant. Number the quadrants in the
order a quarter turn moves a square through them (top left, top right,
bottom right, bottom left). The puzzle is solved when all four colour 1
squares are in the same quadrant t. A layer whose square is in quadrant
p then needs min(d, 4 − d) moves, where d = (p − t) mod 4. Try all four
t and take the cheapest. `O(1)`.

In the example three colour 1 squares are in the top-left quadrant and
one in the bottom-left, a quarter turn away: one move.

Pitfalls:

- aligning colour 1 relies on the shared cyclic colour order (as in test
  01); having each colour once per layer alone is not enough;
- the solved state may have colour 1 in any quadrant: the cube may end
  up turned as a whole;
- a layer half a turn away costs two moves whichever way it turns;
- the quadrants must be numbered round the circle, not row by row,
  for the distances to be right.

The Python solution agrees with an independent breadth-first search over
physical layer turns on all 1,536 solvable boards, including every
number-to-colour assignment.

## Optimized solutions

`1878_math_optimized.java`. Keep four quadrant counts and the exact expression 4−max(|a−d|,|b−c|) for the fixed 4×4 grid. O(1) time and storage. All numeric fields used by the computation are consumed before output. Reuse one 256-byte array for input and then output, reserving twelve bytes per signed int; reverse only its newly written digits. This removes separate input/output/digit arrays without overwriting any value still needed by the algorithm. Time for parsing/output is linear in consumed bytes; buffer storage is fixed.

Exact-source Java 1.8 Accepted #11327768: 0.093 s / 368 KB. Saved 2026-11-20 compiler-cohort ranks, time then memory: 4/31; 2/31. Strict admission uses time only below 1024 KB: top ten or top 15%, ties share rank and percentage cutoff rounds up. An asterisk remains for the separate first-place-in-both language target. The preserved previous variant has its own paired receipt #11308562 (Java 1.8): 0.109 s / 440 KB; do not mix measurements or runtimes. All teaching sources remain unchanged.

- `1878_math_optimized.java`: 0.093 s / 368 KB; retained teaching base `1878_implementation.java` (Java 1.8): 0.14 s / 1668 KB.

`1878_implementation_optimized.go`. Keep the four-target rotation-cost scan. Read the sixteen cells directly into four quadrant counts and compute clockwise quadrant indices arithmetically, without retaining the cells. Circular distances and ties are unchanged. The fixed 4×4 puzzle takes constant time and storage. Use bounded 256-byte input and 64-byte output buffers with Go 1.14 syscall.Read/Write, retrying EINTR and partial writes and handling zero-byte EOF. This removes fmt/bufio/os.File initialization overhead. Linux tests and Windows cross-builds establish functional/build checks; the paired memory figures below come from our own exact Windows judge Accepted. Preserve the readable teaching source.

Compared with `1878_implementation.go`: time 0.031 s → 0.015 s; memory 1084 KB → 292 KB.

`1878_implementation_optimized.rs`. Keep the same four-target quadrant rotation-cost scan. Read the sixteen cells directly into four u8 white counts, each at most four; derive the clockwise quadrant index arithmetically instead of retaining all cells and a mapping table. Direct numeric output replaces formatting. Work and auxiliary storage are constant for the fixed 4×4 puzzle; the shortest circular distance and tie handling are unchanged.

Compared with `1878_implementation.rs`: time 0.046 s → 0.031 s; memory 208 KB → 60 KB.

A fixed-board imbalance formula replaces enumeration of target colors and modular-distance loops. Count one color in each row-major quadrant, compare opposite quadrant imbalances and take the corresponding complement. The cyclic color order in the physical diagram is essential to the derivation; arbitrary reordering of quadrants is not equivalent. The board size is fixed, so both storage and arithmetic are constant with respect to the input parameters.

- `1878_math.java`: 0.109 s / 440 KB; base `1878_implementation.java`: 0.140 s / 1668 KB; relative change: time -22.1%, memory -73.6%.
- `1878_math.py`: 0.125 s / 288 KB; base `1878_implementation.py`: 0.093 s / 432 KB; relative change: time +34.4%, memory -33.3%.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1878_implementation_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1878_implementation.cpp](1878_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 108 KB | 11309211 |
| [1878_implementation.go](1878_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1084 KB | 11291010 |
| [1878_implementation.java](1878_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1668 KB | 11291012 |
| [1878_implementation.py](1878_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 432 KB | 11309212 |
| [1878_implementation.rs](1878_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 208 KB | 11309213 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1878_math.java](1878_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 440 KB | 11308562 |
| [1878_math_optimized.java](1878_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.093 s | 368 KB | 11327768 |
| [1878_math.py](1878_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 288 KB | 11309395 |
| [1878_implementation_optimized.rs](1878_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(1), fixed 16-cell puzzle | AC | 0.031 s | 60 KB | 11325617 |
| [1878_implementation_optimized.go](1878_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(1), fixed 16-cell puzzle | AC | 0.015 s | 292 KB | 11325658 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
