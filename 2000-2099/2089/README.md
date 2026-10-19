# 2089. Pick winners so that no team wins twice

[Timus 2089](https://acm.timus.ru/problem.aspx?space=1&num=2089) · difficulty 949 · graphs, greedy

Original problem by Alexander Ipatov, prepared by Egor Shchelkonogov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

k teams play n pairs; each team plays from one to three pairs. Choose
the winner of every pair, one of its two teams, so that no team wins
two pairs, or report that it is impossible. Any valid choice is
accepted. The limits are 2 seconds and 256 MB.

## Input

n and k, 1 ≤ n ≤ 10⁵, 2 ≤ k ≤ 10⁵, then the n pairs.

## Output

`Yes` and the winners of the pairs in order, or `No`.

## Checking

A checker accepts `No` only when the expected output says so, and
otherwise checks that every winner plays in its pair and wins once.

## Examples

### Example 1

Input:

```
3 4
1 2
2 3
1 4
```

Output:

```
Yes
1
2
4
```

### Example 2

Input:

```
6 4
1 2
1 3
1 4
2 3
2 4
3 4
```

Output:

```
No
```

## Solution

Teams are vertices and pairs are edges; choosing winners means pointing
every edge at one of its ends so that every vertex gets at most one
edge. A connected part with more edges than vertices cannot be done,
and a part with at most as many can: a tree, or a tree plus one edge,
which has exactly one cycle.

The construction peels leaves. A team with a single undecided pair wins
it; that can never hurt, since the team has no other use, and the
pair's other team loses one undecided pair, possibly becoming a leaf in
turn. When no leaf is left, every remaining team has zero or at least
two undecided pairs. If some team still has three, its part has too
many edges, and the answer is No. Otherwise the remaining pairs form
disjoint cycles, and walking each cycle gives every pair to the team it
leads to, so each team on a cycle wins exactly one. With degrees at
most three everything is O(n + k).

In the second example four teams play six pairs, more than they can
win, so the answer is No.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2089_graphs_greedy.cpp](2089_graphs_greedy.cpp) | G++ 13.2 x64 | graphs, greedy | O(n + k) | AC | 0.234 s | 6492 KB |
| [2089_graphs_greedy.go](2089_graphs_greedy.go) | Go 1.14 x64 | graphs, greedy | O(n + k) | AC | 0.109 s | 13268 KB |
| [2089_graphs_greedy.java](2089_graphs_greedy.java) | Java 1.8 | graphs, greedy | O(n + k) | AC | 0.250 s | 20632 KB |
| [2089_graphs_greedy.py](2089_graphs_greedy.py) | Python 3.12 x64 | graphs, greedy | O(n + k) | AC | 0.578 s | 51484 KB |
| [2089_graphs_greedy.rs](2089_graphs_greedy.rs) | Rust 1.75 x64 | graphs, greedy | O(n + k) | AC | 0.093 s | 13104 KB |
