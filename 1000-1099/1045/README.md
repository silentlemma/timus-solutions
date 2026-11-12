# 1045. A token game on a tree with burned vertices

[Timus 1045](https://acm.timus.ru/problem.aspx?space=1&num=1045) · difficulty 523 · games, trees

Original problem by Dmitry Filimonenkov, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree has `n` vertices (`n ≤ 1000`, every vertex has at most 20
neighbours). A token starts at vertex `k`. Two players move in turn: a
move takes the token along an edge to a neighbour, and the vertex it left
is destroyed for good. The player who cannot move loses. Determine who
wins with perfect play; if the first player wins, give the winning first
move, the smallest such vertex if there are several.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` and `k`, then `n − 1` lines with the edges.

## Output

`First player wins flying to airport L` with the vertex `L` of the first
move, or `First player loses`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4 3
3 2
3 1
1 4
```

Output:

```
First player wins flying to airport 2
```

### Example 2

Input:

```
3 1
1 2
2 3
```

Output:

```
First player loses
```

## Solution

All destroyed vertices lie on the path from `k` to the token, so the only
neighbour the token cannot go to is the one it came from. Every game is a
walk down the tree rooted at `k`, and the position depends only on the
current vertex.

So it is the classic win/lose evaluation: a vertex is winning for the
player to move when at least one child is losing; a leaf is losing. The
first player wins if `k` has a losing child, and the answer is the
smallest such child.

The tree can be a path of 1000 vertices, so the solutions avoid deep
recursion: a breadth-first order from `k` lists parents before children,
and going through it backwards marks a parent as winning as soon as a
losing child is found. `O(n)`.

Pitfalls:

- the smallest winning move is wanted, not the first one in the input;
- `n = 1`: no edges and no move, the first player loses;
- the first player wins only by moving to a *losing* child; a child that
  is winning for the next player is a bad move.

The teaching C++ version follows the recurrence directly with depth-first search. The previous airport is the only destroyed neighbor in a tree. A call returns true as soon as it finds a child that is losing for the next player. If no such child exists, the position is losing. From the start, keep the smallest move that leaves a losing position. The searched subtrees are disjoint, so the time is O(n). The call stack follows one path and has depth at most n ≤ 1000.

## Optimized solutions

Go keeps the same winning/losing tree DP but removes non-root leaves instead of building adjacency lists and a parent/order traversal. Store only the XOR of remaining neighbour IDs, an 8-bit degree and a winning flag per vertex. A 16-bit FIFO holds each removed vertex once. At degree one, XOR is exactly the remaining parent. Removing a losing child makes its parent winning; XOR the child out and decrement the parent degree, queuing it when it becomes a non-root leaf. The root is never queued, and every other vertex is processed after its rooted children. When the remaining parent is the initial airport, track the smallest losing child ID, preserving the required tie break. A singleton correctly loses. IDs≤1000 fit 16 bits and degree≤20 fits 8 bits. Static arrays and direct standard handles keep the runtime storage small. A fixed byte buffer formats the short answer. Time O(n), storage O(n). All simple programs remain; the other four families reuse admitted bases.

The accepted Go 1.14 x64 run takes 0.062 s versus 0.031 s for the base and uses 348 KB versus 1216 KB.

The accepted base implementations [1045_games.cpp](1045_games.cpp), [1045_games.java](1045_games.java), [1045_games.py](1045_games.py), [1045_games.rs](1045_games.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The original files build a breadth-first order and process it backward. The optimized Go file processes the same tree recurrence by removing non-root leaves.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1045_games.cpp](1045_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.015 s | 252 KB | 11278624 |
| [1045_games.go](1045_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.031 s | 1216 KB | 11278625 |
| [1045_games.java](1045_games.java) | Java 1.8 | games | O(n) | AC | 0.109 s | 716 KB | 11278627 |
| [1045_games.py](1045_games.py) \* | Python 3.12 x64 | games | O(n) | AC | 0.078 s | 624 KB | 11278626 |
| [1045_games.rs](1045_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.015 s | 284 KB | 11278628 |
| [1045_dfs.cpp](1045_dfs.cpp) | G++ 13.2 x64 | dfs | O(n) | AC | 0.015 s | 224 KB | 11315853 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1045_games_optimized.go](1045_games_optimized.go) \* | Go 1.14 x64 | games | O(n) | AC | 0.062 s | 348 KB | 11315879 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
