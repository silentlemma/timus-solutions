# 1617. Flat Spots

[Timus 1617](https://acm.timus.ru/problem.aspx?space=1&num=1617) · difficulty 65 · implementation

Original problem by Vladimir Yakovlev, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A depot has n wheel pairs (1 ≤ n ≤ 150), each of an integer diameter
from 600 to 700 mm. A tram car needs four wheel pairs of the same
diameter. How many cars can be equipped?

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

n, then the n diameters.

## Output

The number of cars.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
9
689
690
690
689
689
690
689
688
688
```

Output:

```
1
```

## Solution

Count the pairs of each diameter. A diameter with c pairs equips ⌊c / 4⌋
cars, and the diameters do not interact, so the answer is the sum over
all diameters. `O(n)`.

Pitfalls:

- leftover pairs of different diameters cannot be combined (test 01);
- eight pairs of one size equip two cars, not one (test 03).

## Optimized solutions

The optimized Java solution reads the input in 1 KB blocks and parses it
by hand instead of using `Scanner`; the diameters, from 600 to 700, are
counted in a plain array of 101 counters shifted by 600: 0.109 s instead
of 0.140 s and 336 KB instead of 1680 KB.

`1617_implementation_optimized.py`. Replace Counter with a list of 101 frequencies indexed by diameter-600, justified by the allowed range 600..700. Sum frequency//4, since cars cannot mix diameters. The byte-token iterator avoids decoded text and hash-table keys, but it still retains input tokens: total storage O(N+101), not constant-space streaming. Time O(N+101). The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1617_implementation.py`: time 0.093 s → 0.125 s; memory 368 KB → 244 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1617_implementation_optimized.py`: time place 88/104, memory place 1/104 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1617_implementation.cpp](1617_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11288341 |
| [1617_implementation.go](1617_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1092 KB | 11288342 |
| [1617_implementation.java](1617_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1680 KB | 11288344 |
| [1617_implementation.py](1617_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 368 KB | 11288343 |
| [1617_implementation.rs](1617_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 240 KB | 11303771 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1617_implementation_optimized.java](1617_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.109 s | 336 KB | 11303764 |
| [1617_implementation_optimized.py](1617_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N+101) | AC | 0.125 s | 244 KB | 11325072 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
