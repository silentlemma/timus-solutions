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

`1150_math_optimized.go`. Keep positional high/current/low digit counting and the leading-zero correction. Guard multiplication of the place value and compare via limit/place/radix to avoid overflow. O(log N) time and constant auxiliary space; no enumeration of all numbers. Use bounded 256-byte input and 64-byte output buffers with Go 1.14 syscall.Read/Write, retrying EINTR and partial writes and handling zero-byte EOF. This removes fmt/bufio/os.File initialization overhead. Linux tests and Windows cross-builds establish functional/build checks; the paired memory figures below come from our own exact Windows judge Accepted. Preserve the readable teaching source.

Compared with `1150_math.go`: time 0.031 s → 0.015 s; memory 1084 KB → 292 KB.

`1150_math_optimized.rs`. Retain the same high/current/low positional formulas, including the correction that excludes leading zeros. Direct numeric input and ten direct integer output lines replace the standard text/formatting path; the fixed ten counters and the algorithm itself are unchanged. Time O(log(N+1)), auxiliary space O(1) within the statement’s integer bounds. Keep the readable formula-based source alongside the measured smaller-runtime variant.

Compared with `1150_math.rs`: time 0.015 s → 0.046 s; memory 236 KB → 40 KB.

The positional counting algorithm is unchanged: at each decimal place split N into higher digits, the current digit and lower digits. Each nonzero digit gets complete cycles plus the partial cycle; zero excludes the all-leading-zero block. Keep the ten counters and advance the place by a factor of ten. The compact sources reduce input/output overhead, rather than introduce a different counting formula. The Python source has its own PyPy receipt; it trades higher measured time for lower memory, while every readable version remains.

- `1150_math_optimized.java`: 0.078 s / 320 KB; base `1150_math.java`: 0.109 s / 1568 KB; relative change: time -28.4%, memory -79.6%.
- `1150_math_optimized.py`: 0.140 s / 316 KB; base `1150_math.py`: 0.062 s / 460 KB; relative change: time +125.8%, memory -31.3%.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1150_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [1150_math_optimized.rs](1150_math_optimized.rs) \* | Rust 1.75 x64 | math | O(log(N+1)) time; O(1) space | AC | 0.046 s | 40 KB | 11325542 |
| [1150_math_optimized.go](1150_math_optimized.go) \* | Go 1.14 x64 | math | O(log N) time; O(1) space | AC | 0.015 s | 292 KB | 11325653 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
