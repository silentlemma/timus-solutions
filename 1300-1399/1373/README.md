# 1373. Pictura ex Machina

[Timus 1373](https://acm.timus.ru/problem.aspx?space=1&num=1373) · difficulty 837 · geometry

Original problem by Pavel Egorov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A plotter paints N ≤ 100 000 strokes. Each stroke goes X millimetres
in one direction, turns 90° clockwise and goes X millimetres more; it
is given by its start and end, integers of absolute value at most
10 000. Print the width and height of the smallest axis-parallel frame
that holds all the strokes, to 4 decimal places.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Up to the end of the input, lines of four integers: the start and the
end of a stroke.

## Output

The width and the height of the frame.

## Examples

### Example 1

Input:

```
0 0 1 1
1 1 2 0
2 0 0 0
2 0 3 0
```

Output:

```
3.0000 2.0000
```

## Solution

A stroke is two segments, so the frame only has to hold its start, its
end and its corner. If the first leg is (p, q), a clockwise turn makes
the second (q, −p), and together they give the shift from start to end:
p + q = dx and q − p = dy. So the corner is the start plus
((dx − dy) / 2, (dx + dy) / 2). The answer is the bounding box of all
these points. Doubling every coordinate keeps the halves whole, and the
box is halved again at the end. `O(N)`.

Pitfalls:

- the y axis points up: the example gives 3 × 2 this way and 3 × 1.5
  with the opposite turn;
- the corners can lie outside the range of the input, up to 20 000 from
  the origin (test 06);
- there may be no strokes at all, which gives 0 × 0 (test 02);
- the count of strokes is not given: read to the end of the input.

## Language notes

- Go reads with a word scanner, which is faster than `fmt.Fscan` for
  400 000 numbers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1373_geometry.cpp](1373_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.218 s | 144 KB |
| [1373_geometry.go](1373_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.093 s | 10332 KB |
| [1373_geometry.java](1373_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.187 s | 5024 KB |
| [1373_geometry.py](1373_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.312 s | 41448 KB |
| [1373_geometry.rs](1373_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 14464 KB |
