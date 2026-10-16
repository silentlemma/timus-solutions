# 1809. Chapaev and Potatoes

[Timus 1809](https://acm.timus.ru/problem.aspx?space=1&num=1809) · difficulty 598 · implementation

Original problem by Dmitry Ivankov, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Four potatoes lie on distinct cells of a 20 × 20 board. A potato can
shoot another one if they share a row or a column with no potato
between them. Move as few potatoes as possible to free cells so that
every potato can shoot exactly one other.

## Input

Four lines with the coordinates x and y of the potatoes, from 1 to 20.

## Output

The new coordinates in the same order. Any best answer is accepted.

## Examples

### Example 1

Input:

```
1 1
2 2
4 4
4 3
```

Output:

```
1 2
2 2
4 4
4 3
```

## Solution

The goal is a layout where the "can shoot" relation splits the four
potatoes into two pairs. Check the layout as given. Otherwise try
moving one potato to each of the 400 cells. Otherwise two moves always
suffice. If the two kept potatoes see each other, the other two can
form a pair of their own in a row and columns that the kept ones do
not use. If not, each moved potato can go next to one of the kept
ones. So for every choice of the two to move, it is enough to try the
cells next to the kept potatoes and that one separate pair. A stress
run over 20000 random layouts never found the two-move step empty.
`O(1)`.

In the example the second pair, (4, 4) and (4, 3), is already fine, and
moving the first potato to (1, 2) pairs it with (2, 2).

Pitfalls:

- a potato between two others blocks the shot, so four in one line do
  not form pairs;
- a potato may not see more than one other, so a pair must not share a
  line with the other pair;
- the moved potatoes must land on free cells inside the board.

The checker tests the layout and compares the number of moved potatoes
with that of the expected answer. All solutions pass it on random
layouts, crowded corners, single lines and nearly valid layouts, against
an independent accepted implementation that tries every pair of cells.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1809_implementation.cpp](1809_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 204 KB |
| [1809_implementation.go](1809_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1124 KB |
| [1809_implementation.java](1809_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1820 KB |
| [1809_implementation.py](1809_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.125 s | 876 KB |
| [1809_implementation.rs](1809_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 244 KB |
