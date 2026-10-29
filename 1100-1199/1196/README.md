# 1196. How many dates on a student's list the teacher also has

[Timus 1196](https://acm.timus.ru/problem.aspx?space=1&num=1196) · difficulty 52 · binary_search, hashing

Original problem: folklore, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A teacher has a sorted list of `1 ≤ N ≤ 15000` years, and a student
writes down `1 ≤ M ≤ 10⁶` years in any order; both lists may repeat
years, each from 1 to `10⁹`. Count the entries of the student's list
that also appear on the teacher's list.

Time limit: 1.5 seconds. Memory limit: 64 MB.

## Input

`N` and the teacher's years, one per line, then `M` and the student's.

## Output

The number of matching entries.

## Examples

### Example 1

Input:

```
2
1054
1492
4
1492
65536
1492
100
```

Output:

```
2
```

## Solution

The teacher's list is already sorted, so each of the student's years is
looked up by binary search; every match counts, including repeats on the
student's side, while repeats on the teacher's side change nothing.
`O(N + M log N)`. With a million numbers to read, reading the input quickly
matters more than the lookups.

Pitfalls:

- a year the student writes twice counts twice;
- the input has about a million lines, so slow line-by-line reading can
  run out of time in some languages.

The answers were compared with a separately written solution, which uses
a hash set, on every test.

## Optimized solutions

The optimized C++ solution parses the up to a million numbers by hand
from 64 KB blocks read with `fread` instead of calling `scanf` for each:
0.046 s instead of 0.687 s, with about the same memory (260 KB against
256 KB). The binary search is the same.

The optimized Go solution parses the dates by hand from a 4 KB buffered
reader instead of a 1 MB word scanner, keeps them as `int32` and
searches them with its own binary search: 0.062 s instead of 0.171 s and
996 KB instead of 5576 KB. The optimized Rust solution parses the dates
by hand from a 64 KB buffer instead of reading the whole input into a
string and keeps them as `u32`: 320 KB instead of 9300 KB, with the same
time. The optimized Python solution relies on one date per line: it
converts each line as it is and counts the known dates with `map`
instead of a Python loop: 0.343 s instead of 0.687 s and 1324 KB instead
of 1456 KB.

## Language notes

- Python puts the teacher's years in a set; the other languages binary
  search the sorted array.
- Python reads the student's years one line at a time. Splitting the
  whole input at once keeps a million small strings alive together,
  about 62 MB, and that version exceeded the 64 MB limit on test 8.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1196_binary_search.cpp](1196_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N + M log N) | AC | 0.687 s | 256 KB | 11283484 |
| [1196_binary_search.go](1196_binary_search.go) | Go 1.14 x64 | binary_search | O(N + M log N) | AC | 0.171 s | 5576 KB | 11283485 |
| [1196_binary_search.java](1196_binary_search.java) | Java 1.8 | binary_search | O(N + M log N) | AC | 0.328 s | 592 KB | 11303453 |
| [1196_binary_search.rs](1196_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N + M log N) | AC | 0.031 s | 9300 KB | 11283493 |
| [1196_hashing.py](1196_hashing.py) | Python 3.12 x64 | hashing | O(N + M) expected | AC | 0.687 s | 1456 KB | 11283490 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1196_binary_search_optimized.cpp](1196_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O(N + M log N) | AC | 0.046 s | 260 KB | 11303577 |
| [1196_binary_search_optimized.go](1196_binary_search_optimized.go) | Go 1.14 x64 | binary_search | O(N + M log N) | AC | 0.062 s | 996 KB | 11303718 |
| [1196_binary_search_optimized.rs](1196_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O(N + M log N) | AC | 0.046 s | 320 KB | 11303720 |
| [1196_hashing_optimized.py](1196_hashing_optimized.py) | Python 3.12 x64 | hashing | O(N + M) expected | AC | 0.343 s | 1324 KB | 11303721 |
