# 1221. The largest black square with a white diamond inside

[Timus 1221](https://acm.timus.ru/problem.aspx?space=1&num=1221) · difficulty 424 · implementation

Original problem by Nikita Shamgunov, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sheet of `N × N` cells, `N ≤ 100`, is painted black (1) and white (0).
Cut out the largest square, sides along the grid, that is black except
for a white square turned by 45 degrees whose corners touch the middles
of its sides. Print its size, or `No solution`. The input holds several
sheets and ends with `0`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

For each sheet, integer `1 ≤ N ≤ 100`, followed by N rows of N binary cells (`1` black, `0` white). Cells may be written with or without spaces. A final `0` ends the input and is not a sheet.

## Output

For each sheet, the size of the largest such figure or `No solution`.

## Examples

### Example 1

Input:

```
4
1011
0001
1011
1111
1
0
0
```

Output:

```
3
No solution
```

## Solution

The white diamond has a centre cell and reaches the middle of every side,
so the figure has an odd size `2r + 1` with `r ≥ 1`: a cell at offsets
`(d, e)` from the centre is white exactly when `|d| + |e| ≤ r`. Row `d`
of the figure is therefore `|d|` black cells, a white run of
`2(r − |d|) + 1` cells and `|d|` black cells again, and with prefix sums
of black cells along every row each row is checked in constant time.

Try the radii from the largest down and, for each, every centre; the
first figure found is the answer. Most candidates fail at once on three
single cells (the centre and the top tip must be white, the top left
corner black), and the rest usually fail on the first row checked.
`O(N⁴)` at worst, far less in practice.

Pitfalls:

- a single white cell is not a figure: the diamond needs room inside a
  black square, so the smallest figure is 3 × 3;
- figures have odd sizes only;
- several sheets follow each other until the `0`.

The answers were compared with a separately written solution on 300
files of random, planted and uniform sheets.

For S sheets with maximum side N, the row-checking algorithm uses `O(N²)` live grid/prefix entries and up to `O(Σ N_i⁴)` search time, plus reading I input bytes. C++/Go process one sheet and stream answers with bounded buffers. Java retains all answer lines, adding `O(S)` output space. Simple Python and Rust also retain the whole input, adding `O(I + S)` to their `O(N²)` current-sheet storage; Python temporarily keeps a flat cell list as well. Optimized Python reads bounded chunks and uses byte grid/prefix entries (row counts ≤100), but still retains all S answers: `O(N² + S + B + T)` space for chunk size B and maximum token T, with no whole-input allocation. Its search remains O(N⁴), not the transformed-prefix algorithm. The Go prefix version has logical O(N²) tables; its actual arrays are fixed at M=100 (101²+200² uint16 entries) plus buffers. Clearing these costs O(M²) per sheet, followed by O(N²) prefix construction and O(N³) search; allocated space is O(M²+B) even for a small sheet.

## Optimized solutions

The new Go algorithm counts white cells with two 2D prefix-sum tables: one in the original grid and one after u=row+column, v=row−column+N−1. A radius-r diamond becomes an axis-aligned rectangle in the transformed grid; unused parity positions contain zeros. It contains exactly A=2r(r+1)+1 actual cells. Require A white cells in that rectangle and exactly A in the surrounding (2r+1)-square. The first condition makes the entire diamond white; the second makes every other square cell black. Both queries cost O(1), so all candidate centres and radii take O(N³), after O(N²) preprocessing, with O(N²) storage. Counts are at most 10000 and fit uint16.

The accepted Go 1.14 x64 run takes 0.031 s versus 0.001 s for the base and uses 352 KB versus 2116 KB.

The cached exact-source audit and shared [rating criteria](../../RATING_CRITERIA.md) qualify all sources except simple Python. Python fast coverage is #11328771, 0.156 s / 924 KB: below 1024 KB only time is required. The preserved base #11283692, 0.140 s / 1908 KB, passes time but fails its required memory reference (901.6 KB limit). Thus the slightly slower recorded run qualifies without asserting an algorithmic speedup. C++/Java/Rust and optimized Go are time-only; simple Go at 2116 KB requires both metrics and uses the same-language fallback. Python/Rust use applicable exact-compiler references. All meaningful teaching sources remain unstarred and paired measurements remain intact.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1221_implementation_optimized.py`. Store grid rows as bytes and row-prefix counts in compact byte arrays. Stream successive grids while retaining the original largest-figure search and its acceptance conditions. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328771 (Python 3.12 x64): **0.156 s / 924 KB**. Archived comparison: `1221_implementation.py` (Python 3.12 x64) — 0.14 s / 1908 KB (#11283692).

Accepted #11328771 and its numerical qualification describe the historical exact source. Structural lint requires naming the existing whitespace limit 32 as `WHITESPACE_LIMIT`; reversing that constant substitution exactly reproduces the previous bytes. The algorithm, comments and simple Python remain preserved. The revised file hash needs its own Accepted in the later batch; the old pair does not certify the new bytes.

## Language notes

These notes describe the simple implementations.

- All languages read the cells one digit at a time, so rows written with
  or without spaces both work.

## Checking

`tests/tests.json` uses `lines`: preserve sheet order and one answer per sheet, ignoring leading/trailing and repeated whitespace within each line. Line count, token spelling/case (`No solution`) and token order remain significant; do not answer the terminating 0. The own example and small fixtures are independently checked by comparing every candidate square cell to the required Manhattan-distance color pattern, without prefix sums.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1221_implementation.cpp](1221_implementation.cpp) | G++ 13.2 x64 | implementation | O(N⁴) | AC | 0.015 s | 316 KB | 11283690 |
| [1221_implementation.go](1221_implementation.go) | Go 1.14 x64 | implementation | O(N⁴) | AC | 0.001 s | 2116 KB | 11283691 |
| [1221_implementation.java](1221_implementation.java) | Java 1.8 | implementation | O(N⁴) | AC | 0.062 s | 936 KB | 11283693 |
| [1221_implementation.py](1221_implementation.py) | Python 3.12 x64 | implementation | O(N⁴) | AC | 0.14 s | 1908 KB | 11283692 |
| [1221_implementation.rs](1221_implementation.rs) | Rust 1.75 x64 | implementation | O(N⁴) | AC | 0.031 s | 500 KB | 11283694 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1221_prefix_sums.go](1221_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N³) | AC | 0.031 s | 352 KB | 11314933 |
| [1221_implementation_optimized.py](1221_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N⁴) | AC | 0.171 s | 932 KB | 11331077 |
