# 1293. Eniya

[Timus 1293](https://acm.timus.ru/problem.aspx?space=1&num=1293) · difficulty 14 · math

Original problem by Den Raskovalov, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N rectangular panels of A by B metres must be coated on both sides,
and one square metre takes one nanogram of coating
(1 ≤ N, A, B ≤ 100). How many nanograms are needed?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, A and B on one line.

## Output

The number of nanograms.

## Examples

### Example 1

Input:

```
5 2 3
```

Output:

```
60
```

## Solution

Each panel has two sides of A · B square metres, so the answer is
2 · N · A · B. `O(1)`.

Pitfalls:

- both sides count: forgetting the factor 2 gives 30 instead of 60 on
  the example (test 01);
- the largest answer is 2 000 000, which fits easily in 32 bits
  (test 03).

## Language notes

- All languages print the same product.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1293_math.cpp](1293_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.001 s | 128 KB |
| [1293_math.go](1293_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1152 KB |
| [1293_math.java](1293_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1596 KB |
| [1293_math.py](1293_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 344 KB |
| [1293_math.rs](1293_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 224 KB |
