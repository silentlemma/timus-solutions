# 2066. The smallest value of three numbers

[Timus 2066](https://acm.timus.ru/problem.aspx?space=1&num=2066) · difficulty 28 · bruteforce

Original problem by Kirill Borozdin, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three non-negative integers may be written in any order with one of the
signs +, − or × between each two neighbours; multiplication goes first,
and there are no brackets or unary minus. Find the smallest value such
an expression can have. The limits are 1 second and 64 MB.

## Input

The numbers a ≤ b ≤ c, 0 ≤ a, each on its own line, c ≤ 100.

## Output

The smallest value.

## Checking

Outputs are compared token by token.

## Examples

### Example 1

Input:

```
1
2
3
```

Output:

```
-5
```

## Solution

There are at most 6 orders and 9 pairs of signs, so the programs try up to
54 expressions. Evaluate x op₁ y op₂ z with the usual precedence: if
only the second sign is ×, compute y × z first; otherwise go from left
to right.

The search always ends with the same shape: the smallest number minus
the larger of b + c and b × c, that is a − max(b + c, b × c). Subtracting
as much as possible from the smallest number is clearly best, and b + c
beats b × c only when one of them is 0 or 1. Checking all 176 851
inputs confirms the formula, but the plain search needs no argument.

In the example 1 − 2 × 3 = −5.

## Optimized solutions

The optimized Java solution parses the numbers byte by byte from
`System.in` instead of using `Scanner`: 0.093 s instead of 0.140 s and
400 KB instead of 1584 KB.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2066_bruteforce.cpp](2066_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 176 KB | 11303806 |
| [2066_bruteforce.go](2066_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1080 KB | 11294375 |
| [2066_bruteforce.java](2066_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.140 s | 1584 KB | 11303807 |
| [2066_bruteforce.py](2066_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 532 KB | 11294380 |
| [2066_bruteforce.rs](2066_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.046 s | 224 KB | 11303808 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2066_bruteforce_optimized.java](2066_bruteforce_optimized.java) | Java 1.8 | bruteforce | O(1) | AC | 0.093 s | 400 KB | 11303798 |
