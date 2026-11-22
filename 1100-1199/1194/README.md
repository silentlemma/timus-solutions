# 1194. How many handshakes when a party splits up on the way home

[Timus 1194](https://acm.timus.ru/problem.aspx?space=1&num=1194) · difficulty 84 · math

Original problem by Leonid Volkov, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 20000` hobbits, `K` of them married couples, leave a party together.
At every crossroads a group splits into smaller groups, and everyone
shakes hands with everyone they are parting from. Groups keep splitting
until each is a single hobbit or a married couple. The splits are given;
count all handshakes.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `K`, then for each split the group number, the number of new
groups and the number and size of each.

## Output

The number of handshakes.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
3 0
1 2 2 2 3 1
2 2 4 1 5 1
```

Output:

```
3
```

## Solution

Any two hobbits, except spouses, shake hands exactly once: at the split
where they first end up in different groups. The only pairs that never
part are the married couples, which go home together. So the answer is
`N·(N − 1)/2 − K`, and the description of the splits does not matter.
`O(1)`, apart from reading the first line.

Pitfalls:

- the split lines may be skipped altogether, but a solution that adds up
  the pairs parted at each split gets the same number;
- `N·(N − 1)/2` reaches about `2·10⁸`, which still fits in 32 bits, though
  64-bit arithmetic costs nothing here.

The answers were compared with a separately written solution, which sums
the handshakes split by split, on 200 random parties and on every test.

## Optimized solutions

`1194_math_optimized.java`. Keep n*(n-1)/2-married in exact int arithmetic. As before, hierarchy records are irrelevant and are not parsed after the two header counts. All numeric fields used by the computation are consumed before output. Reuse one 256-byte array for input and then output, reserving twelve bytes per signed int; reverse only its newly written digits. This removes separate input/output/digit arrays without overwriting any value still needed by the algorithm. Time for parsing/output is linear in consumed bytes; buffer storage is fixed.

Exact-source Java 1.8 Accepted #11327761: 0.093 s / 356 KB. Saved 2026-11-20 compiler-cohort comparison: time 10/106, memory 3/106. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303576 was 0.125 s / 308 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1194_math_optimized.java`: 0.093 s / 356 KB; retained teaching base `1194_math.java`: 0.125 s / 1552 KB.

`1194_math_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327016 measures 0.078 s / 652 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 4/39, memory rank 24/39. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11324849, 0.125 s / 220 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`1194_math_optimized.go`. Keep the same number of unordered hobbit pairs, h(h−1)/2, minus the given couples. Only scalar arithmetic and constant auxiliary storage are needed. Use bounded 256-byte input and 64-byte output buffers with Go 1.14 syscall.Read/Write, retrying EINTR and partial writes and handling zero-byte EOF. This removes fmt/bufio/os.File initialization overhead. Linux tests and Windows cross-builds establish functional/build checks; the paired memory figures below come from our own exact Windows judge Accepted. Preserve the readable teaching source.

Compared with `1194_math.go`: time 0.015 s → 0.015 s; memory 1064 KB → 280 KB.

`1194_math_optimized.cpp`. Keep N(N-1)/2-K: every non-couple pair separates once, independently of the split descriptions. Read only the two header numbers and write the result with explicit C byte conversion instead of formatted integer scanning and printing. The algorithm and auxiliary state are constant-sized.

Compared with `1194_math.cpp`: time 0.031 s → 0.015 s; memory 128 KB → 80 KB.

`1194_math_optimized.py`. Read only the documented first line containing N and K as raw bytes; leave the split log unread because the pair-count invariant does not depend on it. Print N(N-1)/2-K, flush the answer explicitly and exit without normal interpreter teardown. No complete-input string or token list is retained.

Compared with `1194_math.py`: time 0.093 s → 0.125 s; memory 328 KB → 220 KB.

`1194_math_optimized.rs`. Use the same pair-count invariant while reading only two signed integers through the C runtime. The split descriptions need no storage or processing. Manual decimal output avoids Rust formatting and full input/output strings; time and auxiliary state stay O(1) under the integer bounds.

Compared with `1194_math.rs`: time 0.015 s → 0.015 s; memory 208 KB → 48 KB.

## Language notes

- All languages read only `N` and `K`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1194_math.cpp](1194_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB | 11283468 |
| [1194_math.go](1194_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1064 KB | 11283469 |
| [1194_math.java](1194_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1552 KB | 11283472 |
| [1194_math.py](1194_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 328 KB | 11283471 |
| [1194_math.rs](1194_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 208 KB | 11283473 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1194_math_optimized.java](1194_math_optimized.java) \* | Java 1.8 | math | O(1) arithmetic; header input only | AC | 0.093 s | 356 KB | 11327761 |
| [1194_math_optimized.cpp](1194_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 80 KB | 11325056 |
| [1194_math_optimized.py](1194_math_optimized.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 652 KB | 11327016 |
| [1194_math_optimized.rs](1194_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 48 KB | 11324859 |
| [1194_math_optimized.go](1194_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 280 KB | 11325654 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
