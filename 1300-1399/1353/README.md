# 1353. Milliard Vasya's Function

[Timus 1353](https://acm.timus.ru/problem.aspx?space=1&num=1353) · difficulty 103 · dp

Original problem by Denis Musin, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given S, 1 ≤ S ≤ 81, count the integers from 1 to 10⁹ whose digit sum
is S.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number S.

## Output

The count.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
1
```

Output:

```
10
```

## Solution

Every number below 10⁹ is a string of nine digits once leading zeros are
added, and leading zeros do not change the digit sum. So count digit
strings: ways[s] after k digits is the number of k-digit strings with
sum s, and each new digit d from 0 to 9 moves ways[s] into s + d. After
nine digits, ways[S] counts the numbers from 0 to 999 999 999 with sum
S. Zero has sum 0, so it is never counted, and 10⁹ itself, with digit
sum 1, adds one when S = 1. `O(9 · 81 · 10)`.

Pitfalls:

- 10⁹ is in the range: S = 1 gives 10, not 9 (test 01);
- from S = 10 on, a single digit can no longer carry the whole sum, so
  plain stars and bars overcounts (test 07);
- the counts are symmetric, ways[s] = ways[81 − s], and the largest is
  45 433 800 at S = 40 and 41, which fits in 32 bits.

The same table for 10⁶ in place of 10⁹ was compared with counting the
digit sums of every number up to 10⁶.

## Optimized solutions

`1353_dp_optimized.java`. Retain the nine-digit DP and the extra number 10^9 when S=1. Replace ten digit transitions per sum by a sliding sum of ten previous states, reusing two long arrays of S+1 cells. The one input integer is parsed through a 1024-byte buffer instead of Scanner. Time O(9S), auxiliary space O(S); the basic ten-transition DP remains unchanged. Admission follows the own Accepted memory measurements, not a first-place claim.

Compared with `1353_dp.java`: time 0.125 s → 0.093 s; memory 1 576 KB → 476 KB.

`1353_dp_optimized.py`. Keep digit DP, but calculate each next row with a sliding sum rather than ten additions per state. Only sums up to min(S,9k) are stored after k digits, using two rows; time O(9S), auxiliary space O(S). The input has one bounded integer. Flush the complete answer before os._exit(0), which skips interpreter teardown; this alone is not an algorithmic speed guarantee. The judge used PyPy 3.10, while the retained simple source was rechecked on CPython 3.12: the displayed measurements belong to those compiler/runtime pairs. Memory improves from 496 KB to 228 KB, while time increases from 0.093 s to 0.125 s. Keep the simple source and mark the unmet rating target.

Compared with `1353_dp.py`: time 0.093 s → 0.125 s; memory 496 KB → 228 KB.

`1353_dp_optimized.rs`. Retain the same digit DP, replacing ten digit transitions by a sliding sum of ten previous states. Two fixed arrays of 82 u32 cells cover all sums through 81; only reachable sums are visited after each digit. For D=9 digits and M=9D, time is O(DM) and auxiliary space O(M), both bounded constants for this task. Counts never exceed the 10^9 possible digit strings and fit u32. C-runtime byte input/output avoids the standard Rust text and formatting allocations. Keep the extra 10^9 for S=1 and retain the simple source. The measured gain is memory; do not infer a speedup from a different historical run.

Compared with `1353_dp.rs`: time 0.062 s → 0.062 s; memory 216 KB → 60 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The five simple source files are unchanged. Their table rows now use the new exact-source Accepted rechecks, including both measurements and the submission ID; the original README tables are retained in the integration backup. These rechecks are not optimization claims.

`1353_dp_optimized.java`: time place 4/94, memory place 10/94 in this comparable sample.

`1353_dp_optimized.py`: time place 71/97, memory place 1/97 in this comparable sample.

`1353_dp_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission ID |
|----------|----------|----------|------------|---------|------|--------|----------|
| [1353_dp.cpp](1353_dp.cpp) | G++ 13.2 x64 | dp | O(9·81·10) | AC | 0.015 s | 184 KB | 11325593 |
| [1353_dp.go](1353_dp.go) | Go 1.14 x64 | dp | O(9·81·10) | AC | 0.031 s | 1096 KB | 11325576 |
| [1353_dp.java](1353_dp.java) | Java 1.8 | dp | O(9·81·10) | AC | 0.125 s | 1576 KB | 11325572 |
| [1353_dp.py](1353_dp.py) | Python 3.12 x64 | dp | O(9·81·10) | AC | 0.093 s | 496 KB | 11325599 |
| [1353_dp.rs](1353_dp.rs) | Rust 1.75 x64 | dp | O(9·81·10) | AC | 0.062 s | 216 KB | 11325616 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission ID |
|----------|----------|----------|------------|---------|------|--------|----------|
| [1353_dp_optimized.java](1353_dp_optimized.java) \* | Java 1.8 | dp | O(9S) time; O(S) space | AC | 0.093 s | 476 KB | 11324972 |
| [1353_dp_optimized.py](1353_dp_optimized.py) \* | PyPy 3.10 x64 | dp | O(9S) time; O(S) space | AC | 0.125 s | 228 KB | 11325475 |
| [1353_dp_optimized.rs](1353_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(DM) time; O(M) space | AC | 0.062 s | 60 KB | 11325096 |


\* Accepted; the rating target is not yet met. This version may be optimized further.
