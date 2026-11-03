# 1150. How many times each digit appears in the page numbers from 1 to N

[Timus 1150](https://acm.timus.ru/problem.aspx?space=1&num=1150) · difficulty 249 · math

Original problem by Evgeny Bryzgalov, from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Pages are numbered from 1 to `N`, `N < 10⁹`. Count how many times each
digit from 0 to 9 is written.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

Ten lines: the counts of zeros, ones, …, nines.

## Checking

Compare ten exact integer counts in digit order 0..9; whitespace is ignored. The new exact Python source passed 12 repository fixtures under PyPy 3.10. Other retained native variants keep their own saved target-runtime checks and exact Accepted receipts. Compare output according to the problem checker, not by choosing one historical formatting.

## Examples

### Example 1

Input:

```
12
```

Output:

```
1
5
2
1
1
1
1
1
1
1
```

## Solution

Count every decimal position separately. For the position with weight
`p` (1, 10, 100, …), split `N` into the part above it, `high = N / (10p)`,
the digit `cur` there and the part below, `low = N mod p`. Look at the
numbers from 1 to `N` by their part above this position:

- every upper part from `0` to `high − 1` is followed by all `10p` lower
  endings, so each digit appears `p` times at this position for each of
  them;
- with the upper part equal to `high`, a digit `d < cur` appears `p` more
  times, `d = cur` appears `low + 1` more times (for the endings `0` to
  `low`), and larger digits not at all.

Zeros are different: a zero at this position is written only if some
nonzero digit stands above it, so the upper part `0` does not count. That
gives `(high − 1)·p` for the full upper parts from 1, and then `p` or
`low + 1` as above, all only when `high > 0`. There are at most nine
positions. `O(log N)`.

Pitfalls:

- leading zeros are not written, which is why zeros need the separate
  rule;
- the counts reach `9·10⁸` for `N = 999999999`, still within 32 bits;
- `N` itself is included.

The answers were compared with writing out every number for all `N` up
to 3000 and many up to 30000, and with a digit-by-digit count over the
decimal form of `N` on every test.

## Optimized solutions

The positional counting algorithm is unchanged: at each decimal place split N into higher digits, the current digit and lower digits. Each nonzero digit gets complete cycles plus the partial cycle; zero excludes the all-leading-zero block. Keep the ten counters and advance the place by a factor of ten. The compact sources reduce input/output overhead, rather than introduce a different counting formula. The Python source has its own PyPy receipt; it trades higher measured time for lower memory, while every readable version remains.

- `1150_math_optimized.java`: 0.078 s / 320 KB; base `1150_math.java`: 0.109 s / 1568 KB; relative change: time -28.4%, memory -79.6%.
- `1150_math_optimized.py`: 0.140 s / 316 KB; base `1150_math.py`: 0.062 s / 460 KB; relative change: time +125.8%, memory -31.3%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1150_math.cpp`; covering source `1150_math.cpp`; time/memory places 1/1, other-author entries 39/39.

- Go: preferred teaching base `1150_math.go`; covering source `1150_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1150_math.java`; covering source `1150_math_optimized.java`; time/memory places 1/1, other-author entries 5/5.

- Python/PyPy: preferred teaching base `1150_math.py`; covering source `1150_math_optimized.py`; time/memory places 22/4, other-author entries 21/21.

- Rust: preferred teaching base `1150_math.rs`; covering source `1150_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1150_math.cpp](1150_math.cpp) | G++ 13.2 x64 | math | O(log N) | AC | 0.015 s | 128 KB | 11280268 |
| [1150_math.go](1150_math.go) | Go 1.14 x64 | math | O(log N) | AC | 0.031 s | 1084 KB | 11280291 |
| [1150_math.java](1150_math.java) | Java 1.8 | math | O(log N) | AC | 0.109 s | 1568 KB | 11280333 |
| [1150_math.py](1150_math.py) | Python 3.12 x64 | math | O(log N) | AC | 0.062 s | 460 KB | 11280317 |
| [1150_math.rs](1150_math.rs) | Rust 1.75 x64 | math | O(log N) | AC | 0.015 s | 236 KB | 11280335 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1150_math_optimized.java](1150_math_optimized.java) | Java 1.8 | math | O(log N) | AC | 0.078 s | 320 KB | 11308801 |
| [1150_math_optimized.py](1150_math_optimized.py) \* | PyPy 3.10 x64 | math | O(log N) | AC | 0.140 s | 316 KB | 11309691 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
