# 1085. The cheapest tram stop for a group of friends to meet

[Timus 1085](https://acm.timus.ru/problem.aspx?space=1&num=1085) · difficulty 625 · bfs, graphs

Original problem by Alexander Somov, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city has `N` stops and `M` tram routes (`1 ≤ N, M ≤ 100`), each a list
of 2 to 100 stops. A ticket costs 4 and is good for one ride along one
route; every change of route needs a new ticket. Each of `K` friends
(`1 ≤ K ≤ 100`) starts at some stop with at most 1000 in money, and some
have a pass that makes every ride free. Find the stop where all friends
can meet, each paying for their own trip, with the smallest total cost
(the smallest such stop on ties), and print it with the cost, or `0` if
there is no such stop.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N` and `M`; `M` lines with the length of a route and its stops; `K`;
`K` lines with a friend's money, starting stop and 1 for a pass or 0.

## Output

The stop and the total cost, or `0`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4 3
2 1 2
2 2 3
2 3 4
3
27 1 0
15 4 0
45 4 0
```

Output:

```
4 12
```

## Solution

A trip costs 4 times the number of rides, and one ride covers any part of
a route, so what matters is the fewest rides from the start to each stop.
A breadth-first search finds it: from a stop, every route through it that
has not been used yet is opened once, and all its unreached stops get one
ride more. Each route is opened at most once, so one search takes
`O(N + ΣL)`.

Run the search from every friend's stop. For each stop `t`, a friend
without a pass pays `4 · rides`, which must not exceed their money; a
friend with a pass pays nothing but still needs `t` to be reachable. Sum
the costs over the friends, mark the stops that someone cannot reach or
afford, and take the cheapest remaining stop with the smallest number.
`O(K · (N + ΣL))`.

Pitfalls:

- a pass makes the trip free but does not make an unreachable stop
  reachable;
- the friend's own stop costs nothing even if no route passes through it;
- a friend may have less money than one ticket, and then only their own
  stop is possible.

The answers were checked against Floyd–Warshall on the graph of stops
where two stops on a common route are one ride apart.

## Language notes

- All five languages keep for each stop the list of routes through it and
  mark the routes already opened in each search.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1085_bfs.cpp](1085_bfs.cpp) | G++ 13.2 x64 | bfs | O(K · (N + ΣL)) | AC | 0.015 s | 220 KB |
| [1085_bfs.go](1085_bfs.go) | Go 1.14 x64 | bfs | O(K · (N + ΣL)) | AC | 0.031 s | 1384 KB |
| [1085_bfs.java](1085_bfs.java) | Java 1.8 | bfs | O(K · (N + ΣL)) | AC | 0.109 s | 1020 KB |
| [1085_bfs.py](1085_bfs.py) | Python 3.12 x64 | bfs | O(K · (N + ΣL)) | AC | 0.078 s | 756 KB |
| [1085_bfs.rs](1085_bfs.rs) | Rust 1.75 x64 | bfs | O(K · (N + ΣL)) | AC | 0.015 s | 244 KB |
