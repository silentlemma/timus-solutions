# 1196. How many dates on a student's list the teacher also has

[Timus 1196](https://acm.timus.ru/problem.aspx?space=1&num=1196) · difficulty 53 · binary_search

Original problem: folklore, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A teacher has a sorted list of `N ≤ 15000` years, and a student writes
down `M ≤ 10⁶` years in any order; both lists may repeat years, all up to
`10⁹`. Count the entries of the student's list that also appear on the
teacher's list.

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
`O(M log N)`. With a million numbers to read, reading the input quickly
matters more than the lookups.

Pitfalls:

- a year the student writes twice counts twice;
- the input has up to a million lines, so slow line-by-line reading can
  run out of time in some languages.

The answers were compared with a separately written solution, which uses
a hash set, on every test.

## Language notes

- Python puts the teacher's years in a set; the other languages binary
  search the sorted array. Java reads the input with a hand-written byte
  reader.
- Python reads the student's years one line at a time. Splitting the
  whole input at once keeps a million small strings alive together,
  about 62 MB, and that version exceeded the 64 MB limit on test 8.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1196_binary_search.cpp](1196_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(M log N) | AC | 0.687 s | 256 KB |
| [1196_binary_search.go](1196_binary_search.go) | Go 1.14 x64 | binary_search | O(M log N) | AC | 0.171 s | 5576 KB |
| [1196_binary_search.java](1196_binary_search.java) | Java 1.8 | binary_search | O(M log N) | AC | 0.312 s | 616 KB |
| [1196_binary_search.py](1196_binary_search.py) | Python 3.12 x64 | binary_search | O(M log N) | AC | 0.687 s | 1456 KB |
| [1196_binary_search.rs](1196_binary_search.rs) | Rust 1.75 x64 | binary_search | O(M log N) | AC | 0.031 s | 9300 KB |
