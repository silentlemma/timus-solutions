# 1296. Hyperjump

[Timus 1296](https://acm.timus.ru/problem.aspx?space=1&num=1296) · difficulty 60 · dp

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
for the empty segment. Read each signed integer, add it to `ending`,
clamp `ending` to 0, and update `best`. This takes `O(N)` time and
`O(1)` auxiliary memory; the simple Python and Rust solutions buffer the
input in `O(N)` memory.

Pitfalls:

- with only negative numbers the answer is 0, not the largest number
  (test 02);
- N = 0 is allowed (test 03);
- an explicit plus sign is valid: Java must skip it before reading the
  numeric token, so `+0` is read as 0 (test 09);
- the sum reaches 60 000 · 30 000 = 1.8 · 10⁹, close to the 32-bit
  limit, so the solutions use 64 bits (test gen2).

The answers were compared with checking every segment on 1500 random
sequences.

## Optimized solutions

The optimized Python solution reads the numbers line by line, one per
line, instead of splitting the whole input, and compares the running
sums directly instead of calling `max()`: 0.078 s instead of 0.125 s and
388 KB instead of 4788 KB. The optimized Rust solution reads the numbers
line by line through a 1 KB buffered reader instead of reading the whole
input into a string: 228 KB instead of 1260 KB, with the same time.

## Language notes

- All languages keep just two running sums, `best` and `ending`.
- C++, Go and Java, and the optimized Python and Rust solutions, use
  `O(1)` total memory; the simple Python and Rust solutions use `O(N)`
  total memory for buffered input.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1296_dp.cpp](1296_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.046 s | 132 KB | 11297977 |
| [1296_dp.go](1296_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1512 KB | 11297978 |
| [1296_dp.java](1296_dp.java) | Java 1.8 | dp | O(N) | AC | 0.109 s | 464 KB | 11297980 |
| [1296_dp.py](1296_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.125 s | 4788 KB | 11297981 |
| [1296_dp.rs](1296_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 1260 KB | 11297982 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1296_dp_optimized.py](1296_dp_optimized.py) | Python 3.12 x64 | dp | O(N) | AC | 0.078 s | 388 KB | 11303735 |
| [1296_dp_optimized.rs](1296_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 228 KB | 11303736 |
