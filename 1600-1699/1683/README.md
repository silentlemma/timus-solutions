# 1683. Fridge

[Timus 1683](https://acm.timus.ru/problem.aspx?space=1&num=1683) · difficulty 137 · greedy

Original problem by Stanislav Vasilyev, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A paper strip 1 cm wide and n cm long is folded into a 1 × 1 cm square
of n layers. Each fold measures a whole number of centimetres from the
left end and folds that part over to the right, so the left end moves
by that amount. Find the fewest folds and the lengths measured.

## Input

n (1 ≤ n ≤ 10⁹).

## Output

The number of folds, then the measured lengths in order. Any shortest
sequence is accepted.

## Examples

### Example 1

Input:

```
12
```

Output:

```
4
5 3 2 1
```

## Solution

Folding x cm of a strip of length L is possible only if the flap fits on
the rest, x ≤ L − x, and leaves a strip of L − x ≥ ⌈L / 2⌉. So no fold
more than halves the strip, rounding up, and folding ⌊L / 2⌋ every time
achieves exactly that: the number of folds is the least m with
2ᵐ ≥ n. `O(log n)`.

Pitfalls:

- n = 1 needs no folds: print 0 and an empty list;
- the example's 5 3 2 1 is one of many answers, so a checker compares
  the count and replays the folds.

The checker replays every fold and compares the count with the
greedy one.

## Optimized solutions

The optimized C++ solution keeps the folds in a fixed array of
30 numbers on the stack instead of a growing `std::vector`. Since
n ≤ 10⁹ < 2³⁰, at most 30 halvings bring the strip down to 1 cm, so the
array always suffices and the program itself allocates nothing on the
heap: {1683_greedy_optimized.cpp}.

The optimized Java solution reads the single line with a
`BufferedReader` and converts it with `Long.parseLong` instead of
creating a `Scanner`, whose regular expressions and locale data cost far
more than 30 halvings: {1683_greedy_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1683_greedy_optimized.cpp`: time reduction +0.00%; memory reduction
  +47.92%; base: `1683_greedy.cpp`.

- `1683_greedy_optimized.java`: time reduction +25.60%; memory reduction
  +72.84%; base: `1683_greedy.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1683_greedy.go](1683_greedy.go).
- [1683_greedy.rs](1683_greedy.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy.cpp](1683_greedy.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 192 KB | 11288846 |
| [1683_greedy.go](1683_greedy.go) | Go 1.14 x64 | greedy | O(log n) | AC | 0.031 s | 1096 KB | 11288848 |
| [1683_greedy.java](1683_greedy.java) | Java 1.8 | greedy | O(log n) | AC | 0.125 s | 1664 KB | 11288850 |
| [1683_greedy.py](1683_greedy.py) | Python 3.12 x64 | greedy | O(log n) | AC | 0.125 s | 372 KB | 11288849 |
| [1683_greedy.rs](1683_greedy.rs) | Rust 1.75 x64 | greedy | O(log n) | AC | 0.015 s | 244 KB | 11288851 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy_optimized.cpp](1683_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 100 KB | 11304447 |
| [1683_greedy_optimized.java](1683_greedy_optimized.java) | Java 1.8 | greedy | O(log n) | AC | 0.093 s | 452 KB | 11304448 |
