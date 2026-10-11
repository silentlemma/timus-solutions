# 1296. Hyperjump

[Timus 1296](https://acm.timus.ru/problem.aspx?space=1&num=1296) · difficulty 63 · dp

Original problem by Den Raskovalov, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a sequence of N ≤ 60 000 integers from −30 000 to 30 000, find
the largest sum of a contiguous segment. The empty segment is allowed
and gives 0.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N numbers, one per line. N may be 0.

## Output

The largest sum.

## Examples

### Example 1

Input:

```
10
31
-41
59
26
-53
58
97
-93
-23
84
```

Output:

```
187
```

### Example 2

Input:

```
3
-1
-5
-6
```

Output:

```
0
```

## Solution

This is the maximum subarray problem, solved by Kadane's algorithm in
one pass. Keep `ending`, the largest sum of a segment that ends at the
current number, where the empty segment counts. Each new number p
either extends that segment or, if the sum would turn negative, is
better left out:

ending = max(ending + p, 0).

The answer is the largest value `ending` ever takes, and it starts at 0
for the empty segment. `O(N)` time, `O(1)` memory.

Pitfalls:

- with only negative numbers the answer is 0, not the largest number
  (test 02);
- N = 0 is allowed (test 03);
- the sum reaches 60 000 · 30 000 = 1.8 · 10⁹, close to the 32-bit
  limit, so the solutions use 64 bits (test gen2).

The answers were compared with checking every segment on 300 random
sequences.

## Language notes

- All languages keep just two running sums, `best` and `ending`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1296_dp.cpp](1296_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.046 s | 136 KB |
| [1296_dp.go](1296_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1540 KB |
| [1296_dp.java](1296_dp.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 484 KB |
| [1296_dp.py](1296_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 4572 KB |
| [1296_dp.rs](1296_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 1252 KB |
