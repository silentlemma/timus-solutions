# 1726. Visits

[Timus 1726](https://acm.timus.ru/problem.aspx?space=1&num=1726) · difficulty 120 · sorting

Original problem by Denis Dublennykh, from the Ural Regional Team Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The n members of a committee live at street crossings of a grid city
and walk to each other along the streets by shortest paths. Everyone
visits everyone equally often. Find the average walking distance,
rounded down.

## Input

n (2 ≤ n ≤ 10⁵), then n pairs of coordinates x and y
(1 ≤ x, y ≤ 10⁶).

## Output

The average distance between two members' houses, rounded down.

## Examples

### Example 1

Input:

```
3
10 10
20 20
10 20
```

Output:

```
13
```

## Solution

A shortest walk along the streets has length |dx| + |dy|, so the sum
over all pairs splits into the sum of |x_i − x_j| and the sum of
|y_i − y_j|. Sort the x values: the i-th one (from 0) is at least each
of the i before it, so it adds i·x_i minus their sum, which a running
total keeps. The same goes for y. The average over the n(n − 1)/2
pairs is that sum divided by the number of pairs, rounded down.
`O(n log n)`.

In the example the distances are 20, 10 and 10, so the average is
40/3, rounded down to 13.

Pitfalls:

- the sum reaches about 5·10¹⁵ when half of the houses stand in each of
  two far corners, so it needs 64 bits;
- comparing all pairs directly takes about 5·10⁹ steps, far too many;
- with 2·10⁵ numbers to read, the Go solution parses the input by hand
  to stay well inside the time limit.

The averages match a sum over all pairs on 300 small random maps, and
an independent accepted implementation on the large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1726_sorting.cpp](1726_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.156 s | 1764 KB |
| [1726_sorting.go](1726_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.078 s | 2732 KB |
| [1726_sorting.java](1726_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.171 s | 2044 KB |
| [1726_sorting.py](1726_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.203 s | 20712 KB |
| [1726_sorting.rs](1726_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 4740 KB |
