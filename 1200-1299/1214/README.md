# 1214. Undoing a strange procedure

[Timus 1214](https://acm.timus.ru/problem.aspx?space=1&num=1214) · difficulty 102 · math

Original problem by Anatoly Uglov, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A procedure takes two integers `x` and `y`. If both are positive, it runs
`x + y` times a loop body that sets `y ← x² + y`, then `x ← x² + y`, then
`y ← ⌊√(x − y)⌋`, then subtracts `y` from `x` `2y` times; at the end it
prints `x` and `y`. Given what it printed, both from `−32000` to `32000`,
recover the input. No variable ever overflows.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The printed `x` and `y`.

## Output

The input `x` and `y`.

## Examples

### Example 1

Input:

```
1 1
```

Output:

```
1 1
```

## Solution

Follow one turn of the loop from `(x, y)`. First `y` becomes `x² + y`,
then `x` becomes `2x² + y`. Their difference is `x²`, so the new `y` is
`x`. Subtracting it `2x` times takes `2x²` from `2x² + y` and leaves
`y`. So each turn just swaps the two numbers, and the sum `x + y`, which
fixes the number of turns, stays the same. After `x + y` turns the
numbers are swapped exactly when the sum is odd.

So the procedure swaps its input when both numbers are positive and
their sum is odd, and changes nothing otherwise. That is its own inverse:
apply the same rule to the printed pair. `O(1)`.

Pitfalls:

- with a zero or negative number the loop does not run at all, so such a
  pair is printed unchanged;
- the sum, not the numbers themselves, decides the parity.

Running the procedure on every pair from `−3` to `15` and undoing the
result gave back the original pair each time.

## Language notes

- All languages apply the same one-line rule.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1214_math.cpp](1214_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1214_math.go](1214_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1068 KB |
| [1214_math.java](1214_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1584 KB |
| [1214_math.py](1214_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 444 KB |
| [1214_math.rs](1214_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 212 KB |
