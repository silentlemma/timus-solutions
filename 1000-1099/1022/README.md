# 1022. Ordering a family so that ancestors come first

[Timus 1022](https://acm.timus.ru/problem.aspx?space=1&num=1022) · difficulty 142 · graphs, bfs, dfs

Original problem from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` members (`1 ≤ N ≤ 100`), numbered `1..N`, are related by parent-child
links: a member may have any number of parents and children, and there are
no cycles. Print an order of all members in which every member comes before
all of its descendants. Any such order is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines: the `i`-th lists the children of member `i` in any
order and ends with `0` (a line with just `0` means no children).

## Output

The `N` numbers in the chosen order, separated by spaces.

## Checking

Any valid order is accepted. The checker verifies that the output is a
permutation of `1..N` and that every member comes before each of its
children (which gives "before all descendants" by induction).

## Examples

### Example 1

Input:

```
4
0
1 0
1 4 0
1 0
```

Output:

```
2 3 4 1
```

### Example 2

Input:

```
1
0
```

Output:

```
1
```

## Solution

The members and the links form a directed acyclic graph, and the required
order is a **topological order** of it.

**Kahn's algorithm (BFS).** Count the parents of every member. Members
without parents can speak first; put them in a queue. Take members from the
queue one by one; for each of its children decrease the parent count, and a
child whose count drops to zero joins the queue — all its parents have
already spoken. The queue in the order of insertion is the answer.

**Depth-first search.** Run a DFS from every unvisited member and append a
member to a list when its DFS finishes, i.e. after all of its descendants.
The reversed list puts every member before its descendants.

Both are `O(N + E)`, where `E` is the number of links — at most about
5 000 here.

Pitfalls:

- the input lists children, not parents: count in-degrees from the lists;
- a line with just `0` is an empty list, not the end of the input.

## Language notes

- **C++**, **Go**, **Java**: Kahn's algorithm.
- **C++**, **Rust**: recursive DFS (the depth is at most 100); **Python**:
  the same DFS with an explicit stack of iterators.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1022_bfs_graphs.cpp](1022_bfs_graphs.cpp) | G++ 13.2 x64 | bfs, graphs | O(N + E) | AC | 0.015 s | 204 KB |
| [1022_bfs_graphs.go](1022_bfs_graphs.go) | Go 1.14 x64 | bfs, graphs | O(N + E) | AC | 0.015 s | 1124 KB |
| [1022_bfs_graphs.java](1022_bfs_graphs.java) | Java 1.8 | bfs, graphs | O(N + E) | AC | 0.125 s | 1828 KB |
| [1022_dfs_graphs.cpp](1022_dfs_graphs.cpp) | G++ 13.2 x64 | dfs, graphs | O(N + E) | AC | 0.015 s | 196 KB |
| [1022_dfs_graphs.py](1022_dfs_graphs.py) | Python 3.12 x64 | dfs, graphs | O(N + E) | AC | 0.078 s | 512 KB |
| [1022_dfs_graphs.rs](1022_dfs_graphs.rs) | Rust 1.75 x64 | dfs, graphs | O(N + E) | AC | 0.015 s | 236 KB |
