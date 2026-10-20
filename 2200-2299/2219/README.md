# 2219. Fewest cups whose walk lengths add up to reach each room

[Timus 2219](https://acm.timus.ru/problem.aspx?space=1&num=2219) · difficulty 1468 · bfs, greedy

Original problem by Ivan Moskovchenko, from the ICPC Ural Regional Contest qualifier 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected simple graph has N rooms and M corridors. Cup i lets a
walker take exactly aᵢ corridors, revisits allowed. For every room v,
find the fewest cups whose lengths sum to the length of some walk from
room 1 to v, or −1. The limits are 2.5 seconds and 256 MB.

## Input

N, M and K, 2 ≤ N ≤ 10⁵, N − 1 ≤ M ≤ 2 · 10⁵, 1 ≤ K ≤ 10⁵, then the
corridors, then a₁ … a_K with 1 ≤ aᵢ ≤ 10⁹.

## Output

The answers for rooms 1 … N.

## Examples

### Example 1

Input:

```
5 4 4
1 2
2 3
3 4
4 5
1 2 3 4
```

Output:

```
0 1 1 1 1
```

### Example 2

Input:

```
5 4 2
1 2
2 3
3 4
4 5
1 2
```

Output:

```
0 1 1 2 -1
```

### Example 3

Input:

```
2 1 1
1 2
999
```

Output:

```
0 1
```

## Solution

A walk can always be stretched by 2 by stepping back and forth, so a
walk of length L from 1 to v exists exactly when L is at least the
shortest walk to v with the same parity as L. Those two shortest walks
per room come from one breadth-first search over (room, parity) states.

So for each count x and each parity p, it is enough to know the largest
sum of x cups with parity p. With the cups sorted in decreasing order,
the largest sum overall is the top x, and the best sum of the other
parity swaps one cup: remove the smallest chosen cup of some parity and
add the largest unchosen cup of the other parity, trying both choices.
This is the standard exchange argument for a parity constraint on a
largest sum.

Going through x = 1, 2, …, two pointers per parity record, for every
length L below 2N, the first count whose best sum of L's parity reaches
L. A room then takes the smaller count over its two parity distances,
and room 1 needs no cups.

In the second example room 5 is 4 corridors away, while the cups give
at most 1 + 2 = 3, so the answer is −1.

The search takes O(N + M), and the cups O(K log K) for sorting.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2219_bfs_greedy.cpp](2219_bfs_greedy.cpp) | G++ 13.2 x64 | bfs, greedy | O(N + M + K log K) | AC | 0.187 s | 11000 KB |
| [2219_bfs_greedy.go](2219_bfs_greedy.go) | Go 1.14 x64 | bfs, greedy | O(N + M + K log K) | AC | 0.156 s | 21080 KB |
| [2219_bfs_greedy.java](2219_bfs_greedy.java) | Java 1.8 | bfs, greedy | O(N + M + K log K) | AC | 0.265 s | 10852 KB |
| [2219_bfs_greedy.py](2219_bfs_greedy.py) | Python 3.12 x64 | bfs, greedy | O(N + M + K log K) | AC | 1.234 s | 57712 KB |
| [2219_bfs_greedy.rs](2219_bfs_greedy.rs) | Rust 1.75 x64 | bfs, greedy | O(N + M + K log K) | AC | 0.062 s | 15152 KB |
