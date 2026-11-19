# 1644. A Whole Lot of Walnuts

[Timus 1644](https://acm.timus.ru/problem.aspx?space=1&num=1644) · difficulty 100 · implementation

Original problem by Alexey Samsonov, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A parrot ate between 3 and 9 walnuts in each of n experiments and wrote
down whether it stayed hungry or was satisfied. Satisfaction is
monotone: more walnuts never leave it hungrier. It is known that ten
walnuts always satisfy it and two never do. Find the least number of
walnuts that surely satisfies it, or report that the records contradict
each other.

## Input

n (0 ≤ n ≤ 100), then n lines: a number of walnuts and `hungry` or
`satisfied`.

## Output

The least number of walnuts that is sure to satisfy, or
`Inconsistent`.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
4
4 hungry
7 satisfied
5 hungry
8 satisfied
```

Output:

```
7
```

### Example 2

Input:

```
2
6 hungry
5 satisfied
```

Output:

```
Inconsistent
```

## Solution

Take the largest hungry amount, starting from 2, and the smallest
satisfying amount, starting from 10. The records fit a monotone
threshold exactly when the second is larger; then the smallest
satisfying amount is the answer, since anything less has never been
seen to satisfy. Otherwise `Inconsistent`. `O(n)`.

Pitfalls:

- with no records the answer is 10 (test 03), with only hungry ones the
  answer stays 10 (test 04);
- the same amount recorded both ways is a contradiction (test 06).

The answers match an independent accepted implementation on 180 random
record sets.

## Optimized solutions

`1644_implementation_optimized.py`. Keep the maximum hungry observation and minimum full observation, initialized to 2 and 10. Iterate exactly n numeric/verdict byte pairs instead of making two strided list slices. Output the full bound only when it strictly exceeds the hungry bound. The algorithm uses two extrema, but split input is still retained: O(n) time and O(I) total storage for input size I. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `1644_implementation.py`: time 0.109 s → 0.156 s; memory 444 KB → 212 KB.

The optimized Java solution parses the numbers by hand from a small
buffer instead of using `Scanner` and tells the two words apart by their
first letter, `h` or `s`, skipping the rest: 400 KB instead of
1708 KB, with the same time.

The optimized C++ solution reads with `scanf` into a small `char` array
instead of `iostream` and `std::string`, and tells the two words apart
by the first letter: 128 KB instead of 388 KB, with the same time.

`1644_implementation_optimized.rs`. Update only the largest hungry observation and the smallest satisfied observation. Distinguish the two stated response words by their first byte and skip the rest of the token without allocating it. The interval is consistent exactly when the upper bound exceeds the lower bound. O(N) time, O(1) auxiliary state. Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1644_implementation.rs`: time 0.015 s → 0.031 s; memory 220 KB → 64 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1644_implementation_optimized.py`: time place 53/53, memory place 1/53 in this comparable sample.

`1644_implementation_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1644_implementation.cpp](1644_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 388 KB | 11303499 |
| [1644_implementation.go](1644_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1084 KB | 11288487 |
| [1644_implementation.java](1644_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1708 KB | 11288489 |
| [1644_implementation.py](1644_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 444 KB | 11288488 |
| [1644_implementation.rs](1644_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 220 KB | 11288490 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1644_implementation_optimized.cpp](1644_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303768 |
| [1644_implementation_optimized.java](1644_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 400 KB | 11303630 |
| [1644_implementation_optimized.rs](1644_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 64 KB | 11324867 |
| [1644_implementation_optimized.py](1644_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) time; O(I) space | AC | 0.156 s | 212 KB | 11325477 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
