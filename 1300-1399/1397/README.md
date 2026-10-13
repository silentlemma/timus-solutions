# 1397. Points Game

[Timus 1397](https://acm.timus.ru/problem.aspx?space=1&num=1397) · difficulty 1663 · geometry, games

Original problem by Michael Medvedev, from the Open All-Ukrainian Collegiate Programming Contest 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are 2n points in the plane, n ≤ 500. Two players colour them in
turns, the first white and the second black, until each has coloured n
points. A player's score is the sum of the distances between all pairs
of points of that player's colour. With best play on both sides, print
the winner's score minus the loser's, with three digits after the
point. The input holds several games.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Games one after another: n, then 2n lines with the points.

## Output

The difference for every game.

## Examples

### Example 1

Input:

```
2
0 0
0 1
1 0
1 1
2
0 0
1 0
0 3
1 5
```

Output:

```
0.000
1.937
```

## Solution

Let Dᵢ be the sum of distances from point i to all other points. Summed
over the white points, every white pair is counted twice and every pair
of different colours once: ΣW Dᵢ = 2·WW + WB, and likewise
ΣB Dᵢ = 2·BB + WB. So the difference of the scores is

WW − BB = (ΣW Dᵢ − ΣB Dᵢ) / 2,

and the game only adds up a fixed value per point. Each player then
does best by taking the point with the largest Dᵢ left: sort the Dᵢ in
decreasing order, the first player gets the ones at even places, and
the answer is half the alternating sum. `O(n²)` per game for the
distances.

Pitfalls:

- the input has several games and runs to the end of the file;
- the alternating sum can come out as a tiny negative number when the
  game is even, which would print as -0.000, so its absolute value is
  printed;
- in Java Math.hypot is far slower than Math.sqrt on a million pairs per
  game.

The answers were compared with a full minimax over all colourings on 200
random games of up to 8 points.

## Language notes

- Python runs under PyPy: ten games of 1 000 points take about 0.7 s with
  CPython and well under 0.1 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1397_greedy.cpp](1397_greedy.cpp) | G++ 13.2 x64 | greedy | O(n^2) | AC | 0.001 s | 244 KB |
| [1397_greedy.go](1397_greedy.go) | Go 1.14 x64 | greedy | O(n^2) | AC | 0.015 s | 1180 KB |
| [1397_greedy.java](1397_greedy.java) | Java 1.8 | greedy | O(n^2) | AC | 0.078 s | 1064 KB |
| [1397_greedy.py](1397_greedy.py) | PyPy 3.10 x64 | greedy | O(n^2) | AC | 0.140 s | 6328 KB |
| [1397_greedy.rs](1397_greedy.rs) | Rust 1.75 x64 | greedy | O(n^2) | AC | 0.031 s | 372 KB |
