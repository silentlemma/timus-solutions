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

## Optimized solutions

Python reads the path from the least significant bit, building the coefficients of the two initial bounds. Leading left moves are folded into the denominator in one step. Submission 11317193 took 0.093 s and used 428 KB, versus 0.093 s and 456 KB for the base. It ranks 10th by time and 3rd by memory among comparable runs in the saved snapshot.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321834 · Go 1.14 x64 №11321835 · Java 1.8 №11322409 · Rust 1.75 x64 №11321837 · Python 3.12 x64 №11322446.

This variant reads the path from the least significant bit, accumulates the coefficients of the initial bounds, and counts the leading left moves in one step. G++ 13.2 x64, submission 11322447. Time 0.015 → 0.015 s, memory 424 → 112 KB.

This variant reads the path from the least significant bit, accumulates the coefficients of the initial bounds, and counts the leading left moves in one step. Go 1.14 x64, submission 11322448. Time 0.031 → 0.031 s, memory 1112 → 796 KB.

This variant reads the path from the least significant bit, accumulates the coefficients of the initial bounds, and counts the leading left moves in one step. Rust 1.75 x64, submission 11322449. Time 0.062 → 0.046 s, memory 224 → 212 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2209_math.cpp](2209_math.cpp) | G++ 13.2 x64 | math | O(log M) | AC | 0.015 s | 424 KB | 11321834 |
| [2209_math.go](2209_math.go) | Go 1.14 x64 | math | O(log M) | AC | 0.031 s | 1112 KB | 11321835 |
| [2209_math.java](2209_math.java) | Java 1.8 | math | O(log M) | AC | 0.109 s | 368 KB | 11322409 |
| [2209_math.py](2209_math.py) | Python 3.12 x64 | math | O(log M) | AC | 0.093 s | 456 KB | 11322446 |
| [2209_math.rs](2209_math.rs) | Rust 1.75 x64 | math | O(log M) | AC | 0.062 s | 224 KB | 11321837 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2209_math_optimized.py](2209_math_optimized.py) | Python 3.12 x64 | math | O(log M) | AC | 0.093 s | 428 KB | 11317193 |
| [2209_math_optimized.cpp](2209_math_optimized.cpp) | G++ 13.2 x64 | math | O(log M) | AC | 0.015 s | 112 KB | 11322447 |
| [2209_math_optimized.go](2209_math_optimized.go) | Go 1.14 x64 | math | O(log M) | AC | 0.031 s | 796 KB | 11322448 |
| [2209_math_optimized.rs](2209_math_optimized.rs) | Rust 1.75 x64 | math | O(log M) | AC | 0.046 s | 212 KB | 11322449 |
