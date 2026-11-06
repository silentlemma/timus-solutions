# 1873. GOV Chronicles

[Timus 1873](https://acm.timus.ru/problem.aspx?space=1&num=1873) · difficulty 365 · implementation

Original problem by Mikhail Rubinchik, from the Ural Regional School Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The statement tells the long history of the team Alarm, later
Team.GOV, contest by contest, with every change of its line-up. The
players are numbered from 0 to 13. Given a player's number, print how
many contests that player played for the team. The warm-up round of
the last Ural championship does not count.

## Input

A player number from 0 to 13.

## Output

The number of contests the player played for the team.

## Examples

### Example 1

Input:

```
1
```

Output:

```
21
```

### Example 2

Input:

```
11
```

Output:

```
0
```

## Solution

All the work is in reading the story carefully; the program only looks
up a table. The contests and their line-ups, in order:

| Contests | Players |
| --- | --- |
| Alarm: university, quarterfinal, semifinal, Ural, Tatarstan | 0, 1, 2 |
| university, autumn 2008 | 1, 2 |
| quarterfinal | 1, 2, 3 |
| semifinal | 1, 2, 4 |
| selection for the Ural championship | 1, 2, 5 |
| Ural championship | 1, 5 |
| quarterfinal, university, semifinal | 1, 2, 6 |
| Battle of Generations | 1, 6, 7 |
| selection for the Ural championship | 5, 6 |
| Ural championship | 1, 5, 6 |
| university, quarterfinal, All-Siberian, semifinal | 1, 8, 9 |
| the last Ural championship | 1, 3, 10 |
| SWERC | 1, 12, 13 |

Summing up gives 5, 21, 12, 2, 1, 4, 6, 1, 4, 4, 1, 0, 1, 1 contests
for players 0 to 13. `O(1)`.

Pitfalls:

- player 11 only took part in the warm-up round, so the answer is 0;
- some contests were played by two people: the 2008 university
  championship without player 3, a Ural championship without player 2,
  and a selection round without player 1;
- the SWERC contest from the end of the story counts too.

The table agrees with an independent accepted implementation for all
fourteen players.

## Optimized solutions

Go and Python preserve the same fourteen-entry contest count table. Go reads the identifier directly into a fixed byte buffer and reuses it for the answer. Go accesses standard handles through syscall.Read and syscall.Write, handling interrupted calls and partial writes. The PyPy version uses unbuffered binary streams to read the identifier and write the pre-encoded answer without text formatting.

The accepted PyPy 3.10 x64 run takes 0.14 s versus 0.078 s for the base and uses 208 KB versus 388 KB.

The accepted base implementations [1873_implementation.cpp](1873_implementation.cpp), [1873_implementation.java](1873_implementation.java), [1873_implementation.rs](1873_implementation.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1873_implementation.cpp](1873_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 128 KB | 11290960 |
| [1873_implementation.go](1873_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1072 KB | 11290961 |
| [1873_implementation.java](1873_implementation.java) \* | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1584 KB | 11290964 |
| [1873_implementation.py](1873_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 388 KB | 11290962 |
| [1873_implementation.rs](1873_implementation.rs) \* | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 240 KB | 11290966 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1873_implementation_optimized.go](1873_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 288 KB | 11311200 |
| [1873_implementation_optimized.py](1873_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(1) | AC | 0.14 s | 208 KB | 11311240 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
