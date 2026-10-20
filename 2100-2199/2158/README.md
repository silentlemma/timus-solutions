# 2158. Splitting a multiset into an arithmetic and a geometric progression

[Timus 2158](https://acm.timus.ru/problem.aspx?space=1&num=2158) · difficulty 1856 · math, greedy

Original problem by Valentin Zuev, from the Ural School Programming Contest 2021.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Split N non-negative integers into a non-empty arithmetic progression
and a non-empty geometric progression with a non-zero ratio, each number
used once, and print both, or −1. Any valid split is accepted. The limits
are 2 seconds and 256 MB.

## Input

N, 2 ≤ N ≤ 50 000, then the numbers, 0 ≤ aᵢ ≤ 10⁹.

## Output

−1, or the length of the arithmetic progression, its terms in order and
the terms of the geometric progression in order.

## Checking

A checker verifies the multiset and both progressions, and compares −1
with the stored answer.

## Examples

### Example 1

Input:

```
6
0 2 3 4 6 8
```

Output:

```
3
0 3 6
2 4 8
```

### Example 2

Input:

```
6
4 4 6 6 8 9
```

Output:

```
3
4 6 8
4 6 9
```

### Example 3

Input:

```
4
0 0 0 0
```

Output:

```
1
0
0 0 0
```

### Example 4

Input:

```
5
0 0 1 1 2
```

Output:

```
-1
```

## Solution

Sort the numbers. The key bound: a geometric progression with ratio
q ≠ 1 has at most about 30 terms, because its terms are integers up to
10⁹ and the ratio p / r in lowest terms forces the first term to be a
multiple of r^(t−1), so the terms grow at least like 2^(t−1). Zeros only
fit a progression of zeros. Progressions with ratio 1 or step 0 consist
of equal numbers, and these cases are handled first:

- one distinct value, or two distinct values: put each value apart;
- exactly one value repeated: its copies form the constant progression,
  possibly leaving one copy to the other one, and the rest is checked;
- at most 31 numbers: try every single number as one progression.

Otherwise all numbers are distinct where it matters, the geometric part
has at most 30 terms and the arithmetic part holds the rest. For large N
the arithmetic step is the median of the gaps between neighbours, and
its first term is among the first 31 numbers; for smaller N the first
two terms are tried among the first 32 numbers. For a start and a step,
one greedy pass takes every number equal to the next arithmetic term and
leaves the rest to the geometric part, giving up once it has more than
30 numbers. The last one or two arithmetic terms may belong to the
geometric part instead, so these few variants are checked too. All
checks are exact integer comparisons.

In the second example 4, 6, 8 has step 2 and 4, 6, 9 has ratio 3 / 2.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2158_math_greedy.cpp](2158_math_greedy.cpp) | G++ 13.2 x64 | math, greedy | O(N log N + 30^2 N) | AC | 0.031 s | 2148 KB |
| [2158_math_greedy.go](2158_math_greedy.go) | Go 1.14 x64 | math, greedy | O(N log N + 30^2 N) | AC | 0.031 s | 7880 KB |
| [2158_math_greedy.java](2158_math_greedy.java) | Java 1.8 | math, greedy | O(N log N + 30^2 N) | AC | 0.156 s | 7108 KB |
| [2158_math_greedy.py](2158_math_greedy.py) | Python 3.12 x64 | math, greedy | O(N log N + 30^2 N) | AC | 0.265 s | 8684 KB |
| [2158_math_greedy.rs](2158_math_greedy.rs) | Rust 1.75 x64 | math, greedy | O(N log N + 30^2 N) | AC | 0.046 s | 2892 KB |
