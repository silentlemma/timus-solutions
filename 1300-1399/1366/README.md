# 1366. Presents

[Timus 1366](https://acm.timus.ru/problem.aspx?space=1&num=1366) · difficulty 524 · math

Original problem: idea by Stanislav Vasiliev, prepared by Pavel Egorov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n ≤ 1000 children brings a present, and the presents are
exchanged so that every child gets exactly one present and nobody keeps
their own. Count the ways to do it.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number n.

## Output

The number of exchanges.

## Examples

### Example 1

Input:

```
3
```

Output:

```
2
```

## Solution

An exchange is a permutation with no fixed point, a derangement. By
inclusion–exclusion their number is d(k) = Σ (−1)ⁱ · k! / i! over
i = 0 … k, and multiplying d(k − 1) by k gives every term of d(k) but
the last one, (−1)ᵏ. So d(1) = 0 and d(k) = k · d(k − 1) + (−1)ᵏ: start
from 0 and apply it for k = 2 … n.

The answer for n = 1000 has 2 568 digits, so it needs long arithmetic:
each step multiplies by a small number and adds or subtracts 1.
`O(n²)` digit operations.

Pitfalls:

- one child cannot exchange at all: the answer is 0 (test 02);
- d(21) is the first count that no longer fits in 64 bits (test 06);
- after the multiplication the number is at least 3 for k ≥ 3, so
  subtracting 1 never goes below zero.

The recurrence was compared with counting all permutations for n ≤ 8,
and with the inclusion–exclusion sum for n = 50.

## Language notes

- Python, Go and Java use their built-in big integers.
- C++ and Rust keep the number as limbs of nine decimal digits, lowest
  first, and print every limb but the top one padded to nine digits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1366_math.cpp](1366_math.cpp) | G++ 13.2 x64 | math | O(n²) | AC | 0.031 s | 196 KB |
| [1366_math.go](1366_math.go) | Go 1.14 x64 | math | O(n²) | AC | 0.031 s | 1268 KB |
| [1366_math.java](1366_math.java) | Java 1.8 | math | O(n²) | AC | 0.125 s | 3320 KB |
| [1366_math.py](1366_math.py) | Python 3.12 x64 | math | O(n²) | AC | 0.093 s | 412 KB |
| [1366_math.rs](1366_math.rs) | Rust 1.75 x64 | math | O(n²) | AC | 0.046 s | 252 KB |
