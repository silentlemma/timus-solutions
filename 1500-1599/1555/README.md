# 1555. Find the Treasure!

[Timus 1555](https://acm.timus.ru/problem.aspx?space=1&num=1555) · difficulty 7392 · games

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two players move in turns on an N × N maze (2 ≤ N ≤ 6, at most 30 walls;
each cell may have a wall on any side, so two walls can stand between
neighbours). A move is a step to a free neighbouring cell through no
wall, a pass, or a shot of the one rocket each player has: north, east,
south, west or down. A rocket flies until it leaves the board, hits a
wall (which is destroyed) or hits the other player (who dies); a rocket
fired down kills the shooter. A player who dies loses; a player who has
stepped on the chest may also win by leaving the board. Leaving without
the chest is forbidden. Both play optimally. Print `Draw`, or `Win` or
`Lose` for the first player with
the number of turns (the first player makes it smallest, the second
largest) and the first player's first move: `M` or `S` with a direction
on the keypad (8 north, 6 east, 2 south, 4 west, 5 pass or down).

Time limit: 5 seconds. Memory limit: 64 MB.

## Input

N, then 3N lines of 3N characters: every cell is a 3 × 3 square with
its walls `-` and `|` at the middles of its sides and `1`, `2`, `*` or a
space in the centre. The digits mark the players and `*` marks the chest;
each of `1`, `2` and `*` occurs exactly once. North is at the top. Only
in the examples are spaces replaced by dots for clarity.

## Output

`Draw` on one line, or `Win`/`Lose` and the number of turns separated by
a space on the first line, then the first move on the second line.
In a move, `M` means moving (or passing) and `S` means shooting.

## Examples

### Example 1

Input:

```
3
.-..-..-.
|1....|2|
.........
.........
|*|.....|
.........
.........
|.......|
.-..-..-.
```

Output:

```
Win 5
M2
```

### Example 2

Input:

```
2
.-..-.
|2..*|
.-....
.-....
|1||.|
.-..-.
```

Output:

```
Lose 1
S5
```

## Solution

A retrograde analysis. A position is the two cells, who holds the chest
and whose turn it is; on top of it each rocket is loaded, fired out of
the board, or spent on wall w. A nonterminal shot only moves to rocket
states with fewer loaded rockets, so the rocket states are solved from
none loaded to both loaded, and each one is a game graph of up to 7 560 positions
whose nonterminal shots lead to positions already solved.

Inside a rocket state the results come by backward induction: a
position is won as soon as one move wins for the player to move, lost
when every move loses, and what is left unresolved is a draw. The number
of turns then comes by a Dijkstra-like pass with a heap (buckets in
Python): a position of the first player takes the fewest turns among
its moves that keep the
result, a position of the second player the most, once all those moves
are known. The first move is the best by result, then by turns, then
in the order M8, M6, M2, M4, M5, S8, S6, S2, S4, S5.
For W walls, S = W + 2 ≤ 32 is the number of states of one rocket,
and P = 6N²(N² − 1) is the number of positions per pair of rocket states.
The four compiled solutions take `O(S² · P log P)` time; Python takes
`O(S² · P)`.

Pitfalls:

- the first player keeps the number of turns small even when losing: in
  the second example it shoots down at once (`Lose 1`);
- of two walls between neighbours a rocket destroys only the first one
  it meets, and a destroyed wall stays gone (test 08);
- a rocket that leaves the board only spends itself;
- with the chest a player leaves the board only through a side without
  a wall;
- positions left unresolved by retrograde analysis are a draw (test 03).

The answers were compared with an independent accepted implementation
on the tests here and on 40 random mazes, 6 × 6 boards with 30 walls
among them.

## Language notes

- The Python solution runs under PyPy and was Accepted with PyPy 3.10
  x64 in 3.515 s, using 48 720 KB, within the 5 s limit. A direct port
  took about 20 s, so it works differently from the other four:
  - a rocket state is who still holds a rocket and which walls are
    gone, so states that differ only in who destroyed a wall or which
    rocket left the maze share a table (about 530 instead of about a
    thousand);
  - without rockets only the open steps and the exits matter, and
    states with the same ones share a table too;
  - the moves that do not depend on the walls are built once, each
    step with the side it goes through, so a state only marks which
    sides are open;
  - the number of turns comes from a list of buckets instead of a heap,
    since it only grows, and the won and the lost positions take one
    pass together.
- The other four solutions keep the moves and the predecessors of the
  positions in flat arrays reused for every rocket state: allocating
  them anew for each of about a thousand states made them up to twice
  as slow.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1555_games.cpp](1555_games.cpp) | G++ 13.2 x64 | games | O(S² · P log P) | AC | 2.156 s | 25108 KB |
| [1555_games.go](1555_games.go) | Go 1.14 x64 | games | O(S² · P log P) | AC | 4.078 s | 54920 KB |
| [1555_games.java](1555_games.java) | Java 1.8 | games | O(S² · P log P) | AC | 3.203 s | 29212 KB |
| [1555_games.py](1555_games.py) | PyPy 3.10 x64 | games | O(S² · P) | AC | 3.515 s | 48720 KB |
| [1555_games.rs](1555_games.rs) | Rust 1.75 x64 | games | O(S² · P log P) | AC | 2.140 s | 26488 KB |
