# 1244. Which cards are missing from a deck, by weight

[Timus 1244](https://acm.timus.ru/problem.aspx?space=1&num=1244) · difficulty 254 · dp

Original problem by Alexander Petrov, from the Ural State University Personal Contest, March 1, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A full deck has N cards (2 ≤ N ≤ 100) of known weights from 1 to 1000
milligrams. A partial deck weighs W, less than the full one. Print the
numbers of the missing cards in increasing order if they are determined
uniquely, -1 if several sets of cards could be missing, and 0 if none
can.

Time limit: 1 second. Memory limit: 64 MB.

## Input

W, then N, then the N card weights.

## Output

The missing cards, -1 or 0.

## Examples

### Example 1

Input:

```
270
4
100
110
170
200
```

Output:

```
2 4
```

### Example 2

Input:

```
270
4
100
110
160
170
```

Output:

```
-1
```

### Example 3

Input:

```
270
4
100
120
160
180
```

Output:

```
0
```

## Solution

The cards left in the deck form a set of total weight W, and the missing
ones are the rest. So count the sets of cards that weigh W, but only up
to 2, since that is all that matters: `ways[i][s]` is the number of sets
of the first i cards weighing s, capped at 2, and
`ways[i][s] = min(2, ways[i−1][s] + ways[i−1][s − w_i])`. Then
`ways[N][W]` is 0, 2 (print -1) or exactly 1.

For the unique set, go back from the last card with s = W: card i is
missing exactly when the first i − 1 cards already make s on their own,
`ways[i−1][s] = 1`; otherwise it is in the deck and s drops by its
weight. Uniqueness means only one of the two can hold. `O(N·W)` with
W < 100 000.

Pitfalls:

- equal cards are different cards: with two cards of weight 1 and W = 1
  either one may be missing, so the answer is -1 (test 04);
- several cards can be missing, up to all but one (test 08).

The answers were compared with checking every subset on 1500 random small
decks.

## Language notes

- Python keeps "at least one way" and "at least two ways" as two big
  integers used as bitsets, one pair per prefix of the deck; the other
  languages keep a byte per weight.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1244_dp.cpp](1244_dp.cpp) | G++ 13.2 x64 | dp | O(N·W) | AC | 0.031 s | 9472 KB |
| [1244_dp.go](1244_dp.go) | Go 1.14 x64 | dp | O(N·W) | AC | 0.031 s | 11676 KB |
| [1244_dp.java](1244_dp.java) | Java 1.8 | dp | O(N·W) | AC | 0.109 s | 12768 KB |
| [1244_dp.py](1244_dp.py) | Python 3.12 x64 | dp | O(N·W) | AC | 0.093 s | 2848 KB |
| [1244_dp.rs](1244_dp.rs) | Rust 1.75 x64 | dp | O(N·W) | AC | 0.031 s | 9692 KB |
