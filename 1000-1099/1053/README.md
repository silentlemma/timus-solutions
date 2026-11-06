# 1053. Cutting pieces until one remains

[Timus 1053](https://acm.timus.ru/problem.aspx?space=1&num=1053) · difficulty 344 · number_theory

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

- the lengths reach `2^31 − 1`, which still fits in a signed 32-bit
  integer;
- a single piece is the answer by itself;
- simulating the cuts one by one is far too slow for lengths like
  `2^31 − 1` and 1.

## Optimized solutions

Go and Rust update one running gcd as lengths arrive. Once it becomes one, the answer cannot change, so they finish immediately without reading the remaining lengths. Input is buffered and the gcd is printed directly, with constant auxiliary space. Go uses the standard handles directly and completes short writes. Rust reads and writes through the C runtime.

The accepted Rust 1.75 x64 run takes 0.031 s versus 0.015 s for the base and uses 68 KB versus 244 KB.

The accepted base implementations [1053_number_theory.cpp](1053_number_theory.cpp), [1053_number_theory.java](1053_number_theory.java), [1053_number_theory.py](1053_number_theory.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- All languages fold the lengths with Euclid's algorithm.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1053_number_theory.cpp](1053_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log L) | AC | 0.015 s | 132 KB | 11278705 |
| [1053_number_theory.go](1053_number_theory.go) | Go 1.14 x64 | number_theory | O(N log L) | AC | 0.015 s | 1100 KB | 11278706 |
| [1053_number_theory.java](1053_number_theory.java) \* | Java 1.8 | number_theory | O(N log L) | AC | 0.093 s | 776 KB | 11278708 |
| [1053_number_theory.py](1053_number_theory.py) \* | Python 3.12 x64 | number_theory | O(N log L) | AC | 0.078 s | 488 KB | 11278707 |
| [1053_number_theory.rs](1053_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log L) | AC | 0.015 s | 244 KB | 11278709 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1053_number_theory_optimized.go](1053_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(N log L) | AC | 0.015 s | 296 KB | 11311219 |
| [1053_number_theory_optimized.rs](1053_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(N log L) | AC | 0.031 s | 68 KB | 11311238 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
