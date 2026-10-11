# 1290. Sabotage

[Timus 1290](https://acm.timus.ru/problem.aspx?space=1&num=1290) · difficulty 80 · sorting

Original problem: folklore (prepared by Den Raskovalov), from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A slow function takes N ≤ 25 000 positive integers, each at most
25 000. It prints how many of them are at least 1, then how many are
greater than 1, greater than 2 and so on, stopping before the first 0.
The printed numbers are read back as a new array and the same step is
applied once more; the second list is the result. Produce that result
quickly.

For 4 1 6 the first list is 3 2 2 2 1 1 and the second is 6 4 1.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N numbers, one per line. N may be 0.

## Output

The resulting numbers, one per line.

## Examples

### Example 1

Input:

```
3
4
1
6
```

Output:

```
6
4
1
```

## Solution

Picture the numbers as rows of cells: the number p is a row of p cells,
all rows aligned on the left. The j-th printed number counts the rows
that reach column j, so the first list is the length of each column:
the picture turned on its side (the conjugate partition). Turning it a
second time gives back the rows, from the longest to the shortest.

So the function simply sorts the array in descending order. The values
are at most 25 000, so a counting sort is enough: count each value,
then print the values from 25 000 down to 1, each as many times as it
occurred. `O(N + 25 000)`.

Pitfalls:

- with N = 0 the output is empty (test 02);
- equal numbers all come back (tests 04 and 06).

The equivalence was checked against a direct simulation of the two
steps on 200 random arrays.

## Language notes

- All languages keep one counter per value, 25 001 in all, and print
  through a buffer.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1290_sorting.cpp](1290_sorting.cpp) | G++ 13.2 x64 | sorting | O(N + 25000) | AC | 0.031 s | 280 KB |
| [1290_sorting.go](1290_sorting.go) | Go 1.14 x64 | sorting | O(N + 25000) | AC | 0.031 s | 1384 KB |
| [1290_sorting.java](1290_sorting.java) | Java 1.8 | sorting | O(N + 25000) | AC | 0.125 s | 2056 KB |
| [1290_sorting.py](1290_sorting.py) | Python 3.12 x64 | sorting | O(N + 25000) | AC | 0.109 s | 4732 KB |
| [1290_sorting.rs](1290_sorting.rs) | Rust 1.75 x64 | sorting | O(N + 25000) | AC | 0.015 s | 724 KB |
