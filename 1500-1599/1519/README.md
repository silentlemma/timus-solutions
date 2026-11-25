# 1519. Formula 1

[Timus 1519](https://acm.timus.ru/problem.aspx?space=1&num=1519) · difficulty 466 · dp

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A field of N × M cells (2 ≤ N, M ≤ 12) has some cells taken by burrows.
A race track is one closed loop that passes through every free cell
exactly once, moving between cells that share a side. Count the
tracks; the count fits in 63 bits.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then N rows of M characters: '.' free, '*' a burrow. At least
four cells are free.

## Output

The number of tracks.

## Examples

### Example 1

Input:

```
4 4
**..
....
....
....
```

Output:

```
2
```

### Example 2

Input:

```
4 4
....
....
....
....
```

Output:

```
6
```

## Solution

Dynamic programming over a broken profile, cell by cell in row order,
with the connectivity of the pieces crossing the profile as the state.
The profile has M + 1 plugs: the lower sides of cells from the previous
or current row and the left side of the current cell.
Each plug is empty or an end of a path piece, and the two ends of every
piece nest like brackets, so a plug is "(", ")" or nothing: 2 bits, and
a state fits in 26 bits. At a free cell with left plug L and upper plug
U:

- no plugs: start a new piece going right and down;
- one plug: continue it right or down;
- "(" and "(": join the pieces, and the ")" matching U becomes "(";
- ")" and ")": join them, and the "(" matching L becomes ")";
- ")" and "(": join two pieces into one;
- "(" and ")": this closes a loop, allowed only at the last free cell
  with no other plugs left, and then it counts.

A burrow passes only states with both plugs empty. At the end of a row
the profile shifts by one plug. On the empty 12 × 12 field at most about
14000 states appear at once, and the work is `O(N·M²·S)` for S states.

Pitfalls:

- the loop may only close at the last free cell, when nothing else is
  open (test 09);
- an odd number of free cells, or a free area cut off from the rest,
  gives 0 (tests 05, 06, 08);
- the empty 12 × 12 field has about 1.08·10¹⁸ tracks, so the counts
  need 64 bits (test 03);
- holes scattered one by one usually leave no track, so the generated
  tests mostly cut out whole 2 × 2 blocks (gen1, gen2, gen3).

## Optimized solutions

All new versions keep the same balanced-bracket profile transitions and allow closing a cycle only at the last free cell with no remaining plugs. After transposing as needed, the height is H = max(N, M) and the profile width is W = min(N, M). C++, Go and Rust use two reusable dense arrays of 32-bit states and 64-bit counts, indexed during merging by one 65536-slot table of 16-bit positions. Linear probing compares full keys. A profile has at most 13 slots. For t pairs, choose the 2t occupied slots and fill them with a balanced bracket word. Summing binom(13, 2t) times the t-th Catalan number gives 41,835 states. Each layer starts with space for 16,384 entries and grows as needed. Row shifts are injective and change keys in place without another hash map. Python additionally rejects disconnected, colour-unbalanced or degree-below-two free graphs, inlines bracket matching and reuses two dictionaries. These necessary rejections do not approximate the count. With S the maximum number of states in a layer, expected transition work is O(H·W²·S). Native packed storage reduces allocation and key overhead. All five original files remain; Java reuses its admitted base. Each Python row reports its actual accepted runtime.

The new Python row uses CPython and the original row uses PyPy. The new implementation removes fully blocked borders before choosing a scan direction. If the resulting field has even height and its halves mirror across the middle, Python builds profiles for just the top half. Reflection gives the same pairing counts for the bottom half. Only profiles using the same cut columns can join. With more than two endpoints, any shared pair forms a separate two-edge cycle. A bit mask rejects such pairs before traversal. Alternate top and bottom partners from one endpoint and count the pair precisely when the loop visits all endpoints. Multiply the two counts, counting both orders for distinct profiles. With four or six endpoints and no common pair, only one cycle is possible. Column reflection also gives equal contributions for reflected groups when both axes are symmetric. For wide asymmetric fields, choose the cut in the middle third with the fewest available crossings and scan each side toward it. The cropped field has free cells on both sides, so fewer than two crossing edges rules out a cycle. Narrow asymmetric fields use a full scan. If P is the sum of squared combined group sizes by cut-column mask, joining costs O(W·P).

The accepted Python 3.12 x64 run takes 0.703 s versus 0.609 s for the base and uses 4 880 KB versus 10768 KB.

The accepted base implementations [1519_dp.java](1519_dp.java) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The ordinary Python file was Accepted under PyPy; its CPython execution exceeded the judge limit on test18. The new Python source is checked separately and its own Accepted interpreter is recorded in the table. An Accepted for one source/runtime is not transferred to another.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1519_dp.cpp](1519_dp.cpp) | G++ 13.2 x64 | dp | O(N * M^2 * S) | AC | 0.203 s | 2076 KB | 11287360 |
| [1519_dp.go](1519_dp.go) | Go 1.14 x64 | dp | O(N * M^2 * S) | AC | 0.203 s | 10420 KB | 11287361 |
| [1519_dp.java](1519_dp.java) \* | Java 1.8 | dp | O(N * M^2 * S) | AC | 0.328 s | 18436 KB | 11287364 |
| [1519_dp.py](1519_dp.py) | PyPy 3.10 x64 | dp | O(N * M^2 * S) | AC | 0.609 s | 10768 KB | 11287363 |
| [1519_dp.rs](1519_dp.rs) | Rust 1.75 x64 | dp | O(N * M^2 * S) | AC | 0.062 s | 1600 KB | 11287365 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1519_dp_optimized.cpp](1519_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(H·W²·S) | AC | 0.031 s | 444 KB | 11315274 |
| [1519_dp_optimized.go](1519_dp_optimized.go) \* | Go 1.14 x64 | dp | O(H·W²·S) | AC | 0.031 s | 848 KB | 11315276 |
| [1519_dp_optimized.rs](1519_dp_optimized.rs) | Rust 1.75 x64 | dp | O(H·W²·S) | AC | 0.046 s | 440 KB | 11315281 |
| [1519_dp_optimized.py](1519_dp_optimized.py) \* | Python 3.12 x64 | dp | O(H·W²·S + W·P) | AC | 0.703 s | 4880 KB | 11316056 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
