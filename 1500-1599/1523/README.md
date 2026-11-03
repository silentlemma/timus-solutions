# 1523. K-inversions

[Timus 1523](https://acm.timus.ru/problem.aspx?space=1&num=1523) · difficulty 296 · fenwick

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a permutation a1, …, an of 1 … n (1 ≤ n ≤ 20000), count its
k-inversions (2 ≤ k ≤ 10): index sequences i1 < i2 < … < ik with
ai1 > ai2 > … > aik. Print the count modulo 10⁹.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n and k, then the permutation.

## Output

The number of k-inversions modulo 10⁹.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
3 2
3 1 2
```

Output:

```
2
```

### Example 2

Input:

```
5 3
5 4 3 2 1
```

Output:

```
10
```

## Solution

Let ends[i] count the decreasing runs of length L that end at position
i; for L = 1 it is 1 everywhere. A run of length L + 1 ending at i is a
run of length L ending at some earlier position p with ap > ai, followed
by i. So each level is one pass from left to right with a Fenwick tree
over the values: query the sum over values above ai, then add ends[i]
at ai. Counting values from the top turns "above" into a prefix. k − 1
passes give `O(n·k·log n)`.

Pitfalls:

- k can exceed the length of the longest decreasing run, or even n, and
  then the answer is 0 (tests 04, 05, gen3);
- the counts grow like C(20000, 10), so reduce them modulo 10⁹ as
  they are added (gen2, gen5).

## Optimized solutions

The layered inversion DP uses one array in place. At each position, save its old-layer count, query a Fenwick tree containing only earlier old-layer positions, overwrite the array cell, then insert the saved old count. Inserting the newly computed count would mix layers and is incorrect. Clear and reuse the tree for the next layer. Bounded residues and coordinates permit compact cells; conditional subtraction replaces division for sums of two residues.

- `1523_fenwick_optimized.cpp`: 0.015 s / 192 KB; base `1523_fenwick.cpp`: 0.031 s / 596 KB; relative change: time -51.6%, memory -67.8%.
- `1523_fenwick_optimized.java`: 0.140 s / 624 KB; base `1523_fenwick.java`: 0.125 s / 3512 KB; relative change: time +12.0%, memory -82.2%.
- `1523_fenwick_optimized.py`: 0.859 s / 2000 KB; base `1523_fenwick.py`: 0.562 s / 5172 KB; relative change: time +52.8%, memory -61.3%.
- `1523_fenwick_optimized.rs`: 0.031 s / 472 KB; base `1523_fenwick.rs`: 0.031 s / 1292 KB; relative change: time -0.0%, memory -63.5%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1523_fenwick.cpp`; covering source `1523_fenwick_optimized.cpp`; time/memory places 1/1, other-author entries 95/95.

- Go: preferred teaching base `1523_fenwick.go`; covering source `1523_fenwick.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1523_fenwick.java`; covering source `1523_fenwick_optimized.java`; time/memory places 4/1, other-author entries 5/5.

- Python/PyPy: preferred teaching base `1523_fenwick.py`; covering source `1523_fenwick_optimized.py`; time/memory places 7/1, other-author entries 7/7.

- Rust: preferred teaching base `1523_fenwick.rs`; covering source `1523_fenwick_optimized.rs`; time/memory places 2/1, other-author entries 2/2.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1523_fenwick.cpp](1523_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 596 KB | 11287382 |
| [1523_fenwick.go](1523_fenwick.go) | Go 1.14 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 4576 KB | 11287383 |
| [1523_fenwick.java](1523_fenwick.java) | Java 1.8 | fenwick | O(n * k * log n) | AC | 0.125 s | 3512 KB | 11287388 |
| [1523_fenwick.py](1523_fenwick.py) | Python 3.12 x64 | fenwick | O(n * k * log n) | AC | 0.562 s | 5172 KB | 11287386 |
| [1523_fenwick.rs](1523_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 1292 KB | 11287389 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1523_fenwick_optimized.cpp](1523_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(NK log N) | AC | 0.015 s | 192 KB | 11309407 |
| [1523_fenwick_optimized.java](1523_fenwick_optimized.java) \* | Java 1.8 | fenwick | O(NK log N) | AC | 0.140 s | 624 KB | 11309408 |
| [1523_fenwick_optimized.py](1523_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(NK log N) | AC | 0.859 s | 2000 KB | 11309406 |
| [1523_fenwick_optimized.rs](1523_fenwick_optimized.rs) \* | Rust 1.75 x64 | fenwick | O(NK log N) | AC | 0.031 s | 472 KB | 11309409 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
