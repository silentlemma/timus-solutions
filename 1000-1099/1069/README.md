# 1069. Rebuilding a tree from its Prüfer code

[Timus 1069](https://acm.timus.ru/problem.aspx?space=1&num=1069) · difficulty 517 · trees

Original problem by Magaz Asanov, from the Ural State University Personal Contest Online, February 2001, Students Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree on vertices `1 … N` (`2 ≤ N ≤ 7500`) is encoded like this: take the
leaf with the smallest number, remove it and write down its neighbour;
repeat until one vertex is left (it is always `N`). The `N − 1` written
numbers are the code. Given the code, print the adjacency list of every
vertex.

Time limit: 0.25 seconds. Memory limit: 8 MB.

## Input

The code: `N − 1` numbers separated by spaces and line breaks.

## Output

For each vertex in increasing order, a line `v: a b c …` with its
neighbours in increasing order.

## Checking

The output is compared line by line; within a line, token by token.

## Examples

### Example 1

Input:

```
2 1 6 2 6
```

Output:

```
1: 4 6
2: 3 5 6
3: 2
4: 1
5: 2
6: 1 2
```

## Solution

During the encoding a vertex is written once for every neighbour removed
before it, and it becomes a leaf when only one neighbour is left. So a
vertex `v` has degree `1 + (the number of times v occurs in the code)`,
and at every step the current leaves are exactly the vertices that are not
removed yet and no longer occur in the rest of the code.

The decoder follows the encoding step by step. Start with the degrees
above and a min-heap of the vertices of degree 1. For each number `c` of
the code, the smallest leaf is the vertex that was removed: join it to `c`
and decrease the degree of `c`; when it drops to 1, `c` has become a leaf
and goes into the heap. Then sort every adjacency list. `O(N log N)`.

Pitfalls:

- this code has `N − 1` numbers and ends with `N`, one more than the usual
  Prüfer code, so `N` is the count of numbers plus one;
- vertex `N` never leaves the heap too early: a tree always has at least
  two leaves, so a smaller one is always there;
- the numbers may be spread over lines in any way, so they are read as
  tokens;
- the limits are tight (0.25 seconds and 8 MB), so the output is built in
  one buffer and the lists are kept compact.

The answers were checked the other way round: the printed tree, encoded
again by the definition, gives back the input.

## Language notes

- C++ makes `std::priority_queue` a min-heap with `std::greater`; Rust
  does the same with `Reverse` in a `BinaryHeap`.
- Go uses `container/heap` with a small `[]int` type.
- Java keeps every adjacency list in an `int` array sized by the degree,
  and the leaves in a `PriorityQueue`.
- Python uses `heapq`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1069_trees.cpp](1069_trees.cpp) | G++ 13.2 x64 | trees | O(N log N) | AC | 0.015 s | 420 KB |
| [1069_trees.go](1069_trees.go) | Go 1.14 x64 | trees | O(N log N) | AC | 0.031 s | 2564 KB |
| [1069_trees.java](1069_trees.java) | Java 1.8 | trees | O(N log N) | AC | 0.125 s | 1972 KB |
| [1069_trees.py](1069_trees.py) | Python 3.12 x64 | trees | O(N log N) | AC | 0.109 s | 3176 KB |
| [1069_trees.rs](1069_trees.rs) | Rust 1.75 x64 | trees | O(N log N) | AC | 0.062 s | 1188 KB |
