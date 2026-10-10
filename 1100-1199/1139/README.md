# 1139. Counting the blocks a diagonal flight passes over in a grid of streets

[Timus 1139](https://acm.timus.ru/problem.aspx?space=1&num=1139) · difficulty 78 · number_theory

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` avenues and `M` streets, `1 < N, M < 32000`, cut a city into square
blocks. A helicopter flies straight from the south-west corner to the
north-east corner. Count the blocks it flies over; a block is the open
inside of its square, so touching a corner does not count.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `M`.

## Output

The number of blocks.

## Examples

### Example 1

Input:

```
4 3
```

Output:

```
4
```

### Example 2

Input:

```
3 3
```

Output:

```
2
```

## Solution

The blocks form an `a × b` grid with `a = N − 1` and `b = M − 1`, and the
flight is its diagonal. It starts inside the first block, and each time it
crosses a line of the grid it enters a new block. It crosses the
`a − 1` inner vertical lines and the `b − 1` inner horizontal lines, but
at an inner corner of the grid it crosses one of each at the same moment
and enters only one new block. The diagonal passes through the points
`(k·a/g, k·b/g)`, so it meets exactly `g − 1` inner corners, where
`g = gcd(a, b)`. In total
`1 + (a − 1) + (b − 1) − (g − 1) = a + b − gcd(a, b)`. `O(log min(a, b))`.

Pitfalls:

- the input counts lines, not blocks: subtract one from each;
- in a square grid the diagonal goes through every corner on its way and
  crosses only `a` blocks;
- with a single row or column the flight crosses every block in it.

The answers were compared with a column-by-column count of the blocks
under the diagonal, using exact floor and ceiling, for all `N, M ≤ 40` and
on every test.

## Language notes

- All languages apply the same formula.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1139_number_theory.cpp](1139_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 128 KB |
| [1139_number_theory.go](1139_number_theory.go) | Go 1.14 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 1060 KB |
| [1139_number_theory.java](1139_number_theory.java) | Java 1.8 | number_theory | O(log min(N, M)) | AC | 0.109 s | 1592 KB |
| [1139_number_theory.py](1139_number_theory.py) | Python 3.12 x64 | number_theory | O(log min(N, M)) | AC | 0.078 s | 400 KB |
| [1139_number_theory.rs](1139_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 248 KB |
