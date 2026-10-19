# 2112. Checking a shooter match log and guessing the teams

[Timus 2112](https://acm.timus.ru/problem.aspx?space=1&num=2112) · difficulty 812 · dsu, greedy, simulation

Original problem by Ivan Sychev, from the University Academic School Olympiad in Informatics 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n players play in hidden teams of four. Every player has a state 3
(healthy), 2 (wounded), 1 (knocked down) or 0 (dead) and starts at 3.
The log has three kinds of events: a hit in the body or the head lowers
the target by 1 or 2 (not below 0), a medkit restores the user to 3, and
a revive moves a teammate from 1 to 2. Only a player in state 3 or 2 may
act, and only a knocked-down teammate may be revived. Print "FAKE" if no
split into teams of four makes the log valid, otherwise "CORRECT" and any
valid split. The limits are 1 second and 256 MB.

## Input

n, 4 ≤ n ≤ 1000, divisible by 4, the n distinct names, then m,
0 ≤ m ≤ 10⁴, and the events "X HIT Y IN BODY", "X HIT Y IN HEAD",
"X USES MEDKIT" and "X REVIVE Y".

Names contain only lowercase and uppercase English letters and have at
most 20 characters.

## Output

"FAKE", or "CORRECT" followed by n / 4 lines of four names.

## Checking

A checker accepts any valid split.

## Examples

### Example 1

Input:

```
8
Shroud
Forsen
Wycc
Ragyra
BeastQT
Lirik
Asmadey
Ninja
12
Wycc HIT Shroud IN BODY
Shroud HIT Wycc IN HEAD
Ragyra REVIVE Wycc
Wycc USES MEDKIT
Lirik HIT BeastQT IN BODY
Asmadey HIT BeastQT IN BODY
Asmadey REVIVE BeastQT
Ragyra HIT Forsen IN HEAD
Shroud REVIVE Forsen
BeastQT HIT Shroud IN HEAD
Wycc HIT Forsen IN HEAD
Ninja HIT BeastQT IN HEAD
```

Output:

```
CORRECT
Wycc Ragyra BeastQT Asmadey
Lirik Ninja Shroud Forsen
```

### Example 2

Input:

```
8
Shroud
Forsen
Wycc
Ragyra
BeastQT
Lirik
Asmadey
Ninja
8
Shroud HIT Wycc IN HEAD
Shroud HIT Ragyra IN HEAD
Shroud HIT BeastQT IN HEAD
Shroud HIT Asmadey IN HEAD
Lirik REVIVE Wycc
Lirik REVIVE Ragyra
Lirik REVIVE BeastQT
Lirik REVIVE Asmadey
```

Output:

```
FAKE
```

### Example 3

Input:

```
4
Shroud
Forsen
Wycc
Ragyra
3
Shroud HIT Wycc IN HEAD
Wycc HIT Shroud IN HEAD
Wycc HIT Shroud IN BODY
```

Output:

```
FAKE
```

## Solution

The states do not depend on the teams, so simulate the log directly. An
event whose actor is in state 1 or 0 is fake, and so is a revive of a
target that is not in state 1. Hits on anybody are allowed, even on
oneself.

The only link to the teams is that a revive puts the two players in the
same team. Join them in a disjoint-set union. Every resulting group must
fit into one team, so a group larger than four is fake. The groups are
then packed into teams of four:

- groups of four are teams already;
- each group of three needs a single player, and if there are fewer
  singles than triples the log is fake;
- groups of two are paired with each other;
- an odd pair left over takes two singles, which exist because n is
  divisible by four;
- the rest of the singles form teams of four.

Simulation and packing outside the DSU take O(n + m), assuming expected
O(1) name lookups. The DSU uses path halving and links roots by index,
without union by size or rank; a general bound for the total running
time is O((n + m) log n).

Pitfall: DSU components are not bounded by four during simulation:
oversized groups are rejected only after the log (test 26). Thus the
team size alone does not justify a linear DSU bound.

In the third example Wycc is knocked down by a head shot and still
shoots, so the log is fake.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2112_dsu_greedy_simulation.cpp](2112_dsu_greedy_simulation.cpp) | G++ 13.2 x64 | dsu, greedy, simulation | O((n + m) log n) | AC | 0.031 s | 644 KB |
| [2112_dsu_greedy_simulation.go](2112_dsu_greedy_simulation.go) | Go 1.14 x64 | dsu, greedy, simulation | O((n + m) log n) | AC | 0.046 s | 2824 KB |
| [2112_dsu_greedy_simulation.java](2112_dsu_greedy_simulation.java) | Java 1.8 | dsu, greedy, simulation | O((n + m) log n) | AC | 0.156 s | 4712 KB |
| [2112_dsu_greedy_simulation.py](2112_dsu_greedy_simulation.py) | Python 3.12 x64 | dsu, greedy, simulation | O((n + m) log n) | AC | 0.109 s | 1140 KB |
| [2112_dsu_greedy_simulation.rs](2112_dsu_greedy_simulation.rs) | Rust 1.75 x64 | dsu, greedy, simulation | O((n + m) log n) | AC | 0.046 s | 1280 KB |
