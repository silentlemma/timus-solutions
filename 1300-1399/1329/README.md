# 1329. Galactic History

[Timus 1329](https://acm.timus.ru/problem.aspx?space=1&num=1329) · difficulty 453 · dfs

Original problem by Evgeny Krokhalev, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Up to 40 000 milestones of history form a rooted tree; each has a
number from 0 to 40 000 and the number of its parent, −1 for the root.
Answer up to 40 000 questions about two different milestones A and B:
1 if A is an ancestor of B, 2 if B is an ancestor of A, and 0 otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines with a milestone and its parent, then L and L lines
with A and B.

## Output

One answer per line.

## Examples

### Example 1

Input:

```
10
234 -1
12 234
13 234
14 234
15 234
16 234
17 234
18 234
19 234
233 19
5
234 233
233 12
233 13
233 15
233 19
```

Output:

```
1
0
0
0
2
```

## Solution

Walk the tree depth first and stamp each milestone with the time it is
entered and the time its whole subtree is left. A is an ancestor of B
exactly when B is entered while A is still open:
enter[A] ≤ enter[B] < leave[A]. Each question then takes at most two
interval checks. `O(N + L)`.

The walk uses an explicit stack. After a milestone is popped, its
complement ~v is pushed before its children to mark the moment
its subtree is done. This matters because the tree can be a chain of
40 000 milestones, too deep for recursion in some languages.

Pitfalls:

- the milestones come in any order, children before their parents
  (test 03);
- milestone 0 exists, so the leave marker cannot be −v; ~v = −v − 1
  works for 0 as well (test 03);
- a chain of 40 000 (test gen2);
- siblings and cousins are not ancestors of each other (test 05).

The answers were compared with walking up the parents on 300 random
trees of up to 12 milestones.

## Language notes

- Java reads the input through its own byte buffer, since a buffered
  stream that is locked on every byte is noticeably slower here.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1329_dfs.cpp](1329_dfs.cpp) | G++ 13.2 x64 | dfs | O(N + L) | AC | 0.078 s | 2064 KB |
| [1329_dfs.go](1329_dfs.go) | Go 1.14 x64 | dfs | O(N + L) | AC | 0.031 s | 5948 KB |
| [1329_dfs.java](1329_dfs.java) | Java 1.8 | dfs | O(N + L) | AC | 0.140 s | 2420 KB |
| [1329_dfs.py](1329_dfs.py) | Python 3.12 x64 | dfs | O(N + L) | AC | 0.156 s | 17292 KB |
| [1329_dfs.rs](1329_dfs.rs) | Rust 1.75 x64 | dfs | O(N + L) | AC | 0.046 s | 5376 KB |
