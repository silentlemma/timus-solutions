# 2128. Solitaire from rows into suit piles as a topological order

[Timus 2128](https://acm.timus.ru/problem.aspx?space=1&num=2128) · difficulty 994 · graphs

Original problem by Alexander Ipatov, prepared by Oleg Dolgorukov, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A deck has m suits with ranks 1 … n, laid out in k rows. A move takes the
rightmost card of a row and puts it on the pile of its suit, which is
allowed when the pile's top card is one rank lower, or the pile is empty
and the card has rank 1. Decide whether all cards can be moved to the
piles and print an order of moves. Any valid order is accepted. The
limits are 1 second and 128 MB.

## Input

m, n and k, 1 ≤ n · m ≤ 10⁵, 1 ≤ k ≤ 10⁵, then the rows: aᵢ ≥ 1 and aᵢ
pairs (suit, rank) from left to right, with 1 ≤ suit ≤ m and 1 ≤ rank ≤ n.
All cards are distinct and together form the complete deck of n · m cards.

## Output

"NO", or "YES" and the cards in the order they are moved.

## Checking

A checker replays the moves.

## Examples

### Example 1

Input:

```
2 3 2
3 1 3 2 3 1 1
3 1 2 2 2 2 1
```

Output:

```
YES
1 1
2 1
2 2
2 3
1 2
1 3
```

### Example 2

Input:

```
2 3 2
3 1 3 2 2 1 2
3 1 1 2 3 2 1
```

Output:

```
NO
```

## Solution

A card can be moved only after two other cards, when they exist: the
card of the same suit one rank lower, which must be on the pile, and the
card to its right in its row, which must already be gone. These are all
the conditions, so a sequence of moves is valid exactly when it lists
every card after its two predecessors.

That is a topological order of a graph with at most two incoming edges
per card. Kahn's algorithm starts from the cards with no predecessor
(rank-1 cards at the right end of their rows) and releases the next card
of the suit and the left neighbour in the row as they become free. If it
reaches every card the order is the answer, otherwise there is a cycle
and the answer is NO. The work is O(nm + k).

In the second example the 1 of suit 1 is covered by the 3 of suit 2,
which needs the 2 of suit 2; that card is covered by the 2 of suit 1,
which needs the 1 of suit 1: a cycle.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2128_graphs.cpp](2128_graphs.cpp) | G++ 13.2 x64 | graphs | O(nm + k) | AC | 0.062 s | 1612 KB |
| [2128_graphs.go](2128_graphs.go) | Go 1.14 x64 | graphs | O(nm + k) | AC | 0.031 s | 8160 KB |
| [2128_graphs.java](2128_graphs.java) | Java 1.8 | graphs | O(nm + k) | AC | 0.109 s | 8788 KB |
| [2128_graphs.py](2128_graphs.py) | Python 3.12 x64 | graphs | O(nm + k) | AC | 0.312 s | 17992 KB |
| [2128_graphs.rs](2128_graphs.rs) | Rust 1.75 x64 | graphs | O(nm + k) | AC | 0.046 s | 4728 KB |
