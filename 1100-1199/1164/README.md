# 1164. Which letters are left after finding all words of a fillword

[Timus 1164](https://acm.timus.ru/problem.aspx?space=1&num=1164) · difficulty 207 · strings

Original problem by Alex Selivanov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A grid of `N×M` capital letters (`2 ≤ N, M ≤ 10`) hides `P ≤ 100` words.
Each word occupies a path of side-adjacent cells, and no cell belongs to
two words or twice to the same word. A valid placement always exists.
Print the letters of the cells not used by any word, in alphabetical
order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, `M` and `P`, then `N` rows of the grid, then the `P` words.

## Output

The leftover letters, sorted, on one line.

## Checking

Compare the remaining uppercase-letter token exactly; an empty remainder permits empty output. The new exact Python source passed 11 repository fixtures under PyPy 3.10. Other retained native variants keep their own saved target-runtime checks and exact Accepted receipts. Compare output according to the problem checker, not by choosing one historical formatting.

## Examples

### Example 1

Input:

```
3 3 2
EBG
GEE
EGE
BEG
GEE
```

Output:

```
EEG
```

## Solution

No path search is needed. For each letter `c`, let `G[c]` count its
cells in the grid and `U[c]` its occurrences in the listed words. Any valid
placement uses exactly `U[c]` different cells carrying `c`: paths cannot
reuse cells, and different words cannot overlap. Thus every placement
leaves exactly `G[c] − U[c]` copies of `c`, independently of its geometry.
The promise that a placement exists guarantees nonnegative differences.

Count grid letters, subtract word letters with multiplicity, and emit
each letter from `A` through `Z` the remaining number of times. This
produces precisely the leftover multiset in sorted order. Duplicate
words still consume their letters separately. If all cells are used,
print an empty line. The promise also gives total word length
`W ≤ N M ≤ 100`, and hence each word fits in 100 characters.

Time is `O(N M + W + 26)`. Native bases keep 26 counters; Python's
readable base uses `Counter`. Including stored input and output, `O(N M + W)`
space is a bound for all versions; streaming versions need less input
storage. All five original Accepted sources are retained unchanged.

## Optimized solutions

All placements consume the same multiset of letters. Keep the clear counting sources and the compact C++ counter. Python scans the grid and concatenated words for each of the fixed 26 capital letters, then emits each positive difference in sorted order. Multiplying a linear scan by a constant alphabet remains linear. It avoids importing Counter and keeping a separate dictionary per multiset, while retaining the input strings. Reading the existing text streams and writing the final string also avoids extra input wrappers. The measured improvement is memory only; preserve the slower-time tradeoff below.

- `1164_strings_optimized.cpp`: 0.015 s / 104 KB; base `1164_strings.cpp`: 0.015 s / 380 KB; relative change: time -0.0%, memory -72.6%.
- `1164_strings_optimized.py`: 0.109 s / 260 KB; base `1164_strings.py`: 0.078 s / 436 KB; relative change: time +39.7%, memory -40.4%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1164_strings.cpp`; covering source `1164_strings_optimized.cpp`; time/memory places 1/1, other-author entries 46/46.

- Go: preferred teaching base `1164_strings.go`; covering source `1164_strings.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1164_strings.java`; covering source `1164_strings.java`; time/memory places 1/1, other-author entries 1/1.

- Python/PyPy: preferred teaching base `1164_strings.py`; covering source `1164_strings_optimized.py`; time/memory places 7/2, other-author entries 12/12.

- Rust: preferred teaching base `1164_strings.rs`; covering source `1164_strings.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1164_strings.cpp](1164_strings.cpp) | G++ 13.2 x64 | strings | O(N M + W) | AC | 0.015 s | 380 KB | 11283052 |
| [1164_strings.go](1164_strings.go) | Go 1.14 x64 | strings | O(N M + W) | AC | 0.031 s | 1184 KB | 11283056 |
| [1164_strings.java](1164_strings.java) | Java 1.8 | strings | O(N M + W) | AC | 0.109 s | 1640 KB | 11283063 |
| [1164_strings.py](1164_strings.py) | Python 3.12 x64 | strings | O(N M + W) | AC | 0.078 s | 436 KB | 11283059 |
| [1164_strings.rs](1164_strings.rs) | Rust 1.75 x64 | strings | O(N M + W) | AC | 0.015 s | 220 KB | 11283064 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1164_strings_optimized.cpp](1164_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(N M + W) | AC | 0.015 s | 104 KB | 11308330 |
| [1164_strings_optimized.py](1164_strings_optimized.py) \* | PyPy 3.10 x64 | strings | O(N M + W) | AC | 0.109 s | 260 KB | 11309679 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
