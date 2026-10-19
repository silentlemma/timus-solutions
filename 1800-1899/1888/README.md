# 1888. Pilot Work Experience

[Timus 1888](https://acm.timus.ru/problem.aspx?space=1&num=1888) · difficulty 463 · bfs

Original problem by Magaz Asanov, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n flights had two of p pilots, and the experience of one of
them was exactly one year more than that of the other; nobody knows
which. Every experience is a whole number of years from 1 to 50. Find
the largest possible difference between the most and the least
experienced pilot and experiences that give it, or print −1 if the
data are contradictory.

## Input

n and p (2 ≤ n ≤ 1000, 2 ≤ p ≤ 50), then n flights, each as two
different pilot numbers.

## Output

The largest difference and then the p experiences, or −1. Any valid
experiences are accepted.

## Examples

### Example 1

Input:

```
4 4
1 2
3 1
2 4
3 4
```

Output:

```
2
1 2 2 3
```

### Example 2

Input:

```
3 3
1 2
2 3
1 3
```

Output:

```
-1
```

## Solution

Pilots joined by a flight differ by one, so their experiences have
different parity. A connected group of pilots must therefore be
bipartite; an odd cycle means −1.

Within one group, two pilots at distance k differ by at most k, so the
spread is at most the diameter. It is reached: experience 1 + (distance
from one end of a diameter) changes by exactly one along every flight,
because the distances of neighbours in a bipartite graph differ by
one. With p ≤ 50 the diameter is at most 49, so these values stay
within 1 … 50.

Separate groups can be shifted independently, so with two or more of
them the answer is the full 49: one group alternates 1 and 2 by parity
and the others alternate 49 and 50. BFS from every pilot costs
`O(p·(p + n))`.

In the first example the pilots form the cycle 1–2–4–3 of length four,
whose diameter is 2: from pilot 1 the distances are 0, 1, 1, 2.

Pitfalls:

- several groups give 49 at once, however small they are;
- one group cannot exceed its diameter, even if it is long and thin;
- the same pair may fly several times, which changes nothing.

The answers agree with an independent accepted implementation, and the
experiences pass a checker, on 200 random sets of flights.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1888_bfs.cpp](1888_bfs.cpp) | G++ 13.2 x64 | bfs | O(p (p + n)) | AC | 0.015 s | 204 KB |
| [1888_bfs.go](1888_bfs.go) | Go 1.14 x64 | bfs | O(p (p + n)) | AC | 0.062 s | 1196 KB |
| [1888_bfs.java](1888_bfs.java) | Java 1.8 | bfs | O(p (p + n)) | AC | 0.109 s | 716 KB |
| [1888_bfs.py](1888_bfs.py) | Python 3.12 x64 | bfs | O(p (p + n)) | AC | 0.109 s | 760 KB |
| [1888_bfs.rs](1888_bfs.rs) | Rust 1.75 x64 | bfs | O(p (p + n)) | AC | 0.062 s | 256 KB |
