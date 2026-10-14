# 1543. Dance Revolution

[Timus 1543](https://acm.timus.ru/problem.aspx?space=1&num=1543) · difficulty 2149 · simulation

Original problem by Denis Musin, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A song is a row of beats, each empty (N) or asking for one of the keys
U, D, L, R. A beat lasts 1000, 500 or 250 ms on Easy, Medium and Hard
(Diff = 1, 2, 3). Given the log of the player's presses, rate each
non-empty beat (a step) by the first press inside it:

- no press: Boo; a wrong key: Miss;
- the right key less than 40 % of the beat after its start: Perfect,
  less than 70 %: Great, otherwise Good.

Presses after the first in a beat and presses in empty beats do not
count. Then compute

- the stage score: the n-th step gives p·n·⌊B / S⌋ with p = 10 for
  Perfect, 5 for Great and 0 otherwise, B = 10⁶·Diff and S = N(N + 1)/2
  for N steps;
- the combo bonus: in a run of Perfect, Great and Good steps the c-th
  step gives 55·c for Perfect, 33·c for Great and 0 for Good; Boo and
  Miss end the run;
- the dance level bonus from dance points (Perfect +2, Great +1, Good 0,
  Boo −4, Miss −5): 0 if the points ever went below zero, else 10⁷ if
  all steps were Perfect, 10⁶ if all were Perfect or Great, and
  otherwise 10⁵, 10⁴, 10³ or 100 for at least 80 %, 64 %, 50 % or less
  of the most points possible, 2N.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The song length (m:ss) and level, the beats, then lines "time key" of
the presses, in milliseconds from the start.

## Output

The five counts, a line of 20 dashes and the four scores, as in the
example.

## Examples

### Example 1

Input:

```
0:30 Easy
NNNNNLNNRNUNNUNNNDDDNNUNNNNRNU
5201 L
8475 R
8735 L
10000 U
13200 U
17284 D
18355 D
19124 D
22222 U
27543 R
29923 U
```

Output:

```
Perfect: 7
Great: 2
Good: 1
Boo: 0
Miss: 0
--------------------
Stage Score: 7181495
Combo Bonus: 2233
Dance Level Bonus: 100000
Total Score: 7283728
```

## Solution

Beat i covers the times [i·T, (i + 1)·T) for the period T. Sort the
presses (they come sorted, but sorting costs nothing) and walk them
with one pointer: before each beat, skip the presses earlier than its
start; the press under the pointer is then the first one of the beat if
it is earlier than the end. The thresholds are compared in integers,
10·elapsed < 4·T and 10·elapsed < 7·T, and so are the shares,
100·points ≥ 80·2N and so on. The song length is not needed: the beats
are given. Scores fit in 64 bits. `O(L + P log P)` for L beats and P
presses.

The statement leaves room for readings. These follow the statement; the
first two are also confirmed on the judge's discussion board, the third
is our reading of "at least 80 %":

- a beat includes its start and excludes its end;
- the level bonus is 0 as soon as the dance points dip below zero, even
  if the final total is good (test 03);
- the shares are compared exactly: 4 points out of 6 are below 80 %
  (4.8), so test 02 gets 10⁴, not 10⁵.

Pitfalls:

- presses at exactly 40 % and 70 % of the beat are Great and Good
  (test 06);
- a wrong first press makes a Miss even if the right key follows
  (test 07);
- a press in an empty beat just before a step does not count for it
  (test 07);
- Good keeps a combo going without adding to it (test 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1543_simulation.cpp](1543_simulation.cpp) | G++ 13.2 x64 | simulation | O(L + P log P) | AC | 0.031 s | 528 KB |
| [1543_simulation.go](1543_simulation.go) | Go 1.14 x64 | simulation | O(L + P log P) | AC | 0.031 s | 1776 KB |
| [1543_simulation.java](1543_simulation.java) | Java 1.8 | simulation | O(L + P log P) | AC | 0.171 s | 4360 KB |
| [1543_simulation.py](1543_simulation.py) | Python 3.12 x64 | simulation | O(L + P log P) | AC | 0.078 s | 1676 KB |
| [1543_simulation.rs](1543_simulation.rs) | Rust 1.75 x64 | simulation | O(L + P log P) | AC | 0.015 s | 644 KB |
