# 1515. Cashmaster

[Timus 1515](https://acm.timus.ru/problem.aspx?space=1&num=1515) · difficulty 215 · greedy

Original problem by Ilya Grebnov, Nikita Rybak and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There is one banknote of each of N values (1 ≤ N ≤ 100), given in
increasing order, each from 1 to 10⁶. Find the smallest positive value
that is not the sum of some of these banknotes; a single banknote
counts as a sum.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N values in increasing order.

## Output

The smallest value that no set of banknotes adds up to.

## Checking

Exact integer tokens. New sources keep their own full target-runtime tests and Accepted; previously published bases keep their original own Accepted rather than older archive measurements.

## Examples

### Example 1

Input:

```
5
1 2 4 9 100
```

Output:

```
8
```

## Solution

Go through the values in increasing order and keep reach, the largest
number such that every sum from 1 to reach can be paid. If the next
value d is at most reach + 1, then every sum up to reach + d can be paid
too: the sums up to reach as before, and the larger ones as d plus a
sum up to reach. If d > reach + 1, then reach + 1 cannot be paid: the
values taken so far add up to only reach, and every other value is
larger than reach + 1 by itself. The answer is reach + 1. The input is already sorted, so no sorting is needed. The time is `O(N)`
and the greedy keeps `O(1)` extra state. C++, Go and Java read the notes
as a stream; Python and Rust also store the input, using `O(N)` memory.

Pitfalls:

- the given increasing order is essential to the greedy argument; another
  sort is unnecessary (tests 05, 06 have N = 100);
- without a banknote of 1 the answer is 1 (tests 03, 06);
- the answer can be larger than every value, up to the sum of all of
  them plus one (tests 04, 05, gen2);
- the first gap ends the scan, and no later value can fill it: with 1
  and 3 the sum 2 is missing (test 07).

## Optimized solutions

All five teaching versions use the linear greedy scan on the already sorted input. If every sum through `reach` is possible, a banknote of value at most `reach + 1` extends that range through `reach + note`. A larger banknote leaves the first gap unfillable, so the scan ends there. The compact Python version keeps this invariant and writes the answer directly. Its Accepted PyPy run used 244 KB versus 352 KB for the accepted teaching version, a reduction of 30.7%. Runtime rose from 0.093 s to 0.125 s.

- `1515_greedy_optimized.py`: 0.125 s / 244 KB; base `1515_greedy.py`: 0.093 s / 352 KB; relative change: time +34.4%, memory -30.7%.

`1515_greedy_optimized.rs`. Maintain the largest fully representable prefix of nonnegative sums. A sorted note at most reach+1 extends it by the note value; the first larger note exposes the smallest gap, so remaining input need not be stored or processed. O(N) worst-case time and O(1) auxiliary space. Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1515_greedy.rs`: time 0.015 s → 0.031 s; memory 220 KB → 64 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1515_greedy_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1515_greedy.cpp](1515_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.015 s | 112 KB | 11307976 |
| [1515_greedy.go](1515_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 1072 KB | 11307979 |
| [1515_greedy.java](1515_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.078 s | 420 KB | 11307981 |
| [1515_greedy.py](1515_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.093 s | 352 KB | 11307983 |
| [1515_greedy.rs](1515_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.015 s | 220 KB | 11307984 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1515_greedy_optimized.py](1515_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(N) time; O(N) input tokens | AC | 0.125 s | 244 KB | 11309746 |
| [1515_greedy_optimized.rs](1515_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N) | AC | 0.031 s | 64 KB | 11325100 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
