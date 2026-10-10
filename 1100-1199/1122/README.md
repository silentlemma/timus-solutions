# 1122. The fewest moves that turn a 4 × 4 board to one colour

[Timus 1122](https://acm.timus.ru/problem.aspx?space=1&num=1122) · difficulty 250 · bitmask

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

## Language notes

- All languages walk the same `2^16` sets; the lowest set bit and the bit
  count come from built-in functions, and Python uses
  `(s & -s).bit_length()` and `bin(s).count("1")`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1122_bitmask.cpp](1122_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^16) | AC | 0.015 s | 428 KB |
| [1122_bitmask.go](1122_bitmask.go) | Go 1.14 x64 | bitmask | O(2^16) | AC | 0.031 s | 1608 KB |
| [1122_bitmask.java](1122_bitmask.java) | Java 1.8 | bitmask | O(2^16) | AC | 0.109 s | 1852 KB |
| [1122_bitmask.py](1122_bitmask.py) | Python 3.12 x64 | bitmask | O(2^16) | AC | 0.109 s | 3192 KB |
| [1122_bitmask.rs](1122_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^16) | AC | 0.031 s | 736 KB |
