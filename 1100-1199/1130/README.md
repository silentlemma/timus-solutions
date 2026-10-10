# 1130. Choosing a direction for each vector so that the walk ends within √2·L of the start

[Timus 1130](https://acm.timus.ru/problem.aspx?space=1&num=1130) · difficulty 937 · geometry, greedy

Original problem by Dmitry Filimonenkov, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A child runs along `N ≤ 10000` integer vectors in turn, each no longer
than `L ≤ 100`, and for each one the teacher chooses whether to run along
it or against it. Choose the directions so that the child ends no farther
than `√2·L` from the start. Print `YES` and the choice as a line of `+` and
`-`, or `WRONG ANSWER` if no choice works.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`N`, then `L`, then `N` lines with the two coordinates of a vector.

## Output

`YES` and a line of `N` signs, `+` for running along a vector and `-` for
running against it; or `WRONG ANSWER`.

## Checking

Any valid choice is accepted. The checker verifies the line of signs and
compares the squared distance of the end point with `2L²` exactly.

## Examples

### Example 1

Input:

```
4
5
5 0
0 5
0 0
-3 4
```

Output:

```
YES
+--+
```

## Solution

A good choice always exists, so the answer is always `YES`. The key fact:
among any three vectors no longer than `L`, two of them have a sum or a
difference no longer than `L`. The three lines through them split the
half-turn into three angles, so two of the lines are at most 60° apart;
taking those two vectors with the signs that point them at most 60° apart,
the difference has squared length `a² + b² − 2ab·cos θ ≤ a² + b² − ab`,
which is at most `max(a, b)² ≤ L²`.

So keep at most two vectors that are still free. When a third arrives,
find a pair and a sign that give a vector no longer than `L` and replace
the pair by that combination. At the end at most two vectors remain; choose
the sign that makes their dot product non-positive, and the squared length
of the result is at most `2L²`. Each combination is a node of a forest
whose children carry a relative sign; the final sign of an input vector
is the product of the relative signs on its way to the root. Every node
is created after its children, so one pass over the nodes in reverse order
fills in the signs. All arithmetic is in integers. `O(N)`.

Pitfalls:

- `WRONG ANSWER` is never the answer;
- comparing squared lengths keeps everything exact; no square roots are
  needed;
- flipping the sign of a combined vector flips all vectors inside it,
  which the relative signs in the forest take care of without touching
  them;
- zero vectors and `L = 0` need no special case.

The answers were checked by the checker on every test and on 150 random
sets of vectors, among them vectors close to three directions 120° apart,
where the merging step has the least room.

## Language notes

- All languages run the same merging with the same search order, so their
  answers are identical.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1130_geometry.cpp](1130_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 528 KB |
| [1130_geometry.go](1130_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 2636 KB |
| [1130_geometry.java](1130_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 2340 KB |
| [1130_geometry.py](1130_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.140 s | 3796 KB |
| [1130_geometry.rs](1130_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 1864 KB |
