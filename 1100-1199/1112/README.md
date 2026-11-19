# 1112. Keeping the most segments with no common inner point

[Timus 1112](https://acm.timus.ru/problem.aspx?space=1&num=1112) · difficulty 165 · greedy

Original problem from the Bulgarian National Olympiad in Informatics, Day 2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` segments on a line (`1 ≤ N ≤ 99`), segment `i` from `A_i`
to `B_i` with integers `−999 ≤ A_i < B_i ≤ 999`. Remove as few segments as
possible so that no two of the remaining ones share an inner point; ends
may touch. Print the remaining segments.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines `A_i B_i`.

## Output

The number `P` of segments kept, then `P` lines `A B` in increasing order
of the left ends. Any optimal answer is accepted.

## Checking

Any optimal answer is accepted. The checker computes the largest possible
number of segments by a quadratic DP and verifies that the output keeps
that many, takes them from the input, lists them by left end and has no
two of them overlapping.

## Examples

### Example 1

Input:

```
3
3 6
1 3
2 5
```

Output:

```
2
1 3
3 6
```

## Solution

This is interval scheduling. Sort the segments by their right ends and
take each one that starts no earlier than the right end of the last taken
segment. The segment that ends first is always part of some optimal
answer: in any optimal set, the segment with the leftmost right end can be
swapped for it without creating an overlap. Repeating the argument on the
rest proves the greedy choice. The kept segments are disjoint, so their
order by right end is also their order by left end. `O(N log N)`.

Pitfalls:

- touching segments (one ends where the next starts) share no inner point
  and may both stay;
- sorting by left end, or by length, and taking greedily gives wrong
  answers: a long segment that starts first can block several short ones;
- segments may repeat; each copy is a separate segment, but at most one of
  them can stay.

The answers were checked by the checker on every test and on 150 random
sets, including touching chains, repeated segments and nested ones.

## Optimized solutions

`1112_greedy_optimized.py`. Keep earliest-finish interval scheduling and allow touching endpoints. Store (end,start) tuples and sort them directly instead of storing an input list and using a key function. Compact chosen intervals into the same list prefix, then emit them without a second chosen list or joined output string. O(n log n) time, O(n) space. Ties may select another equally valid optimum, checked by the constructive checker. Flush before direct PyPy exit.

Compared with `1112_greedy.py`: time 0.078 s → 0.125 s; memory 460 KB → 272 KB.

The optimized C++ solution keeps the segments in one global array of 99
pairs, since `N ≤ 99`, instead of two `vector`s, and writes the kept
segments over the front of the same array: a kept segment only takes the
place of one already scanned. No heap memory is allocated:
{1112_greedy_optimized.cpp}.

The optimized Java solution reads the input in 4 KB blocks and parses
the signed numbers by hand instead of `Scanner`, keeps the ends in two
`int` arrays instead of an array object per segment, and sorts them by
insertion, which for `N ≤ 99` is cheap and needs no comparator; the kept
segments are written over the front of the same arrays:
{1112_greedy_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1112_greedy_optimized.cpp`: time reduction +0.00%; memory reduction
  +41.67%; base: `1112_greedy.cpp`.

- `1112_greedy_optimized.java`: time reduction +40.38%; memory reduction
  +89.45%; base: `1112_greedy.java`.

`1112_greedy_optimized.rs`. Keep earliest-finish interval scheduling, allowing touching endpoints. Sort the one segment vector with sort_unstable_by_key, then compact chosen segments into its already-scanned prefix. No separate chosen vector or output builder is needed. Equal finishing times may be reordered: any optimal valid set is accepted. Time O(N log N), storage O(N). The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1112_greedy.rs`: time 0.015 s → 0.031 s; memory 232 KB → 64 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1112_greedy_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1112_greedy.cpp](1112_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 192 KB | 11279212 |
| [1112_greedy.go](1112_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.015 s | 1156 KB | 11279213 |
| [1112_greedy.java](1112_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.156 s | 3944 KB | 11279215 |
| [1112_greedy.py](1112_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 460 KB | 11279214 |
| [1112_greedy.rs](1112_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 232 KB | 11279216 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1112_greedy_optimized.cpp](1112_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 112 KB | 11307228 |
| [1112_greedy_optimized.java](1112_greedy_optimized.java) | Java 1.8 | greedy | O(N²) | AC | 0.093 s | 416 KB | 11307227 |
| [1112_greedy_optimized.rs](1112_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.031 s | 64 KB | 11325084 |
| [1112_greedy_optimized.py](1112_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(n log n) time; O(n) space | AC | 0.125 s | 272 KB | 11325703 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
