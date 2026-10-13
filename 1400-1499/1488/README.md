# 1488. ACM Poker

[Timus 1488](https://acm.timus.ru/problem.aspx?space=1&num=1488) · difficulty 1540 · implementation

Original problem by Vladimir Yakovlev, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players get three cards each. Dima may secretly swap one or two of
the dealt cards for the two cards up the sleeve, but never takes out a
card equal to one of Sasha's, and never ends up with two equal cards.
Hands rank, from the best: three threes, straight flush, three of a
kind, straight, flush, pair, high card. Equal combinations, or two hands
without a pair, are compared by ranks from the highest down; a pair
compares the pair first, then the odd card. Aces are high, and A-2-3
and K-A-2 are not straights. For each game print "Dima" if Dima can
win, "Artyom" (the dealer, who takes a draw) if Dima can only draw, and
"Sasha" otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Games separated by empty lines: Sasha's three cards, Dima's three cards
and the two sleeve cards, written like 10H or QS.

## Output

One name per game.

## Examples

### Example 1

Input:

```
4C AC 2C
4S KD 6H
5C KH

JS 8H JC
8C 8D 10H
8H 10H

10D 8D 9D
3D 3C 3H
AH AS

2C 3D 4H
2D 3H 4S
AH AH
```

Output:

```
Dima
Sasha
Dima
Artyom
```

## Solution

Dima has at most ten hands to choose from: the dealt one, each of the
three cards replaced by either sleeve card, and both sleeve cards kept
with one dealt card. Sleeve cards equal to one of Sasha's are dropped
first, and hands with two equal cards are skipped.

Each hand gets a key that sorts like the hands: the combination number,
then the ranks that break ties. Ranks go from the highest down; for a
pair, the pair's rank and then the odd card. Three threes need nothing
more. Dima wins if some key beats Sasha's, draws if some key equals it,
and loses otherwise. `O(1)` per game.

Pitfalls:

- A-2-3 and K-A-2 are not straights, but Q-K-A is (test 02);
- the sleeve may hold one of Sasha's cards, a copy of Dima's own card
  or two equal cards, and none of them may be used in a forbidden way
  (tests 01, 02, gen3);
- three threes beat even the best straight flush (tests 01, 02);
- equal keys mean a draw even with different suits (test 02, gen2).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1488_implementation.cpp](1488_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) per game | AC | 0.001 s | 428 KB |
| [1488_implementation.go](1488_implementation.go) | Go 1.14 x64 | implementation | O(1) per game | AC | 0.031 s | 5896 KB |
| [1488_implementation.java](1488_implementation.java) | Java 1.8 | implementation | O(1) per game | AC | 0.156 s | 6824 KB |
| [1488_implementation.py](1488_implementation.py) | Python 3.12 x64 | implementation | O(1) per game | AC | 0.203 s | 2232 KB |
| [1488_implementation.rs](1488_implementation.rs) | Rust 1.75 x64 | implementation | O(1) per game | AC | 0.015 s | 1256 KB |
