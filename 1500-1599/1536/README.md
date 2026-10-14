# 1536. Delights of Pipe-weed

[Timus 1536](https://acm.timus.ru/problem.aspx?space=1&num=1536) · difficulty 7335 · dp

Original problem by Sergey Pupyrev, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An expression a1+a2=b (0 ≤ a1, a2, b < 10⁸) is laid out of sticks,
one symbol per cell. Every cell has twelve places for a stick: the
seven of a digital display (top, middle, bottom and four sides), a
slash "/" in the upper half and one in the lower half, the vertical bar
of the plus and the two bars of the equals sign. The statement's picture
draws the symbols as follows (all slashes lean the same way):

| Symbol | Sticks | Places |
|---|---|---|
| `0` | 6 | top, both upper sides, both lower sides, bottom |
| `1` | 3 | upper slash, upper right, lower right |
| `2` | 4 | top, upper right, lower slash, bottom |
| `3` | 4 | top, upper slash, middle, lower slash |
| `4` | 4 | upper left, upper right, middle, lower right |
| `5` | 5 | top, upper left, middle, lower right, bottom |
| `6` | 5 | upper slash, middle, lower left, lower right, bottom |
| `7` | 3 | top, upper slash, lower left |
| `8` | 7 | all seven of the usual digital places |
| `9` | 5 | top, upper left, upper right, middle, lower slash |
| `+` | 2 | middle, a vertical bar through the centre |
| `=` | 2 | two short bars of its own |

Moving at most K sticks (0 ≤ K ≤ 100), turn the expression into a true
sum X+Y=Z with the same number of characters, where X, Y and Z have 1 to
8 digits and no leading zeros. Sticks may not be added or removed. Print
such a sum or "Impossible".

Time limit: 1 second. Memory limit: 64 MB.

## Input

The expression on the first line, K on the second.

## Output

A true expression reachable in at most K moves, or `Impossible`.

## Examples

### Example 1

Input:

```
33+88=127
2
```

Output:

```
33+88=121
```

### Example 2

Input:

```
3+3=7
1
```

Output:

```
Impossible
```

## Solution

If the new expression uses as many sticks as the old one, the fewest
moves are the sticks of the new one that do not lie in a place the old
one already fills in the same cell: those stay, every other stick moves.
So maximise the number of kept sticks under the condition that the total
is unchanged.

Try every length of X and Y (Z takes the rest, and must be at least as
long as both); this fixes the cells of the plus and the equals sign. Then
fill the columns from the right, as in written addition. The state is
the column, the carry and the number of sticks used so far, and the
value is the most sticks kept; a step picks the digits of X and Y in the
column, which fix the digit of Z and the next carry. Digits beyond the
end of X or Y are absent and cost no sticks; the leading digit of a
number longer than one digit must not be 0. A length split is feasible
when the state after the last column has carry 0, all sticks used and
at least total − K sticks kept; the stored choices give the digits.
About 64 splits × 8 columns × 2 carries × 180 stick counts × 100 digit
pairs, under 2·10⁷ steps.

Pitfalls:

- the bar of the plus lies exactly where a middle stick does, so it can
  stay in place when a digit with a middle stick takes the plus's cell, as
  the 5 does in test 05, where the answer needs 17 moves, and 18
  without that;
- the signs may move: in test 05 the plus goes from the fourth cell to
  the second;
- all sticks must be used: in test 07 dropping sticks would allow 3
  moves, keeping them all needs 5; in test 09 the eights hold more
  sticks than any true sum of that length;
- leading zeros are not allowed, which turns a 9-move answer into an
  impossible one in test 06;
- the shapes come from the picture: 1 has a slash at the top, 7 a stick
  at the lower left, and 3 is two bars and two slashes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1536_dp.cpp](1536_dp.cpp) | G++ 13.2 x64 | dp | O(L^3 * S * 100) | AC | 0.015 s | 504 KB |
| [1536_dp.go](1536_dp.go) | Go 1.14 x64 | dp | O(L^3 * S * 100) | AC | 0.031 s | 2608 KB |
| [1536_dp.java](1536_dp.java) | Java 1.8 | dp | O(L^3 * S * 100) | AC | 0.140 s | 1432 KB |
| [1536_dp.py](1536_dp.py) | Python 3.12 x64 | dp | O(L^3 * S * 100) | AC | 0.140 s | 1172 KB |
| [1536_dp.rs](1536_dp.rs) | Rust 1.75 x64 | dp | O(L^3 * S * 100) | AC | 0.031 s | 496 KB |
