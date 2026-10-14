# 1549. Another Japanese Puzzle

[Timus 1549](https://acm.timus.ru/problem.aspx?space=1&num=1549) · difficulty 2339 · constructive

Original problem by Stanislav Vasiliev, prepared by Vladimir Yakovlev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are S straight and T turning square track pieces
(0 ≤ S, T ≤ 1000, S + T > 0). Build the longest closed track: a loop of pieces on
distinct squares of a grid, each joined to the next through the middle
of a side. Print its length and the pieces in order as F (straight),
L (left turn) and R (right turn), or "Atawazu" if no loop can be built.

Time limit: 1 second. Memory limit: 64 MB.

## Input

S and T.

## Output

The number of pieces and the string of F, L and R, or `Atawazu`.

## Examples

### Example 1

Input:

```
5 6
```

Output:

```
10
FLLFRLLFLF
```

### Example 2

Input:

```
49 3
```

Output:

```
Atawazu
```

## Solution

Which counts of straights f and turns t can form a loop?

- the squares of a loop alternate between the two colours of a chess
  board, so f + t is even;
- every turn switches between horizontal and vertical moves, so t is
  even, and therefore f too;
- a loop turns by 360°, so t ≥ 4;
- with no straights the moves alternate horizontal and vertical, and
  closing the loop needs an even number of each, so t is a multiple of
  4; and t = 8 does not fit (a search over all loops of 8 squares).

These conditions are also enough, by three constructions:

- the border of a 2-row box, (f/2 + b + 2) squares wide, with b bumps:
  each bump inserts two new neighbouring squares just outside the top
  or bottom row, adding 4 turns and taking 2 straights; this covers t = 4 + 4b,
  and both rows together hold enough room for the bumps when f ≥ 2 or b
  is 0;
- for t = 6 + 4b (then f ≥ 2) a 3-row box with the same bumps and one
  corner cut in: the corner square moves diagonally inwards, which turns
  two straights into turns;
- with no straights and t ≥ 12, a staircase: L, then LR repeated
  t/4 − 2 times, L, LR, and the same once more.

If T < 4, print `Atawazu`. Otherwise the answer takes the largest even
f ≤ S and even t ≤ T; only when f is 0, t drops to the largest multiple
of 4 that is 4 or at least 12.
The program reads letters from box paths and builds staircase strings directly.
All S, T ≤ 120, and every f or t up to 1000 next to small values of the
other, were checked by walking the track; a search over all loops of up
to 18 squares found exactly these (f, t) pairs.

Pitfalls:

- eight turns alone cannot all be used, four can (tests 04, 12);
- an odd straight or turn is left over (tests 01, 11, 17);
- the example's track is only one of many; a checker walks the output
  (all tests with a loop).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1549_constructive.cpp](1549_constructive.cpp) | G++ 13.2 x64 | constructive | O((S + T) log(T + 2)) | AC | 0.015 s | 244 KB |
| [1549_constructive.go](1549_constructive.go) | Go 1.14 x64 | constructive | O(S + T) | AC | 0.031 s | 1308 KB |
| [1549_constructive.java](1549_constructive.java) | Java 1.8 | constructive | O(S + T) | AC | 0.125 s | 1868 KB |
| [1549_constructive.py](1549_constructive.py) | Python 3.12 x64 | constructive | O(S + T) | AC | 0.093 s | 1000 KB |
| [1549_constructive.rs](1549_constructive.rs) | Rust 1.75 x64 | constructive | O(S + T) | AC | 0.046 s | 440 KB |
