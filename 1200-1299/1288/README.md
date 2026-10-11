# 1288. Astrolocation

[Timus 1288](https://acm.timus.ru/problem.aspx?space=1&num=1288) · difficulty 2191 · simulation

Original problem by Alexander Mironenko, from the Ural State University Personal Contest 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A locator gives N ≤ 10 000 readings from 0 to 100. Find in them:

- the front wall: the first reading of 95 or more that has some reading
  of 35 or less before it;
- after the front wall at position f, the reading at position m is
  multiplied by 1 + (m − f) · A (0 ≤ A ≤ 0.1, at most three decimals),
  and only these values are used from then on;
- the back wall: the first value of 95 or more at least D positions
  after the front wall, with some value of 35 or less between the walls;
- in each of two zones, positions f + S to f + E but never at or beyond
  the back wall, the largest value (the first of equal ones); an object
  is there if that value reaches the zone's level L.

Report the front wall's position, the back wall's distance from it,
and for each zone the object's distance, no object, or no search when
the zone holds no reading at all.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, D, S1, E1, L1, S2, E2, L2 and A, then the N readings.

## Output

The report lines, word for word as in the example.

## Examples

### Example 1

Input:

```
10 4 1 1 50 2 2 56 0.09
9
26
96
56
21
73
73
93
96
97
```

Output:

```
Surface found at 3.
Bottom found at 4.
Channel 1: Object at 1.
Channel 2: No object.
```

## Solution

The task is a careful simulation of the rules above, in one pass for
each wall and one scan of each zone. `O(N)`.

To avoid rounding, use scaled integers. A has at most three decimals, so
1 + (m − f) · A is an exact number of thousandths. The readings retain
up to six decimals in millionths, so each corrected value is an exact
integer number of 10⁻⁹. The thresholds 95, 35 and L, the
comparisons between values and the search for the first maximum then
need no tolerance at all: 50 attenuated by 1 + 9 · 0.1 is exactly 95, a
wall (test 06).

Pitfalls:

- a reading of 95 or more before any reading of 35 or less is not the
  front wall (test 03);
- a high value closer than D to the front wall is not the back wall,
  but it can be an object (test 04);
- the back wall and everything after it are never searched, and a zone
  that lies wholly there prints "No search." (test 08);
- a zone may run past the end of the readings (test 07);
- with no front wall only "No surface." is printed (test 02).

The answers were compared with an independent implementation on 300
random signals.

## Language notes

- Decimals are parsed by hand into scaled integers: 64-bit,
  or arbitrary precision in Python.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1288_simulation.cpp](1288_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.015 s | 348 KB |
| [1288_simulation.go](1288_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.031 s | 1452 KB |
| [1288_simulation.java](1288_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.109 s | 3492 KB |
| [1288_simulation.py](1288_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.078 s | 1464 KB |
| [1288_simulation.rs](1288_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 380 KB |
