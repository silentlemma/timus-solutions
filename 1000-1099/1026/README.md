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

## Language notes

- **C++**: both the sort and the counting sort with binary search.
- **Go**, **Python**, **Java**, **Rust**: sorting; Python reads all tokens
  at once.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1026_prefix_sums.cpp](1026_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.015 s | 440 KB |
| [1026_sorting.cpp](1026_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + K) | AC | 0.015 s | 816 KB |
| [1026_sorting.go](1026_sorting.go) | Go 1.14 x64 | sorting | O(N log N + K) | AC | 0.046 s | 2324 KB |
| [1026_sorting.java](1026_sorting.java) | Java 1.8 | sorting | O(N log N + K) | AC | 0.109 s | 5112 KB |
| [1026_sorting.py](1026_sorting.py) | Python 3.12 x64 | sorting | O(N log N + K) | AC | 0.109 s | 11668 KB |
| [1026_sorting.rs](1026_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + K) | AC | 0.031 s | 2128 KB |
