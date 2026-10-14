# 1575. Yekaterinburg Subway 2

[Timus 1575](https://acm.timus.ru/problem.aspx?space=1&num=1575) · difficulty 861 · bfs

Original problem by Alexander Ipatov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The statement shows a map of a future subway: 70 stations on 8 lines,
one of them a circle, with changes between 2 to 4 lines at some
stations. A run between neighbouring stations takes a minute, and
changes and waiting take no time. Answer up to 4900 questions: the
least number of minutes from one station to another.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number of questions, then two station names per line.

## Output

One number of minutes per question.

## Examples

### Example 1

Input:

```
6
Prospekt_Kosmonavtov Geologicheskaya
Shevchenko Vilonovskaya
Koltsovo Zelyony_ostrov
Teatralnaya Kamennye_palatki
China_town Italyanskaya
1905_year_square 1905_year_square
```

Output:

```
6
3
11
3
9
0
```

## Solution

The only real work is copying the map from the picture. Each line is
written down as its stations in order, and the circle line also joins
its last station to its first. A change station is drawn as two or
more circles side by side, sometimes with a short piece of line between
them, but it is one station: the eight lines name exactly 70 stations,
so every circle belongs to a named one. Teatralnaya, for example, joins
the light blue, blue and yellow lines, and 1905_year_square four lines.

With free changes, the answer is the number of runs on a shortest path
in the graph of stations, found by a breadth-first search from every
station once. `O(70 · edges + questions)`. The map was copied from the
picture independently and the answers for all 4900 ordered pairs agree
with an independent program.

Pitfalls:

- two stations are written differently in the picture than in the
  input: `Prospekt Kosmonavtov` and `Kamennye palatki` appear with a
  space and a line break, but come with underscores;
- the circle line is a ring of 12 stations;
- a question may ask for the way from a station to itself (0).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1575_bfs.cpp](1575_bfs.cpp) | G++ 13.2 x64 | bfs | O(V E + Q) | AC | 0.015 s | 408 KB |
| [1575_bfs.go](1575_bfs.go) | Go 1.14 x64 | bfs | O(V E + Q) | AC | 0.031 s | 2400 KB |
| [1575_bfs.java](1575_bfs.java) | Java 1.8 | bfs | O(V E + Q) | AC | 0.171 s | 6332 KB |
| [1575_bfs.py](1575_bfs.py) | Python 3.12 x64 | bfs | O(V E + Q) | AC | 0.109 s | 1532 KB |
| [1575_bfs.rs](1575_bfs.rs) | Rust 1.75 x64 | bfs | O(V E + Q) | AC | 0.046 s | 836 KB |
