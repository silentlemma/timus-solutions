# 1644. A Whole Lot of Walnuts

[Timus 1644](https://acm.timus.ru/problem.aspx?space=1&num=1644) · difficulty 100 · implementation

Original problem by Alexey Samsonov, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A parrot ate between 3 and 9 walnuts in each of n experiments and wrote
down whether it stayed hungry or was satisfied. Satisfaction is
monotone: more walnuts never leave it hungrier. It is known that ten
walnuts always satisfy it and two never do. Find the least number of
walnuts that surely satisfies it, or report that the records contradict
each other.

## Input

n (0 ≤ n ≤ 100), then n lines: a number of walnuts and `hungry` or
`satisfied`.

## Output

The least number of walnuts that is sure to satisfy, or
`Inconsistent`.

## Examples

### Example 1

Input:

```
4
4 hungry
7 satisfied
5 hungry
8 satisfied
```

Output:

```
7
```

### Example 2

Input:

```
2
6 hungry
5 satisfied
```

Output:

```
Inconsistent
```

## Solution

Take the largest hungry amount, starting from 2, and the smallest
satisfying amount, starting from 10. The records fit a monotone
threshold exactly when the second is larger; then the smallest
satisfying amount is the answer, since anything less has never been
seen to satisfy. Otherwise `Inconsistent`. `O(n)`.

Pitfalls:

- with no records the answer is 10 (test 03), with only hungry ones the
  answer stays 10 (test 04);
- the same amount recorded both ways is a contradiction (test 06).

The answers match an independent accepted implementation on 180 random
record sets.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1644_implementation.cpp](1644_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 392 KB |
| [1644_implementation.go](1644_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1084 KB |
| [1644_implementation.java](1644_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1708 KB |
| [1644_implementation.py](1644_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 444 KB |
| [1644_implementation.rs](1644_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 220 KB |
