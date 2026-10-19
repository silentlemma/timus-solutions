# 2039. Counting squares formed by complete black lines

[Timus 2039](https://acm.timus.ru/problem.aspx?space=1&num=2039) · difficulty 5497 · two_pointers, bitmask

Original problem by Kirill  Borozdin , prepared by Oleg Merkurev, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a binary `n × m` board and a positive integer `k`, count
contiguous square regions having exactly `k` entirely black rows and
exactly `k` entirely black columns. Every cell outside the union of
those rows and columns must be white. The selected rows and columns need
not be consecutive. Squares with different top-left cells or side
lengths are distinct.

## Input

The first line contains `n, m, k`, each from 1 to 1000. The following
`n` lines contain exactly `m` binary characters each: `0` is white and
`1` is black. In particular, `k` may exceed either board dimension. The
limits are 0.5 seconds and 64 MB.

## Output

One integer: the number of qualifying squares. A side shorter than `k`
cannot qualify. At side `k`, precisely the all-black squares qualify.
For longer sides, some white cells must remain. If `k > min(n,m)`, the
answer is zero. The total number of squares in any allowed board is at
most 333833500; 64-bit accumulators are convenient, although this bound
also fits a signed 32-bit integer.

## Checking

Outputs are compared token by token.

## Examples

```
5 6 2
010100
111111
010100
111111
010100
```

```
7
```

Using one-based `(row,column,side)` coordinates, the seven squares are
`(2,2,3)`, `(1,1,4)`, `(1,2,4)`, `(2,1,4)`, `(2,2,4)`, `(1,1,5)` and
`(1,2,5)`. In the side-three square the middle row and middle column are
white except where they cross the two complete black lines in the other
direction. The side-four and side-five windows still contain exactly two
complete lines in each direction. No side-two window is all black. Thus
the answer is `1+4+2=7`.

## Solution

### A hereditary square property

Call a square shaped correctly when its white cells are exactly a
Cartesian product `R × C`, where `R` consists of rows containing white
and `C` consists of columns containing white. The all-black square has
both sets empty. This is equivalent to every nonempty white row having
the same white-column pattern. It is precisely the required
union-of-black-lines shape, before prescribing the number of black
lines.

For a nonempty white product of side `s`, the full-black line counts are
`s-|R|` and `s-|C|`. Define property `P` as the correct shape together
with both counts at most `k`. Every subsquare of a square with `P` also
has `P`. If white remains, its black lines are subsets of the parent's
black lines. If the subsquare is all black, all its rows or all its
columns must come from the parent's selected black lines; otherwise a
white row and white column would intersect inside it. Its side is
therefore at most `k`, so its two counts also satisfy the bounds.

### One moving window along each diagonal

The C++, Go, Rust and Java programs visit bottom-right cells along each
northwest–southeast diagonal. A start pointer stores the longest suffix
square satisfying `P`. The pointer only moves forward. Extending a
larger invalid square cannot become valid, because `P` is hereditary;
repeatedly shrinking the old valid window and retrying therefore finds
the longest valid window for the next endpoint. The total number of
extensions and removals is `O(nm)`.

There is no need to store the whole sets `R,C` for a window. Store the
bottommost white row `pr` and rightmost white column `pc`, or two absent
pivots for an all-black window, together with its two black-line counts.
To append the new bottom row over the old columns, its white pattern
must be empty or equal to the old pivot row's restricted pattern. When
there were no whites, any pattern starts a product. Next append the new
right column over all rows, including the just-added row; apply the
analogous comparison with the pivot column. Update the two pivots to the
last white positions. An existing white product classifies the new row
and column by their cells at the opposite pivot. When whites first
appear in a formerly all-black window, the new nonempty white row or
column and its number of black cells give the counts directly. Commit
only if both counts are at most `k`.

On failure, remove the old top row and old left column, without
committing the tentative extension. If the removed row equals `pr` or
the removed column equals `pc`, one factor of the white product
disappears entirely: the remaining old square becomes all black.
Otherwise the pivots remain, and the two line counts decrease exactly
when the removed row or column was black at the opposite pivot. This
maintains the shape, pivots and counts after every removal.

Let the current diagonal endpoint be offset `t` and its longest valid
window start at offset `a`. All candidate squares at this endpoint lie
inside that window. The side-`k` suffix contributes once exactly when it
fits and either white pivot lies before its row/column boundary; then
the white product misses that suffix.

For longer sides, no suffix can gain selected black lines. Thus a
contribution is possible only if the current counts both equal `k` and
whites are present. Let `fr,fc` be the first selected row and column,
expressed as diagonal offsets. A suffix must retain all selected rows
and columns, at least one white row and white column, and side greater
than `k`. Its start `x` must satisfy `a ≤ x ≤ min(t-k,fr,fc,pr,pc)`,
with pivots also expressed as offsets. Keeping the first selected row
retains every selected row; keeping the last white row retains a white
row, and similarly for columns. These conditions are both necessary and
sufficient. Add the number of integers in this interval. Every square
has one endpoint and is counted once.

Both line counts must equal `k`. Additional black cells invalidate a
square even when its line counts match. Treat all-black side `k`
separately from larger mixed squares. Test the new column after adding
the new row, and never keep half an unsuccessful extension. Clear both
pivots when either white factor vanishes.

### Python: reducing the board

Python first rejects dimensions smaller than `k`. An all-black board
contributes exactly its side-`k` squares; an all-white board contributes
zero. Otherwise it crops to the bounding rectangle of the black cells.
Every answer has a black cell in every row and column, since `k` is
positive, so no answer can extend beyond that rectangle.

If every row is either entirely black or a single common pattern, a
larger square is determined independently by a row window containing
exactly `k` full rows and a column window containing exactly `k` ones of
the pattern. Multiply these two window counts for each side. Groups of
consecutive `k` ones describe all such windows: their first and last
ones must be included, while the neighboring ones must be excluded. The
number of placements as a function of length is a trapezoid, accumulated
with second differences. Side `k` is counted separately by runs of full
rows or full columns, subtracting their intersection once.

With few distinct row patterns and no full row, the program also tries
separating the black cells into components of the bipartite graph whose
vertices are rows and columns. It recurses only if each component
occupies consecutive rows and consecutive columns. A qualifying square
connects all its row and column vertices through its selected black
lines, so it belongs to exactly one such rectangle. Summing their
answers is exact.

Another shortcut handles nested boards: after reflecting rows or columns
if needed, each row is a black prefix and the prefix lengths are
nondecreasing. All-black side-`k` squares follow from the shortest
prefix in each row window. In a larger answer, some equal shortest rows
are followed by exactly `k` longer rows. The left boundary is fixed by
requiring exactly `k` black columns. The number of shortest rows
determines the side, and is bounded by their group size, the gap to the
next prefix length, and the remaining width. Each admissible number
gives one square, so these bounds count them without scanning all sides.

The remaining board may be transposed when the opposite orientation has
fewer pattern changes according to an estimate of the work.
Transposition preserves squares and their two stripe counts. After a
safe upper bound on the side is found, a short range uses parallel
counters, a longer range with `k > 1` uses an offline decomposition, and
`k = 1` has its own counting method.

### Python: parallel counters and safe bounds

For a fixed side `s`, a square qualifies exactly when it has `k` full
rows, `k` full columns, and every row has either `k` or `s` black cells.
Indeed, the full columns already supply all `k` black cells of every
nonfull row, leaving no room for an extra black cell.

The board is stored in one large integer, one bit per cell. Shifted AND
operations find full horizontal and vertical segments; doubling the
segment length avoids scanning their cells individually. To count flags
in all windows together, separate integers store the binary digits of
the counters. XOR gives a sum digit and AND gives its carry, so
combining shifted blocks performs ordinary exact binary addition
independently at every position. Intersecting digit planes with the bits
of `k` tests equality. Full-row and full-column counts, together with
the allowed-row test above, give an exact acceptance mask. Masks discard
starts that cross a board edge, and population counts add the answers.

Before counting, necessary local conditions bound the side. A white
Cartesian product cannot have three white cells or two diagonally
opposite white cells in an adjacent `2×2` block. A valid square larger
than `k` cannot contain an all-black square of side `k+1`. For small
`k`, blocks of side `2k+1` with too many full rows or columns are
excluded as well. Tables for power-of-two squares test the absence of
these blocks using four overlapping corner blocks. All-white candidates
are removed because `k` is positive. The existence of a remaining mixed
candidate is monotone in its side: a smaller corner square can retain
adjacent cells of different colors and inherits the exclusions. Binary
search therefore gives a safe upper bound, not an acceptance test.

When sizes are processed in bands, the crop retains every possible full
row and column long enough for the band's smallest side, with margins
for its largest side. Every answer contains such lines, so nothing
outside the crop can contribute. Empty masks and insufficient dimensions
can end a scan safely. The final counters still decide every surviving
candidate.

### Python: offline decomposition for `k > 1`

For a long range of sizes, the program avoids repeating the counters for
each side. Side `k` consists of all-black squares. Side `k+1` requires
exactly one white cell: the remaining rows and columns are precisely its
`k` black stripes. Both cases are counted with parallel masks, tracking
zero or at most one white cell while combining disjoint blocks.

For larger sides, first certify the shape in every contained block of
side `k+2`. With small `k`, pairs of rows must have identical white
patterns unless one is full, and all-black blocks of side `k+1` are
forbidden. Otherwise, the union of white columns must have the same size
as each nonempty white row, which forces those sets to coincide; at
least two rows and two columns must contain white. Every valid square
passes the corresponding test. Adjacent certified blocks share white
cells in their overlap, so their Cartesian products agree and extend to
one product over the whole square. A square dynamic program gives the
largest side satisfying these certificates at each start. Its row is
evaluated with packed minima and distances to the next failed
certificate.

Within a qualifying square, at least one of its first `k+1` rows is not
a stripe. Their bitwise intersection is therefore exactly the set of
full columns. Intersecting the first `k+1` columns similarly identifies
the full rows. For each start, the position of the `k`-th selected line
gives an inclusive lower bound on the side, and the next selected line
gives an inclusive upper bound: the window must include the former and
exclude the latter. Intersect the row and column intervals with the
shape bound and the minimum side `k+2`; add the length of the resulting
interval. Every accepted side then has the certified shape and exactly
the required counts, and every answer appears at its unique start.

Successor positions are obtained from runs or packed ranks, and repeated
patterns reuse exact endpoint arrays. Small changes may update only
affected ranks. Endpoints and bounds occupy separate guarded fields of
large integers, allowing minima, maxima and interval lengths to be
computed for many columns together. Field widths cover all allowed
coordinates, and masks prevent cross-field carries or borrows from
changing a result. These are exact operations, with no probabilistic
comparisons. If certificates leave only a short range, the program
returns to the parallel counters.

### Python: one stripe and its unique crossing

For `k = 1`, side one contributes every black cell. The other small
sides are grouped into bands. At the smallest side of a band, masks find
exactly one full row and one full column, with local shape certificates
for sides above two. These conditions are sufficient: the certified
shape forces each nonfull row to contain only the black cell in the full
column. Any larger one-stripe square contains a smaller square with the
same crossing, so the masks also locate every region that can contribute
within the band. Candidate row groups are expanded by the necessary
margins; separate groups have disjoint crops. Inside each crop, either
the common-pattern formula or the parallel counters count only that
band's sides.

For long sides, a fixed smaller side supplies candidate crossings. Each
surviving square has one crossing of its full row and full column;
looking in a different column identifies the full row. A set removes
duplicate crossings found in several smaller squares. Every larger
answer contains one of these smaller squares with the same crossing, so
no crossing is missed.

For each crossing, the black runs through it bound all possible answers.
Inside those bounds, erase its row and column. A square containing the
crossing is valid exactly when the remaining cells are all white. A
packed dynamic program finds the largest empty square at every top-left
cell. The distances needed to include the crossing give a lower bound on
its side; the empty-square size and the requested range give an upper
bound. Summing the integer interval lengths counts all answers for that
crossing. Erasing the two lines is safe because the run bounds already
ensure that both lines were black. Unique crossings prevent counting a
square twice.

## Language notes

Write `L=min(n,m)`. The moving-window programs make `O(nm)` updates, but
byte-string comparisons and searches may inspect `O(L)` characters: the
conservative C++/Go/Rust bound is `O(nmL)` time and `O(nm)` space. Java
uses exact 64-bit chunks, masked boundary words, population counts and
prefix tables for last white positions; its bound is `O(nmB₆₄)` time and
`O(nm)` space, where `B₆₄=ceil(max(n,m)/64)`. A shift by 64 is handled
separately.

For Python, write `D=max(n,m)` and let `B` be the number of machine
words needed for a packed row with `D` guarded coordinate fields. With
the problem's coordinate limit, this is `O(D)` bits. Charging
multiplication and division of such integers conservatively as `O(B²)`,
and using standard amortized dictionary operations, a bound covering all
branches is `O(nm(nm+DB²))` time and `O(nm+DB log(L+1))` space.

This intentionally loose time bound allows up to `nm` distinct
crossings, each scanning at most `nm` cells and `D` packed rows at cost
`O(B²)` per row. It also covers the offline preprocessing, all side
scans, and quadratic arithmetic on whole-board integers. Only one
crossing is processed at a time; the stored masks, endpoint arrays,
caches and power-of-two tables fit the stated space bound. The
reductions and packed operations make the actual work much smaller on
many boards.

The solution runs on CPython and is Accepted on Timus with Python 3.12
x64 in 0.359 s and 21 964 KB, within the 0.5 s limit. Earlier versions
exceeded the time limit on the judge's tests 4, 26 and 24; what made
test 24 slow was found by comparing the running times of two versions on
many generated boards.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2039_bitmask.py](2039_bitmask.py) | Python 3.12 x64 | bitmask | O(nm(nm+DB^2)) | AC | 0.359 s | 21964 KB |
| [2039_two_pointers.cpp](2039_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(nmL) | AC | 0.218 s | 2276 KB |
| [2039_two_pointers.go](2039_two_pointers.go) | Go 1.14 x64 | two_pointers | O(nmL) | AC | 0.234 s | 4436 KB |
| [2039_two_pointers.java](2039_two_pointers.java) | Java 1.8 | two_pointers | O(nmB64) | AC | 0.312 s | 8088 KB |
| [2039_two_pointers.rs](2039_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(nmL) | AC | 0.265 s | 3368 KB |
