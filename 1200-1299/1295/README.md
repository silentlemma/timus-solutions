# 1295. Crazy Notions

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · difficulty 151 · number_theory

Original problem by Den Raskovalov, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

How many zeros does the decimal number 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ end with,
for 1 ≤ n ≤ 300 000?

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The number n.

## Output

The number of trailing zeros.

## Examples

### Example 1

Input:

```
1
```

Output:

```
1
```

### Example 2

Input:

```
3
```

Output:

```
2
```

## Solution

The sum has more than 180 000 digits for the largest n, but its trailing
zeros are limited by the power of 2 in it. Let S = 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ.

- n = 1: S = 10, one zero.
- Even n: 1ⁿ + 3ⁿ ≡ 1 + 1 = 2 (mod 4), and 2ⁿ, 4ⁿ are multiples of 4,
  so S is divisible by 2 but not by 4.
- Odd n ≥ 3: 3ⁿ ≡ 3 (mod 8), so 1ⁿ + 3ⁿ ≡ 4 (mod 8), while 2ⁿ and 4ⁿ
  are multiples of 8; S is divisible by 4 but not by 8.

So S never ends in three zeros, and S mod 100 decides everything: 2
zeros if it is 0, 1 zero if it ends in 0, none otherwise. The four
powers modulo 100 come from fast exponentiation. `O(log n)`.

In fact the answer depends only on n mod 20: 0 when 4 divides n, 2
when n leaves 3 mod 4 or 5 mod 20, and 1 otherwise. The solutions
compute it directly rather than rely on this table.

Pitfalls:

- n leaving 1 mod 4 usually gives one zero, but n = 5, 25, … give two
  (tests 05 and 06);
- the full sum can be built with big integers, but it is never needed:
  only its last two digits matter.

The results were compared with the exact big-integer sum for every n
up to 3000.

## Optimized solutions

The optimized Java solution parses `n` by hand from a 4 KB buffer filled
from `System.in` instead of creating a `Scanner`, so the JVM does not
load the scanner and its regular expressions; the powers modulo 100 are
the same: {1295_number_theory_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1295_number_theory_optimized.java`: time reduction +12.80%; memory
  reduction +79.75%; base: `1295_number_theory.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1295_number_theory.cpp](1295_number_theory.cpp).
- [1295_number_theory.go](1295_number_theory.go).
- [1295_number_theory.rs](1295_number_theory.rs).

- Python uses the built-in three-argument `pow`; the other languages
  square and multiply by hand modulo 100.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB | 11284634 |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB | 11284638 |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB | 11284648 |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB | 11284644 |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB | 11284651 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory_optimized.java](1295_number_theory_optimized.java) | Java 1.8 | number_theory | O(log n) | AC | 0.109 s | 324 KB | 11305839 |
