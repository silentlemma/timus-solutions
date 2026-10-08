# 1010. The steepest chord above a discrete function

[Timus 1010](https://acm.timus.ru/problem.aspx?space=1&num=1010) · difficulty 293 · math

Original problem from the Third Open USTU Collegiate Programming Contest (PhysTech Cup), 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A function is given by its values `f(1), ..., f(N)` (`2 ≤ N ≤ 100 000`,
`-2^31 ≤ f(i) ≤ 2^31 - 1`). A pair of points `A = (a, f(a))` and
`B = (b, f(b))`, `a < b`, is **valid** if every point `(i, f(i))` with
`a < i < b` lies strictly below the line `AB`. Among the valid pairs find one
with the largest absolute value of the slope of `AB`; if there are several,
the one with the smallest `a`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `N` values `f(1), ..., f(N)`, one per line.

## Output

`a` and `b`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
1
5
2
-4
```

Output:

```
3 4
```

### Example 2

Input:

```
2
7
7
```

Output:

```
1 2
```

## Solution

The answer is always a pair of neighbours `(a, a + 1)`: the first one with
the largest `|f(a + 1) - f(a)|`.

Why: the slope of a chord from `a` to `b` is the mean of the slopes of the
`b - a` unit steps under it, so its absolute value is at most the largest
absolute step slope. Neighbouring pairs are always valid (there is nothing
between them), so the maximum is reached on a step. A longer chord can only
tie if all its steps have the same slope — but then the points between lie on
the line, not strictly below it, and the chord is not valid. So the steps
with the largest `|difference|` are exactly the optimal pairs, and the first
of them has the smallest `a`.

One pass, `O(N)` time and `O(1)` memory (or `O(N)` if the values are stored).

Pitfalls:

- a difference of two values can reach `2^32 - 1`: use 64-bit integers;
- ties: keep the first maximum (a strict comparison while scanning left to
  right);
- the validity condition looks like it needs a convex hull, but it never
  matters for the answer.

## Language notes

The same scan everywhere. Java uses a small byte-buffer reader, since
`Scanner` is slow for `10^5` numbers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1010_math.cpp](1010_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.046 s | 136 KB |
| [1010_math.go](1010_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 2668 KB |
| [1010_math.java](1010_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 580 KB |
| [1010_math.py](1010_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 14648 KB |
| [1010_math.rs](1010_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 3696 KB |
