# 1053. Cutting pieces until one remains

[Timus 1053](https://acm.timus.ru/problem.aspx?space=1&num=1053) · difficulty 343 · number_theory

Original problem from the Rybinsk State Aviation Academy.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` pieces (`1 ≤ N ≤ 1000`) with integer lengths from 1 to
`2^31 − 1`. While more than one piece is left, take any two: if they are
equal, throw one away; otherwise cut a part as long as the shorter piece
off the longer one and throw that part away. Print the length of the last
piece, or `IMPOSSIBLE` if it depends on the choices.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lengths, one per line.

## Output

The length of the last piece.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3
2
3
4
```

Output:

```
1
```

### Example 2

Input:

```
4
12
18
30
42
```

Output:

```
6
```

## Solution

Both steps keep the greatest common divisor of all lengths:
`gcd(a, b) = gcd(a − b, b)`, and dropping one of two equal pieces does not
change the set of divisors. The process ends with a single piece, and the
gcd of one number is the number itself, so the last piece is always the
gcd of the initial lengths, whatever the choices. `IMPOSSIBLE` is never
the answer. `O(N log L)`.

This is the subtraction form of Euclid's algorithm, run on many numbers
at once.

Pitfalls:

- the lengths reach `2^31 − 1`: read them into 64-bit integers or at
  least unsigned 32-bit ones;
- a single piece is the answer by itself;
- simulating the cuts one by one is far too slow for lengths like
  `2^31 − 1` and 1.

## Language notes

- All languages fold the lengths with Euclid's algorithm.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1053_number_theory.cpp](1053_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log L) | AC | 0.015 s | 132 KB |
| [1053_number_theory.go](1053_number_theory.go) | Go 1.14 x64 | number_theory | O(N log L) | AC | 0.015 s | 1100 KB |
| [1053_number_theory.java](1053_number_theory.java) | Java 1.8 | number_theory | O(N log L) | AC | 0.093 s | 776 KB |
| [1053_number_theory.py](1053_number_theory.py) | Python 3.12 x64 | number_theory | O(N log L) | AC | 0.078 s | 488 KB |
| [1053_number_theory.rs](1053_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log L) | AC | 0.015 s | 244 KB |
