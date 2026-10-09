# 1064. Array lengths for which a binary search ends at a given step

[Timus 1064](https://acm.timus.ru/problem.aspx?space=1&num=1064) · difficulty 656 · simulation

Original problem from the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The classic binary search over a non-decreasing array `A[0 … N−1]` keeps
bounds `p = 0`, `q = N − 1`; while `p ≤ q` it looks at `i = ⌊(p + q)/2⌋`,
counts one comparison, stops if `A[i] = x`, and otherwise moves `q` to
`i − 1` (when `x < A[i]`) or `p` to `i + 1`. It stopped at index `i` after
exactly `L` comparisons (`0 ≤ i ≤ 9999`, `1 ≤ L ≤ 14`). Find all lengths
`N` from 1 to 10000 for which this is possible, grouped into runs of
consecutive values.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`i` and `L`.

## Output

The number `K` of runs, then `K` lines with the first and the last length
of each run in increasing order; `0` if there are none.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
9000 2
```

Output:

```
0
```

### Example 2

Input:

```
10 3
```

Output:

```
4
12 12
17 18
29 30
87 94
```

## Solution

For a fixed length `N` the comparisons do not depend on the values, only
on where the search goes. To end at index `i`, every inspected element
before `i` must send the search right and every one after `i` must send it
left, which an array with smaller values before `i` and larger values
after it does. So the search path is forced: start with `[0, N − 1]`, take
the middle, stop if it is `i`, otherwise keep the half that contains `i`.
`N` fits when this path meets `i` at exactly the `L`-th comparison (and
`i < N`).

Try every `N`: at most 14 steps each, `O(10000 · log 10000)`, and join
consecutive good lengths into runs.

Pitfalls:

- `i` must be an index of the array: `N > i`;
- the search may reach `i` earlier or later than `L`; only exactly `L`
  counts;
- the answer can be empty: print just `0`.

## Language notes

- All languages simulate the same path for every length.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1064_simulation.cpp](1064_simulation.cpp) | G++ 13.2 x64 | simulation | O(10000 · log 10000) | AC | 0.031 s | 204 KB |
| [1064_simulation.go](1064_simulation.go) | Go 1.14 x64 | simulation | O(10000 · log 10000) | AC | 0.031 s | 1136 KB |
| [1064_simulation.java](1064_simulation.java) | Java 1.8 | simulation | O(10000 · log 10000) | AC | 0.109 s | 1704 KB |
| [1064_simulation.py](1064_simulation.py) | Python 3.12 x64 | simulation | O(10000 · log 10000) | AC | 0.078 s | 656 KB |
| [1064_simulation.rs](1064_simulation.rs) | Rust 1.75 x64 | simulation | O(10000 · log 10000) | AC | 0.015 s | 280 KB |
