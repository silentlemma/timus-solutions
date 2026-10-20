# 2157. Longest fall through clouds that stop the jumper

[Timus 2157](https://acm.timus.ru/problem.aspx?space=1&num=2157) · difficulty 1281 · dp

Original problem by Valentin Zuev, from the Ural School Programming Contest 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A parachutist falls from (x, y) with acceleration 10 m/s², starting with
zero vertical speed, and can set any horizontal speed between −1 and
1 m/s at any moment. Hitting the point of cloud i stops the fall for cᵢ
seconds, after which the fall starts again from rest. Find the longest
possible time until the ground y = 0 is reached, with absolute or
relative error at most 10⁻⁴. The limits are 3 seconds and 256 MB.

## Input

n, 0 ≤ n ≤ 50 000, the start (x, y) with |x| ≤ 10 000 and
1 ≤ y ≤ 10 000, then the clouds xᵢ, yᵢ, cᵢ with |xᵢ| ≤ 10 000,
0 < yᵢ < y and 1 ≤ cᵢ ≤ 10 000. All input values are integers,
and all cloud positions (xᵢ, yᵢ) are distinct.

## Output

The longest fall time.

## Examples

### Example 1

Input:

```
5
0 80
-1 30 2
-1 60 1
0 40 10
1 20 1
1 50 1
```

Output:

```
20.863703305
```

### Example 2

Input:

```
0
100 100
```

Output:

```
4.472135955
```

## Solution

A fall of height h from rest takes √(h / 5) seconds, and during it the
horizontal position can change by at most that much. So from height Y a
cloud at (x′, y′) is reachable exactly when 5 (x′ − x)² ≤ Y − y′, which
means at most ⌊√(Y / 5)⌋ ≤ 44 columns to each side.

Let best(p) be the longest remaining time from a cloud p after its stop
is over, or from the start: either fall straight to the ground, √(h / 5) for its height h,
or fall to a reachable cloud q and add its density and best(q). Inside
one column only the highest reachable cloud matters. Going through it
on the way down to a lower cloud of the same column is possible and
longer, since √a + √b ≥ √(a + b) and the stop adds time.

So process the clouds and the start by increasing height. Every column
keeps the heights of its processed clouds in increasing order with their
values; for a point, binary search in each of the at most 89 columns
finds the highest cloud low enough, and best of the point is the maximum
over them. The start comes last and its value is the answer. The work
is O(n · 89 · log n).

In the second example there are no clouds, and the fall from 100 m takes
√20 ≈ 4.472 seconds.

Pitfall (test 03): compare answers with the stated absolute or relative
tolerance, not as exact text. At height 1 with no clouds, both
0.447213595 and 0.447214 are valid rounded values of √(1 / 5).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2157_dp.cpp](2157_dp.cpp) | G++ 13.2 x64 | dp | O(89 n log n) | AC | 0.125 s | 3052 KB |
| [2157_dp.go](2157_dp.go) | Go 1.14 x64 | dp | O(89 n log n) | AC | 0.390 s | 6320 KB |
| [2157_dp.java](2157_dp.java) | Java 1.8 | dp | O(89 n log n) | AC | 0.718 s | 7852 KB |
| [2157_dp.py](2157_dp.py) | Python 3.12 x64 | dp | O(89 n log n) | AC | 2.453 s | 23964 KB |
| [2157_dp.rs](2157_dp.rs) | Rust 1.75 x64 | dp | O(89 n log n) | AC | 0.250 s | 4032 KB |
