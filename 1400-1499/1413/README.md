# 1413. Mars Jumper

[Timus 1413](https://acm.timus.ru/problem.aspx?space=1&num=1413) · difficulty 180 · simulation

Original problem by Stanislav Vasiliev, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A rover is driven from a numeric keypad: every key from 1 to 9 except 5
makes a jump of exactly one metre in the direction of that key from the
centre 5 (8 is north, 6 east, 9 north-east and so on), 5 takes a soil
sample and 0 makes the rover destroy itself. Given up to 10⁶ key
presses, print where the rover ends: at the first 0, or after the last
key if there is no 0. The answer is the shift east and north, with an
absolute or relative error of at most 10⁻¹⁰.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The digits of the key presses.

## Output

X and Y, the shift east and north.

## Examples

### Example 1

Input:

```
1236987412369870234567890123456789
```

Output:

```
1.0000000000 0.0000000000
```

## Solution

Count how many times each key was pressed before the first 0. A
straight jump moves one axis by a whole metre and a diagonal one moves
both axes by 1/√2, so the end point is (straight sum) + (diagonal sum)
/ √2 on each axis, computed from integer sums. Counting avoids rounding
at every jump, but the final floating-point multiplication, addition
and ten-decimal output still round; the absolute error can slightly
exceed 10⁻¹⁰. `O(n)`.

Pitfalls:

- keys after the first 0 must be ignored (tests 01, 05, gen2);
- a diagonal jump is one metre long, not √2 (test 04);
- diagonal coordinates are irrational, so counting does not make the
  final coordinates exact (test 04);
- reading a million characters one at a time through slow input calls
  can take a large part of the 0.5 seconds, so the input is read in
  big blocks.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1413_simulation.cpp](1413_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 1640 KB |
| [1413_simulation.go](1413_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.015 s | 3196 KB |
| [1413_simulation.java](1413_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.125 s | 980 KB |
| [1413_simulation.py](1413_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.093 s | 3072 KB |
| [1413_simulation.rs](1413_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 2136 KB |
