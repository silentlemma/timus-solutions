# 1608. Lucky Tickets 2008

[Timus 1608](https://acm.timus.ru/problem.aspx?space=1&num=1608) · difficulty 1042 · math

Original problem by Sergey Pupyrev, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Tickets are numbered 1, 2, 3, … without leading zeros. A ticket
d₁d₂…dₙ is lucky when no two mirrored digits are equal: dᵢ ≠ dₙ₊₁₋ᵢ
whenever i ≠ n + 1 − i. Count the lucky tickets from a to b
(1 ≤ a ≤ b ≤ 10¹⁸).

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

a and b.

## Output

The number of lucky tickets.

## Examples

### Example 1

Input:

```
1 10
```

Output:

```
10
```

### Example 2

Input:

```
100 2000
```

Output:

```
1620
```

## Solution

Count lucky tickets up to n, f(n), and print f(b) − f(a − 1).

The digits fall into mirrored pairs and, for an odd length, a middle
digit. Once some leading digits are fixed, the rest are counted pair by
pair: a pair with both digits fixed must differ (otherwise the count is
0), a pair with only its left digit fixed leaves 9 choices for the
right one, a pair with both digits free leaves 10·9 = 90, and a free
middle digit 10. A prefix is always fixed from the left, so a pair can
never have only its right digit fixed.

f(n) adds up all shorter numbers, by their first digit 1 to 9, and the
numbers of n's length below n, by the first position where they drop
below n and the smaller digit placed there; n itself is added if it is
lucky. With at most 19 digits this is a few thousand steps.

The counts were checked against testing every number up to 300000.

Pitfalls:

- the first digit cannot be 0, also when counting shorter numbers;
- the middle digit of an odd length has no partner and is always free;
- the count up to 10¹⁸ is about 3.9·10¹⁷ and fits in 64 bits, but a − 1
  can be 0, where the count is 0.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1608_math.cpp](1608_math.cpp) | G++ 13.2 x64 | math | O(L²) | AC | 0.031 s | 196 KB |
| [1608_math.go](1608_math.go) | Go 1.14 x64 | math | O(L²) | AC | 0.046 s | 1084 KB |
| [1608_math.java](1608_math.java) | Java 1.8 | math | O(L²) | AC | 0.109 s | 1644 KB |
| [1608_math.py](1608_math.py) | Python 3.12 x64 | math | O(L²) | AC | 0.062 s | 576 KB |
| [1608_math.rs](1608_math.rs) | Rust 1.75 x64 | math | O(L²) | AC | 0.031 s | 228 KB |
