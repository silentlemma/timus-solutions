# 2121. Area between two mirrored parabolas

[Timus 2121](https://acm.timus.ru/problem.aspx?space=1&num=2121) · difficulty 723 · geometry, math

Original problem by Alexey Danilyuk, from the t.me/umnik_team contest, Petrozavodsk training camp, summer 2018.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find the area of the region bounded by the parabolas y = (x − a)² and
x = (y − a)², printed with exactly 10 digits after the decimal point.
The limits are 1 second and 64 MB.

## Input

An integer a, 1 ≤ a ≤ 10¹⁸.

## Output

The area.

## Examples

### Example 1

Input:

```
2
```

Output:

```
7.6666666667
```

## Solution

Shift the origin to (a, a): with x = a + p and y = a + q the region is
q ≥ p² − a and p ≥ q² − a. The two parabolas meet at four points. Two of
them lie on q = p, where p² = p + a, so p = (1 ± s)/2 with s = √(4a + 1).
Subtracting the equations gives (p − q)(p + q + 1) = 0, so the other two
lie on p + q = −1 at p = (−1 ± t)/2 with t = √(4a − 3).

Integrate in p: the top of the region is q = √(p + a), and the bottom is
q = p² − a near both ends and q = −√(p + a) in the middle. At every
corner √(p + a) equals |q|, so every antiderivative turns into a
polynomial in the corner coordinates. Then the sums and products of the
two roots of each pair cancel s and t: the area is exactly 4a − 1/3.

So the answer is 4a − 1 followed by ".6666666667". For a = 10¹⁸ the
integer part is just below 4 · 10¹⁸ and fits in a 64-bit integer, while
floating point would lose the last digits.

In the example 4 · 2 − 1/3 = 7.6666666667.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2121_geometry_math.cpp](2121_geometry_math.cpp) | G++ 13.2 x64 | geometry, math | O(1) | AC | 0.015 s | 132 KB |
| [2121_geometry_math.go](2121_geometry_math.go) | Go 1.14 x64 | geometry, math | O(1) | AC | 0.015 s | 1076 KB |
| [2121_geometry_math.java](2121_geometry_math.java) | Java 1.8 | geometry, math | O(1) | AC | 0.125 s | 1628 KB |
| [2121_geometry_math.py](2121_geometry_math.py) | Python 3.12 x64 | geometry, math | O(1) | AC | 0.078 s | 376 KB |
| [2121_geometry_math.rs](2121_geometry_math.rs) | Rust 1.75 x64 | geometry, math | O(1) | AC | 0.015 s | 240 KB |
