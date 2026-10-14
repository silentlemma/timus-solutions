# 1505. Oil Transfer

[Timus 1505](https://acm.timus.ru/problem.aspx?space=1&num=1505) · difficulty 2801 · graphs

Original problem by Magaz Asanov and Evgeny Krokhalev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N pumping stations (1 ≤ N ≤ 10000) are joined by at most 100000 one-way
pipes. A pipe from i to a has a capacity b, a current flow c
(0 ≤ c ≤ b ≤ 10000) and a price d (0 ≤ d ≤ 10⁶) for each extra unit of
capacity. Oil leaves the network only at station N, which has no
outgoing pipes. Every other station gets no more oil than it sends;
where it gets less, a well nearby can produce one more unit. Raise the
flow into station N by one unit as cheaply as possible and print the
cost and the new flows, or "Impossible".

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then one line per station: its pipes as quadruples a b c d separated
by commas, ending with a dot; a station without pipes has a lone dot.

## Output

The minimal cost, then one line per station with its pipes as pairs
"a flow" separated by commas, ending with a dot; or "Impossible". Any
cheapest change is accepted.

## Examples

### Example 1

Input:

```
4
2 1 1 1, 3 1 1 3.
3 1 0 2, 4 1 1 2.
4 1 1 1.
.
```

Output:

```
2
2 2, 3 1.
3 1, 4 1.
4 2.
.
```

## Solution

One extra unit travels along a path from a station with a well to
station N in the residual network. Along a pipe i → a it can go
forward for free when the pipe has spare capacity and for d when the
pipe is full, since the capacity then grows by one. It can also go
backward, from a to i, for free whenever the pipe carries flow: sending
one unit less from i frees it at i. All prices are non-negative, so
Dijkstra's algorithm from all the well stations at once finds the
cheapest path; then walk back from N and change the flow of each pipe
on it by one. `O((N + M) log N)` for M pipes.

If any well exists, its surplus has to reach N along pipes with flow,
which is a path, so the answer is "Impossible" exactly when no
station has a well.

Pitfalls:

- flow that only goes round a cycle makes no well, so there is no
  answer (test 03);
- the cheapest route can push back the flow of a pipe (test 04);
- a full pipe with d = 0 costs nothing to enlarge (test 05);
- the cost can reach 9999 · 10⁶ = 9999000000, beyond 32 bits (gen5);
- a station's pipes end with a dot, so the input is easiest to read
  by its punctuation rather than by lines (all tests);
- many changes can be cheapest, so the tests use a checker (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1505_graphs.cpp](1505_graphs.cpp) | G++ 13.2 x64 | graphs | O((N + M) log N) | AC | 0.437 s | 11176 KB |
| [1505_graphs.go](1505_graphs.go) | Go 1.14 x64 | graphs | O((N + M) log N) | AC | 0.062 s | 22972 KB |
| [1505_graphs.java](1505_graphs.java) | Java 1.8 | graphs | O((N + M) log N) | AC | 0.218 s | 21788 KB |
| [1505_graphs.py](1505_graphs.py) | Python 3.12 x64 | graphs | O((N + M) log N) | AC | 0.500 s | 43480 KB |
| [1505_graphs.rs](1505_graphs.rs) | Rust 1.75 x64 | graphs | O((N + M) log N) | AC | 0.062 s | 14332 KB |
