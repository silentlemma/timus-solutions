# 1299. Psylonians

[Timus 1299](https://acm.timus.ru/problem.aspx?space=1&num=1299) · difficulty 1525 · implementation

Original problem by Pavel Egorov, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Simulate one decision of a combat robot. It has energy E and
ammunition W, one of four behaviours, and sees M enemies with average
energy MP, the most dangerous one at an angle a. It answers with one
command:

- `LEFT X`, `RIGHT X`, `FRONT X`, `BACKWARD X` with X = min(100, E);
- `FIRE P` with P = min(20, W);
- `STOP`.

The behaviours:

- guard (G): with no enemies, `STOP`; if |a| < 5, fire; otherwise turn
  towards the target, left for a ≥ 5 and right for a ≤ −5;
- defence (D): if 20 · M ≥ W, retreat while firing, otherwise guard;
- attack (A), with N own robots of average energy NP: if
  N · NP > 3 · M · MP, advance while firing, otherwise retreat while
  firing;
- patrol (P), with the deviation d from the next route point: with
  enemies, defence; otherwise head for the point with the front or the
  back, whichever needs the smaller turn, turning if that angle is
  more than 20 and moving otherwise.

Retreating while firing moves backwards when there are no enemies or
the target is at least 5 degrees off, and fires otherwise. Advancing
does the same with `FRONT` and 10 degrees.

Angles are from −179 to 180; all other numbers are from 0 to 1000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

E and W; the behaviour letter; M, MP and a; for an attack also N and
NP, for a patrol also d.

## Output

One command.

## Examples

### Example 1

Input:

```
100 100
P
0 0 0
-100
```

Output:

```
LEFT 100
```

### Example 2

Input:

```
10 1000
A
1 10 30
100 1000
```

Output:

```
FRONT 10
```

### Example 3

Input:

```
10 1000
G
1 10 4
```

Output:

```
FIRE 20
```

## Solution

The rules are applied exactly as listed, with whole numbers only.
Three points of the statement need a reading:

- Positive angles lie to the left. The guard turns left for a ≥ 5, and
  the first example agrees: the point is 100 degrees off to the right,
  so the back is 80 degrees off to the left, and the robot turns
  `LEFT`.
- "At least 5 (or 10) degrees off" while retreating or advancing is
  read as |a| ≥ 5 (or 10), the same absolute angle the guard uses. A
  robot fires only when it is aimed.
- For a patrol the back points along d − 180 (or d + 180 for d ≤ 0).
  When front and back need the same turn, at d = ±90, the front is
  kept, so d = 90 gives `LEFT` (test 19).

`O(1)`.

Pitfalls:

- the thresholds are exact: a = 5 already turns (test 05), and a
  deviation of 20 still moves (tests 13 and 16);
- exactly triple enemy strength still means retreat: the attack
  condition is strict (test 10);
- the amounts are capped by what the robot has: `FIRE 5` with 5 units
  left (test 10), `BACKWARD 0` with no energy (test 16);
- a patrol that meets an enemy follows the defence rules, not the
  route (test 18).

The answers were compared with an independent implementation of the
same reading on 400 random inputs, with angles near every threshold.

## Language notes

- All languages keep the rules as small functions that call each
  other: patrol calls defence, which calls guard or retreat.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1299_implementation.cpp](1299_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 200 KB |
| [1299_implementation.go](1299_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1100 KB |
| [1299_implementation.java](1299_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1684 KB |
| [1299_implementation.py](1299_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 676 KB |
| [1299_implementation.rs](1299_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 236 KB |
