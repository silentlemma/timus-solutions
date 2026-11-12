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

## Optimized solutions

The new C++, Go and Rust sources keep DFS entry/exit intervals but store five 16-bit fields per possible milestone: parent, first child, next sibling, entry and exit. IDs are at most 40000 and the clock at most 40000, so 65535 is a distinct sentinel even for milestone zero. The table has U=40001 entries and 400010 bytes of fields. On entering a vertex, descend to its first child; after finishing a subtree, use a sibling or climb the stored parents until a sibling exists. Each edge is traversed at most twice, without recursion or an event stack. Read all edges before walking, so children may precede parents. Initializing the indexed table costs O(U); traversal and queries cost O(N+L). C++ uses bounded C stdio input, Go bounded standard-handle buffers; Rust additionally retains the input text. All five simple files remain; Java/Python reuse their admitted bases.

The accepted Rust 1.75 x64 run takes 0.062 s versus 0.046 s for the base and uses 2 116 KB versus 5376 KB.

The accepted base implementations [1329_dfs.java](1329_dfs.java), [1329_dfs.py](1329_dfs.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- Java reads the input through its own byte buffer, since a buffered
  stream that is locked on every byte is noticeably slower here.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1329_dfs.cpp](1329_dfs.cpp) | G++ 13.2 x64 | dfs | O(N + L) | AC | 0.078 s | 2064 KB | 11284994 |
| [1329_dfs.go](1329_dfs.go) | Go 1.14 x64 | dfs | O(N + L) | AC | 0.031 s | 5948 KB | 11284995 |
| [1329_dfs.java](1329_dfs.java) | Java 1.8 | dfs | O(N + L) | AC | 0.140 s | 2420 KB | 11284997 |
| [1329_dfs.py](1329_dfs.py) \* | Python 3.12 x64 | dfs | O(N + L) | AC | 0.156 s | 17292 KB | 11284996 |
| [1329_dfs.rs](1329_dfs.rs) | Rust 1.75 x64 | dfs | O(N + L) | AC | 0.046 s | 5376 KB | 11284998 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1329_dfs_optimized.cpp](1329_dfs_optimized.cpp) | G++ 13.2 x64 | dfs | O(U + N + L) | AC | 0.015 s | 468 KB | 11315161 |
| [1329_dfs_optimized.go](1329_dfs_optimized.go) \* | Go 1.14 x64 | dfs | O(U + N + L) | AC | 0.031 s | 692 KB | 11315171 |
| [1329_dfs_optimized.rs](1329_dfs_optimized.rs) \* | Rust 1.75 x64 | dfs | O(U + N + L) | AC | 0.062 s | 2116 KB | 11315177 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
