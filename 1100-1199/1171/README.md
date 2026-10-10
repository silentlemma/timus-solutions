# 1171. The trip down a space station with the best food per day

[Timus 1171](https://acm.timus.ru/problem.aspx?space=1&num=1171) · difficulty 1265 · dp

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A station has `N ≤ 16` levels, each a `4×4` grid of rooms with food from
1 to 255, and some rooms have a door to the same room one level down.
Starting in a given room on the top level, an astronaut moves one step a
day (north, east, south, west, or down through a door), never enters a
room twice and never goes up, and must finish on level 1. Each room
entered gives its food. Maximise the food gathered divided by the number
of days, which is the number of rooms visited, and print such a trip.

Time limit: 1 second. Memory limit: 4 MB.

## Input

`N`, then for each level from the top four rows of food and four rows of
doors, then the starting row and column.

## Output

The best ratio with four decimals, the number of moves and, if there are
any, the moves as letters `N`, `E`, `S`, `W` and `D`.

## Checking

Any trip is accepted if it is legal, ends on level 1 and reaches the best
ratio; the checker replays the moves.

## Examples

### Example 1

Input:

```
2
1 20 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1 1
20 1 1 1
1 1 1 1
1 1 1 1
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1
```

Output:

```
8.6000
4
EDSW
```

## Solution

Inside one level the trip is a simple path of the `4×4` grid, and there
are only 28,512 of those. For each level, a depth-first walk over all of
them records `best[s][e][k]`, the most food on a path of `k` rooms from
`s` to `e`.

A ratio is maximised with Dinkelbach's method. For a current ratio
`num/den`, find the trip with the largest `den·food − num·rooms`. That is
a simple dynamic programme from the bottom level up: the value of
entering a level at room `s` is the best over its exits `e` (doors, or
any room on level 1) and lengths `k` of
`den·best[s][e][k] − num·k` plus the value of entering the next level at
`e`. If the best trip scores above zero, its own ratio is higher, so it
becomes the new `num/den`; when nothing scores above zero, the ratio is
optimal. All of this is integer arithmetic, so the stop is exact. Each
round costs `O(N·16³)`, and the rounds are few.

Finally the trip is rebuilt: for every level, a second walk looks for a
path from its start to its end with the recorded length and food.

Pitfalls:

- the trip must reach level 1, so on upper levels only door rooms can end
  a level's path, while on level 1 any room can;
- the days are the rooms visited, one more than the moves, and a single
  level with a rich start can mean no moves at all;
- the memory limit is 4 MB, so the paths themselves are not stored, only
  the best food per start, end and length.

The ratios were compared with a separately written solution on 300
random stations of 1 to 16 levels, and every printed trip passed the
checker.

## Language notes

- All languages run the same walks and the same Dinkelbach rounds.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1171_dp.cpp](1171_dp.cpp) | G++ 13.2 x64 | dp | O(N·16³) per round | AC | 0.031 s | 492 KB |
| [1171_dp.go](1171_dp.go) | Go 1.14 x64 | dp | O(N·16³) per round | AC | 0.046 s | 1732 KB |
| [1171_dp.java](1171_dp.java) | Java 1.8 | dp | O(N·16³) per round | AC | 0.140 s | 1612 KB |
| [1171_dp.py](1171_dp.py) | Python 3.12 x64 | dp | O(N·16³) per round | AC | 0.453 s | 2420 KB |
| [1171_dp.rs](1171_dp.rs) | Rust 1.75 x64 | dp | O(N·16³) per round | AC | 0.031 s | 648 KB |
