# 1211. Accusations without a ring and with one confession

[Timus 1211](https://acm.timus.ru/problem.aspx?space=1&num=1211) · difficulty 310 · graphs

Original problem by Leonid Volkov, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of `N ≤ 25000` children either confesses to breaking the cup (written
as 0) or names another child as the culprit. The statements look
consistent if exactly one child confessed and no group of children accuse
each other around a ring. Answer `YES` or `NO` for each of up to 16
tests.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`T`, then for each test `N` and the `N` statements.

## Output

`YES` or `NO` for each test, one per line.

## Examples

### Example 1

Input:

```
4
4
2 0 2 2
4
2 0 2 1
5
2 3 4 1 3
3
0 3 2
```

Output:

```
YES
YES
NO
NO
```

## Solution

Every child except a confessor points at exactly one other child, so the
statements form a graph where each vertex has at most one outgoing edge.
With exactly one confession, there is no ring exactly when following the
accusations from any child always ends at the confessor.

Walk from every child in turn, marking the children on the current walk.
The walk stops at the confessor or at a child already known to lead
there; then every child on the walk leads there too. If it instead runs
into a child marked on the current walk, the accusations go round in a
ring. Each child is walked over once. `O(N)` per test.

Pitfalls:

- a child naming themselves is a ring of one;
- no confession, or two, already means `NO`;
- chains can be 25000 long, so the walk is a loop rather than a recursion.

The answers were compared with a separately written solution on 200
files of 16 random tests of every kind.

## Language notes

- All languages walk the chains iteratively with the same three states.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1211_graphs.cpp](1211_graphs.cpp) | G++ 13.2 x64 | graphs | O(N) per test | AC | 0.265 s | 592 KB |
| [1211_graphs.go](1211_graphs.go) | Go 1.14 x64 | graphs | O(N) per test | AC | 0.218 s | 6820 KB |
| [1211_graphs.java](1211_graphs.java) | Java 1.8 | graphs | O(N) per test | AC | 0.156 s | 5760 KB |
| [1211_graphs.py](1211_graphs.py) | Python 3.12 x64 | graphs | O(N) per test | AC | 0.343 s | 26364 KB |
| [1211_graphs.rs](1211_graphs.rs) | Rust 1.75 x64 | graphs | O(N) per test | AC | 0.031 s | 5212 KB |
