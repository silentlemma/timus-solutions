# 1125. Undoing colour flips at integer distances on a grid

[Timus 1125](https://acm.timus.ru/problem.aspx?space=1&num=1125) · difficulty 236 · bitmask

Original problem by Dmitry Filimonenkov, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A field of `M × N` unit cells (`0 ≤ M, N ≤ 50`) is coloured black (`B`)
and white (`W`). Every time a cell is visited, every cell whose centre is
an integer distance from its centre changes colour, the visited cell
itself included (distance 0). Given the final colours and how many times
each cell was visited (up to `2·10^9`), print the initial colours.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`M N`, then `M` lines of the final colours, then `M` lines of `N` visit
counts.

## Output

`M` lines of the initial colours.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6 6
BWBBWW
BWBBWB
BBWWBW
BBBBBW
BBWWWW
BBWBBW
2 0 12 46 2 0
3 0 0 0 0 200
4 2 1 1 4 2
4 2 1 1 4 4
0 0 0 0 0 0
2 56 24 4 2 2
```

Output:

```
WWBBWW
WBWWBW
WBBBBW
WBWWBW
WBWWBW
WBWWBW
```

## Solution

Only the parity of the flips matters, so only the parity of each visit
count matters. A cell `(r, c)` is flipped once by every odd-visited cell
at an integer-length offset `(dr, dc)`, that is with `dr² + dc²` a perfect
square. Inside a 50 × 50 field there are just 405 such offsets: the cell
itself, the row and column, and Pythagorean ones like `(3, 4)`.

Store each row of odd visits as a bit mask. For a row `r`, the cells it
flips through offset `(dr, dc)` are row `r + dr` shifted by `dc`, so the
flip parity of the whole row `r` is the XOR of those shifted masks over
all offsets. Flipping the final colours by that parity restores the
start. `O(M · K)` mask operations for the `K ≤ 405` offsets, about
20 000.

Pitfalls:

- the visited cell flips too: distance 0 is an integer;
- visit counts up to `2·10^9` only matter by parity;
- `M` or `N` may be 0, and then the field has no cells to print.

The answers were checked against a direct computation over all pairs of
cells, adding the visits at integer distance, on every test and 30
random fields.

## Language notes

- C++, Go, Java and Rust keep the rows in 64-bit words; Python uses its
  integers. Java shifts with `>>>`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1125_bitmask.cpp](1125_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.001 s | 456 KB |
| [1125_bitmask.go](1125_bitmask.go) | Go 1.14 x64 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.031 s | 1092 KB |
| [1125_bitmask.java](1125_bitmask.java) | Java 1.8 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.078 s | 968 KB |
| [1125_bitmask.py](1125_bitmask.py) | Python 3.12 x64 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.046 s | 900 KB |
| [1125_bitmask.rs](1125_bitmask.rs) | Rust 1.75 x64 | bitmask | O(M·K), K ≤ 405 offsets | AC | 0.015 s | 240 KB |
