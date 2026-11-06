# 1287. Canals on Mars

[Timus 1287](https://acm.timus.ru/problem.aspx?space=1&num=1287) · difficulty 383 · dp

Original problem by Alexander Mironenko (prepared by Igor Goldberg), from the Ural State University Personal Contest 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An N × N field (N ≤ 1400) is sown with two kinds of grain, `s` and `S`,
one per cell. Find the longest straight run of equal cells along a row,
a column or either diagonal. Print the letter whose longest run is
longer, or `?` if both are equal, and then that length.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines of N letters.

## Output

The winning letter or `?`, then the longest run.

## Examples

### Example 1

Input:

```
3
SsS
sSs
SsS
```

Output:

```
S
3
```

### Example 2

Input:

```
2
sS
Ss
```

Output:

```
?
2
```

## Solution

Go through the field row by row. For every cell keep the length of the
run that ends there in each of the four directions: from the left, from
above, from the upper left and from the upper right. Each is the
neighbour's run plus one when the neighbour has the same letter, and 1
otherwise. Only the previous row is needed, and the longest run of
each letter is kept on the way. The DP takes `O(N²)` time and `O(N)`
state; total memory depends on how the input is stored (see below).

Pitfalls:

- the diagonal from the upper right is easy to forget (test 06);
- equal longest runs print `?` (test 02);
- the field has almost two million cells, so the reading should be
  fast.

The answers were compared with walking every run from every cell on
1,200 random fields of up to twelve cells a side and all 530 fields
with sides from one to three cells.

## Optimized solutions

C++ uses SSE2 to update eight columns at a time for the vertical and diagonal runs. Comparing letters gives a mask that keeps the previous run only where the letters match. Horizontal runs are scanned separately. Go packs a run length and its letter into a 16-bit value and updates the three arrays in place, saving the old upper-left entry for the next column. Both take O(N²) time and O(N) space.

The accepted base implementations [1287_dp.java](1287_dp.java), [1287_dp.py](1287_dp.py), [1287_dp.rs](1287_dp.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- C++, Go, Java and Rust keep three run arrays for each of two rows
  and a scalar for the horizontal run. C++, Go and Java use `O(N)`
  total memory; Rust retains the whole input and uses `O(N²)`.
- Python would be too slow cell by cell. It builds the rows, the
  columns and both diagonals as byte strings: the diagonals are the
  columns of the rows shifted one step each, and `zip` does the
  transposing. A binary search on k then asks whether k copies of a
  letter occur in the text, with `bytes.find`. Dot separators and padding
  prevent runs from crossing between lines or extending outside the field.
  Building the text takes `O(N²)` time and memory; the binary searches
  take `O(N² log N)` time in the worst case, with `O(N²)` total memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1287_dp.cpp](1287_dp.cpp) | G++ 13.2 x64 | dp | O(N²) | AC | 0.093 s | 232 KB | 11284526 |
| [1287_dp.go](1287_dp.go) | Go 1.14 x64 | dp | O(N²) | AC | 0.109 s | 6276 KB | 11284528 |
| [1287_dp.java](1287_dp.java) \* | Java 1.8 | dp | O(N²) | AC | 0.171 s | 4624 KB | 11284535 |
| [1287_dp.py](1287_dp.py) \* | Python 3.12 x64 | dp | O(N² log N) | AC | 0.406 s | 25392 KB | 11284533 |
| [1287_dp.rs](1287_dp.rs) | Rust 1.75 x64 | dp | O(N²) | AC | 0.046 s | 3160 KB | 11284536 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1287_dp_optimized.cpp](1287_dp_optimized.cpp) \* | G++ 13.2 x64 | dp | O(N²) | AC | 0.062 s | 124 KB | 11311205 |
| [1287_dp_optimized.go](1287_dp_optimized.go) \* | Go 1.14 x64 | dp | O(N²) | AC | 0.046 s | 916 KB | 11310411 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
