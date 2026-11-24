# 1125. Undoing colour flips at integer distances on a grid

[Timus 1125](https://acm.timus.ru/problem.aspx?space=1&num=1125) · difficulty 236 · bitmask

Original problem by Dmitry Filimonenkov, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A field of `M × N` unit cells (`0 ≤ M, N ≤ 50`) is coloured black (`B`)
and white (`W`). Every time a cell is visited, every cell whose centre is
an integer distance from its centre changes colour, the visited cell
itself included (distance 0). Given the final colours and how many times
each cell was visited (up to `2·10^9`), print the initial colours.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`M N`, then `M` lines of the final colours, then `M` lines of `N` visit
counts.

## Output

`M` lines of the initial colours.

## Checking

Output colour rows are compared as tokens. Both the direct Python
simulation and the newer row-mask Python source were independently checked
on 5748 fields each against literal source-target pair evaluation with
integer-distance tests. The oracle uses no masks or axis grouping.
It exhausts colours and visit parities on 2×2 and 2×3, all visit parities
with two uniform final colours on 3×3, and includes empty/skinny fields,
random fields, maximum 50×50 odd/even/random visits and isolated odd visits.

Each of the eight added programs (five simulations and three newer bitmask
implementations) passed 11 repository inputs plus 78 actual main-program
inputs in Docker and has an exact-source Accepted. All saved outputs and
return codes are rechecked against independently recomputed pairwise answers,
bound to source hashes. The 5748 checks are Python, not native counts.
Four CPython simulation stress inputs peaked locally at 0.0687 CPU seconds
and 17288 KB RSS, within 0.25 seconds/64 MB; judge metrics remain separate.

## Examples

### Example 1

Input:

```
6 6
BWBBWW
BWBBWB
BBWWBW
BBBBBW
BBWWWW
BBWBBW
2 0 12 46 2 0
3 0 0 0 0 200
4 2 1 1 4 2
4 2 1 1 4 4
0 0 0 0 0 0
2 56 24 4 2 2
```

Output:

```
WWBBWW
WBWWBW
WBBBBW
WBWWBW
WBWWBW
WBWWBW
```

## Solution

The preferred teaching algorithm directly simulates the changes.
A flip is XOR with one: two flips cancel and visit order is irrelevant,
so use only the parity of each visit count. Generate every signed offset
`(dr,dc)` within the field's possible displacement range whose squared
length is a perfect square, including `(0,0)`. For each odd-visited source
cell, toggle every in-bounds target at one of these offsets.

Every qualifying source-target pair has exactly one such displacement,
so its parity contribution is counted once. Changing the final colours
by these same flips recovers the initial colours, because a flip is its
own inverse. There are `K≤405` offsets for sides at most 50. Generation
takes `O((M+N)²)` elementary tests and simulation `O(MNK)` time;
storage is `O(MN+K)`. These five implementations use ordinary cells and
coordinate loops, with no row-bitmask shifts, and each has its own Accepted.

Include distance zero. Counts up to two billion matter only modulo two
and fit signed 32-bit input arithmetic. For a zero dimension, output `M`
empty lines. All earlier bitmask sources and implementations remain.

## Optimized solutions

`1125_bitmask_optimized.rs`. Keep row parity bitmasks and XOR shifts for integral-distance flips. Replace the stored signed-offset list and floating square-root tests by an exact square lookup table for squared distances below 2S², S=50. For each source row apply the zero horizontal shift and both directions of each valid positive shift. Only the first C output bits matter; high shifted bits may be discarded. Store the board and row masks in fixed arrays, with no retained input/output String. Time O(R²C+S²), storage O(S²); zero rows/columns preserve the required blank lines.

Compared with `1125_bitmask.rs`: time 0.015 s → 0.001 s; memory 240 KB → 52 KB.

A colour flip is XOR with one, so the order of visits does not matter:
two flips cancel. Keep only each visit count modulo two. If `R[r]` is the
bit mask of odd visits in row `r`, the parity affecting an entire target
row is the XOR of shifted source rows for every offset `(dr,dc)` with
`dr²+dc²` a perfect square. Clip to the lowest `N` bits. Each source-target
pair appears exactly once, and reversing a flip is the same operation,
so XORing this parity into the final colours restores the initial field.

The five original Accepted sources enumerate all signed offsets, including
`(0,0)`. At `M=N=50` there are 405 offsets; every smaller field uses a
subset. With `K` offsets the work is `O(MN+MK)` row-mask operations,
including input, output and offset generation. Native rows fit in one
64-bit word because `N≤50`; Python uses arbitrary-precision integers,
whose shifts/XORs cost their number of limbs. Native data storage is
`O(MN+M+K)` words/characters; the original Python also holds all input
tokens and visit integers, `O(MN+M+K)` objects. All originals are retained.

Distance zero must be included. Counts up to two billion need only their
low bit and fit signed 32-bit input arithmetic. If either dimension is
zero, print `M` empty lines; there are no cells to recover.

The three new sources keep the same parity-and-row-mask algorithm,
hence `_optimized`. They group the axes and the four signs of each
strictly positive offset. Let `C` be the XOR of all `R[r]`, and let `F`
have its lowest `N` bits set. Contributions along the target's whole row
are `F` when `popcount(R[r])` is odd; same-column contributions are `C`.
These count the origin twice, so XOR `R[r]` once more to restore its one
required contribution.

For every `dr>0,dc>0` of integral length, form
`T = R[r−dr] XOR R[r+dr]`, treating an out-of-field row as zero.
Then XOR `(T<<dc) XOR (T>>dc)`. This accounts for all four signs exactly
once; axes and origin are disjoint from these terms. Finally retain only
the target columns. There are at most `P=52` positive offset pairs rather
than 405 signed offsets. Time is `O(MN+MP)` mask operations. Store the
final colours, one mask per row and `P` pairs. C++/Java additionally use
a fixed 5000-entry square table; Python's square set has `O(M+N)` entries.
Python shifts can temporarily reach `2N−1` bits, not an assumed single
machine word. Native shifts are below 64; discarded higher bits cannot
affect the retained low `N` bits, and Java uses logical `>>>`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1125_bitmask_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1125_simulation.cpp](1125_simulation.cpp) | G++ 13.2 x64 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.001 s | 136 KB | 11308651 |
| [1125_simulation.go](1125_simulation.go) | Go 1.14 x64 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.015 s | 1144 KB | 11308665 |
| [1125_simulation.java](1125_simulation.java) | Java 1.8 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.093 s | 536 KB | 11308659 |
| [1125_simulation.py](1125_simulation.py) | Python 3.12 x64 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.093 s | 564 KB | 11308679 |
| [1125_simulation.rs](1125_simulation.rs) | Rust 1.75 x64 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.015 s | 200 KB | 11308669 |

