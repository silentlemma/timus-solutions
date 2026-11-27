# 1116. Cutting one piecewise-constant function by the domain of another

[Timus 1116](https://acm.timus.ru/problem.aspx?space=1&num=1116) · difficulty 333 · two_pointers

Original problem by Oleg Kats, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A piecewise-constant function is a list of disjoint half-open intervals
`[A, B)` with a value `Y` on each, sorted by `A`; two touching intervals
never have the same value. Given two such functions `F1` and `F2` (each
with `1 ≤ N ≤ 15000` intervals, `|A|, |B| < 32000`, `A < B`, `|Y| ≤ 100`),
build `F`: it equals `F1` wherever `F1` is defined and `F2` is not, and is
undefined everywhere else.

All interval endpoints A,B and values Y are integers.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

Two lines, one per function: `N`, then `N` triples `A B Y`.

## Output

One line in the same format describing `F`; `0` alone if `F` is defined
nowhere.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 -1 1 2 1 3 4 4 6 3
2 -2 2 1 5 7 5
```

Output:

```
2 2 3 4 4 5 3
```

## Solution

Both lists are sorted, so a single pass with two pointers is enough. For
each interval `[A, B)` of `F1`, walk a cursor from `A` to `B`: skip the
intervals of `F2` that end at or before the cursor; if the next one
already covers the cursor, jump the cursor to its end; otherwise emit the
piece from the cursor to the start of that interval (or to `B`) with the
value `Y`. The pointer into `F2` never moves back, so the whole pass is
`O(N1 + N2)`.

Let Q be the number of output pieces. Each masking interval can add
at most one split to the N1 original intervals, so Q<=N1+N2. Simple
versions retain both input lists and their collected result pieces or
answer text: O(N1+N2+Q) cells plus any P output bytes. Python/Rust
retain the full I-byte input as well; Python also retains split tokens.
Optimized C++/Go stream the masking list but keep the first list and
Q result triples. Optimized Python/Rust retain both packed lists and
Q packed triples; buffered output avoids retaining a full output string.
Packing changes constants, not the linear storage bound.

The pieces need no merging: pieces cut from one interval are separated by
holes, and pieces of two different intervals can only touch where the
intervals touched, and those have different values.

Pitfalls:

- the intervals are half-open: `[0, 2)` and `[2, 4)` touch but do not
  overlap, so an interval of `F2` ending at `x` does not cover `x`;
- an interval of `F2` may span several intervals of `F1`, so its pointer
  must not advance just because one interval of `F1` is finished;
- when nothing is left, the answer is the single number `0`.

The answers were checked against a brute force that evaluates both
functions on every unit cell of the coordinate range and merges runs of
equal values back into intervals, on every test and 100 random pairs.

## Optimized solutions

The C++ revision retains signed 16-bit interval fields and the linear masking sweep. Fixed 16 KB input/output buffers replace per-field scanf and printf calls, including signed endpoints and values. The result count is still known before its compact interval array is printed.

Exact-source Accepted (G++ 13.2 x64, #11326648: 0.015 s / 412 KB); teaching base `1116_two_pointers.cpp`: 0.046 s / 1880 KB. The previous optimized measurement was 0.062 s / 444 KB. In the saved 20 November 2026 comparison, time place is 1/37, memory place 2/37; below 1 MiB the policy evaluates the time rank only.

The C++ and Go versions store each interval as three signed 16-bit values. They keep the first list and read the second as needed, retaining only the current masking interval. Each masking interval is read at most once. The output intervals are collected in a compact array because their count must be printed first. Time is O(N1 + N2).

The exact-source cached audit confirms simple Java by both ordinary
ranks. Simple Python/Rust do not qualify: their large-memory receipts
fail the applicable comparison. Python is covered by its distinct
1332-KB optimized source, passing both small-cohort metrics; Rust by
the distinct 688-KB implementation version, comparing time only in its
small exact-compiler cohort. Optimized C++ and both Go versions also
qualify on their applicable metrics. Reuse passing sources without
copies and keep meaningful teaching versions unstarred.

The current optimized Python/Rust revisions only name unchanged
constants: three fields per interval, whitespace cutoff 32, and Rust
inline token capacity 32. Python Accepted #11328769 (0.187 s / 1332 KB)
and Rust #11328958 (0.015 s / 688 KB) belong to preceding source bytes.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1116_two_pointers_optimized.py`. Pack interval triples into signed 16-bit arrays, which cover the stated coordinate bounds. Stream the intervals and buffer output in chunks; the two-pointer clipping logic remains unchanged. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328769 (Python 3.12 x64): **0.187 s / 1332 KB**. Archived comparison: `1116_two_pointers.py` (Python 3.12 x64) — 0.14 s / 13144 KB (#11279238).

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1116_two_pointers_implementation_optimized.rs`. Store interval endpoints in signed 16-bit values within their bounds and stream the output through a bounded writer instead of accumulating one large answer string. Interval processing is unchanged. Read tokens through a bounded native byte buffer; short tokens stay inline and only long tokens allocate spill storage. Decimal conversion retains the signed bounds without keeping the full command input. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328958 (Rust 1.75 x64): **0.015 s / 688 KB**. Archived comparison: `1116_two_pointers.rs` (Rust 1.75 x64) — 0.015 s / 2112 KB (#11279241).

## Language notes

These notes describe the simple implementations.

- All languages run the same pass; Go buffers writes, while the others
  build an output string.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1116_two_pointers.cpp](1116_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 1880 KB | 11279235 |
| [1116_two_pointers.go](1116_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 6832 KB | 11279236 |
| [1116_two_pointers.java](1116_two_pointers.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 5400 KB | 11279239 |
| [1116_two_pointers.py](1116_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N1 + N2) | AC | 0.14 s | 13144 KB | 11279238 |
| [1116_two_pointers.rs](1116_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 2112 KB | 11279241 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1116_two_pointers_optimized.cpp](1116_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 412 KB | 11326648 |
| [1116_two_pointers_optimized.go](1116_two_pointers_optimized.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.031 s | 1712 KB | 11310385 |
| [1116_two_pointers_optimized.py](1116_two_pointers_optimized.py) | Python 3.12 x64 | two_pointers | O(N1 + N2) | AC | 0.171 s | 1480 KB | 11331071 |
| [1116_two_pointers_implementation_optimized.rs](1116_two_pointers_implementation_optimized.rs) | Rust 1.75 x64 | two_pointers, implementation | O(N1 + N2) | AC | 0.031 s | 680 KB | 11331114 |
