# 1167. Splitting a line of black and white horses into stables with the least unhappiness

[Timus 1167](https://acm.timus.ru/problem.aspx?space=1&num=1167) · difficulty 136 · dp

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 500` horses, each black or white, stand in a line. Split the line
into exactly `K` non-empty consecutive groups, one per stable. A stable
with `i` black and `j` white horses has unhappiness `i·j`. Find the least
possible total unhappiness.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `K`, then `N` colours: `1` for black, `0` for white.

## Output

The least total unhappiness.

## Examples

### Example 1

Input:

```
6 3
1
1
0
1
0
1
```

Output:

```
2
```

## Solution

Let `best[s][i]` be the least unhappiness of the first `i` horses in `s`
stables. The last stable takes some horses `j..i−1`, so
`best[s][i] = min over j of best[s−1][j] + cost(j, i)`, where the cost is
black times white, read off prefix counts of black horses. That is
`O(K·N²)` in all, about 20 million steps at the limits, which is fine for
compiled languages but slow for Python.

The cost has a useful property. For `a ≤ b ≤ c ≤ d`, write `x`, `y`, `z`
for the pieces `a..b`, `b..c`, `c..d`; then
`cost(a, d) + cost(b, c) − cost(a, c) − cost(b, d) = Bx·Wz + Bz·Wx ≥ 0`,
with `B` and `W` the black and white counts. By this quadrangle
inequality, the best last split never moves left when `i` grows. So each
layer is filled by divide and conquer: find the best split for the middle
`i`, then the left half only searches splits up to it and the right half
only splits from it. Each layer costs `O(N log N)`, all of them
`O(K·N log N)`.

Pitfalls:

- the stables must all be used, so `best[s][i]` only exists for `i ≥ s`;
- with no stables yet, only `best[0][0] = 0` is possible, and every other
  start must count as unreachable.

The answers were compared with the plain `O(K·N²)` recurrence on 400
random inputs of up to 40 horses and on every test.

## Language notes

- All languages run the same divide and conquer; Python uses an explicit
  stack instead of recursion.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1167_dp.cpp](1167_dp.cpp) | G++ 13.2 x64 | dp | O(K·N log N) | AC | 0.015 s | 196 KB |
| [1167_dp.go](1167_dp.go) | Go 1.14 x64 | dp | O(K·N log N) | AC | 0.031 s | 3204 KB |
| [1167_dp.java](1167_dp.java) | Java 1.8 | dp | O(K·N log N) | AC | 0.125 s | 1464 KB |
| [1167_dp.py](1167_dp.py) | Python 3.12 x64 | dp | O(K·N log N) | AC | 0.421 s | 552 KB |
| [1167_dp.rs](1167_dp.rs) | Rust 1.75 x64 | dp | O(K·N log N) | AC | 0.031 s | 244 KB |
