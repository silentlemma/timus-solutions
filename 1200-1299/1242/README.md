# 1242. Suspects for a werewolf in a village of relatives

[Timus 1242](https://acm.timus.ru/problem.aspx?space=1&num=1242) · difficulty 177 · graphs

Original problem by Leonid Volkov, from the Ural State University Personal Contest, March 1, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A village has N people (1 < N ≤ 1000), and for some of them it is known
who their parents are (at most two each, no cycles). A werewolf lives
among them, and it never attacks its own ancestors or descendants. Given
the list of its victims, print everyone who may be the werewolf, in
increasing order, or 0 if nobody can.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then lines `child parent`, then the word `BLOOD` and the victims, one
per line.

## Output

The possible werewolves in increasing order, or 0.

## Examples

### Example 1

Input:

```
8
1 3
3 6
4 5
6 2
4 6
8 1
BLOOD
3
8
```

Output:

```
4 5 7
```

### Example 2

Input:

```
6
1 2
3 2
1 4
3 4
2 6
5 2
5 4
BLOOD
2
5
```

Output:

```
0
```

## Solution

Someone is cleared by a single victim: the victim itself, any ancestor of
a victim (the victim would be the werewolf's descendant) and any
descendant of a victim (the victim would be its ancestor). Everyone else
is consistent with every attack.

So walk up the parent links from all victims at once and mark everyone
reached, then walk down the child links the same way; whoever is left
unmarked is a suspect. Each walk visits every person and link at most
once. `O(N + links)`.

Pitfalls:

- relatives that are neither ancestors nor descendants, like cousins or
  siblings, stay suspects (test 05);
- the list of victims may be empty, and then everyone is a suspect;
- one long line of 1000 generations needs an explicit stack rather than
  deep recursion.

## Language notes

- Python and Rust read the whole input and split it at the word `BLOOD`;
  C++, Go and Java read word by word until it.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1242_graphs.cpp](1242_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + links) | AC | 0.015 s | 232 KB |
| [1242_graphs.go](1242_graphs.go) | Go 1.14 x64 | graphs | O(N + links) | AC | 0.015 s | 1120 KB |
| [1242_graphs.java](1242_graphs.java) | Java 1.8 | graphs | O(N + links) | AC | 0.093 s | 1100 KB |
| [1242_graphs.py](1242_graphs.py) | Python 3.12 x64 | graphs | O(N + links) | AC | 0.078 s | 912 KB |
| [1242_graphs.rs](1242_graphs.rs) | Rust 1.75 x64 | graphs | O(N + links) | AC | 0.031 s | 312 KB |
