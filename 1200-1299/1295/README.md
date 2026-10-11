# 1295. Crazy Notions

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · difficulty 151 · number_theory

Original problem by Den Raskovalov, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

How many zeros does the decimal number 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ end with,
for 1 ≤ n ≤ 300 000?

Time limit: 1 second. Memory limit: 64 MB.

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

## Language notes

- Python uses the built-in three-argument `pow`; the other languages
  square and multiply by hand modulo 100.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB |
