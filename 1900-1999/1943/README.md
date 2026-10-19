# 1943. A Five-Card Winning Prefix

[Timus 1943](https://acm.timus.ru/problem.aspx?space=1&num=1943) · difficulty 906 · bruteforce, constructive

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of two players starts with a permutation of ranks 1 through n.
The fronts of both queues are revealed simultaneously. Equal cards are
both discarded. Otherwise the higher card wins both: append the lower
card first and the higher card last to the winner's queue. A player with
an empty queue loses; simultaneous emptiness is a draw. Given the other
player's initial queue, choose our permutation that wins, or prove none
exists. Merely drawing or repeating forever is insufficient.
Limits: 1 second, 64 MB.

## Input

n with 2≤n≤500, followed by a permutation of 1..n in the opponent's
top-to-bottom order. Every rank appears once in each initial deck.

## Output

NO alone if no winning deck exists. Otherwise YES on the first line,
and a winning permutation on the second, top to bottom. Any winner is valid.

## Checking

A checker replays the whole game with the printed deck and accepts any
deck that really wins. `NO` is never correct for five or more cards, by
the lemma below.

## Examples

```
4
2 3 4 1
```

```
YES
2 4 1 3
```

## Solution

Use only m=min(n,5) cards: take the opponent's first m ranks, enumerate
their permutations, and simulate each resulting m-card game. Store the
pair of current queues to detect a cycle; stop at the first actual win.
For n≤5 this searches every possible answer, so failure proves NO.

The key lemma is that every ordering of five distinct ranks has a
winning reply. Only the order of the ranks matters, so ranks 1 to 5
cover every set of five cards, and the lemma is checked by playing all
120² = 14 400 pairs of orderings. This short script does it, together
with the smaller decks:

```python
from collections import deque
from itertools import permutations

def game(a, b):
    a, b = deque(a), deque(b)
    seen, steps = set(), 0
    while a and b:
        state = tuple(a), tuple(b)
        if state in seen:
            return False, steps
        seen.add(state)
        x, y = a.popleft(), b.popleft()
        steps += 1
        if x > y:
            a.extend((y, x))
        elif y > x:
            b.extend((x, y))
    return bool(a), steps

for size in range(2, 6):
    orders = list(permutations(range(1, size + 1)))
    possible, longest = 0, 0
    for opponent in orders:
        results = [game(own, opponent) for own in orders]
        possible += any(won for won, _ in results)
        longest = max(longest, max(steps for _, steps in results))
    print(size, len(orders), possible, longest)
```

| Cards | Opponent orders | Orders with a winning reply | Longest game |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 4 |
| 3 | 6 | 3 | 7 |
| 4 | 24 | 22 | 16 |
| 5 | 120 | 120 | 49 |

There are only finitely many queue states because at most ten cards
remain; repeated states cannot win. The enumeration terminates, and each
of the 120 five-card opponent orders has a witnessed win. The test bundle
contains all 6 inputs and explicit winning outputs, as well as all
13 smaller opponent orders. These are a reproducible finite certificate.
Five is the smallest universal size because two four-card orders cannot win.

For n>5, replace only the first five cards by a locally winning permutation;
copy every remaining opponent card unchanged. During the first n rounds,
unplayed original cards remain ahead of all captures, so neither queue
can empty early. The last n−5 original pairs are equal and disappear.
After round n the remaining queues are exactly those of the five-card
game after round five. Every later round is identical, so the local win
becomes a full win. If the local win takes t rounds, the full game takes
n+t−5≤n+44. Thus every n≥5 input admits our construction, and exhaustive
search on the smaller full decks makes the algorithm complete.

O(n) time and space, plus a fixed local search of at most 5! candidates.
The complete local domain establishes at most 49 rounds per game and
at most ten active cards. These are verified bounds, not round cutoffs
in the programs. The first winning trial is at most 68 in this domain;
the code still enumerates normally until a win or all candidates finish.

Captured order is lower then higher. Equal cards disappear from both
queues, and simultaneous empty is a draw. Accept only a win, not survival
or a bounded-round guess. Trying five cards does not mean five rounds.
Untouched cards must occupy matching original positions, so they cancel
before any capture reaches the front. A convenient observed pattern of
sorted or nearly sorted decks cannot replace the full finite lemma.

## Language notes

C++ uses next_permutation; Python uses itertools.permutations. Go, Java
and Rust implement the usual pivot/successor/reverse step on five items.
All game engines keep exact queue states for cycle detection. Go uses
queue head indices; Java and Rust use deques. Only the prefix is searched;
the rest is copied. Standard libraries suffice, with no stored answer table.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1943_bruteforce_constructive.cpp](1943_bruteforce_constructive.cpp) | G++ 13.2 x64 | bruteforce, constructive | O(n) | AC | 0.015 s | 520 KB |
| [1943_bruteforce_constructive.go](1943_bruteforce_constructive.go) | Go 1.14 x64 | bruteforce, constructive | O(n) | AC | 0.031 s | 1236 KB |
| [1943_bruteforce_constructive.java](1943_bruteforce_constructive.java) | Java 1.8 | bruteforce, constructive | O(n) | AC | 0.109 s | 848 KB |
| [1943_bruteforce_constructive.py](1943_bruteforce_constructive.py) | Python 3.12 x64 | bruteforce, constructive | O(n) | AC | 0.062 s | 600 KB |
| [1943_bruteforce_constructive.rs](1943_bruteforce_constructive.rs) | Rust 1.75 x64 | bruteforce, constructive | O(n) | AC | 0.046 s | 468 KB |