### Other Accepted approaches

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1125_bitmask.cpp](1125_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.001 s | 456 KB | 11279311 |
| [1125_bitmask.go](1125_bitmask.go) | Go 1.14 x64 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.031 s | 1092 KB | 11279315 |
| [1125_bitmask.java](1125_bitmask.java) | Java 1.8 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.078 s | 968 KB | 11279320 |
| [1125_bitmask.rs](1125_bitmask.rs) | Rust 1.75 x64 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.015 s | 240 KB | 11279322 |

### Optimized

**Current improvements versus the preferred simulation**

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1125_bitmask.py](1125_bitmask.py) | Python 3.12 x64 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.046 s | 900 KB | 11279316 |
| [1125_bitmask_optimized.py](1125_bitmask_optimized.py) | Python 3.12 x64 | bitmask | O(MN+MP), P ≤ 52 | AC | 0.046 s | 580 KB | 11308647 |

**Historical bitmask-pair improvements; current 30% simulation criterion not met**

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1125_bitmask_optimized.cpp](1125_bitmask_optimized.cpp) | G++ 13.2 x64 | bitmask | O(MN+MP), P ≤ 52 | AC | 0.001 s | 132 KB | 11308644 |
| [1125_bitmask_optimized.java](1125_bitmask_optimized.java) | Java 1.8 | bitmask | O(MN+MP), P ≤ 52 | AC | 0.093 s | 424 KB | 11308646 |
| [1125_bitmask_optimized.rs](1125_bitmask_optimized.rs) | Rust 1.75 x64 | bitmask | O(R²C+S²) time; O(S²) space | AC | 0.001 s | 52 KB | 11325540 |
