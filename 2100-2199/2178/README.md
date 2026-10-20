# 2178. Counting segments that hold a set of consecutive numbers

[Timus 2178](https://acm.timus.ru/problem.aspx?space=1&num=2178) · difficulty 1459 · two_pointers

Original problem by Vadim Barinov, from the Ural School Programming Contest 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the segments of an array of N numbers whose values are distinct
and form a set of consecutive integers in some order. The limits are
1 second and 512 MB.

## Input

N, 1 ≤ N ≤ 10⁵, then a₁ … aₙ, 1 ≤ aᵢ ≤ 10⁵.

## Output

The number of such segments.

## Examples

### Example 1

Input:

```
5
4 2 3 1 2
```

Output:

```
11
```

## Solution

A segment [l, r] qualifies exactly when its values are distinct and
max − min = r − l. Distinctness is a window condition: for every
position the farthest segment end without a repeated value comes from
the last occurrences of the values, in two linear passes, so every
start l has a bound R(l) on its end and every end a bound on its start.

The rest is the usual divide and conquer over the array. Segments
inside one half are counted recursively; for those crossing the middle,
prefix minima and maxima are taken outward from the middle on both
sides. Four cases follow from where the minimum and the maximum lie:

- both on the left side: the end is fixed as l + max − min, check it;
- both on the right side: symmetric, the start is fixed;
- maximum on the left, minimum on the right: the condition reads
  min(right part) + r = max(left part) + l, so the right ends whose
  prefix maximum stays below the left maximum and whose prefix minimum
  is below the left minimum form a window that moves monotonically as l
  goes left; counts of the key min + r over the window answer each l;
- minimum on the left, maximum on the right: the same with the key
  max − r.

The windows are also cut by R(l). Each level does linear work, so the
total is O(N log N), with a direct scan for very short ranges.

In the example 11 segments qualify, among them [4, 2, 3, 1] and
[3, 1, 2].

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2178_two_pointers.cpp](2178_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N log N) | AC | 0.046 s | 2488 KB |
| [2178_two_pointers.go](2178_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N log N) | AC | 0.062 s | 9076 KB |
| [2178_two_pointers.java](2178_two_pointers.java) | Java 1.8 | two_pointers | O(N log N) | AC | 0.156 s | 3168 KB |
| [2178_two_pointers.py](2178_two_pointers.py) | PyPy 3.10 x64 | two_pointers | O(N log N) | AC | 0.656 s | 18628 KB |
| [2178_two_pointers.rs](2178_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N log N) | AC | 0.046 s | 4680 KB |
