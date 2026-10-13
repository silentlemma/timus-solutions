# 1415. Mobile Life

[Timus 1415](https://acm.timus.ru/problem.aspx?space=1&num=1415) · difficulty 8920 · geometry, simulation

Original problem by Evgeny Krokhalev, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N base stations (N ≤ 100) stand at integer points; station c has a
threshold distance R_c and a name. The signal power falls in inverse
proportion to the distance, and the phone's indicator shows violet
within R_c, then drops one colour (indigo, blue, green, yellow, orange,
red) for every 2 dB of power lost, staying red beyond that. A phone is
carried along a polyline of M ≤ 1000 segments. On power on it picks the
strongest station, ties going to the smaller name; it stays with that
station until the indicator turns red, and while red it switches to the
strongest station whose signal is not red as soon as one exists. Print
the log of power on, cell changes and colour changes; a red line is
written even if the phone switches at that very moment.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then N lines X Y R name, then M, then M segments X1 Y1 X2 Y2.

## Output

The log.

## Examples

### Example 1

Input:

```
4
0 0 1 Romashka
0 10 1 Lutik
10 10 2 Znaika
10 0 1 Children
2
5 5 -5 -5
-5 -5 5 5
```

Output:

```
Power on. CELL_ID:Znaika, SIGNAL_LEVEL:GREEN
Signal changed. SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:ORANGE
Signal changed. SIGNAL_LEVEL:RED
Cell changed. CELL_ID:Romashka, SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:ORANGE
Signal changed. SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:GREEN
Signal changed. SIGNAL_LEVEL:BLUE
Signal changed. SIGNAL_LEVEL:INDIGO
Signal changed. SIGNAL_LEVEL:VIOLET
Signal changed. SIGNAL_LEVEL:INDIGO
Signal changed. SIGNAL_LEVEL:BLUE
Signal changed. SIGNAL_LEVEL:GREEN
Signal changed. SIGNAL_LEVEL:YELLOW
Signal changed. SIGNAL_LEVEL:ORANGE
```

## Solution

Power is proportional to R / d, so the loss is 10·log₁₀(d / R) dB and
the colour changes on the circles of radius R·10^(k/5) for k = 0..5:
violet inside the first, red outside the last, at 10·R.

Along a segment p(t) = s + t·(e − s), the moments when the distance to
a station equals a radius solve a quadratic in t. Only two kinds of
moments matter: the current station crossing any of its six circles,
and any station crossing its red circle (only then can some station
stop or start being red). Sort these moments, merge the ones closer
than 10⁻⁹, and look at the state just after each group at the midpoint
before the next moment:

- if the phone is not red, a new colour of the current station is
  logged; if it is red now, every station that is not red there is a
  candidate;
- if the phone was red, the candidates are the stations of this group
  that are not red any more.

Among the candidates the strongest one wins, comparing R / d at the
moment itself with a relative tolerance so that stations reaching their
red circles together tie and the smaller name decides. If the winner is
the current station, only the colour is logged; otherwise it is a cell
change, its colour is read just after the moment before its own next
circle, and the moments are rebuilt for the new station. `O(M·N·log N)`.

Pitfalls:

- the phone stays with a weak station while it is not red, even next
  to a much stronger one (tests 04, 10);
- getting the current station back from red is a colour change, not a
  cell change (tests 02, 03);
- several stations can reach their red circles at the same instant;
  equal power then goes to the smaller name, compared byte by byte
  (tests 04, 08, 09, gen3);
- the phone can start red with nothing in reach, and segments can have
  zero length (tests 06, 07);
- the forum mentions inputs where events differ by about 10⁻¹³ that
  even long double cannot order; the judge's tests avoid them.

## Language notes

- Python runs under PyPy: CPython exceeds the 2 s limit on the judge's
  test 20, and PyPy takes 1.8 s, close to the limit, although every
  test here takes well under 0.5 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1415_geometry.cpp](1415_geometry.cpp) | G++ 13.2 x64 | geometry | O(M*N*log N) | AC | 0.125 s | 8800 KB |
| [1415_geometry.go](1415_geometry.go) | Go 1.14 x64 | geometry | O(M*N*log N) | AC | 0.140 s | 6788 KB |
| [1415_geometry.java](1415_geometry.java) | Java 1.8 | geometry | O(M*N*log N) | AC | 0.359 s | 44480 KB |
| [1415_geometry.py](1415_geometry.py) | PyPy 3.10 x64 | geometry | O(M*N*log N) | AC | 1.796 s | 46860 KB |
| [1415_geometry.rs](1415_geometry.rs) | Rust 1.75 x64 | geometry | O(M*N*log N) | AC | 0.093 s | 10192 KB |
