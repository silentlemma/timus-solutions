# 1519. Formula 1

[Timus 1519](https://acm.timus.ru/problem.aspx?space=1&num=1519) · difficulty 467 · dp

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A field of N × M cells (2 ≤ N, M ≤ 12) has some cells taken by burrows.
A race track is one closed loop that passes through every free cell
exactly once, moving between cells that share a side. Count the
tracks; the count fits in 63 bits.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then N rows of M characters: '.' free, '*' a burrow. At least
four cells are free.

## Output

The number of tracks.

## Examples

### Example 1

Input:

```
4 4
**..
....
....
....
```

Output:

```
2
```

### Example 2

Input:

```
4 4
....
....
....
....
```

Output:

```
6
```

## Solution

Dynamic programming over a broken profile, cell by cell in row order,
with the connectivity of the pieces crossing the profile as the state.
The profile has M + 1 plugs: the lower sides of the cells already done
in the current row's columns and the left side of the current cell.
Each plug is empty or an end of a path piece, and the two ends of every
piece nest like brackets, so a plug is "(", ")" or nothing: 2 bits, and
a state fits in 26 bits. At a free cell with left plug L and upper plug
U:

- no plugs: start a new piece going right and down;
- one plug: continue it right or down;
- "(" and "(": join the pieces, and the ")" matching U becomes "(";
- ")" and ")": join them, and the "(" matching L becomes ")";
- ")" and "(": join two pieces into one;
- "(" and ")": this closes a loop, allowed only at the last free cell
  with no other plugs left, and then it counts.

A burrow passes only states with both plugs empty. At the end of a row
the profile shifts by one plug. On the empty 12 × 12 field at most about
14000 states appear at once, and the work is `O(N·M·S)` for S states.

Pitfalls:

- the loop may only close at the last free cell, when nothing else is
  open (test 09);
- an odd number of free cells, or a free area cut off from the rest,
  gives 0 (tests 05, 06, 08);
- the empty 12 × 12 field has about 1.08·10¹⁸ tracks, so the counts
  need 64 bits (test 03);
- holes scattered one by one usually leave no track, so the generated
  tests mostly cut out whole 2 × 2 blocks (gen1, gen2, gen3).

## Language notes

- Python runs under PyPy: CPython exceeds the 1 s limit on the judge's
  test 18.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1519_dp.cpp](1519_dp.cpp) | G++ 13.2 x64 | dp | O(N * M * S) | AC | 0.203 s | 2076 KB |
| [1519_dp.go](1519_dp.go) | Go 1.14 x64 | dp | O(N * M * S) | AC | 0.203 s | 10420 KB |
| [1519_dp.java](1519_dp.java) | Java 1.8 | dp | O(N * M * S) | AC | 0.328 s | 18436 KB |
| [1519_dp.py](1519_dp.py) | PyPy 3.10 x64 | dp | O(N * M * S) | AC | 0.609 s | 10768 KB |
| [1519_dp.rs](1519_dp.rs) | Rust 1.75 x64 | dp | O(N * M * S) | AC | 0.062 s | 1600 KB |
