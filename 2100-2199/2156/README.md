# 2156. Splitting the differences around a circle into equal halves

[Timus 2156](https://acm.timus.ru/problem.aspx?space=1&num=2156) · difficulty 656 · math, constructive

Original problem by Semyon Trifochkin, from the Ural Team Programming Contest 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n friends with interest values a₁ … aₙ sit around a table, and the
conversation between neighbours i and i + 1 (n and 1 for the last one)
has interest |aᵢ − aᵢ₊₁|. Split the n conversations into two non-empty
sets with equal total interest, or print NO. Any valid split is
accepted. The limits are 1 second and 256 MB.

## Input

n, 3 ≤ n ≤ 10⁵, then a₁ … aₙ, 1 ≤ aᵢ ≤ 10⁹.

## Output

YES, then the size and the numbers of the first set and of the second
set, or NO.

## Checking

A checker verifies that the two sets are non-empty, split all
conversations and have equal sums.

## Examples

### Example 1

Input:

```
3
1 2 3
```

Output:

```
YES
2
1 2
1
3
```

## Solution

The answer is always YES. Going once around the table, the signed
differences aᵢ − aᵢ₊₁ add up to 0. So the conversations where the value
falls (aᵢ > aᵢ₊₁) have the same total interest as those where it rises,
and conversations between equal neighbours have interest 0 and can join
either side.

If the values are not all equal, there is at least one fall and one
rise, so both sets are non-empty. If they are all equal, every
conversation has interest 0, and one conversation against the other
n − 1 works. The work is O(n).

In the example the values fall only from 3 back to 1, so conversation 3
(interest 2) balances conversations 1 and 2 (interest 1 each).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2156_math_constructive.cpp](2156_math_constructive.cpp) | G++ 13.2 x64 | math, constructive | O(n) | AC | 0.093 s | 2668 KB |
| [2156_math_constructive.go](2156_math_constructive.go) | Go 1.14 x64 | math, constructive | O(n) | AC | 0.125 s | 9912 KB |
| [2156_math_constructive.java](2156_math_constructive.java) | Java 1.8 | math, constructive | O(n) | AC | 0.140 s | 9008 KB |
| [2156_math_constructive.py](2156_math_constructive.py) | Python 3.12 x64 | math, constructive | O(n) | AC | 0.140 s | 21040 KB |
| [2156_math_constructive.rs](2156_math_constructive.rs) | Rust 1.75 x64 | math, constructive | O(n) | AC | 0.046 s | 9448 KB |
