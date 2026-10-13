# 1492. Vasya's Dad 2

[Timus 1492](https://acm.timus.ru/problem.aspx?space=1&num=1492) · difficulty 1995 · math

Original problem by Fedor Fominykh, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A piecewise-linear function is given by N vertices (2 ≤ N ≤ 30000,
integer coordinates up to 15000 in absolute value) with increasing x,
x_1 = −x_N and no three consecutive vertices on a line. Can it be
written as the sum of an even and an odd piecewise-linear function?
Print "Yes" and the vertices of the even part, then of the odd part,
with at least four decimals, or "No".

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines x y.

## Output

"Yes" and the two lists of vertices, or "No".

## Examples

### Example 1

Input:

```
2
-1 0
1 0
```

Output:

```
Yes
-1.0000 0.0000
1.0000 0.0000
-1.0000 0.0000
1.0000 0.0000
```

## Solution

Every function on [−a, a] splits in exactly one way: E(x) =
(f(x) + f(−x))/2 is even, O(x) = (f(x) − f(−x))/2 is odd, and their sum
is f. So the answer is always "Yes", and the two parts are fixed.

Both parts are linear between the points of f and their mirror images,
so these x, sorted and without repeats, are the candidate vertices; the
values come from f by interpolation. A candidate stays only where the
part really bends, since no three consecutive vertices may lie on a
line. The slope of E between two candidates is (a/b − c/d)/2, where a/b
is the slope of f there and c/d the slope of f on the mirrored piece;
O uses a plus sign. Comparing two such fractions by cross
multiplication is exact, and every factor stays below 2·10⁹, so 64 bits
suffice. `O(N log N)`.

Pitfalls:

- "No" is never the answer (all tests);
- a mirrored point is often not a bend of one part, and keeping it puts
  three vertices on a line (tests 05, 07, gen3, gen4);
- an even or odd input leaves the other part as a straight zero with
  just two vertices (tests 01, 02, 03, 05, 07);
- the bends must be found with exact slopes, not by comparing
  interpolated values in floating point (gen5, test 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1492_math.cpp](1492_math.cpp) | G++ 13.2 x64 | math | O(N log N) | AC | 0.187 s | 1700 KB |
| [1492_math.go](1492_math.go) | Go 1.14 x64 | math | O(N log N) | AC | 0.125 s | 5884 KB |
| [1492_math.java](1492_math.java) | Java 1.8 | math | O(N log N) | AC | 0.546 s | 17680 KB |
| [1492_math.py](1492_math.py) | Python 3.12 x64 | math | O(N log N) | AC | 0.468 s | 23408 KB |
| [1492_math.rs](1492_math.rs) | Rust 1.75 x64 | math | O(N log N) | AC | 0.062 s | 4672 KB |
