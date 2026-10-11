# 1218. Which Jedi can win the tournament

[Timus 1218](https://acm.timus.ru/problem.aspx?space=1&num=1218) · difficulty 323 · graphs

Original problem by Leonid Volkov, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of `N ≤ 200` Jedi has three parameters, and in each parameter all
values differ. Of two Jedi, the one stronger in at least two parameters
wins their match, and the loser leaves the tournament. List, in input
order, every Jedi for whom some schedule of matches leaves them as the
last one standing.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then for each Jedi a name of up to 30 letters and three integers up
to `10⁵` in absolute value.

## Output

The possible winners, one per line, in input order.

## Examples

### Example 1

Input:

```
5
Solo 0 0 0
Anakin 20 18 30
Luke 40 12 25
Kenobi 15 3 2
Yoda 35 9 125
```

Output:

```
Anakin
Luke
Yoda
```

## Solution

Every pair has exactly one winner, so the "beats" relation is a
tournament graph. A Jedi can win the tournament exactly when every other
Jedi can be reached from them along a chain of wins.

If every Jedi is reachable, take a tree of such chains rooted at the
candidate and play the matches from the leaves upward: each Jedi meets the
one directly above in the tree, who beats them, until only the candidate
is left. If some Jedi are not reachable, nobody reachable can ever beat
any of them, so the last of them can never be knocked out by the
candidate's side.

So compute the transitive closure of the "beats" relation with
Warshall's algorithm and print every Jedi that reaches all the others.
`O(N³)`.

Pitfalls:

- a single Jedi wins by default;
- in a ring of three, every one of them can win, as the example shows;
- the output keeps the input order, not any order of strength.

The answers were compared with a separately written solution on 200
random tournaments and on every test.

## Language notes

- Python keeps each row of the closure as one big integer, so a row is
  merged in one operation; the other languages use boolean matrices.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1218_graphs.cpp](1218_graphs.cpp) | G++ 13.2 x64 | graphs | O(N³) | AC | 0.031 s | 424 KB |
| [1218_graphs.go](1218_graphs.go) | Go 1.14 x64 | graphs | O(N³) | AC | 0.031 s | 1188 KB |
| [1218_graphs.java](1218_graphs.java) | Java 1.8 | graphs | O(N³) | AC | 0.171 s | 2196 KB |
| [1218_graphs.py](1218_graphs.py) | Python 3.12 x64 | graphs | O(N³) | AC | 0.109 s | 520 KB |
| [1218_graphs.rs](1218_graphs.rs) | Rust 1.75 x64 | graphs | O(N³) | AC | 0.046 s | 288 KB |
