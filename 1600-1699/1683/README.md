# 1683. Fridge

[Timus 1683](https://acm.timus.ru/problem.aspx?space=1&num=1683) · difficulty 136 · greedy

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1683_greedy.cpp](1683_greedy.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 192 KB |
| [1683_greedy.go](1683_greedy.go) | Go 1.14 x64 | greedy | O(log n) | AC | 0.031 s | 1096 KB |
| [1683_greedy.java](1683_greedy.java) | Java 1.8 | greedy | O(log n) | AC | 0.125 s | 1664 KB |
| [1683_greedy.py](1683_greedy.py) | Python 3.12 x64 | greedy | O(log n) | AC | 0.125 s | 372 KB |
| [1683_greedy.rs](1683_greedy.rs) | Rust 1.75 x64 | greedy | O(log n) | AC | 0.015 s | 244 KB |
