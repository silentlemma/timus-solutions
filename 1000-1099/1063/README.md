# 1063. The cheapest extra dominoes for a chain

[Timus 1063](https://acm.timus.ru/problem.aspx?space=1&num=1063) · difficulty 2206 · dijkstra

Original problem from the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A set of `N` dominoes (`2 ≤ N ≤ 100`) has faces from 1 to 6. Add dominoes
(possibly none) with the smallest total of face values so that all
dominoes together can be laid in one chain, where touching halves show the
same number. Print the total, the number of added dominoes and the
dominoes; any cheapest set is accepted.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines with the two faces of a domino.

## Output

The smallest total (`0` if nothing is needed), the number of added
dominoes, then the dominoes.

## Checking

Any cheapest set is accepted. The checker verifies that the total equals
the smallest possible one, that it is the sum of the listed dominoes, and
that all dominoes together form a chain.

## Examples

### Example 1

Input:

```
6
6 1
1 5
5 5
5 2
2 4
4 2
```

Output:

```
0
0
```

### Example 2

Input:

```
5
1 5
6 1
5 5
2 4
2 4
```

Output:

```
6
2
1 2
1 2
```

## Solution

Take the numbers 1…6 as vertices and the dominoes as edges (a double is a
loop). A chain using every domino is an Euler trail, which exists exactly
when the vertices in use are connected and at most two of them have odd
degree. Adding a domino `(a, b)` costs `a + b`, joins the groups of `a`
and `b`, and flips the parity of both faces.

Everything that matters fits in a small state: the partition of the six
faces into connected groups, the set of faces in use and the set of faces
with odd degree. The solutions run Dijkstra's algorithm over these states,
starting from the given set; the moves are the 15 dominoes with different
faces (doubles never help), and the first state that allows a chain gives
the answer, with the added dominoes read back along the path. There are
at most `203 · 64 · 64` states and far fewer are reached.

The search finds detours that a simpler rule would miss. Two separate
doubles `5 5` and `6 6` are joined by one domino `5 6` (total 11). If the
parities must not change, two dominoes through face 1, `1 5` and `1 6`
(total 13), are cheaper than the same domino twice.

Pitfalls:

- doubles count twice for the degree and do not change parity;
- faces that appear on no domino need not be connected;
- the cheapest fix may use a face that is not in the set at all
  (usually 1).

The answers were checked against an exhaustive search over all sets of up
to seven extra dominoes.

## Language notes

- All languages pack a state into one integer (the group labels in base 6
  and the two masks) and keep maps for the distances and the path.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1063_dijkstra.cpp](1063_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.015 s | 336 KB |
| [1063_dijkstra.go](1063_dijkstra.go) | Go 1.14 x64 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.031 s | 1884 KB |
| [1063_dijkstra.java](1063_dijkstra.java) | Java 1.8 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.125 s | 6012 KB |
| [1063_dijkstra.py](1063_dijkstra.py) | Python 3.12 x64 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.093 s | 1236 KB |
| [1063_dijkstra.rs](1063_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.046 s | 616 KB |
