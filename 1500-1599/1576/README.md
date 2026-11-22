# 1576. Telephone Tariffs

[Timus 1576](https://acm.timus.ru/problem.aspx?space=1&num=1576) · difficulty 147 · implementation

Original problem: folklore, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three tariffs: basic, a fee N1 plus C1 per minute; combined, a fee N2
that includes T minutes, plus C2 for each minute over T; unlimited, a
fee N3. Calls of at most 6 seconds are free, and longer calls are
rounded up to whole minutes. Given up to 1000 calls as mm:ss, print the
monthly bill under each tariff.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N1 and C1, then N2, T and C2, then N3, all integers from 1 to 1000,
then K (1 ≤ K ≤ 1000) and the K call lengths as mm:ss, where
0 ≤ mm, ss ≤ 59.

## Output

Three lines in the format of the examples.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
135 1
220 10 1
300
5
00:05
00:10
09:59
07:00
01:01
```

Output:

```
Basic:     155
Combined:  230
Unlimited: 300
```

### Example 2

Input:

```
10 2
100 1 1
1000
1
03:00
```

Output:

```
Basic:     16
Combined:  102
Unlimited: 1000
```

## Solution

Add up the paid minutes: a call of s seconds adds nothing when s ≤ 6
and ⌈s / 60⌉ otherwise. With M minutes the bills are N1 + C1·M,
N2 + C2·max(0, M − T) and N3. They stay below 7·10⁷. `O(K)`.

Pitfalls:

- a call of exactly 6 seconds is free, one of 7 seconds costs a whole
  minute, and a call of exactly one minute costs one (test 03);
- the combined tariff charges nothing extra while the minutes stay
  within T, so the overage is never negative;
- the labels are padded to the same width: `Basic:` with five spaces,
  `Combined:` with two, `Unlimited:` with one.

## Optimized solutions

`1576_implementation_optimized.java`. Java reads each mm:ss call as two integers without splitting a string. Calls of at most six seconds are free; otherwise paid minutes are mm+(ss>0). Only their sum is retained. The same three tariff formulas use int arithmetic: at most 1000 calls of 60 paid minutes and tariff values up to 1000 bound the largest bill by 60001000. Reusable 1024-byte input/output buffers emit the exact labels, spaces and decimal values without StringBuilder concatenation. Time O(K), auxiliary space O(1). All 3600 minute/second pairs were checked against second-based rounding.

Exact-source Java 1.8 Accepted #11327448: 0.078 s / 356 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/54, memory 1/54. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. Both metrics rank first, so the separate language target also passes; no asterisk. The previously documented optimized run #11304530 was 0.125 s / 376 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1576_implementation_optimized.java`: 0.078 s / 356 KB; retained teaching base `1576_implementation.java`: 0.109 s / 2244 KB.

`1576_implementation_optimized.rs`. Keep free calls of at most six seconds and rounding every charged call up to a whole minute. Stream k mm:ss durations directly: the integer reader consumes the colon between the two fields, avoiding token searches and string splits. Accumulate only total charged minutes and preserve all three tariff formulas, labels and alignment spaces. O(k) time, O(1) auxiliary storage; no sorting or change to billing rules.

Compared with `1576_implementation.rs`: time 0.015 s → 0.015 s; memory 232 KB → 52 KB.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1576_implementation_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1576_implementation.cpp](1576_implementation.cpp) | G++ 13.2 x64 | implementation | O(K) | AC | 0.015 s | 132 KB | 11287847 |
| [1576_implementation.go](1576_implementation.go) | Go 1.14 x64 | implementation | O(K) | AC | 0.015 s | 1168 KB | 11287851 |
| [1576_implementation.java](1576_implementation.java) | Java 1.8 | implementation | O(K) | AC | 0.109 s | 2244 KB | 11287858 |
| [1576_implementation.py](1576_implementation.py) | Python 3.12 x64 | implementation | O(K) | AC | 0.078 s | 508 KB | 11287853 |
| [1576_implementation.rs](1576_implementation.rs) | Rust 1.75 x64 | implementation | O(K) | AC | 0.015 s | 232 KB | 11287860 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1576_implementation_optimized.java](1576_implementation_optimized.java) | Java 1.8 | implementation | O(K) time; O(1) auxiliary space | AC | 0.078 s | 356 KB | 11327448 |
| [1576_implementation_optimized.rs](1576_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(k) time; O(1) space | AC | 0.015 s | 52 KB | 11325528 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
