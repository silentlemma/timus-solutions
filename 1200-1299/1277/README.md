# 1277. Cops and thieves

[Timus 1277](https://acm.timus.ru/problem.aspx?space=1&num=1277) · difficulty 867 · flow

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected network of N ≤ 100 stations has M two-way channels.
Holding station i takes x_i police (Σ x_i ≤ 10 000). The thieves go
from station F to station S, and neither of these two may be held.
With K ≤ 10 000 police, can every route from F to S be blocked?

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

K; then N, M, S and F; the N costs; then the M channels.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
10
5 5 1 5
1 6 6 11 1
1 2
1 3
2 4
3 4
4 5
```

Output:

```
NO
```

### Example 2

Input:

```
10
5 5 1 5
1 4 4 11 1
1 2
1 3
2 4
3 4
4 5
```

Output:

```
YES
```

## Solution

The cheapest set of stations that separates S from F is a minimum
vertex cut, which equals a maximum flow once every station is split in
two. Station v becomes an entry and an exit joined by an arc of
capacity x_v, and each channel becomes two arcs from one station's exit
to the other's entry. The arcs of channels, and the station arcs of S
and F, which cannot be held, have unlimited capacity. The answer is
YES exactly when the maximum flow from S's exit to F's entry is at
most K.

"Unlimited" only needs to exceed K, so it is K + 1, and Dinic's
algorithm stops as soon as the flow passes K. `O(V² E)` in general,
with V = 2N nodes and E arcs, but far less here.

Pitfalls:

- S may equal F, and then no blocking is possible (test 03);
- a channel straight between S and F cannot be blocked either: the
  flow through it exceeds any K (test 04);
- the limit is inclusive: a cut costing exactly K is enough (tests 05,
  06).

The answers were compared with trying every set of stations on 199
random galaxies of up to ten stations, also with K set just at and
just below the cheapest cut.

## Language notes

- All languages run the same Dinic's algorithm with a recursive search
  for augmenting paths.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1277_flow.cpp](1277_flow.cpp) | G++ 13.2 x64 | flow | O(V² E) | AC | 0.015 s | 384 KB |
| [1277_flow.go](1277_flow.go) | Go 1.14 x64 | flow | O(V² E) | AC | 0.031 s | 3860 KB |
| [1277_flow.java](1277_flow.java) | Java 1.8 | flow | O(V² E) | AC | 0.109 s | 804 KB |
| [1277_flow.py](1277_flow.py) | Python 3.12 x64 | flow | O(V² E) | AC | 0.125 s | 2732 KB |
| [1277_flow.rs](1277_flow.rs) | Rust 1.75 x64 | flow | O(V² E) | AC | 0.031 s | 1268 KB |
