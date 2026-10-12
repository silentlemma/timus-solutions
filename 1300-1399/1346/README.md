# 1346. Intervals of Monotonicity

[Timus 1346](https://acm.timus.ru/problem.aspx?space=1&num=1346) · difficulty 297 · greedy

Original problem by Alexander Klepinin, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A function F is given on the integer grid A, A + 1, …, B, with
0 ≤ A < B ≤ 100 000 and values from −100 000 to 100 000. Split the grid
into the fewest intervals on each of which F does not decrease or does
not increase, and print how many there are.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A and B, then the values F(A), …, F(B), separated by spaces or line
breaks.

## Output

The smallest number of intervals.

## Examples

### Example 1

Input:

```
1 10
1 2 3 4 2 1 -1 3 6 7
```

Output:

```
3
```

## Solution

The intervals split the points of the grid, so the step between the
last point of one interval and the first point of the next one is free.
Any part of a monotone interval is monotone again. So it never hurts to
make the first interval as long as possible, and the same holds for
every next one: the greedy count is the smallest.

An interval is stretched while it stays monotone. Its direction is set
by its first step that is not flat, and flat steps fit either
direction. The first step against that direction ends the interval, and
the next one starts at the following point. `O(B − A)`.

Pitfalls:

- the step between two intervals is free: 1 3 2 4 needs only 2
  intervals, 1 3 and 2 4 (test 02);
- flat steps belong to the interval whichever way it goes, and a
  constant function is a single interval (tests 03, 05 and 06);
- the values may come on several lines.

The counts were compared with a dynamic program over all splits on 500
random functions of up to 12 points.

## Language notes

- All five solutions make the same single pass.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1346_greedy.cpp](1346_greedy.cpp) | G++ 13.2 x64 | greedy | O(B - A) | AC | 0.062 s | 588 KB |
| [1346_greedy.go](1346_greedy.go) | Go 1.14 x64 | greedy | O(B - A) | AC | 0.031 s | 2512 KB |
| [1346_greedy.java](1346_greedy.java) | Java 1.8 | greedy | O(B - A) | AC | 0.109 s | 900 KB |
| [1346_greedy.py](1346_greedy.py) | Python 3.12 x64 | greedy | O(B - A) | AC | 0.140 s | 11140 KB |
| [1346_greedy.rs](1346_greedy.rs) | Rust 1.75 x64 | greedy | O(B - A) | AC | 0.015 s | 2632 KB |
