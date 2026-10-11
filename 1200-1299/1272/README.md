# 1272. Non-Yekaterinburg subway

[Timus 1272](https://acm.timus.ru/problem.aspx?space=1&num=1272) · difficulty 147 · dsu

Original problem by Magaz Asanov (prepared by Igor Goldberg), from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A town stands on N ≤ 10 000 islands joined by K ≤ 12 000 tunnels and
M ≤ 12 000 bridges, and all of them together connect every island. A
subway must connect all islands using some of these links, with as few
bridges as possible. How many bridges does it need?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, K and M, then K tunnels and M bridges, each as two island numbers.

## Output

The least number of bridges.

## Examples

### Example 1

Input:

```
6 3 4
1 2
2 3
4 5
1 3
3 4
4 6
5 6
```

Output:

```
2
```

## Solution

Tunnels cost nothing, so take all of them: they split the islands into
groups that are already connected. Each bridge can join at most two
groups into one, and since the whole network is connected, bridges can
always be chosen to join the groups one by one. So the answer is the
number of tunnel groups minus one, counted with a union–find structure
over the tunnels; the bridges themselves need not even be read.
`O((N + K) α(N))`.

Pitfalls:

- the bridges do not matter, only that they connect the groups, which
  the statement promises;
- tunnels may repeat or join an island to itself (test 05);
- with one island, or tunnels alone connecting everything, the answer
  is 0 (tests 02, 04).

## Language notes

- All languages use the same union–find with path halving.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1272_dsu.cpp](1272_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + K) α(N)) | AC | 0.031 s | 228 KB |
| [1272_dsu.go](1272_dsu.go) | Go 1.14 x64 | dsu | O((N + K) α(N)) | AC | 0.015 s | 1428 KB |
| [1272_dsu.java](1272_dsu.java) | Java 1.8 | dsu | O((N + K) α(N)) | AC | 0.140 s | 488 KB |
| [1272_dsu.py](1272_dsu.py) | Python 3.12 x64 | dsu | O((N + K) α(N)) | AC | 0.093 s | 3328 KB |
| [1272_dsu.rs](1272_dsu.rs) | Rust 1.75 x64 | dsu | O((N + K) α(N)) | AC | 0.046 s | 732 KB |
