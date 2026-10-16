# 1784. Rounders

[Timus 1784](https://acm.timus.ru/problem.aspx?space=1&num=1784) · difficulty 1243 · greedy

Original problem by Alexander Ipatov, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A deck of 52 cards lies in four piles of 13. Each pile holds the ranks
2, 3, …, A from top to bottom, but the suits are mixed. One move takes
a few cards of one suit from the top of a pile, keeping their order,
and either starts a new pile with them or puts them onto the card whose
rank is one higher than the bottom card taken. Find the fewest moves
that leave four piles, each of a single suit.

## Input

Four lines, the piles from top to bottom, 13 cards each. A card is a
rank (2–9, T, J, Q, K, A) followed by a suit (S, C, D, H). All cards
are different.

## Output

The fewest moves.

## Examples

### Example 1

Input:

```
2C 3C 4C 5C 6C 7C 8C 9C TC JC QC KC AC
2S 3S 4S 5S 6S 7S 8D 9D TD JD QD KD AD
2D 3D 4D 5D 6D 7D 8S 9S TS JS QS KS AS
2H 3H 4H 5H 6H 7H 8H 9H TH JH QH KH AH
```

Output:

```
3
```

## Solution

Go down the ranks. Suppose every pile already starts with a run of one
suit from 2 down to rank r. That run must end up on the card of rank
r + 1 of the same suit, which lies in the next row of some pile. So the
row r gives a mapping from piles to piles: pile i must go onto pile
target(i). A pile mapped to itself needs nothing. The other piles split
into cycles. In a cycle of length L every destination is covered by a
run that also has to move, so one run first goes to a new pile, then
the L − 1 others move one after another, and the parked run moves last:
L + 1 moves. After that every pile again starts with a one-suit run,
now down to rank r + 1, and the next row is handled the same way. The
answer sums the costs over the 12 gaps between rows. `O(1)`, the deck
has a fixed size.

In the example only the gap between 7 and 8 has a change. Spades in
the second pile must go onto 8S in the third pile, and diamonds in the
third pile onto 8D in the second: a cycle of two, 3 moves. The spades
go to a new pile, the diamonds go onto 8D, the spades go onto 8S.

Pitfalls:

- a cycle costs one more than its length, not its length;
- several separate cycles can appear in one row, each paying its extra
  move;
- only the suit of a card matters for the mapping, the rank is fixed by
  the row.

The answers agree with an independent accepted implementation on 120
random deals and with a full search of all moves on 225 small decks
with fewer ranks.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1784_greedy.cpp](1784_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.031 s | 380 KB |
| [1784_greedy.go](1784_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1112 KB |
| [1784_greedy.java](1784_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.140 s | 1652 KB |
| [1784_greedy.py](1784_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 512 KB |
| [1784_greedy.rs](1784_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.031 s | 224 KB |
