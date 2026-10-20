# 2175. Number of prefix maxima while elements only grow

[Timus 2175](https://acm.timus.ru/problem.aspx?space=1&num=2175) · difficulty 1140 · fenwick

Original problem by Ignat Nigmatullin, from the Ural School Programming Contest 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The staircase of an array starts with its first element and repeatedly
takes the first later element strictly greater than the last one taken,
so it consists of the strict prefix maxima. Each of Q updates adds a
non-negative amount to one element; print the length of the staircase
after every update. The limits are 2 seconds and 256 MB.

## Input

N, 1 ≤ N ≤ 10⁵, the array, 0 ≤ aᵢ ≤ 10⁹, then Q, 1 ≤ Q ≤ 10⁵, and the
updates p, x with 0 ≤ x ≤ 10⁹.

## Output

The length of the staircase after every update.

## Examples

### Example 1

Input:

```
5
1 2 5 1 7
3
1 3
2 3
4 6
```

Output:

```
3
3
3
```

## Solution

Keep the staircase as a linked list of positions. When aₚ grows:

- If p is not on the staircase, it joins exactly when its new value is
  larger than every earlier element. The largest earlier element, the
  earliest one among equal values, is on the staircase, and p is linked
  in right after it.
- If p is on the staircase now, the following staircase elements that
  are no larger than the new value drop out, one after another, until a
  larger one or the end.

Values only grow, so every removal pays for an earlier insertion, and
there are at most N + Q insertions. The maximum of a prefix comes from
a Fenwick tree of maxima over positions; growing a value updates its
nodes, and the walk up stops at the first node that already holds a
larger value, because all later nodes contain that one too. The work is
O((N + Q) log N).

In the example the first update makes the array 4 2 5 1 7, and the
staircase 4, 5, 7 has three elements.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2175_fenwick.cpp](2175_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((N + Q) log N) | AC | 0.078 s | 1404 KB |
| [2175_fenwick.go](2175_fenwick.go) | Go 1.14 x64 | fenwick | O((N + Q) log N) | AC | 0.046 s | 11164 KB |
| [2175_fenwick.java](2175_fenwick.java) | Java 1.8 | fenwick | O((N + Q) log N) | AC | 0.125 s | 8376 KB |
| [2175_fenwick.py](2175_fenwick.py) | Python 3.12 x64 | fenwick | O((N + Q) log N) | AC | 0.625 s | 36632 KB |
| [2175_fenwick.rs](2175_fenwick.rs) | Rust 1.75 x64 | fenwick | O((N + Q) log N) | AC | 0.031 s | 7376 KB |
