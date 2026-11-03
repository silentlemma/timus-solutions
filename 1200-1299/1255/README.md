# 1255. Packing 1 × K coffins into a square

[Timus 1255](https://acm.timus.ru/problem.aspx?space=1&num=1255) · difficulty 282 · math

Original problem by Stanislav Vasilyev and Alexey Lakhtin, from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

How many 1 × K rectangles (coffins) fit, without overlapping and parallel
to the sides, into an N × N square (1 < N, K < 10 000)?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and K.

## Output

The largest number of coffins.

## Checking

Compare one exact integer token; formatting whitespace is ignored. The new exact Python source passed 16 repository fixtures under PyPy 3.10. Other retained native variants keep their own saved target-runtime checks and exact Accepted receipts. Compare output according to the problem checker, not by choosing one historical formatting.

## Examples

### Example 1

Input:

```
5 3
```

Output:

```
8
```

## Solution

If K > N nothing fits. Otherwise write N = qK + r with 0 ≤ r < K and let
s = min(r, K − r). The answer is

```text
(N² − s²) / K
```

and it is always a whole number, since N ≡ r and so N² ≡ r² ≡ (K − r)²
modulo K.

That many fit:

- for r ≤ K/2, coffins lying along the rows fill the first qK columns of
  every row, and coffins standing along the columns fill the last r
  columns in all but r rows, leaving an r × r corner empty;
- for r > K/2, four blocks of coffins arranged like a pinwheel around
  the centre leave a hole of (K − r) × (K − r).

No more fit: colour each cell by `(row + column) mod K`. A coffin covers
K consecutive cells of a row or a column, so exactly one cell of each
colour, and the number of coffins is at most the size of the smallest
colour class, which a count along the diagonals shows to be exactly
(N² − s²) / K. `O(1)`.

Pitfalls:

- the leftover square has side min(r, K − r), not r: for N = 7, K = 4,
  r = 3 but only a 1 × 1 hole is left, and 12 coffins fit (test 08);
- N² is at most 99,980,001 (N = 9999, test 03), which still fits in 32 bits.

The formula was compared with an exhaustive search for all N and K from
2 to 7.

## Optimized solutions

Use exactly the same integer corner-square formula as the teaching sources. For r=N mod K, let s=min(r,K-r); if N>=K, return (N*N-s*s)//K, otherwise zero. No floating-point rounding or answer table is involved. The compact source reads the existing text stream and writes the exact integer directly. Its own PyPy run supplies the memory saving; interpreter identity and the increased runtime are explicit below. The five simple files remain unchanged.

- `1255_math_optimized.java`: 0.109 s / 320 KB; base `1255_math.java`: 0.125 s / 1600 KB; relative change: time -12.8%, memory -80.0%.
- `1255_math_optimized.py`: 0.140 s / 248 KB; base `1255_math.py`: 0.078 s / 376 KB; relative change: time +79.5%, memory -34.0%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1255_math.cpp`; covering source `1255_math.cpp`; time/memory places 1/2, other-author entries 31/31.

- Go: preferred teaching base `1255_math.go`; covering source `1255_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1255_math.java`; covering source `1255_math_optimized.java`; time/memory places 3/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `1255_math.py`; covering source `1255_math_optimized.py`; time/memory places 6/1, other-author entries 7/7.

- Rust: preferred teaching base `1255_math.rs`; covering source `1255_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1255_math.cpp](1255_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11284031 |
| [1255_math.go](1255_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1132 KB | 11284034 |
| [1255_math.java](1255_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1600 KB | 11284037 |
| [1255_math.py](1255_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 376 KB | 11284036 |
| [1255_math.rs](1255_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 220 KB | 11284039 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1255_math_optimized.java](1255_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.109 s | 320 KB | 11309313 |
| [1255_math_optimized.py](1255_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.140 s | 248 KB | 11309692 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
