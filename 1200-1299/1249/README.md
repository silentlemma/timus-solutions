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
2 3
1 1 1
1 0 1
```

Output:

```
No
```

### Example 2

Input:

```
3 4
1 1 0 1
1 1 0 1
0 0 0 1
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

Keep adjacent rows and test each 2×2 window as its last cell arrives. Native readable versions test the cells explicitly; Python represents a row by an integer bitmask. Reading costs O(NM); row state is O(M) entries natively or O(M) bits in Python plus its current line. A maximum 3000×3000 byte-per-pixel image takes 9000000 bytes and exceeds 4 MiB; smaller images can fit, and even the maximum bit-packed bitmap can fit. Thus full-image storage is not unconditionally impossible: streaming avoids the worst unpacked-input storage. Corner-only contact does not connect components.

Only the inaccurate memory comment was revised in the following five files; executable code and meaningful explanations remain. Their table rows retain historical Accepted pairs.

`1249_implementation.cpp` (#11283966); `1249_implementation.go` (#11283967); `1249_implementation.java` (#11283977); `1249_implementation.rs` (#11283979); `1249_implementation_parsing_optimized.go` (#11329324).

## Optimized solutions

`1249_implementation_optimized.rs`. Keep the forbidden 2×2 sum-of-three test. Replace two rows by one byte row plus saved upper-left and left cells; read each cell and update its column only after checking the window. Early No and final Yes are unchanged. O(NM) time and O(M) storage.

Compared with `1249_implementation.rs`: time 0.031 s → 0.625 s; memory 224 KB → 68 KB.

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

Recorded pairs are preserved: C++ 0.531 s/208 KB→0.078 s/128 KB (85.3% less time, 38.5% less memory); Python 0.218 s/1532 KB→0.125 s/3684 KB (42.7% less time, higher memory). The fast Python source is not admitted for time alone: 3684 KB≥1024, so memory is mandatory. Its exact-compiler reference allows 2060.8 KB; it fails memory despite passing time, and keeps its star. The unchanged simple Python 1532 KB passes both required metrics and covers the language. No independent time-improvement exception applies.

`1249_implementation_parsing_optimized.go` parses dimensions as integers and decodes input chunks directly into the current byte row, then tests windows against the previous row. It reserves 8192 input bytes, handles refill/EOF and avoids a byte-helper call per pixel. fastPrint supports only strings and writes fixed Yes/No text plus newline through a reusable buffer. It has no numeric output conversion; numeric routines are input-only. Geometry is unchanged.

The following Go Accepted pair belongs to the historical pre-comment source. Keep the paired measurements and the simple/distinct versions.

Accepted #11329324 (Go 1.14 x64): **0.031 s / 820 KB**.

## Language notes

The Python candidate was compared on 75,254 small images with an
independent flood fill that checks each component's bounding box,
including every binary image with each dimension at most four. Both
actual candidates passed the repository's 14 test inputs in Docker,
including 3000 × 3000 cases. Extra native/Python checks cover all four
missing-corner orientations and diagonal-only patterns at word boundaries.

The old 2 November filtered ranks are superseded by the source-bound cache and shared [rating criteria](../../RATING_CRITERIA.md): optimized C++ and simple Java qualify by time only; revised Go parser historically qualifies by time against the second of two exact-compiler peers, whereas base Go misses time. Both Rust measurements qualify through same-language fallback, not an empty-sample inference. Base C++ remains teaching. Numerical qualification of historical hashes and fresh exact-source Accepted for revised bytes are separate.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1249_implementation.cpp](1249_implementation.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.562 s | 188 KB | 11331141 |
| [1249_implementation.go](1249_implementation.go) | Go 1.14 x64 | implementation | O(N M) | AC | 0.062 s | 1052 KB | 11331015 |
| [1249_implementation.java](1249_implementation.java) | Java 1.8 | implementation | O(N M) | AC | 0.125 s | 476 KB | 11331046 |
| [1249_implementation.py](1249_implementation.py) | Python 3.12 x64 | implementation | O(N M) | AC | 0.218 s | 1532 KB | 11283970 |
| [1249_implementation.rs](1249_implementation.rs) | Rust 1.75 x64 | implementation | O(N M) | AC | 0.046 s | 216 KB | 11331109 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1249_implementation_optimized.cpp](1249_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N M) | AC | 0.078 s | 128 KB | 11308213 |
| [1249_implementation_optimized.py](1249_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N M) | AC | 0.125 s | 3684 KB | 11308214 |
| [1249_implementation_optimized.rs](1249_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(NM) time; O(M) space | AC | 0.625 s | 68 KB | 11325546 |
| [1249_implementation_parsing_optimized.go](1249_implementation_parsing_optimized.go) | Go 1.14 x64 | implementation, parsing | O(nm) time; O(m) row state + bounded input buffer | AC | 0.062 s | 816 KB | 11331016 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
