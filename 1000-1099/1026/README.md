# 1026. The k-th smallest element of a database

[Timus 1026](https://acm.timus.ru/problem.aspx?space=1&num=1026) · difficulty 156 · sorting, prefix_sums

Original problem by Leonid Volkov, from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A database holds `N` integers (`N ≤ 100 000`, each from 1 to 5000, in any
order, with repeats). Answer `K` queries (`1 ≤ K ≤ 100`): for a given `i`
(`1 ≤ i ≤ N`), print the `i`-th smallest element, counting repeats.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `N` numbers, one per line; then a line `###`; then `K` and
the `K` queries, one per line.

## Output

`K` lines: the answers to the queries in order.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
42
7
5000
7
1
300
###
5
1
2
3
6
4
```

Output:

```
1
7
7
5000
42
```

### Example 2

Input:

```
1
3000
###
1
1
```

Output:

```
3000
```

## Solution

**Sorting.** Sort the database once; the answer to a query `i` is the
element at position `i` (counting from 1). `O(N log N + K)`.

**Counting.** The values are small, so count how many times each value
`v ≤ 5000` occurs and take prefix sums: `atMost[v]` is the number of
elements not greater than `v`. The `i`-th smallest element is the smallest
`v` with `atMost[v] ≥ i`, found by binary search over the non-decreasing
array. `O(N + V + K log V)` with `V = 5000`.

Pitfalls:

- repeated values occupy several positions: with 7 twice, positions 2 and 3
  both hold 7;
- the separator line `###` must be skipped, not parsed as a number;
- read the input quickly: `10^5` lines.

## Optimized solutions

The optimized C++ solution counts the values like the simple counting
solution, but keeps the counts in a global array of 5001 `int`, parses
the numbers by hand from a 4 KB buffer refilled with `fread` (the `###`
line is skipped with the other non-digits) and prints with `printf`
instead of `iostream`: {1026_prefix_sums_optimized.cpp}.

The optimized Go solution counts instead of sorting: it keeps only how
many times each value from 1 to 5000 occurs, takes prefix sums and
answers each query by binary search with `sort.SearchInts`, so the
database is neither stored nor sorted. It also parses the digits by hand
from the `bufio` reader instead of `fmt.Fscan`: {1026_prefix_sums.go}.

The optimized Java solution counts instead of sorting as well: the
frequencies of the values up to 5000, their prefix sums and a binary
search per query. It reads the input in 4 KB blocks and parses the
digits by hand, skipping the `###` line, instead of making a `String` of
every line: {1026_prefix_sums.java}.

The optimized Python solution counts instead of sorting too. It reads
the database line by line, since every value is on its own line, counts
each value in a list of 5001 frequencies, takes prefix sums and answers
each query with `bisect_left`; neither the list of all tokens nor the
sorted list of `N` numbers is kept: {1026_prefix_sums.py}.

The optimized Rust solution counts the values in a fixed array of 5001
`u32` while it reads the input line by line into one reused `String`,
then answers each query by binary search over the prefix sums instead of
sorting; it keeps neither the whole input nor the database:
{1026_prefix_sums.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1026_prefix_sums_optimized.cpp`: time reduction +0.00%; memory
  reduction +76.36%; base: `1026_prefix_sums.cpp`.

- `1026_prefix_sums.go`: time reduction +67.39%; memory reduction
  +53.87%; base: `1026_sorting.go`.

- `1026_prefix_sums.java`: time reduction +0.00%; memory reduction
  +92.25%; base: `1026_sorting.java`.

- `1026_prefix_sums.py`: time reduction +14.68%; memory reduction
  +95.17%; base: `1026_sorting.py`.

- `1026_prefix_sums.rs`: time reduction -48.39%; memory reduction
  +89.10%; base: `1026_sorting.rs`.

## Language notes

- **C++**: both the sort and the counting sort with binary search.
- **Go**, **Python**, **Java**, **Rust**: sorting; Python reads all tokens
  at once.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1026_prefix_sums.cpp](1026_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.015 s | 440 KB | 11278309 |
| [1026_sorting.cpp](1026_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + K) | AC | 0.015 s | 816 KB | 11278308 |
| [1026_sorting.go](1026_sorting.go) | Go 1.14 x64 | sorting | O(N log N + K) | AC | 0.046 s | 2324 KB | 11278311 |
| [1026_sorting.java](1026_sorting.java) | Java 1.8 | sorting | O(N log N + K) | AC | 0.109 s | 5112 KB | 11278313 |
| [1026_sorting.py](1026_sorting.py) | Python 3.12 x64 | sorting | O(N log N + K) | AC | 0.109 s | 11668 KB | 11278312 |
| [1026_sorting.rs](1026_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + K) | AC | 0.031 s | 2128 KB | 11278314 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1026_prefix_sums_optimized.cpp](1026_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.001 s | 104 KB | 11305903 |
| [1026_prefix_sums.go](1026_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.015 s | 1072 KB | 11305908 |
| [1026_prefix_sums.java](1026_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.109 s | 396 KB | 11305911 |
| [1026_prefix_sums.py](1026_prefix_sums.py) \* | Python 3.12 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.093 s | 564 KB | 11305912 |
| [1026_prefix_sums.rs](1026_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.046 s | 232 KB | 11305916 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
