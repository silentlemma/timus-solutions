# 1264. Workdays

[Timus 1264](https://acm.timus.ru/problem.aspx?space=1&num=1264) · difficulty 21 · math

Original problem by Den Raskovalov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A function counts how many times each value from 0 to M occurs in an
array of N elements, written as one `if` line for every element and
every value (0 ≤ N, M ≤ 40 000). One line takes one second to write.
How many seconds does the whole function take?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M.

## Output

The number of seconds.

## Examples

### Example 1

Input:

```
3 1
```

Output:

```
6
```

## Solution

There are N elements and M + 1 values, so the answer is N · (M + 1).
`O(1)`.

Pitfalls:

- the values run from 0 to M, so there are M + 1 of them, not M;
- the answer reaches 40 000 · 40 001 = 1 600 040 000, close to the
  32-bit signed limit; the solutions use 64 bits (test 05);
- N = 0 gives 0 whatever M is (tests 02, 03).

## Language notes

- All languages print the same product.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1264_math.cpp](1264_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1264_math.go](1264_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB |
| [1264_math.java](1264_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1552 KB |
| [1264_math.py](1264_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 320 KB |
| [1264_math.rs](1264_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB |
