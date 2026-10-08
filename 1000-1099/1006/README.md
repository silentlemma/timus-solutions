# 1006. Restoring the order of overlapping square frames

[Timus 1006](https://acm.timus.ru/problem.aspx?space=1&num=1006) · difficulty 988 · greedy

Original problem from the Ural State University Championship 1997.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text screen has 50 columns and 20 rows and is filled with `.` (byte 46).
A square frame with upper left corner in column `x`, row `y` and side `a`
(`a ≥ 2`, the frame lies inside the screen) is drawn by writing these bytes
on its border; a later frame overwrites an earlier one:

| Cell | Byte (cp437) | Character |
|------|--------------|-----------|
| upper left corner | 218 | `┌` |
| upper right corner | 191 | `┐` |
| lower left corner | 192 | `└` |
| lower right corner | 217 | `┘` |
| other cells of the left and right sides | 179 | `│` |
| other cells of the top and bottom sides | 196 | `─` |

The input is the screen after `N` frames (`1 ≤ N ≤ 15`) were drawn. Find any
sequence of at most 2000 frames that, drawn in order on an empty screen, gives
exactly this picture. It does not have to be the original one.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

20 lines of 50 bytes each: the rows of the screen from top to bottom, in the
single-byte cp437 encoding (not UTF-8). A solution should read raw bytes and
accept both LF and CRLF line endings.

## Output

The number `K` of frames, then `K` lines `x y a`: column and row of the upper
left corner (counted from 0) and the side, in drawing order.

## Checking

Any valid answer is accepted. The checker verifies that `0 ≤ K ≤ 2000`, every
frame has `a ≥ 2` and lies inside the screen, and drawing the frames in the
given order on an empty screen yields exactly the input picture.

## Examples

The pictures are shown as characters; the program receives them as cp437 bytes.

### Example 1

Input:

```
........................................┌────────┐
....................┌──────────┐........│........│
...┌───────┐........│..........│........│........│
...│.......│........│..........│........│........│
...│.......│........│..........│........│........│
...│......┌────┐....│..........│........│........│
...│......││...│....│..........│........│........│
...│......││...│....│..........│........│........│
...│......││...│....│..........│........│........│
...│......││...│....│......┌───┐........└────────┘
...└──────└────┘....│......│...│..................
....................│......│...│..................
....................└──────│───│...┌──────┐.......
...........................└───┘...│......│.......
...................................│......│.......
...................................│......│.......
...................................│......│.......
...................................│......│.......
...................................│......│.......
...................................└──────┘.......
```

Output:

```
6
3 2 9
10 5 6
20 1 12
27 9 5
40 0 10
35 12 8
```

## Solution

Undo the drawing from the end. The frame drawn last is fully visible. Once it
is removed, its cells could have held anything before it was drawn, so they
become *wildcards*. In general, a frame **fits** if every cell of its border
either is a wildcard or shows exactly the character this frame would put
there, and at least one of these cells is not yet a wildcard.

Repeatedly scan all corners and sides (`50 · 20` corners, up to 19 sides each,
checking the four corners of a candidate first to reject most of them at once);
every frame that fits is recorded and its border becomes wildcards. Stop when
no non-`.` cell is left. Print the recorded frames in reverse order.

Why it works: drawn in that order, each recorded frame writes correct
characters on its non-wildcard cells, and its wildcard cells are overwritten
by frames recorded earlier, i.e. drawn later. The process never gets stuck:
among the original frames that still cover a non-wildcard cell, take the one
drawn last; every cell of it that it does not show is covered by a later
original frame, whose cells are all wildcards already, so this frame fits.
Each recorded frame turns at least one of the at most 1000 cells into a
wildcard, so `K ≤ 1000`.

A scan looks at about `50 · 20 · 19` candidates, most rejected at a corner, and
only a few scans are needed (each one removes at least the topmost remaining
original frame), so the run time is negligible.

Pitfalls:

- the input is not UTF-8: read bytes, and treat bytes ≥ 128 as unsigned;
- `.` cells must never be covered: they are not wildcards;
- a frame made only of wildcards is useless and is not recorded.

## Language notes

The same scan in every language. Python skips candidates whose upper left cell
is neither `┌` nor a wildcard before building the list of border cells.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1006_greedy.cpp](1006_greedy.cpp) | G++ 13.2 x64 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.015 s | 160 KB |
| [1006_greedy.go](1006_greedy.go) | Go 1.14 x64 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.031 s | 1060 KB |
| [1006_greedy.java](1006_greedy.java) | Java 1.8 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.093 s | 564 KB |
| [1006_greedy.py](1006_greedy.py) | Python 3.12 x64 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.109 s | 1348 KB |
| [1006_greedy.rs](1006_greedy.rs) | Rust 1.75 x64 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.046 s | 224 KB |
