# 1330. Intervals

[Timus 1330](https://acm.timus.ru/problem.aspx?space=1&num=1330) · difficulty 95 · prefix_sums

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 10 000 sensors give integer readings from −10 000 to 10 000. Answer
up to 100 000 questions: the sum of the readings of sensors i to j,
i ≤ j.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then N readings, then Q and Q pairs i, j.

## Output

One sum per line.

## Examples

### Example 1

Input:

```
5
1
2
3
-1
4
3
1 5
4 4
1 4
```

Output:

```
9
-1
5
```

## Solution

Keep before[i], the sum of the first i readings, with before[0] = 0.
The sum from i to j is then before[j] − before[i − 1], one subtraction
per question. `O(N + Q)`.

Pitfalls:

- the sums lie between −10⁸ and 10⁸, which fits a 32-bit integer;
- there may be no questions at all (test 03);
- with 100 000 questions the input and the output have to be read and
  written in large pieces to stay within 0.5 seconds.

## Optimized solutions

`1330_prefix_sums_optimized.py`. Keep prefix sums and answer [i,j] as before[j]-before[i-1]. Parse 65536-byte blocks with split/map, carrying a numeric token across a boundary rather than parsing each line through another generator. Store prefixes in a Python list and emit batches of at most 4096 answers. For N readings and Q queries, time remains O(N+Q), state O(N) plus bounded input/output batches; query lists and the complete output are not retained.

Exact-source CPython 3.12 Accepted #11326660: 0.156 s / 2648 KB. Saved current-compiler comparison, 2026-11-20: time rank 5/34, memory rank 5/34. Both required metrics pass the strict top-ten or top-15% rule, with percentage cutoffs rounded up. The asterisk tracks Python's separate first-place target in both metrics.

The previously documented optimized run #11303743 (Python 3.12 x64) recorded 0.203 s / 1440 KB. The current CPython 3.12 run has lower recorded time and higher memory. These are separate paired judge measurements; interpreter choice and judge variability are part of the comparison. The retained simple run is faster at 0.125 s; this version favors lower memory.

- `1330_prefix_sums_optimized.py`: 0.156 s / 2648 KB; retained teaching base `1330_prefix_sums.py` (Python 3.12 x64): 0.125 s / 27608 KB.

The optimized C++ and Java solutions keep the prefix sums as 32-bit
integers, which is enough for sums between −10⁸ and 10⁸. C++ parses the
numbers and writes the answers by hand through 4 KB buffers and keeps
the sums in a static array: 0.015 s instead of 0.125 s and 132 KB
instead of 2784 KB.

The optimized Java solution reads the input in 4 KB blocks and parses it by hand instead of using `StreamTokenizer`, and writes the answers into a 4 KB byte buffer instead of building strings: 0.125 s instead of 0.156 s and 452 KB instead of 7324 KB.

## Language notes

- The simple Java solution reads with `StreamTokenizer`, which handles
  the negative readings, and collects the answers in one string.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1330_prefix_sums.cpp](1330_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 2784 KB | 11284999 |
| [1330_prefix_sums.go](1330_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 2828 KB | 11285000 |
| [1330_prefix_sums.java](1330_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.156 s | 7324 KB | 11303461 |
| [1330_prefix_sums.py](1330_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 27608 KB | 11285001 |
| [1330_prefix_sums.rs](1330_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 3736 KB | 11285004 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1330_prefix_sums_optimized.cpp](1330_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.015 s | 132 KB | 11303598 |
| [1330_prefix_sums_optimized.java](1330_prefix_sums_optimized.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.125 s | 452 KB | 11303742 |
| [1330_prefix_sums_optimized.py](1330_prefix_sums_optimized.py) \* | Python 3.12 x64 | prefix_sums | O(N+Q) time; O(N+B+S) space | AC | 0.156 s | 2648 KB | 11326660 |

\* Accepted; the separate rating target is not yet met: C++ requires top ten or top 15% in both time and memory, and the other language families require first place in both. This marker is separate from the admission criteria; the version may be optimized further.
