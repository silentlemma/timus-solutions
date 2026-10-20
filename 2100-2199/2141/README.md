# 2141. Maximum alternating sum of a segment

[Timus 2141](https://acm.timus.ru/problem.aspx?space=1&num=2141) · difficulty 251 · dp

Original problem by Alexander Lozhkin, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose a contiguous segment of a sequence, possibly empty, and sum it
with alternating signs: the first chosen element with a plus, the second
with a minus and so on. Find the largest possible value. The limits are
1 second and 256 MB.

## Input

n, 1 ≤ n ≤ 10⁵, then a₁ … aₙ, −10⁵ ≤ aᵢ ≤ 10⁵.

## Output

The largest alternating sum (0 for the empty segment).

## Examples

### Example 1

Input:

```
5
1 2 3 4 5
```

Output:

```
5
```

### Example 2

Input:

```
5
1 -2 3 -4 5
```

Output:

```
15
```

### Example 3

Input:

```
5
-1 -2 -3 -4 -5
```

Output:

```
2
```

## Solution

Scan the sequence keeping two values for segments that end at the
current element: P, the best sum when this element has a plus, and M,
the best sum when it has a minus. An element with a plus either starts a
new segment or follows an element with a minus, and an element with a
minus always follows one with a plus:

- P = a + max(0, previous M),
- M = previous P − a.

The first element can only have a plus, so it starts with P = a₁, and M
is set to 0, which in the next step only means "start anew". The answer
is the largest P or M seen, or 0. Sums reach 10¹⁰, so they need 64-bit
integers. The scan takes O(n).

In the second example 1 − (−2) + 3 − (−4) + 5 = 15.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2141_dp.cpp](2141_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.078 s | 140 KB |
| [2141_dp.go](2141_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.078 s | 1916 KB |
| [2141_dp.java](2141_dp.java) | Java 1.8 | dp | O(n) | AC | 0.125 s | 496 KB |
| [2141_dp.py](2141_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.125 s | 12312 KB |
| [2141_dp.rs](2141_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.031 s | 2148 KB |
