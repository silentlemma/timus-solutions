# 1266. Kirchhoff's law

[Timus 1266](https://acm.timus.ru/problem.aspx?space=1&num=1266) · difficulty 1401 · math

Original problem by Alexander Klepinin (prepared by Stanislav Vasilyev), from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A circuit has N nodes (2 ≤ N ≤ 20) and M resistors (1 ≤ M < 1000),
each joining two nodes with an integer resistance from 1 to 1000; a
pair of nodes may be joined by many resistors. Find the total
resistance between nodes 1 and N, rounded to two digits after the
point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then M lines `A B R`.

## Output

The resistance.

## Examples

### Example 1

Input:

```
4 5
1 2 15
2 4 5
1 3 10
3 4 10
2 3 1
```

Output:

```
9.40
```

## Solution

Follow the recipe from the statement. Add up the conductances 1/R of
all resistors between each pair of nodes. Fix the potential of node 1
at 1 and of node N at 0; at every other node the currents sum to zero:

```text
sum over v of g(u, v) · (V(u) − V(v)) = 0
```

That is a linear system of at most 18 unknowns, solved by Gaussian
elimination with partial pivoting. The current leaving node 1 is
I = Σ g(1, v) · (1 − V(v)), and the resistance is 1 / I.

Components cut off from both terminals carry no current, and their
potentials are undetermined. Before forming the system, a search from
node 1 drops all inner nodes unreachable from it. Every remaining inner node
is connected to node 1, whose potential is fixed, so the system has a
unique solution. `O(M + N³)`.

Pitfalls:

- isolated nodes and pieces cut off from both ends make the system
  singular if they are kept (tests 05, 06);
- parallel resistors between the same nodes add up as conductances
  (test 03);
- with N = 2 there are no unknowns at all (tests 02, 03).

The answers were compared on 120 random circuits with Kirchhoff's
matrix-tree formula, the ratio of two minors of the Laplacian computed
in exact fractions.

## Language notes

- All languages run the same elimination in doubles.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1266_math.cpp](1266_math.cpp) | G++ 13.2 x64 | math | O(M + N³) | AC | 0.001 s | 236 KB |
| [1266_math.go](1266_math.go) | Go 1.14 x64 | math | O(M + N³) | AC | 0.031 s | 1140 KB |
| [1266_math.java](1266_math.java) | Java 1.8 | math | O(M + N³) | AC | 0.078 s | 1484 KB |
| [1266_math.py](1266_math.py) | Python 3.12 x64 | math | O(M + N³) | AC | 0.078 s | 792 KB |
| [1266_math.rs](1266_math.rs) | Rust 1.75 x64 | math | O(M + N³) | AC | 0.031 s | 256 KB |
