# 1804. The Machinegunners in a Playoff

[Timus 1804](https://acm.timus.ru/problem.aspx?space=1&num=1804) · difficulty 411 · implementation

Original problem by Alex Samsonov, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two teams play a home game and an away game. More goals in total wins;
on equal totals, more goals scored at the other team's stadium wins;
if that is equal too, a coin decides. No team scores more than 30 in a
game. Given the first game, find the fewest goals the Machinegunners
must score in the second game to have any chance to advance, and the
most goals they can score that still leaves the opponents a chance.

## Input

t (1 ≤ t ≤ 200), then t lines of the form "The Machinegunners played
where game, scored x goals, and conceded y goals.", where is home or
away, 0 ≤ x, y ≤ 30.

## Output

For each line, the two numbers.

## Examples

### Example 1

Input:

```
2
The Machinegunners played home game, scored 28 goals, and conceded 0 goals.
The Machinegunners played home game, scored 1 goals, and conceded 1 goals.
```

Output:

```
0 1
1 29
```

## Solution

Try every score g of the Machinegunners and o of the opponents in the
second game, 31 × 31 pairs. Compare the pairs (total, away goals) of
both teams. The Machinegunners can advance if theirs is at least the
opponents' and can fail if it is at most, so a full tie allows both.
The first g that can advance and the last g that can fail are the
answers. The away goals are the Machinegunners' g and the opponents'
y if the first game was at home, otherwise x and o. `O(t)`, with 961
pairs each.

In the first line, after 28:0 at home, even 0:28 away is a full tie,
so 0 goals keep a chance. With 1 goal, 1:30 still loses, but with 2
goals the worst case, 2:30, wins on away goals.

Pitfalls:

- a tie on both counts goes to a coin, so it counts both as a chance
  to advance and as a chance to fail;
- which team's away goals come from the second game depends on where
  the first was played;
- the scores of a game stop at 30.

The answers agree with an independent accepted implementation on 600
random first games and on every extreme and close score at both
venues.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1804_implementation.cpp](1804_implementation.cpp) | G++ 13.2 x64 | implementation | O(t) | AC | 0.031 s | 388 KB |
| [1804_implementation.go](1804_implementation.go) | Go 1.14 x64 | implementation | O(t) | AC | 0.015 s | 1216 KB |
| [1804_implementation.java](1804_implementation.java) | Java 1.8 | implementation | O(t) | AC | 0.109 s | 2600 KB |
| [1804_implementation.py](1804_implementation.py) | Python 3.12 x64 | implementation | O(t) | AC | 0.156 s | 520 KB |
| [1804_implementation.rs](1804_implementation.rs) | Rust 1.75 x64 | implementation | O(t) | AC | 0.015 s | 268 KB |
