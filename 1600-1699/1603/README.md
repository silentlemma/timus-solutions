# 1603. Erudite

[Timus 1603](https://acm.timus.ru/problem.aspx?space=1&num=1603) · difficulty 255 · implementation

Original problem by Vladimir Yakovlev, from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 4 × 4 grid holds lowercase letters. A word can be written in it along a
path of horizontally or vertically neighbouring cells that may turn at
right angles anywhere but never uses a cell twice. For each of up to 100
words of 1 to 16 letters, say whether it can be found.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Four rows of the grid, then n and the words.

## Output

`word: YES` or `word: NO` for each word.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
abra
adac
babr
arca
3
abracadabra
ababaab
ababaaba
```

Output:

```
abracadabra: YES
ababaab: YES
ababaaba: NO
```

## Solution

Search depth-first from every cell holding the first letter, stepping to
an unused neighbouring cell with the next letter. The cells used so far
form a 16-bit mask. Repeated letters can make the search revisit the
same situation many times: the same set of used cells ending in the
same cell, with the same rest of the word ahead. So a failed pair
(mask, cell) is remembered and never searched again; at most 16·2¹⁶
such pairs exist, and in practice far fewer are reachable. A quick check
first rejects a word that needs more of some letter than the grid has.

The results were compared with an independent implementation on
generated grids, including grids of one repeated letter with long words.

Pitfalls:

- letter counts can reject a word before any search: fifteen `a` cells
  cannot supply sixteen `a` letters, and the single `b` cell cannot be
  used for both ends of a word (test 04);
- repeated letters can lead to repeated search states, so remember failed
  (mask, cell) pairs; test 07 has fourteen `a` cells and distinct `b` and
  `c` cells, and its longest word passes the letter-count check;
- such a NO can come from parity alone: the grid is coloured like a
  chessboard, a path of 16 cells always ends on the other colour, so a
  word starting and ending in cells of one colour cannot use all 16
  cells (test 07);
- a cell must not be used twice, and steps are only horizontal or
  vertical (test 03).

## Optimized solutions

The search still follows neighboring cells without revisiting a cell. Memoize failed states by the current endpoint and visited-cell mask; the word position follows from the mask size, so it need not enlarge the key. Character domains and adjacency masks prune impossible continuations before branching. Repeated identical words reuse their result. The board is fixed and small, so the subset bound is explicit rather than a claim of polynomial search time.

- `1603_implementation_optimized.cpp`: 0.015 s / 176 KB; base `1603_implementation.cpp`: 0.031 s / 452 KB; relative change: time -51.6%, memory -61.1%.
- `1603_implementation_optimized.go`: 0.031 s / 988 KB; base `1603_implementation.go`: 0.031 s / 5708 KB; relative change: time -0.0%, memory -82.7%.
- `1603_implementation_optimized.java`: 0.093 s / 620 KB; base `1603_implementation.java`: 0.109 s / 5228 KB; relative change: time -14.7%, memory -88.1%.
- `1603_implementation_optimized.py`: 0.093 s / 1128 KB; base `1603_implementation.py`: 0.359 s / 21264 KB; relative change: time -74.1%, memory -94.7%.
- `1603_implementation_optimized.rs`: 0.031 s / 292 KB; base `1603_implementation.rs`: 0.062 s / 420 KB; relative change: time -50.0%, memory -30.5%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1603_implementation.cpp`; covering source `1603_implementation_optimized.cpp`; time/memory places 1/1, other-author entries 59/59.

- Go: preferred teaching base `1603_implementation.go`; covering source `1603_implementation.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1603_implementation.java`; covering source `1603_implementation_optimized.java`; time/memory places 1/2, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1603_implementation.py`; covering source `1603_implementation_optimized.py`; time/memory places 1/1, other-author entries 3/3.

- Rust: preferred teaching base `1603_implementation.rs`; covering source `1603_implementation_optimized.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1603_implementation.cpp](1603_implementation.cpp) | G++ 13.2 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 452 KB | 11288124 |
| [1603_implementation.go](1603_implementation.go) | Go 1.14 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 5708 KB | 11288126 |
| [1603_implementation.java](1603_implementation.java) | Java 1.8 | implementation | O(n·16·2^16) | AC | 0.109 s | 5228 KB | 11288130 |
| [1603_implementation.py](1603_implementation.py) | Python 3.12 x64 | implementation | O(n·16·2^16) | AC | 0.359 s | 21264 KB | 11288128 |
| [1603_implementation.rs](1603_implementation.rs) | Rust 1.75 x64 | implementation | O(n·16·2^16) | AC | 0.062 s | 420 KB | 11288131 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1603_implementation_optimized.cpp](1603_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(16*2^16) per distinct word | AC | 0.015 s | 176 KB | 11309250 |
| [1603_implementation_optimized.go](1603_implementation_optimized.go) | Go 1.14 x64 | implementation | O(16*2^16) per distinct word | AC | 0.031 s | 988 KB | 11309252 |
| [1603_implementation_optimized.java](1603_implementation_optimized.java) \* | Java 1.8 | implementation | O(16*2^16) per distinct word | AC | 0.093 s | 620 KB | 11309251 |
| [1603_implementation_optimized.py](1603_implementation_optimized.py) | Python 3.12 x64 | implementation | O(16*2^16) per distinct word | AC | 0.093 s | 1128 KB | 11309249 |
| [1603_implementation_optimized.rs](1603_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(16*2^16) per distinct word | AC | 0.031 s | 292 KB | 11309253 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
