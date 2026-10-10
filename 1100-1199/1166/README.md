# 1166. Can a player lay out the whole hand without letting the opponent move

[Timus 1166](https://acm.timus.ru/problem.aspx?space=1&num=1166) · difficulty 3552 · games

Original problem by Andrew Lopatine, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players are left in a card game played with a 54-card deck that
includes two jokers. Each laid card must be covered by a card of the same
suit or the same value; after a queen only the suit announced with it
counts. After a 6, a 7, an ace or the king of spades the opponent skips
the turn, so the same player moves again and covers their own card. A
joker may be laid as any card its owner names. Given the first player's
hand (they cannot draw any more) and the face-up card, decide whether
they can lay out all their cards one after another without the opponent
ever moving, and if so, print such an order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The hand as two-letter cards (`T` for ten, `*` for a joker) on one line,
then the face-up card; a queen there is followed by the announced suit,
and a joker by the card it stands for.

## Output

`YES` and the order of the cards, with each laid joker followed by the
card it stands for and each queen by the suit it announces, or `NO`.

## Checking

Any order is accepted if it lays out exactly the hand, each card covers
the one before it, every card but the last makes the opponent skip, and
queens and jokers are written in full. The verdict `YES` or `NO` is taken
from the stored answer.

## Examples

### Example 1

Input:

```
6C QD 6S KS 7S *
*QHS
```

Output:

```
YES
7S KS 6S 6C *6D QDS
```

## Solution

After any card other than the thirteen turn-skipping ones (a 6, 7 or ace
of each suit and the king of spades) the opponent moves. So every card but
the last must be one of them, either real or a joker named as one. A hand
with two other cards is a `NO` at once, and a single other card has to go
last.

What remains is a path that starts at the face-up card and goes through
the hand, each card covering the one before. The state is which real
turn-skipping cards are already laid (at most `2^13` sets), how many
jokers are used (they are interchangeable, so only their number matters)
and the card on top: one of the thirteen or the face-up card. A depth-first
search remembers the states it failed from and returns the order once
every card is laid. When one card is left, it is checked against the top:
the other card if there is one, otherwise the last turn-skipping card; a
last joker can always be named, say, the two of the suit on top.
`O(2^13·3·14·26)` at worst.

Pitfalls:

- a queen on the table is covered only by its announced suit, even by
  another queen;
- a joker on the table counts as the card it was named;
- an eight or a queen gives the opponent a move, so it can only be last;
- a laid queen needs an announced suit in the output, even as the last
  card.

The verdicts were compared with a separately written solution on 495
random deals, and every printed order passed the checker.

## Language notes

- All languages run the same search with the same table of failed states.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1166_games.cpp](1166_games.cpp) | G++ 13.2 x64 | games | O(2^13·3·14·26) | AC | 0.015 s | 556 KB |
| [1166_games.go](1166_games.go) | Go 1.14 x64 | games | O(2^13·3·14·26) | AC | 0.031 s | 1168 KB |
| [1166_games.java](1166_games.java) | Java 1.8 | games | O(2^13·3·14·26) | AC | 0.109 s | 952 KB |
| [1166_games.py](1166_games.py) | Python 3.12 x64 | games | O(2^13·3·14·26) | AC | 0.093 s | 940 KB |
| [1166_games.rs](1166_games.rs) | Rust 1.75 x64 | games | O(2^13·3·14·26) | AC | 0.062 s | 380 KB |
