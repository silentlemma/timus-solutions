# 1198. Which senators can pass a law on their own

[Timus 1198](https://acm.timus.ru/problem.aspx?space=1&num=1198) · difficulty 488 · graphs

Original problem by Nikita Rybak.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of `N ≤ 2000` senators keeps compromising files on some of the
others. A senator who wants a law calls everyone they hold files on and
asks them to support it and to make the same calls in turn. A law passes
when every senator supports it. Find all senators who can get a law
passed this way on their own.

Time limit: 1.5 seconds. Memory limit: 96 MB.

## Input

`N`, then one line per senator listing the senators they hold files on,
ended by `0`.

## Output

The numbers of those senators in increasing order on one line, followed
by `0`; just `0` when there are none.

## Examples

### Example 1

Input:

```
5
3 2 0
0
4 5 0
1 5 0
2 0
```

Output:

```
1 3 4 0
```

## Solution

Draw an edge from each senator to everyone they hold files on; the
answer is the set of vertices from which every vertex is reachable.

Search the graph from every vertex not reached yet, each search marking
only unmarked vertices. Nothing marked earlier can reach the root of a
later search, since a search would have marked it, so the root of the
last search lies in a strongly connected component that no other
component reaches. If that root does not reach everyone, nobody does,
because anyone who reaches everyone reaches the root and therefore lies
in its component. If it does, the answer is exactly the vertices that
reach the root, found by one more search along reversed edges.
`O(N + M)` for `M` files, up to about `4·10⁶`.

Pitfalls:

- the input can be close to 20 MB, so slow reading costs more than the
  graph work;
- adjacency lists of `4·10⁶` entries must be stored compactly, as 32-bit
  numbers in flat arrays, to stay well under the memory limit;
- a senator may appear in their own list or twice in one list;
- when nobody qualifies, the output is a single `0`.

The answers were compared with a separately written solution, based on
the transitive closure with bit sets, on 300 small random graphs and on
every test.

## Language notes

- C++, Go, Java and Rust store both graphs as flat arrays with offsets,
  building the reverse one by counting.
- Python stores each senator's list as a big integer with one byte per
  senator, filled through a `bytearray`, so all per-file work stays in
  built-in functions; the searches then cost a few whole-set operations
  per senator, and the reverse graph comes from `zip` over the rows. It
  reads the whole input at once, which is much faster here than reading
  line by line.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1198_graphs.cpp](1198_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.140 s | 32064 KB |
| [1198_graphs.go](1198_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.296 s | 50472 KB |
| [1198_graphs.java](1198_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.250 s | 37092 KB |
| [1198_graphs.py](1198_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 1.281 s | 36148 KB |
| [1198_graphs.rs](1198_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.281 s | 64220 KB |
