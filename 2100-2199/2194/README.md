# 2194. Fewest turns on a board of snakes where a six rolls again

[Timus 2194](https://acm.timus.ru/problem.aspx?space=1&num=2194) · difficulty 495 · bfs

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A token starts on cell 1 of a board of N cells. A roll of k moves it
min(i + k, N); landing on N wins, and landing on a snake of length pᵢ
sends it to i − pᵢ, possibly onto another snake. A roll of six lets the
player roll again in the same turn. Find the fewest turns needed to win
if the dice cooperate, or −1. The limits are 1 second and 256 MB.

## Input

N, 2 ≤ N ≤ 2 · 10⁵, then p₂ … p_{N−1} with 0 ≤ pᵢ < i.

## Output

The fewest turns, or −1.

## Examples

### Example 1

Input:

```
10
0 1 1 1 1 1 1 0
```

Output:

```
-1
```

### Example 2

Input:

```
10
1 2 1 2 0 1 1 1
```

Output:

```
1
```

### Example 3

Input:

```
10
1 1 2 2 0 6 7 8
```

Output:

```
2
```

## Solution

Snakes only send the token left, so the cell where it finally rests
after arriving at i is computed once from left to right:
land(i) = land(i − pᵢ), or i if there is no snake.

Now a state is the cell where the token is about to roll, with the
number of turns begun so far. A roll of one to five ends the turn, so it
is an edge of weight 1, and a six keeps the turn going, an edge of
weight 0. The start has one turn begun, and the first roll that reaches
N gives the answer with the current turn count. A 0-1 breadth-first
search with a deque handles the two weights in O(6N).

In the second example a six from cell 1 lands on 7, slides to 6, and a
four from there reaches 10 in the same turn.

## Optimized solutions

The C++ alternative computes land[i] while reading each leftward teleport, eliminating the jump array. Process one turn layer at a time: first close all reachable six-roll paths, extending the current frontier; only afterwards enqueue outcomes one through five for the next turn. By induction the first discovery of each resting cell has minimum turn count, so a visited bitmap replaces distances. If any roll can reach N from a cell, a six can also reach or overshoot it. Checking the six during the current turn therefore covers all winning rolls. Old cells need not be expanded again; their free and paid moves were already explored no later. Each cell enters one append-only uint32 queue once, so both arrays use O(N), the bitmap O(N/64) words, and time O(6N)=O(N). All simple 0–1 deque versions remain; the other four families reuse admitted bases.

The accepted base implementations [2194_bfs.go](2194_bfs.go), [2194_bfs.java](2194_bfs.java), [2194_bfs.py](2194_bfs.py), [2194_bfs.rs](2194_bfs.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2194_bfs.cpp](2194_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.156 s | 2552 KB | 11295294 |
| [2194_bfs.go](2194_bfs.go) \* | Go 1.14 x64 | bfs | O(N) | AC | 0.156 s | 8952 KB | 11295296 |
| [2194_bfs.java](2194_bfs.java) \* | Java 1.8 | bfs | O(N) | AC | 0.140 s | 6640 KB | 11295299 |
| [2194_bfs.py](2194_bfs.py) \* | Python 3.12 x64 | bfs | O(N) | AC | 0.312 s | 21612 KB | 11295297 |
| [2194_bfs.rs](2194_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.046 s | 7656 KB | 11295301 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2194_bfs_optimized.cpp](2194_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.015 s | 1196 KB | 11315428 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
