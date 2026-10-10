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

The odd-session order is the post-order of the search tree, and a
post-order of a binary search tree with distinct keys determines the tree.
Read backwards, it lists each chairman, then the whole right wing, then
the whole left wing. Rebuild the tree in one pass over that reversed list
with a stack of chairmen whose left wing may still come:

- if the next number is larger than the top of the stack, it is the right
  child of that top;
- otherwise pop every chairman larger than it; the last one popped is the
  chairman whose left wing it starts, and it becomes that left child.

Every number is pushed once and popped at most once, so this is `O(N)`.
The even-session order is the ordinary root, left, right order read
backwards, which an explicit stack produces without recursion.

Pitfalls:

- the tree can be a chain 3000 deep, so recursion is avoided;
- numbers may share lines; read them as tokens;
- a single member is both orders.

The answers were compared on every test and on 300 random parliaments
with a rebuild by plain insertion and recursive walks, which also checked
that each input is a valid odd-session order.

## Language notes

- All languages use the same two stacks, with arrays indexed by the
  member number for the children.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1136_trees.cpp](1136_trees.cpp) | G++ 13.2 x64 | trees | O(N) | AC | 0.015 s | 776 KB |
| [1136_trees.go](1136_trees.go) | Go 1.14 x64 | trees | O(N) | AC | 0.046 s | 2396 KB |
| [1136_trees.java](1136_trees.java) | Java 1.8 | trees | O(N) | AC | 0.093 s | 1524 KB |
| [1136_trees.py](1136_trees.py) | Python 3.12 x64 | trees | O(N) | AC | 0.078 s | 1336 KB |
| [1136_trees.rs](1136_trees.rs) | Rust 1.75 x64 | trees | O(N) | AC | 0.046 s | 1296 KB |
