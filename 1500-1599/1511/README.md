# 1511. Fiscal Operations

[Timus 1511](https://acm.timus.ru/problem.aspx?space=1&num=1511) · difficulty 1207 · dp

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tax return states three positive numbers A, B and C (each below
10¹⁰⁰⁰), but A + B ≠ C. A digit can be replaced by another for a fine
equal to the absolute difference of the two digits; the length of a
number cannot change and its first digit cannot become 0. Find the
smallest total fine that makes A + B = C, or print -1.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A, B and C, one per line.

## Output

The smallest total fine, or -1.

## Examples

### Example 1

Input:

```
123
554
345
```

Output:

```
8
```

## Solution

A and B cannot be longer than C, since their sum would then be longer
too. Otherwise add column by column from the lowest digit, as on paper,
with the carry as the state: cost[carry] is the cheapest fix of the
columns done so far that passes this carry on. In each column try every
digit x for A and y for B (only 0 past a number's length, and not 0 in
its first digit); the digit of C is then (x + y + carry) mod 10, which
must not be 0 in C's first digit, and the fine is the sum of the three
absolute differences. The answer is cost[0] after the last column of C. At most
2 · 100 transitions per column, `O(len(C))` with a factor of 200.

Pitfalls:

- the first digit cannot become 0, so 1 + 1 = 1 needs C fixed to 2
  (test 02);
- C shorter than A, or at least two digits longer than both addends, gives -1
  (tests 03, 04, gen3);
- when C is one digit longer, the top columns of A and B must carry
  (test 06, gen2);
- the numbers have up to 1000 digits, so they are handled as strings of
  digits (gen1, gen5).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1511_dp.cpp](1511_dp.cpp) | G++ 13.2 x64 | dp | O(len(C)) | AC | 0.031 s | 388 KB |
| [1511_dp.go](1511_dp.go) | Go 1.14 x64 | dp | O(len(C)) | AC | 0.031 s | 1080 KB |
| [1511_dp.java](1511_dp.java) | Java 1.8 | dp | O(len(C)) | AC | 0.125 s | 636 KB |
| [1511_dp.py](1511_dp.py) | Python 3.12 x64 | dp | O(len(C)) | AC | 0.171 s | 768 KB |
| [1511_dp.rs](1511_dp.rs) | Rust 1.75 x64 | dp | O(len(C)) | AC | 0.046 s | 228 KB |
