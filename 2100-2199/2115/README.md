# 2115. Sort a line with at most one swap

[Timus 2115](https://acm.timus.ru/problem.aspx?space=1&num=2115) · difficulty 228 · sorting

Original problem by Ivan Smirnov, from the University Academic School Olympiad in Informatics 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n students stand in a line with heights aᵢ. The line is fine when it is
sorted ascending or descending. Say whether it already is, whether one
swap of two students can make it so (and which swap), or neither. Any
fixing swap is accepted. The limits are 1 second and 256 MB.

## Input

n ≤ 10⁵, then the heights, up to 10⁹.

## Output

`Nothing to do here`; or `Yes` and the two positions; or `No hope`.

## Checking

A checker compares the verdict and, for `Yes`, swaps the two printed
students and checks the order.

## Examples

### Example 1

Input:

```
3
150 160 170
```

Output:

```
Nothing to do here
```

### Example 2

Input:

```
4
140 160 150 170
```

Output:

```
Yes
2 3
```

## Solution

Sort the heights; the target is that sorted line or its reverse. A swap
changes only two places, so it can turn the line into a target only if
the line differs from it in exactly two places i and j, and then it
works exactly when aᵢ and aⱼ are each other's target values. Both
targets are tried, which takes O(n log n) for the sort.

In the second example 140 160 150 170 differs from the ascending order
in places 2 and 3, and swapping them sorts the line (swapping 1 and 4
gives the descending order instead).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2115_sorting.cpp](2115_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.109 s | 2556 KB |
| [2115_sorting.go](2115_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.140 s | 5696 KB |
| [2115_sorting.java](2115_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 3676 KB |
| [2115_sorting.py](2115_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.140 s | 15740 KB |
| [2115_sorting.rs](2115_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.046 s | 3524 KB |
