# 1081. The K-th binary string without two adjacent ones

[Timus 1081](https://acm.timus.ru/problem.aspx?space=1&num=1081) · difficulty 271 · dp

Original problem by Emil Kelevedzhiev, from the Informatics Tournament of the Winter Mathematical Festival, Varna 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Consider all strings of length `N` (`0 < N < 44`) made of 0 and 1 with no
two adjacent ones, sorted lexicographically. Print the `K`-th of them
(`0 < K < 10^9`), or `-1` if there are fewer than `K`.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` and `K`.

## Output

The string, or `-1`.

## Checking

Compare the N-character binary word, or -1 for an out-of-range rank. The new exact Python source passed 15 repository fixtures under PyPy 3.10. Also 239 exhaustive short binary-string/rank checks. Other retained native variants keep their own saved target-runtime checks and exact Accepted receipts. Compare output according to the problem checker, not by choosing one historical formatting.

## Examples

### Example 1

Input:

```
3 1
```

Output:

```
000
```

## Solution

Let `count[r]` be the number of valid strings of length `r`: a string
starts either with 0 and any valid rest, or with `10` and any valid rest,
so `count[r] = count[r − 1] + count[r − 2]` with `count[0] = 1` and
`count[1] = 2`, the Fibonacci numbers.

Build the answer from the left. If the previous character is 1, this one
must be 0. Otherwise the strings with 0 here come first in the order, and
there are `count[rest]` of them, where `rest` is the number of positions
after this one (the 0 does not restrict the next character). If
`K ≤ count[rest]`, write 0; otherwise subtract `count[rest]` from `K` and
write 1. If `K > count[N]` from the start, print `-1`. `O(N)`.

Pitfalls:

- `count[43] = 1 134 903 170` is larger than any `K`, so for `N = 43`
  there is always an answer; the counts are kept in 64-bit integers
  anyway;
- after a 1 the next character is forced and `K` is not changed;
- the strings are counted from `K = 1`, the all-zero string.

The answers were checked against the sorted list of all valid strings for
`N ≤ 20`, and for longer strings by computing the rank of the answer back
from a memoised count.

## Optimized solutions

Keep the readable Fibonacci-count table. The compact versions retain only two adjacent counts and reverse the Fibonacci recurrence while unranking. If the residual zero-based rank is at least the zero-prefix count, subtract that count and emit one; otherwise emit zero. After choosing one, the residual interval is smaller than the next zero-prefix count, so the following bit is forced to zero without a separate special case. Counts also detect ranks outside the total. Python packs output bits into one integer and formats exactly N bits; only the O(N)-bit answer, not a count table, is retained.

- `1081_dp_optimized.java`: 0.078 s / 372 KB; base `1081_dp.java`: 0.125 s / 1640 KB; relative change: time -37.6%, memory -77.3%.
- `1081_dp_optimized.py`: 0.125 s / 284 KB; base `1081_dp.py`: 0.093 s / 476 KB; relative change: time +34.4%, memory -40.3%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1081_dp.cpp`; covering source `1081_dp.cpp`; time/memory places 1/6, other-author entries 93/93.

- Go: preferred teaching base `1081_dp.go`; covering source `1081_dp.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1081_dp.java`; covering source `1081_dp_optimized.java`; time/memory places 1/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1081_dp.py`; covering source `1081_dp_optimized.py`; time/memory places 22/2, other-author entries 22/22.

- Rust: preferred teaching base `1081_dp.rs`; covering source `1081_dp.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1081_dp.cpp](1081_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 200 KB | 11279006 |
| [1081_dp.go](1081_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.015 s | 1084 KB | 11279009 |
| [1081_dp.java](1081_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1640 KB | 11279012 |
| [1081_dp.py](1081_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 476 KB | 11279010 |
| [1081_dp.rs](1081_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 216 KB | 11279014 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1081_dp_optimized.java](1081_dp_optimized.java) | Java 1.8 | dp | O(N) | AC | 0.078 s | 372 KB | 11309292 |
| [1081_dp_optimized.py](1081_dp_optimized.py) \* | PyPy 3.10 x64 | dp | O(N) | AC | 0.125 s | 284 KB | 11309684 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
