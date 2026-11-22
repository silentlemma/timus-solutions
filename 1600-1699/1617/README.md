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

`1617_implementation_optimized.py`. Keep the 101-bin histogram for diameters 600..700 and sum floor(frequency/4). Read binary input directly and write the complete short numeric answer with os.write before os._exit(0). The token split still retains input, so storage is O(I+101), where I is input bytes, not constant-space streaming. O(N+101) arithmetic work; all declared wheel-pair tokens are processed. The teaching Counter version remains.

Exact-source Python 3.12 x64 Accepted #11327789: 0.062 s / 660 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/104, memory 90/104. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11325072 was 0.125 s / 244 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1617_implementation_optimized.py`: 0.062 s / 660 KB; retained teaching base `1617_implementation.py`: 0.093 s / 368 KB.

`1617_implementation_optimized.java`. Keep one-pass grouping of equal diameters 600..700. A byte per diameter stores only the remainder modulo four: when it reaches four, reset it and count a car. The remainder never exceeds three between inputs, so signed bytes suffice; no final histogram pass is required. O(N) time and 101 bytes of grouping state. All numeric fields used by the computation are consumed before output. Reuse one 256-byte array for input and then output, reserving twelve bytes per signed int; reverse only its newly written digits. This removes separate input/output/digit arrays without overwriting any value still needed by the algorithm. Time for parsing/output is linear in consumed bytes; buffer storage is fixed.

Exact-source Java 1.8 Accepted #11327764: 0.078 s / 368 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/221, memory 6/221. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303764 was 0.109 s / 336 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1617_implementation_optimized.java`: 0.078 s / 368 KB; retained teaching base `1617_implementation.java`: 0.14 s / 1680 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

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
| [1617_implementation_optimized.java](1617_implementation_optimized.java) \* | Java 1.8 | implementation | O(N) time; 101 byte remainders | AC | 0.078 s | 368 KB | 11327764 |
| [1617_implementation_optimized.py](1617_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N+101) time; O(I+101) storage | AC | 0.062 s | 660 KB | 11327789 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
