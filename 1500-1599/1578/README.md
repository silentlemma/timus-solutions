# 1578. Mammoth Hunt

[Timus 1578](https://acm.timus.ru/problem.aspx?space=1&num=1578) · difficulty 880 · greedy

Original problem by Alexander Ipatov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given N + 2 different points with integer coordinates (N ≤ 2000),
order them into a polyline whose every turn is acute: at each inner
vertex the two segments make an angle below 90°, where an angle of 0°
(turning straight back) counts as acute. Print `NO` if this is
impossible, otherwise `YES` and the order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N + 2 points.

## Output

`YES` and the numbers of the points in order, or `NO`. Any valid order
is accepted.

## Examples

### Example 1

Input:

```
2
0 0
1 1
1 2
2 0
```

Output:

```
YES
1 3 4 2
```

### Example 2

Input:

```
2
0 0
0 1
0 2
0 3
```

Output:

```
YES
1 3 2 4
```

## Solution

It is always possible: start anywhere and always go to the farthest
point not visited yet. Take a turn at B, with A before it and C after
it. When the path stood at A, both B and C were still free and B was
chosen as the farthest, so |AC| ≤ |AB|. The law of cosines,
|AC|² = |AB|² + |BC|² − 2·|AB|·|BC|·cos B, then gives
cos B ≥ |BC| / (2·|AB|) > 0, so the angle at B is below 90°. `NO` is
never printed. Each step scans the free points once: `O(N²)`, about
2·10⁶ distance comparisons, with exact integer squared distances.

Pitfalls:

- the answer is never `NO`, even for points on one line, where the path
  zigzags back and forth (the second example, test gen2);
- the angle is the one between the two segments at the vertex, so going
  straight on is 180° and not allowed, and turning back is 0° and
  allowed;
- several orders are valid, so a checker tests every turn.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1578_greedy.cpp](1578_greedy.cpp) | G++ 13.2 x64 | greedy | O(N^2) | AC | 0.031 s | 232 KB |
| [1578_greedy.go](1578_greedy.go) | Go 1.14 x64 | greedy | O(N^2) | AC | 0.046 s | 1120 KB |
| [1578_greedy.java](1578_greedy.java) | Java 1.8 | greedy | O(N^2) | AC | 0.156 s | 620 KB |
| [1578_greedy.py](1578_greedy.py) | Python 3.12 x64 | greedy | O(N^2) | AC | 0.671 s | 1548 KB |
| [1578_greedy.rs](1578_greedy.rs) | Rust 1.75 x64 | greedy | O(N^2) | AC | 0.031 s | 288 KB |
