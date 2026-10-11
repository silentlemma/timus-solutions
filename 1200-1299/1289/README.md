# 1289. One-Way Ticket

[Timus 1289](https://acm.timus.ru/problem.aspx?space=1&num=1289) · difficulty 398 · math

Original problem by Leonid Volkov, from the Ural State University Personal Contest 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The compartments of a ship are numbered from 0 to 10^N − 1, every number
written with exactly N digits, leading zeros included; N is even and at
most 200 000. A compartment is free of ore on the way back when the
digital root of the first half of its number equals the digital root of
the second half. Count these compartments.

The digital root of a number is found by adding up its digits again and
again until a single digit remains; the digital root of 0 is 0.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The even number N.

## Output

The count, in full.

## Examples

### Example 1

Input:

```
2
```

Output:

```
10
```

## Solution

Let m = N / 2 and look at one half, a number from 0 to 10^m − 1. Its
digital root is 0 only for the number 0. For positive numbers the
digital root runs 1, 2, …, 9, 1, 2, … and 10^m − 1 is a multiple of 9,
so each root from 1 to 9 is taken by exactly k = (10^m − 1) / 9 numbers,
where k = 11…1 is written with m ones. The count is therefore

1 + 9 · k².

It has up to 200 000 digits, but no big-integer arithmetic is needed.
Since 9 · k = 10^m − 1, we get 9 · k² = k · 10^m − k: m ones followed by
m zeros, minus m ones. For m ≥ 2 this subtraction gives
1…1 0 8…8 9 (m − 1 ones, m − 1 eights), and adding 1 turns the final
89 into 90:

- m = 0: 1;
- m = 1: 10;
- m ≥ 2: m − 1 ones, a 0, m − 2 eights, then 90.

For example N = 6 gives 110890. The answer is printed as a string,
`O(N)`.

Pitfalls:

- with N = 0 there is one compartment, and it counts (test 02);
- N = 2 does not follow the general pattern (test 01);
- the answer for N = 200 000 has 200 000 digits (test gen3).

## Language notes

- Python: since 3.11 converting an integer of more than 4300 digits to
  text raises an error unless the limit is lifted, one more reason to
  build the digits directly.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1289_math.cpp](1289_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 396 KB |
| [1289_math.go](1289_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1688 KB |
| [1289_math.java](1289_math.java) | Java 1.8 | math | O(N) | AC | 0.093 s | 1272 KB |
| [1289_math.py](1289_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 648 KB |
| [1289_math.rs](1289_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.001 s | 596 KB |
