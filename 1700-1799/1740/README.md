# 1740. Deer is Better!

[Timus 1740](https://acm.timus.ru/problem.aspx?space=1&num=1740) · difficulty 138 · math

Original problem by Sergey Pupyrev (prepared by Daniil Ayzenshteyn), from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The way to the polling station is l km long. The deer may run any way
they like, as long as every stretch of k km takes exactly h hours. Find
the shortest and the longest possible time for the whole way.

## Input

l, k and h (1 ≤ k ≤ l ≤ 1000, 1 ≤ h ≤ 1000).

## Output

The shortest and the longest time, with an error of at most 10⁻⁵.

## Examples

### Example 1

Input:

```
30 10 1
```

Output:

```
3.00000000 3.00000000
```

## Solution

Let t(x) be the time to reach kilometre x. Every stretch of k km takes h
hours, so t(x + k) = t(x) + h: t grows by h per k km plus a part that
repeats every k km. With l = nk + r, the whole way takes nh + t(r), and
t(r) lies between t(0) = 0 and t(k) = h. The deer can spend almost no
time on the first r km of every stretch, or almost all of it, so the
answers are nh and, if r > 0, (n + 1)h. `O(1)`.

In the example 30 km is three stretches of 10 km, 3 hours either way.

Pitfalls:

- when k divides l both answers are the same;
- the times are whole numbers; the code prints eight decimal
  places.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1740_math.cpp](1740_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB |
| [1740_math.go](1740_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1092 KB |
| [1740_math.java](1740_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1800 KB |
| [1740_math.py](1740_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB |
| [1740_math.rs](1740_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 252 KB |
