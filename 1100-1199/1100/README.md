# 1100. A results table sorted the way a bubble sort would

[Timus 1100](https://acm.timus.ru/problem.aspx?space=1&num=1100) · difficulty 44 · sorting

Original problem by Pavel Atnashev, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` teams (`1 < N ≤ 150 000`) are given as pairs of a unique ID
(`1 ≤ ID ≤ 10^7`) and a number of solved problems `M` (`0 ≤ M ≤ 100`).
The old software sorted them with a bubble sort that swaps neighbours
while `A[i] < A[i+1]` by `M`. Print the same table, but fast.

Time limit: 1 second. Memory limit: 16 MB.

## Input

`N`, then `N` lines with `ID` and `M`.

## Output

`N` lines with `ID` and `M` in the order the bubble sort gives.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
8
1 2
16 3
11 2
20 3
3 5
26 4
7 1
22 4
```

Output:

```
3 5
26 4
22 4
16 3
20 3
1 2
11 2
7 1
```

## Solution

The bubble sort only swaps neighbours with different scores, so two
teams with equal `M` never pass each other: the result is a stable sort
by `M` in decreasing order. Since `M` takes only 101 values, a counting
sort does it in one pass: put each team into the bucket of its score in
input order, then print the buckets from 100 down to 0. `O(N)`.

Pitfalls:

- an unstable sort mixes up teams with equal scores, which changes the
  answer;
- the memory limit is 16 MB, so the teams are stored compactly and, in
  Python, the input is read line by line and the output is written in
  chunks;
- 150 000 lines of output need buffered writing.

The answers were checked against the bubble sort itself for up to 300
teams and against a library stable sort for larger tables.

## Optimized solutions

The optimized solutions (C++, Java, Rust) read and write the numbers by
hand through 8 KB buffers instead of `scanf` and `printf`, `StreamTokenizer`
and `PrintWriter`, or `parse` and `writeln!`: with 150 000 lines the
conversions between numbers and text take most of the time. The sort is
the same counting sort; Java stores the scores as bytes, since they are at
most 100. C++: 0.031 s instead of 0.265 s, with about the same memory
(1388 KB against 1404 KB); Java: 0.109 s instead of 0.218 s and 1736 KB
instead of 6844 KB; Rust: 1688 KB instead of 6528 KB, with the same
time.

## Language notes

- Go reads the words with `bufio.Scanner` instead of `fmt.Scan`: the input
  has up to 150 000 lines.
- Python keeps the IDs in `array("i")` buckets, four bytes each.
- Java does a stable counting sort with prefix sums over the scores
  instead of lists.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1100_sorting.cpp](1100_sorting.cpp) | G++ 13.2 x64 | sorting | O(N) | AC | 0.265 s | 1404 KB | 11279152 |
| [1100_sorting.go](1100_sorting.go) | Go 1.14 x64 | sorting | O(N) | AC | 0.062 s | 6852 KB | 11303071 |
| [1100_sorting.java](1100_sorting.java) | Java 1.8 | sorting | O(N) | AC | 0.218 s | 6844 KB | 11279155 |
| [1100_sorting.py](1100_sorting.py) | Python 3.12 x64 | sorting | O(N) | AC | 0.234 s | 3308 KB | 11279154 |
| [1100_sorting.rs](1100_sorting.rs) | Rust 1.75 x64 | sorting | O(N) | AC | 0.062 s | 6528 KB | 11279156 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1100_sorting_optimized.cpp](1100_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(N) | AC | 0.031 s | 1388 KB | 11303548 |
| [1100_sorting_optimized.java](1100_sorting_optimized.java) | Java 1.8 | sorting | O(N) | AC | 0.109 s | 1736 KB | 11303549 |
| [1100_sorting_optimized.rs](1100_sorting_optimized.rs) | Rust 1.75 x64 | sorting | O(N) | AC | 0.046 s | 1688 KB | 11303550 |
