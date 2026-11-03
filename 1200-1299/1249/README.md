# 1249. Are all dark regions rectangles?

[Timus 1249](https://acm.timus.ru/problem.aspx?space=1&num=1249) · difficulty 221 · implementation

Original problem by Nikita Shamgunov and Leonid Volkov, from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given an `N × M` binary image with at most 3000 rows and 3000 columns, decide whether every side-connected component of 1s is an axis-aligned filled rectangle. Cells touching only at a corner are not connected. Time limit: 2.5 seconds. Memory limit: 4 MB.

## Input

`N M`, then `N` rows of `M` binary digits separated by spaces.

## Output

Print `Yes` if every component is a filled rectangle; otherwise print `No`.

## Checking

Compare output tokens: `Yes` or `No`, with the indicated capitalization. Whitespace formatting is insignificant.

## Examples

### Example 1

Input:

```
2 2
0 1
1 1
```

Output:

```
No
```

### Example 2

Input:

```
3 3
0 0 1
1 1 0
1 1 0
```

Output:

```
Yes
```

## Solution

A 2 × 2 window with exactly three dark cells belongs to one component,
but that component cannot be a filled rectangle. Conversely, the boundary
of a side-connected component that does not fill a rectangle has an inward
corner, including around a hole. That corner gives a 2 × 2 window with
three dark cells. Thus it suffices to reject exactly these windows.

Keep only adjacent rows, checking each window as its last cell arrives.
The readable native versions test the four cells explicitly; the readable
Python version represents rows by integers and tests odd parity together
with at least two set cells. Input takes `O(N M)` time and row storage is
`O(M)`; storing the entire image or its input text would exceed the memory
limit. Diagonally touching components remain separate. All five original
Accepted sources are preserved byte for byte.

## Optimized solutions

For two adjacent rows, let `B = previous AND current` mark vertically
full columns, and `S = previous XOR current` mark columns with one dark
cell. A forbidden window is exactly a full column beside a single column,
so `(B AND (S >> 1)) OR (S AND (B >> 1))` detects both orientations.

Python factors its former four-cell expression this way and removes row
whitespace with one translation. C++ packs columns in 64-bit words, reads
through a bounded buffer, checks each word in parallel and explicitly
checks the pair crossing each word boundary. It retains the previous
packed row and the current word. Logical row work is `O(ceil(M/64))` for
C++, while reading input still costs `O(N M)`; working row storage is
`O(M/64)` words. Python uses `O(M)` bits plus the current input line.

C++ changes from 0.531 s / 208 KB to 0.078 s / 128 KB: 85.3% less time
and 38.5% less memory. Python changes from 0.218 s / 1532 KB to 0.125 s /
3684 KB: 42.7% less time, but a higher recorded memory peak. Python is
admitted for time alone, not memory; both variants have their own Accepted.
These measurements do not imply that every resource improves.

## Language notes

The Python candidate was compared on 75,254 small images with an
independent flood fill that checks each component's bounding box,
including every binary image with each dimension at most four. Both
actual candidates passed the repository's 14 test inputs in Docker,
including 3000 × 3000 cases. Extra native/Python checks cover all four
missing-corner orientations and diagonal-only patterns at word boundaries.

The rating snapshot is from 2 November 2026. C++ meets the target
(time place 5, memory place 1, with 61 filtered other-author entries).
Python has time place 1 and memory place 2 against one entry, so it keeps
the star. The existing Java version is first on both metrics against four
entries. Go and Rust have empty filtered comparison samples; their formal
coverage does not establish competitive superiority.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1249_implementation.cpp](1249_implementation.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.531 s | 208 KB | 11283966 |
| [1249_implementation.go](1249_implementation.go) | Go 1.14 x64 | implementation | O(N M) | AC | 0.093 s | 1096 KB | 11283967 |
| [1249_implementation.java](1249_implementation.java) | Java 1.8 | implementation | O(N M) | AC | 0.156 s | 452 KB | 11283977 |
| [1249_implementation.py](1249_implementation.py) | Python 3.12 x64 | implementation | O(N M) | AC | 0.218 s | 1532 KB | 11283970 |
| [1249_implementation.rs](1249_implementation.rs) | Rust 1.75 x64 | implementation | O(N M) | AC | 0.031 s | 224 KB | 11283979 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1249_implementation_optimized.cpp](1249_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.078 s | 128 KB | 11308213 |
| [1249_implementation_optimized.py](1249_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N M) | AC | 0.125 s | 3684 KB | 11308214 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
