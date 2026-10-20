# 2147. Cheapest one-way and two-way roads for all visiting requests

[Timus 2147](https://acm.timus.ru/problem.aspx?space=1&num=2147) · difficulty 1890 · graphs

Original problem by Valentin Zuev, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n houses and m requests "a wants a path to b". A one-way road
costs x and a two-way road costs y. Build roads of minimum total cost so
that every request has a directed path. The limits are 3 seconds and
256 MB.

## Input

n, m, x and y, 2 ≤ n ≤ 10⁵, 1 ≤ m ≤ 10⁵, 1 ≤ x, y ≤ 10⁹, then the m
distinct requests.

## Output

The minimum cost.

## Examples

### Example 1

Input:

```
4 3 2 3
1 2
1 3
2 3
```

Output:

```
4
```

### Example 2

Input:

```
4 3 2 3
1 2
1 3
2 1
```

Output:

```
5
```

### Example 3

Input:

```
4 4 2 3
1 2
2 1
1 3
3 1
```

Output:

```
6
```

## Solution

Requests in different weakly connected components of the request graph
never interact, so each component is solved alone. Let it have V houses
and C strongly connected components (SCCs).

If y ≤ x, a spanning tree of two-way roads, (V − 1) · y, serves every
request, and no cheaper set connects V houses at all.

If x < y there are two candidates. One directed cycle through all V
houses, V · x, serves everything. Otherwise every SCC of size s needs a
strongly connected set of roads, and a two-way tree for (s − 1) · y
does it; the SCCs themselves form a DAG, and one-way roads along a
topological order of the SCCs, (C − 1) · x, give every request between
them. That is (V − C) · y + (C − 1) · x. Mixing the two, a cycle for
some SCCs and trees for others, never beats both: once one SCC uses a
cycle, every tree SCC of size s together with its connecting one-way
road costs (s − 1) · y + x > s · x, which is what its houses cost inside
one big cycle. So the answer for the
component is the cheaper candidate.

The SCCs come from Kosaraju's algorithm with iterative searches, and
the weak components from one more search over both directions, in
O(n + m). The sums need 64-bit integers.

In the second example 1 and 2 form an SCC: a two-way road (3) plus a
one-way road to 3 (2) cost 5, while a cycle through 1, 2 and 3 would
cost 6.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2147_graphs.cpp](2147_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + m) | AC | 0.093 s | 9164 KB |
| [2147_graphs.go](2147_graphs.go) | Go 1.14 x64 | graphs | O(n + m) | AC | 0.093 s | 17760 KB |
| [2147_graphs.java](2147_graphs.java) | Java 1.8 | graphs | O(n + m) | AC | 0.140 s | 8460 KB |
| [2147_graphs.py](2147_graphs.py) | Python 3.12 x64 | graphs | O(n + m) | AC | 0.687 s | 39596 KB |
| [2147_graphs.rs](2147_graphs.rs) | Rust 1.75 x64 | graphs | O(n + m) | AC | 0.093 s | 19712 KB |
