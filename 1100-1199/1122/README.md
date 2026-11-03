# 1122. The fewest moves that turn a 4 × 4 board to one colour

[Timus 1122](https://acm.timus.ru/problem.aspx?space=1&num=1122) · difficulty 251 · bitmask

Original problem by Leonid Volkov, Oleg Kats and Alexander Somov, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A `4 × 4` board holds two-sided counters, white (`W`) or black (`B`) side
up. A move picks a cell and flips the counters marked by a fixed `3 × 3`
pattern centred on it; the pattern may be anything, need not be symmetric,
and the parts that fall outside the board are ignored. Find the fewest
moves that make all 16 counters show the same colour, or print
`Impossible`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Four lines of the board, then three lines of the pattern (`1` flips,
`0` does not).

## Output

The fewest moves, or `Impossible`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
WWWW
WBBW
WBWW
WWWW
101
010
101
```

Output:

```
Impossible
```

## Solution

As bit masks, a move XORs the board with a fixed mask for its cell. XOR is
commutative and a move repeated in the same cell cancels itself, so any
sequence of moves is equivalent to a set of cells, each used once. There
are only `2^16` sets: compute the combined flip of every set from the set
without its lowest cell, `flips[s] = flips[s − lowest] ^ move[lowest]`,
and keep the smallest set whose flip equals the board (all white) or the
board with every bit inverted (all black). `O(2^16)`.

Pitfalls:

- either colour is a valid goal, so both targets must be tried;
- the pattern is centred on the chosen cell and clipped at the edges, so
  the same pattern flips fewer counters near the border;
- some patterns can never touch certain cells (for example a single corner
  of the pattern never reaches the last row and column), which makes many
  boards impossible.

The answers were checked against a breadth-first search over all `2^16`
board states, one move at a time, on every test and 40 random games.

## Optimized solutions

Split the 16 moves into two groups of eight. Enumerate each half in Gray
order, so one changed move updates its XOR effect. For every effect in the
left half, retain the fewest moves that produce it. For a right-half effect
`r` and target `t`, look up `t XOR r` on the left, trying both final colours.
Every subset has exactly one such split; keeping only the cheapest left
representation cannot discard an optimal answer, even when a pattern has
dependent moves. There are two lists of `2^8` subsets instead of `2^16`.
With hash tables, expected time and space are `O(2^8)`; hash-table worst-case
time can be quadratic in the number of entries.

All five distinct implementations reduce measured memory by at least 30%
against their unchanged Accepted bases: C++ 57.0%, Go 31.1%, Java 73.9%,
Python 76.1%, Rust 43.5%. Times stay the same or improve; a one-tick
difference is not treated as a reliable speedup. C++, Java and Python meet
the ranking goal in the snapshot of 1 November 2026. The filtered Go and
Rust samples contain no other authors, so they provide no competitive
ranking evidence. Both the exhaustive base and the meet-in-the-middle
versions were also checked against independent state-space oracles.

## Language notes

The five base sources enumerate all `2^16` sets; Python uses bit_length and bit counts. The five new sources use two hash-table searches over eight moves each.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1122_bitmask.cpp](1122_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^16) | AC | 0.015 s | 428 KB | 11279286 |
| [1122_bitmask.go](1122_bitmask.go) | Go 1.14 x64 | bitmask | O(2^16) | AC | 0.031 s | 1608 KB | 11279289 |
| [1122_bitmask.java](1122_bitmask.java) | Java 1.8 | bitmask | O(2^16) | AC | 0.109 s | 1852 KB | 11279292 |
| [1122_bitmask.py](1122_bitmask.py) | Python 3.12 x64 | bitmask | O(2^16) | AC | 0.109 s | 3192 KB | 11279291 |
| [1122_bitmask.rs](1122_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^16) | AC | 0.031 s | 736 KB | 11279293 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1122_bitmask_meet_in_middle.cpp](1122_bitmask_meet_in_middle.cpp) | G++ 13.2 x64 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.015 s | 184 KB | 11308016 |
| [1122_bitmask_meet_in_middle.go](1122_bitmask_meet_in_middle.go) | Go 1.14 x64 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.031 s | 1108 KB | 11308019 |
| [1122_bitmask_meet_in_middle.java](1122_bitmask_meet_in_middle.java) | Java 1.8 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.093 s | 484 KB | 11308020 |
| [1122_bitmask_meet_in_middle.py](1122_bitmask_meet_in_middle.py) | Python 3.12 x64 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.078 s | 764 KB | 11308012 |
| [1122_bitmask_meet_in_middle.rs](1122_bitmask_meet_in_middle.rs) | Rust 1.75 x64 | bitmask, meet_in_middle | O(2^8) expected | AC | 0.015 s | 416 KB | 11308021 |
