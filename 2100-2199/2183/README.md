# 2183. Flipping the signs of one segment to raise the minimum

[Timus 2183](https://acm.timus.ru/problem.aspx?space=1&num=2183) · difficulty 687 · binary_search, dp

Original problem by Artyom Abaturov, from the Ural Team Programming Contest 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Change the signs of all numbers in exactly one non-empty segment of an
array so that its minimum becomes as large as possible, and print that
minimum. The array has a negative number. The limits are 1 second and
256 MB.

## Input

n, 1 ≤ n ≤ 10⁵, then a₁ … aₙ, −10⁹ ≤ aᵢ ≤ 10⁹.

## Output

The largest possible minimum.

## Examples

### Example 1

Input:

```
5
-1 3 -2 -4 5
```

Output:

```
-1
```

### Example 2

Input:

```
4
2 -4 -3 -10
```

Output:

```
2
```

## Solution

Ask whether a minimum of at least x is possible. Every number below x
must be flipped, so the segment has to cover all of them, and every
number inside the segment must become at least x, that is, be at most
−x. A longer segment only adds conditions, so it is enough to test the
shortest one, from the first to the last number below x. If no number
is below x, a single number at most −x still has to be flipped, which
holds whenever the smallest number is at most −x.

Larger x only makes the test harder, so a binary search over x from
−10⁹ to 10⁹ finds the largest value that passes, with an O(n) test,
O(n log C) in total.

In the second example flipping −4 −3 −10 gives 2 4 3 10, whose minimum
is 2.

## Language notes

- The Python solution skips the binary search: one left-to-right pass
  keeps the best prefix minimum with the flip not started, running, or
  finished, which is O(n).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2183_binary_search.cpp](2183_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n log C) | AC | 0.093 s | 984 KB |
| [2183_binary_search.go](2183_binary_search.go) | Go 1.14 x64 | binary_search | O(n log C) | AC | 0.031 s | 3496 KB |
| [2183_binary_search.java](2183_binary_search.java) | Java 1.8 | binary_search | O(n log C) | AC | 0.156 s | 1320 KB |
| [2183_binary_search.rs](2183_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n log C) | AC | 0.031 s | 3708 KB |
| [2183_dp.py](2183_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.125 s | 7524 KB |
