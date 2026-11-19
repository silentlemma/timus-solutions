# 1025. The fewest supporters to win a two-level majority vote

[Timus 1025](https://acm.timus.ru/problem.aspx?space=1&num=1025) · difficulty 67 · greedy, sorting

Original problem from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Voters are split into `K` groups (`K` odd, `1 ≤ K ≤ 101`), each of an odd
size; the total is at most 9999. A group says "yes" when more than half of
its members vote yes, and a decision passes when more than half of the
groups say "yes". Find the smallest number of supporters that, placed in the
right groups, pass any decision.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K`, then the `K` group sizes.

## Output

The smallest number of supporters.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
9 3 11 1 7
```

Output:

```
7
```

### Example 2

Input:

```
1
9999
```

Output:

```
5000
```

## Solution

To pass a decision the supporters must win `K / 2 + 1` groups (integer
division, `K` is odd), and winning a group of `s` voters (`s` odd) takes
`s / 2 + 1` supporters; any more in that group are wasted, and supporters in
lost groups are wasted too.

So choose `K / 2 + 1` groups with the smallest total cost `s / 2 + 1`. The
cost grows with the size, so the best groups are simply the smallest ones:
sort the sizes and add up the costs of the first `K / 2 + 1`.
`O(K log K)`.

Pitfalls:

- the majority of groups is `K / 2 + 1`, and the majority inside a group of
  `s` is `s / 2 + 1`, not `s / 2`;
- the sizes are not sorted in the input.

## Optimized solutions

The optimized Java solution reads the input in 1 KB blocks and parses it
by hand instead of using `Scanner`: 384 KB instead of 1724 KB, with the
same time.

`1025_greedy_sorting_optimized.go`. Go retains the majority-of-the-smallest-groups greedy choice. The optimized source reads bytes directly and inserts each group into one fixed array of at most 101 entries. This deliberately uses insertion sort: O(K²) time instead of the base sort's O(K log K), but avoids its dynamic containers and fmt overhead at this small limit. Sum floor(size/2)+1 for the first floor(K/2)+1 groups. The original library-sort source is preserved.

Compared with `1025_greedy_sorting.go`: time 0.031 s → 0.015 s; memory 1076 KB → 796 KB.

`1025_greedy_sorting_optimized.py`. Python keeps the sort-and-sum greedy algorithm. It converts byte tokens through an iterator directly into sorted, avoiding the separate decoded input string and an extra full integer list before sorting. Explicitly flush the answer before exiting without normal interpreter teardown. Time remains O(K log K), with O(K) storage for the sorted group sizes.

Compared with `1025_greedy_sorting.py`: time 0.093 s → 0.109 s; memory 372 KB → 212 KB.

## Language notes

The same sort and sum everywhere.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1025_greedy_sorting.cpp](1025_greedy_sorting.cpp) | G++ 13.2 x64 | greedy, sorting | O(K log K) | AC | 0.001 s | 188 KB | 11303273 |
| [1025_greedy_sorting.go](1025_greedy_sorting.go) | Go 1.14 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 1076 KB | 11278301 |
| [1025_greedy_sorting.java](1025_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(K log K) | AC | 0.109 s | 1724 KB | 11278306 |
| [1025_greedy_sorting.py](1025_greedy_sorting.py) | Python 3.12 x64 | greedy, sorting | O(K log K) | AC | 0.093 s | 372 KB | 11278304 |
| [1025_greedy_sorting.rs](1025_greedy_sorting.rs) | Rust 1.75 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 220 KB | 11278307 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1025_greedy_sorting_optimized.java](1025_greedy_sorting_optimized.java) \* | Java 1.8 | greedy, sorting | O(K log K) | AC | 0.125 s | 384 KB | 11303704 |
| [1025_greedy_sorting_optimized.go](1025_greedy_sorting_optimized.go) | Go 1.14 x64 | greedy, sorting | O(K²) | AC | 0.015 s | 796 KB | 11325044 |
| [1025_greedy_sorting_optimized.py](1025_greedy_sorting_optimized.py) \* | PyPy 3.10 x64 | greedy, sorting | O(K log K) | AC | 0.109 s | 212 KB | 11324842 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
