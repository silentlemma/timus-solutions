# 1656. Far Away Kingdom's Army

[Timus 1656](https://acm.timus.ru/problem.aspx?space=1&num=1656) · difficulty 206 · constructive

Original problem by Vladimir Yakovlev (idea by Magaz Asanov), from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Arrange n² soldiers of given heights in an n × n square so that in every
row and every column the tallest stands in the middle and heights never
grow from the middle towards either end.

## Input

An odd n from 3 to 9, then n² heights from 170 to 200.

## Output

The square, n rows of n heights. Any valid arrangement is accepted.

## Examples

### Example 1

Input:

```
3
170
170
180
175
170
175
175
170
175
```

Output:

```
170 175 170
175 180 175
170 175 170
```

## Solution

Rank the cells by the pair (nearer, farther) of their distances from the
centre row and the centre column, and give the tallest soldiers to the
lowest ranks. Along a row at distance a from the centre, a cell at
distance b has rank (b, a) while b < a and (a, b) from then on: either
way the rank grows as b grows, so on each side of the middle the heights
never increase outwards. Columns are the same by symmetry. Cells with
equal rank are mirror images, never on the same side of one line.
`O(n² log n)`; Go’s stable sort: `O(n² log² n)`.

Pitfalls:

- "never grow towards the ends" allows equal heights (test 02);
- many arrangements are valid, so a checker verifies the rules and the
  set of heights.

The program's squares pass the checker on 90 random armies.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1656_constructive.cpp](1656_constructive.cpp) | G++ 13.2 x64 | constructive | O(n² log n) | AC | 0.015 s | 200 KB |
| [1656_constructive.go](1656_constructive.go) | Go 1.14 x64 | constructive | O(n² log² n) | AC | 0.031 s | 1152 KB |
| [1656_constructive.java](1656_constructive.java) | Java 1.8 | constructive | O(n² log n) | AC | 0.156 s | 4188 KB |
| [1656_constructive.py](1656_constructive.py) | Python 3.12 x64 | constructive | O(n² log n) | AC | 0.078 s | 448 KB |
| [1656_constructive.rs](1656_constructive.rs) | Rust 1.75 x64 | constructive | O(n² log n) | AC | 0.015 s | 240 KB |
