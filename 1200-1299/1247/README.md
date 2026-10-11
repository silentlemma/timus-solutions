# 1247. No segment heavier than its length plus N

[Timus 1247](https://acm.timus.ru/problem.aspx?space=1&num=1247) · difficulty 240 · dp

Original problem by Alexander Mironenko, from the Ural State University Personal Contest, March 1, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sequence A_1 … A_S of integers from 0 to 100 sums to S + N
(S, N ≤ 30 000). Decide whether every segment satisfies
`A_i + … + A_j ≤ (j − i + 1) + N`.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

S and N, then the S numbers.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
4 3
2
3
0
2
```

Output:

```
YES
```

### Example 2

Input:

```
4 5
1
0
5
3
```

Output:

```
NO
```

## Solution

Subtract 1 from every element: the condition becomes "no segment of
`B_i = A_i − 1` sums to more than N". So only the largest segment sum
matters, and Kadane's scan finds it in one pass: the best sum of a
segment ending at i is `max(previous, 0) + B_i`, and the answer is the
largest of these, compared with N. `O(S)`.

The whole sequence sums to exactly N in B, so the answer is NO exactly
when cutting off a prefix or a suffix with a negative sum leaves a
heavier segment.

Pitfalls:

- a zero at the start already makes the rest too heavy (test 04);
- a segment of one element counts too.

## Language notes

- All languages run the same one-pass scan.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1247_dp.cpp](1247_dp.cpp) | G++ 13.2 x64 | dp | O(S) | AC | 0.031 s | 124 KB |
| [1247_dp.go](1247_dp.go) | Go 1.14 x64 | dp | O(S) | AC | 0.031 s | 1348 KB |
| [1247_dp.java](1247_dp.java) | Java 1.8 | dp | O(S) | AC | 0.109 s | 528 KB |
| [1247_dp.py](1247_dp.py) | Python 3.12 x64 | dp | O(S) | AC | 0.093 s | 1312 KB |
| [1247_dp.rs](1247_dp.rs) | Rust 1.75 x64 | dp | O(S) | AC | 0.062 s | 840 KB |
