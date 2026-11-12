# 1400. Cellular Characters

[Timus 1400](https://acm.timus.ru/problem.aspx?space=1&num=1400) · difficulty 549 · graphs

Original problem by Vladimir Yakovlev, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 256 extra characters of a phone stand in a table with M columns,
filled row by row, the last row possibly short. The cursor moves left,
right, up and down; left and right also run on to the previous or next
row and from one end of the table to the other, while up from the first
row or down to a missing cell leaves it in place. Choose the starting
cell with the smallest average number of key presses to reach a
character, and print that average and the presses for every character.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M.

## Output

"Mean = X" with two digits after the point, then the N numbers of key
presses, M per line. Any best starting cell is accepted.

## Examples

### Example 1

Input:

```
5 3
```

Output:

```
Mean = 1.00
1 0 1
2 1
```

## Solution

Number the cells 0 … N − 1 row by row. Left and right are then i − 1
and i + 1 modulo N, up is i − M if that is a cell, and down is i + M if
that is a cell; otherwise the cursor stays. A breadth-first search from
every starting cell gives all its distances, and the start with the
smallest sum wins. `O(N²)`.

Pitfalls:

- with a single character the answer is Mean = 0.00 and one 0 (test 02);
- a mean like 13/8 = 1.625 is an exact tie at the second digit; the
  solutions print what C's printf prints, 1.62, so Java rounds the exact
  value of the double with BigDecimal instead of String.format (test 07);
- the forum reports tests beyond the stated bounds, such as 46 columns,
  so nothing is sized by them (test 06).

The tests are judged by a checker that asks for the smallest mean and
for distances that come from some starting cell with that mean.

## Optimized solutions

Go keeps the all-start BFS method but reuses one256-byte distance row, one256-byte queue and a256×4 byte neighbor table. The horizontal edges contain the N-cycle, so distances≤floor(N/2)≤128;255 safely marks unseen and vertex indices≤255 fit a byte. Reversal v↦N−1−v preserves horizontal and valid vertical edges, so equal-sum starts come in mirrored pairs. Search only ceil(N/2) starts, remember the best index, then rerun BFS once for its displayed row. The two decimal mean uses the same binary64 division and formatting as the base, including halfway rounding. Time O(N²), bounded O(N) working storage under N≤256; no new distance/queue allocation per start, fmt or string joins. The simpler Go file remains; other families reuse qualifying originals.

The accepted base implementations [1400_graphs.cpp](1400_graphs.cpp), [1400_graphs.java](1400_graphs.java), [1400_graphs.py](1400_graphs.py), [1400_graphs.rs](1400_graphs.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1400_graphs.cpp](1400_graphs.cpp) | G++ 13.2 x64 | graphs | O(N^2) | AC | 0.015 s | 216 KB | 11286012 |
| [1400_graphs.go](1400_graphs.go) | Go 1.14 x64 | graphs | O(N^2) | AC | 0.031 s | 2780 KB | 11286015 |
| [1400_graphs.java](1400_graphs.java) \* | Java 1.8 | graphs | O(N^2) | AC | 0.125 s | 4384 KB | 11286018 |
| [1400_graphs.py](1400_graphs.py) \* | Python 3.12 x64 | graphs | O(N^2) | AC | 0.125 s | 516 KB | 11286016 |
| [1400_graphs.rs](1400_graphs.rs) \* | Rust 1.75 x64 | graphs | O(N^2) | AC | 0.062 s | 324 KB | 11286020 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1400_graphs_optimized.go](1400_graphs_optimized.go) \* | Go 1.14 x64 | graphs | O(N²) | AC | 0.031 s | 916 KB | 11315773 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
