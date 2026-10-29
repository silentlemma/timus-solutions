# 1136. Turning the left-right-root order of a search tree into the right-left-root order

[Timus 1136](https://acm.timus.ru/problem.aspx?space=1&num=1136) · difficulty 100 · trees

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Members of a parliament with distinct positive numbers take their seats
as in a binary search tree: the first one is the chairman, and each next
one goes left if their number is smaller than the current chairman's and
right otherwise, until a free seat is found. In odd sessions members
speak in the order left wing, right wing, chairman, applied recursively;
in even sessions right wing, left wing, chairman. Given the odd-session
order of `N ≤ 3000` members with numbers up to 65535, print the
even-session order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `N` numbers in odd-session order.

## Output

The numbers in even-session order, one per line.

## Examples

### Example 1

Input:

```
9
1
7
5
21
22
27
25
20
10
```

Output:

```
27
21
22
25
20
7
1
5
10
```

## Solution

The odd-session order is the post-order of the search tree: left wing,
right wing, chairman. Read backwards, it names every chairman before all
the members of their wings. So inserting the numbers into an empty binary
search tree in that reversed order puts every member exactly where they
sat: their chairman is already in place when they come. The even-session
order is then a recursive walk: right wing, left wing, chairman.

Each insertion walks down from the root. On a chain of 3000 members that
is up to 3000 steps, about 4.5 million in all: `O(N^2)`, still fast.

Pitfalls:

- the tree can be a chain 3000 deep, and so is the recursion of the walk;
  Python raises its recursion limit;
- numbers may share lines; read them as tokens;
- a single member is both orders.

The answers of both methods were compared on every test and on 300 random
parliaments, which also checked that each input is a valid odd-session
order.

## Optimized solutions

The optimized solutions rebuild the tree in one pass, `O(N)`. Read
backwards, the odd-session order lists each chairman, then the whole right
wing, then the whole left wing. Keep a stack of chairmen whose left wing
may still come:

- if the next number is larger than the top of the stack, it is the right
  child of that top;
- otherwise pop every chairman larger than it; the last one popped is the
  chairman whose left wing it starts, and it becomes that left child.

Every number is pushed once and popped at most once. The even-session order
is the ordinary root, left, right order read backwards, which a second
explicit stack produces without recursion. The children are indexed by
the position in the input; Go also parses the input by hand. C++ needs
188 KB instead of 348 KB and Go 1052 KB instead of 2200 KB, both with
the same time; Python needs 0.078 s instead of 0.500 s and 1028 KB
instead of 1508 KB. Java and Rust have only the simple solutions.

## Language notes

- The simple solutions walk the tree recursively, up to 3000 calls deep:
  no language needs a bigger stack for that, and Python only raises its
  recursion limit.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1136_trees.cpp](1136_trees.cpp) | G++ 13.2 x64 | trees | O(N^2) | AC | 0.015 s | 348 KB | 11303079 |
| [1136_trees.go](1136_trees.go) | Go 1.14 x64 | trees | O(N^2) | AC | 0.031 s | 2200 KB | 11303083 |
| [1136_trees.java](1136_trees.java) | Java 1.8 | trees | O(N^2) | AC | 0.109 s | 640 KB | 11303090 |
| [1136_trees.py](1136_trees.py) | Python 3.12 x64 | trees | O(N^2) | AC | 0.500 s | 1508 KB | 11303091 |
| [1136_trees.rs](1136_trees.rs) | Rust 1.75 x64 | trees | O(N^2) | AC | 0.031 s | 804 KB | 11303094 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1136_trees_optimized.cpp](1136_trees_optimized.cpp) | G++ 13.2 x64 | trees | O(N) | AC | 0.015 s | 188 KB | 11303566 |
| [1136_trees_optimized.go](1136_trees_optimized.go) | Go 1.14 x64 | trees | O(N) | AC | 0.031 s | 1052 KB | 11303567 |
| [1136_trees_optimized.py](1136_trees_optimized.py) | Python 3.12 x64 | trees | O(N) | AC | 0.078 s | 1028 KB | 11303568 |
