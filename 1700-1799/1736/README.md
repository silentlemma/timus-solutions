# 1736. Chinese Hockey

[Timus 1736](https://acm.timus.ru/problem.aspx?space=1&num=1736) · difficulty 1177 · greedy

Original problem by Alexander Ipatov (prepared by Igor Chevdar), from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

In a round robin of n hockey teams every game gives 3 points: 3 : 0 for
a win in normal time and 2 : 1 for a win in overtime. Given the final
points of every team, decide whether such a season exists and, if so,
show the results of all games.

## Input

n (2 ≤ n ≤ 200), then the points in non-increasing order; they add up
to 3n(n − 1)/2 and none exceeds 3(n − 1).

## Output

`INCORRECT`, or `CORRECT` and every game as `i ? j`, where `?` is `<`,
`<=`, `>=` or `>` for a loss in normal time, a loss in overtime, a win
in overtime or a win in normal time of team i. Any fitting season is
accepted.

## Examples

### Example 1

Input:

```
4
8 7 2 1
```

Output:

```
CORRECT
2 <= 1
3 >= 4
1 > 3
4 < 2
1 > 4
2 > 3
```

### Example 2

Input:

```
4
8 8 1 1
```

Output:

```
INCORRECT
```

## Solution

Every game splits 3 points in any of the four ways, so only the
totals matter. Take the team with the fewest points left, s of them,
and settle all its remaining games at once: it keeps s of the
3(m − 1) points of its m − 1 games and hands the rest out, 3 points a
game to the strongest teams first and what is left over to the next
one. Then remove it and repeat. If at some point the weakest team has
more points than its games can give, someone would need negative
points, or a team keeps points at the end, the table is impossible.

Feeding the strongest teams first leaves the most room for the weak
ones, which are the ones the remaining games can starve; an exchange
argument like the one behind the Havel–Hakimi method for graphs shows
that this never loses a season, and the checks below confirm it.
Sorting each round gives `O(n² log n)`.

In the first example team 4 keeps 1 point and hands out 8: 3 to team 1,
3 to team 2 and 2 to team 3. Then team 3 hands its 6 to teams 1 and 2,
and team 2 keeps 1 against team 1.

Pitfalls:

- a table that adds up correctly can still be impossible: in the second
  example the two weakest teams play each other, and that game alone
  gives 3 points, more than their 2;
- the result signs are from the first team's side, so `i < j` means
  that team i lost in normal time.

A table is possible exactly when the k weakest teams have at least
3·C(k, 2) points for every k, since their games among themselves give
that much; this is the max-flow condition for splitting the points.
The verdicts match it on 260 random tables of up to 200 teams, 154 of
them impossible, and every printed season was replayed by the checker.
For n up to 5, every table with the right total was compared with a
listing of all seasons.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1736_greedy.cpp](1736_greedy.cpp) | G++ 13.2 x64 | greedy | O(n² log n) | AC | 0.031 s | 280 KB |
| [1736_greedy.go](1736_greedy.go) | Go 1.14 x64 | greedy | O(n² log n) | AC | 0.031 s | 2188 KB |
| [1736_greedy.java](1736_greedy.java) | Java 1.8 | greedy | O(n² log n) | AC | 0.171 s | 5408 KB |
| [1736_greedy.py](1736_greedy.py) | Python 3.12 x64 | greedy | O(n² log n) | AC | 0.109 s | 2968 KB |
| [1736_greedy.rs](1736_greedy.rs) | Rust 1.75 x64 | greedy | O(n² log n) | AC | 0.031 s | 940 KB |
