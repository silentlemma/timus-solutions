# 1794. Masterpieces of World Architecture

[Timus 1794](https://acm.timus.ru/problem.aspx?space=1&num=1794) · difficulty 197 · implementation

Original problem by Vladislav Isenbaev (prepared by Oleg Dolgorukov), from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n students sit in a circle, numbered 1 to n clockwise, and will speak
one after another clockwise. Student i would like to speak aᵢ-th.
Choose who speaks first so that as many students as possible speak
exactly at the turn they want. Any best choice is accepted.

## Input

n (2 ≤ n ≤ 10⁵), then a₁, …, aₙ (1 ≤ aᵢ ≤ n).

## Output

The number of the student who starts.

## Examples

### Example 1

Input:

```
4
4 1 2 3
```

Output:

```
2
```

### Example 2

Input:

```
3
1 1 1
```

Output:

```
3
```

## Solution

If student k starts, student i speaks at turn ((i − k) mod n) + 1. So
student i is pleased by exactly one start, k = ((i − aᵢ) mod n) + 1.
Count these votes over all students and print a start with the most
votes. `O(n)`.

In the first example all four students vote for start 2: for instance
student 1 wants to be fourth, and 2, 3, 4, 1 puts them fourth.

Pitfalls:

- i − aᵢ may be negative, and in C++, Go and Java the remainder then
  is negative too;
- several starts may tie, as in the second example, where any of the
  three is accepted.

The checker counts the votes itself and accepts any start with the
most. It agrees with a direct count over every start on 300 small
classes, and the answers agree with an independent accepted
implementation on large ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1794_implementation.cpp](1794_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.078 s | 588 KB |
| [1794_implementation.go](1794_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 2400 KB |
| [1794_implementation.java](1794_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 812 KB |
| [1794_implementation.py](1794_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 8340 KB |
| [1794_implementation.rs](1794_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 2136 KB |
