# 1374. Misere

[Timus 1374](https://acm.timus.ru/problem.aspx?space=1&num=1374) · difficulty 9959 · games

Original problem by Den Raskovalov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three players hold 10 cards each from a 32-card deck, all cards open.
They play ten tricks: the leader plays any card, then the next player
and the third one, each following the suit of the first card if they
can. The highest card of that suit takes the trick and leads the next
one. There are no trumps. Player 1 has declared a misère and must take
no trick at all. Print `;)` if player 1 can manage that whatever the
other two do, and `;(` otherwise.

Time limit: 1 second. Memory limit: 16 MB.

## Input

The hands of players 1, 2 and 3, one per line, as cards like `10S` or
`QH`, then the number of the player who leads first.

## Output

`;)` or `;(`.

## Examples

### Example 1

Input:

```
7S 8S 9S 10S JS QS KS AS 7C 8C
9C 10C JC QC KC AC 7D 8D 9D 10D
JD QD KD AD 7H 8H 9H 10H JH QH
1
```

Output:

```
;)
```

## Solution

It is a game of full information with a yes-or-no outcome, so search
it: at player 1's cards some card must keep the misère alive, at the
other players' cards every card must. Three things keep the search
small:

- touching cards are the same card: two cards of one player in one
  suit with no other player's card between them lead to the same
  outcome, so only one of each run is tried;
- the four suits play alike, and only the order of the cards inside a
  suit matters. So a position between tricks is remembered by the sorted
  strings of owners of each suit plus the leader, and positions that
  differ by a renaming of suits or ranks are solved once;
- the remembered positions live in a table of fixed size, keyed by
  that string. A clash only means solving a position again, which keeps
  the memory well inside 16 MB.

On the hardest deals found, about 30 000 positions are stored.
Exponential in the worst case, but fast on every deal tried.

Pitfalls:

- play goes 1 → 2 → 3 around the table, from the leader;
- a player with no card of the led suit may play anything, and such a
  card never takes the trick;
- the misère fails as soon as player 1 takes one trick.

The answers were compared on 300 deals with a plain search without the
suit and rank renaming; the equivalence of touching cards was checked
against a search over every card on further deals. Tests 02 to 05 are
hard deals posted on the problem's discussion board.

Complexity: `O((n!)^3)` for n = 10 cards per player: in the worst case
every order of play is tried.

## Language notes

- Go builds the keys and the lists of cards in fixed arrays: slices made
  at every step leave garbage, and the collector lets the heap grow to
  about twice the 8 MB table, past 16 MB.
- Python runs on CPython and cuts the game tree further: every suit is
  followed by a small precomputed automaton, of comparable replies of
  the defenders only the hardest for the declarer is kept, a suit that
  can no longer hurt the declarer is reduced to the declarer's card
  count and the defenders' order, and equal positions are merged; its
  table of positions is a dictionary capped at 100 000 entries. Earlier
  versions without these cuts exceeded the time limit on the judge's
  test 62 even under PyPy.
- Java keeps a table of 2¹⁹ entries instead of 2²⁰, to leave room for
  the JVM in 16 MB.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1374_games.cpp](1374_games.cpp) | G++ 13.2 x64 | games | O((n!)^3) | AC | 0.140 s | 8564 KB |
| [1374_games.go](1374_games.go) | Go 1.14 x64 | games | O((n!)^3) | AC | 0.140 s | 10056 KB |
| [1374_games.java](1374_games.java) | Java 1.8 | games | O((n!)^3) | AC | 0.406 s | 10240 KB |
| [1374_games.py](1374_games.py) | Python 3.12 x64 | games | O((n!)^3) | AC | 0.187 s | 3628 KB |
| [1374_games.rs](1374_games.rs) | Rust 1.75 x64 | games | O((n!)^3) | AC | 0.156 s | 8280 KB |
