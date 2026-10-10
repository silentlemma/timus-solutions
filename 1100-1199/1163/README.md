# 1163. Who wins a game of flicking draughts off the board

[Timus 1163](https://acm.timus.ru/problem.aspx?space=1&num=1163) · difficulty 3932 · games

Original problem by Nick Durov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Eight red and eight white draughts, discs of radius `0.4`, stand on an
`8×8` board without touching each other. Players alternate, red first. A
move takes one draught of the player's colour and flicks it in any
direction: it slides in a straight line until it falls off the board, and
every draught it touches on the way is removed. A player with no draughts
left on their turn loses. Find the winner when both play optimally.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Two lines with eight pairs of coordinates each: the centres of the red
draughts, then of the white ones.

## Output

`RED` or `WHITE`.

## Examples

### Example 1

Input:

```
0.5 7.5 1.5 7.5 2.5 7.5 3.5 7.5 4.5 7.5 5.5 7.5 6.5 7.5 7.5 7.5
0.5 0.5 1.5 0.5 2.5 0.5 3.5 0.5 4.5 0.5 5.5 0.5 6.5 0.5 7.5 0.5
```

Output:

```
RED
```

## Solution

The moving draught sweeps a strip: another draught is hit exactly when its
centre is ahead of the start and at most `0.8`, two radii, away from the
line of motion. A draught behind the start is never touched, since the
draughts are more than `0.8` apart and the distance only grows.

As the direction turns, a draught at distance `d` is hit inside an arc of
directions bounded by the two tangent angles `atan2 ± asin(0.8/d)`. So the
set of hit draughts changes only at these angles. Trying each tangent
angle itself, where the touch still counts, and the middle of every gap
between neighbouring angles gives every possible set: at most 60 per
draught, fewer after removing repeats.

The game state is the set of draughts still on the board and the side to
move, `2^17` states in all. A move removes the moving draught itself and
everything it hits, so every game ends within 16 moves. A memoized search
marks a state as winning if some move leads to a losing state for the
opponent; a side with no draughts has no moves and loses.
`O(2^16·16·60)` at worst.

Pitfalls:

- the moving draught leaves the board too, so it always counts as lost;
- touching is a hit, so the tangent directions must be tried exactly, with
  a small tolerance for rounding, and not only the gaps between them;
- removing a draught of one's own colour can be a good move, so moves are
  not limited to hitting the opponent.

The answers were compared on every test and on 74 positions, some of them
won by white, with a separate program that samples 200,000 directions per
draught and solves all subsets bottom-up.

## Language notes

- All languages build the same kill sets from the same angles.
- Python keeps the search results in a dictionary; the other languages use
  an array with one entry per state.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1163_games.cpp](1163_games.cpp) | G++ 13.2 x64 | games | O(2^16·16·60) | AC | 0.015 s | 340 KB |
| [1163_games.go](1163_games.go) | Go 1.14 x64 | games | O(2^16·16·60) | AC | 0.031 s | 1340 KB |
| [1163_games.java](1163_games.java) | Java 1.8 | games | O(2^16·16·60) | AC | 0.218 s | 4616 KB |
| [1163_games.py](1163_games.py) | Python 3.12 x64 | games | O(2^16·16·60) | AC | 0.484 s | 3688 KB |
| [1163_games.rs](1163_games.rs) | Rust 1.75 x64 | games | O(2^16·16·60) | AC | 0.015 s | 400 KB |
