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

`1025_greedy_sorting_optimized.py`. Python keeps sorting the group sizes and choosing the smallest floor(K/2)+1. Every group size is odd, so the supporter count is (sum(selected_sizes)+needed)//2: one C-level sum and one division replace a Python generator with a division per group. Read binary integer tokens, write the answer once, and exit inside main before local data teardown. Time O(K log K); sorted data O(K), with the read input also retained during processing. This is the same majority greedy, not a different optimization problem. The clear per-group-cost base remains.

Exact-source Python 3.12 x64 Accepted #11327542: 0.062 s / 648 KB. Saved 2026-11-20 compiler-cohort comparison: time 66/551, memory 502/551. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11324842 (PyPy 3.10 x64) was 0.109 s / 212 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1025_greedy_sorting_optimized.py`: 0.062 s / 648 KB; retained teaching base `1025_greedy_sorting.py`: 0.093 s / 372 KB.

`1025_greedy_sorting_optimized.java`. Java keeps the same smallest-majority greedy: win the smallest floor(K/2)+1 groups, paying floor(size/2)+1 supporters for each. For the given K<=101, insert each input size into its sorted position in an int array rather than loading Arrays.sort. This deliberately trades O(K log K) sorting for bounded O(K^2) comparisons to reduce library startup overhead; it is not an asymptotic improvement. A 1024-byte input buffer and direct decimal output avoid Scanner and number strings. Auxiliary storage O(K); the simpler library-sort teaching source remains available.

Exact-source Java 1.8 Accepted #11327343: 0.093 s / 320 KB. Saved 2026-11-20 compiler-cohort comparison: time 108/770, memory 4/770. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303704 was 0.125 s / 384 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1025_greedy_sorting_optimized.java`: 0.093 s / 320 KB; retained teaching base `1025_greedy_sorting.java`: 0.109 s / 1724 KB.

`1025_greedy_sorting_optimized.go`. Go retains the majority-of-the-smallest-groups greedy choice. The optimized source reads bytes directly and inserts each group into one fixed array of at most 101 entries. This deliberately uses insertion sort: O(K²) time instead of the base sort's O(K log K), but avoids its dynamic containers and fmt overhead at this small limit. Sum floor(size/2)+1 for the first floor(K/2)+1 groups. The original library-sort source is preserved.

Compared with `1025_greedy_sorting.go`: time 0.031 s → 0.015 s; memory 1076 KB → 796 KB.

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
| [1025_greedy_sorting_optimized.java](1025_greedy_sorting_optimized.java) \* | Java 1.8 | greedy, sorting | O(K²) time; O(K) auxiliary space | AC | 0.093 s | 320 KB | 11327343 |
| [1025_greedy_sorting_optimized.go](1025_greedy_sorting_optimized.go) | Go 1.14 x64 | greedy, sorting | O(K²) | AC | 0.015 s | 796 KB | 11328361 |
| [1025_greedy_sorting_optimized.py](1025_greedy_sorting_optimized.py) \* | Python 3.12 x64 | greedy, sorting | O(K log K) time; O(K + I) storage | AC | 0.062 s | 648 KB | 11327542 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
