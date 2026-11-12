# 1019. The longest white interval after repaintings of a line

[Timus 1019](https://acm.timus.ru/problem.aspx?space=1&num=1019) · difficulty 465 · sorting, dsu

Original problem from the Ural State University Internal Contest '99 #2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The segment `[0, 10^9]` of the number line is white. Then `N` repaintings
(`1 ≤ N ≤ 5000`) are applied in order: the `i`-th paints the segment from
`a_i` to `b_i` (`0 < a_i < b_i < 10^9`, integers) white or black. Find the
longest white interval of the result; among intervals of the same length
take the leftmost one.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines `a b c`, where `c` is `w` (white) or `b` (black).

## Output

The ends `x y` (`x < y`) of the longest white interval.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
2 999999998 b
100 500 w
500 900 w
300 310 b
```

Output:

```
310 900
```

### Example 2

Input:

```
1
1 999999999 w
```

Output:

```
0 1000000000
```

## Solution

Collect 0, 10⁹ and every repainting endpoint, then sort and deduplicate them. Between two consecutive coordinates the colour is uniform. Paint these pieces in chronological order, then scan them from left to right, joining adjacent white pieces. Compare physical lengths, not the number of pieces, and update only for a strictly longer run to retain the leftmost tie. There are at most 2N+1 pieces, so direct repainting takes O(N²) time after O(N log N) sorting and O(N) space. At N ≤ 5000 this is at most 50005000 piece assignments. Python performs each repaint with a bytearray slice, whose inner copying runs in native code; this makes the same simple algorithm pass in all five languages. Touching white pieces must merge. The endpoints 0 and 10⁹ must be included, and the untouched prefix [0,min a) guarantees a white answer.

## Optimized solutions

The DSU variants process repaintings backwards. A successor structure finds the first piece not yet assigned by a later repainting; after assigning it, link it to its next piece. Every piece is painted at most once. Sorting and endpoint searches give O(N log N) time and O(N) space. The accepted Go source uses 592 KB at 0.031 s, versus 1784 KB at 0.031 s for direct painting: 66.8% less memory. C++ and Python retain their original accepted DSU sources. Python DSU uses 3560 KB at 0.078 s; the new elementary Python uses 5 464 KB at 0.093 s. The simpler algorithm is kept for teaching despite both worse measurements. C++ DSU uses 212 KB versus 208 KB for direct painting; its 0.031-to-0.015 s difference is one timer tick, so its fast-set admission comes from the saved ranking rule rather than a claimed 30% timing gain. Java and Rust already cover their fast families with the same direct-painting files listed under Simple, without duplicate copies.

## Language notes

Simple direct painting now has Accepted in all five languages. DSU is an alternative algorithm with its own names. The new Go DSU uses standard handles and compact primitive arrays. All previous files and their historical Accepted metrics are preserved. Stars mark only sources selected for the fast set that still miss the language rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1019_sorting.cpp](1019_sorting.cpp) | G++ 13.2 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 208 KB | 11278218 |
| [1019_sorting.go](1019_sorting.go) | Go 1.14 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 1784 KB | 11278227 |
| [1019_sorting.java](1019_sorting.java) \* | Java 1.8 | sorting | O(N^2) after sorting | AC | 0.203 s | 3960 KB | 11278235 |
| [1019_sorting.py](1019_sorting.py) | Python 3.12 x64 | sorting | O(N²) after sorting | AC | 0.093 s | 5 464 KB | 11314812 |
| [1019_sorting.rs](1019_sorting.rs) \* | Rust 1.75 x64 | sorting | O(N^2) after sorting | AC | 0.046 s | 692 KB | 11278240 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1019_dsu_sorting.cpp](1019_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.015 s | 212 KB | 11278221 |
| [1019_dsu_sorting.go](1019_dsu_sorting.go) \* | Go 1.14 x64 | dsu, sorting | O(N log N) | AC | 0.031 s | 592 KB | 11314801 |
| [1019_dsu_sorting.py](1019_dsu_sorting.py) \* | Python 3.12 x64 | dsu, sorting | O(N log N) | AC | 0.078 s | 3560 KB | 11278231 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
