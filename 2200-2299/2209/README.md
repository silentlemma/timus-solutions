# 2209. The M-th fraction on level N of the Stern–Brocot tree

[Timus 2209](https://acm.timus.ru/problem.aspx?space=1&num=2209) · difficulty 651 · math

Original problem by Vadim Barinov, from the University Academic School Olympiad in Informatics 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The Stern–Brocot tree has 1/1 at its root and bounds 0/1 and 1/0, and
each node is the mediant of its nearest left and right ancestors. Find
the M-th fraction from the left on depth N. The limits are 0.5 seconds
and 256 MB.

## Input

N and M, 1 ≤ N ≤ 10⁹, 1 ≤ M ≤ min(2^(N−1), 10⁹).

## Output

The numerator and the denominator.

## Examples

### Example 1

Input:

```
1 1
```

Output:

```
1 1
```

### Example 2

Input:

```
3 3
```

Output:

```
3 2
```

### Example 3

Input:

```
5 7
```

Output:

```
5 7
```

## Solution

Depth N has 2^(N−1) nodes, and the path from the root to the M-th of
them is M − 1 written with N − 1 binary digits, 0 for a step left and 1
for a step right. Walking down keeps the two bounds a/b and c/d of the
current node, the node itself being (a + c)/(b + d): a left step makes
the node the new right bound, a right step makes it the new left bound.

N can be 10⁹, but M ≤ 10⁹ means at most 30 of the digits can be ones,
so the path starts with N − 1 − k zeros, where k is the bit length of
M − 1. Going left from the root z times only changes the right bound to
1/z, so the walk starts from the bounds 0/1 and 1/z (1/0 when z = 0)
and processes just the last k digits.

The numbers grow at most like z times a Fibonacci number of 30 steps,
well inside 64 bits.

In the second example M − 1 = 2 = 10 in binary on two digits: right to
2/1, then left to 3/2.

This takes O(log M).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2209_math.cpp](2209_math.cpp) | G++ 13.2 x64 | math | O(log M) | AC | 0.015 s | 228 KB |
| [2209_math.go](2209_math.go) | Go 1.14 x64 | math | O(log M) | AC | 0.031 s | 896 KB |
| [2209_math.java](2209_math.java) | Java 1.8 | math | O(log M) | AC | 0.109 s | 204 KB |
| [2209_math.py](2209_math.py) | Python 3.12 x64 | math | O(log M) | AC | 0.093 s | 248 KB |
| [2209_math.rs](2209_math.rs) | Rust 1.75 x64 | math | O(log M) | AC | 0.046 s | 24 KB |
