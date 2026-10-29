# 2031. A row that rotates into consecutive integers

[Timus 2031](https://acm.timus.ru/problem.aspx?space=1&num=2031) · difficulty 88 · bruteforce

Original problem by Nikita Sivukhin, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Construct a row of `n` decimal numbers that becomes an increasing consecutive
segment of positive integers when the entire row is rotated by 180 degrees.
Every printed number must have exactly two digits; pad a single-digit number
with a leading zero. Rotation reverses the order of numbers and also reverses
the digits inside every number. Digits `0`, `1`, `8` keep their shapes; `6`
and `9` exchange shapes. Other digits become unreadable and cannot be used.

Input bound: `1 ≤ n ≤ 99`. Time limit: 1 second. Memory limit: 64 MB.

## Input

One integer `n`, the required number of words in the row.

## Output

Print any valid row of `n` two-digit numbers, separated by spaces. If no
row exists, print exactly `Glupenky Pierre`. The rotated numbers must
all be positive, so `00` is not permitted. Leading zeros in other
two-digit words are essential.

## Checking

A checker rotates the printed row and verifies that it becomes a run of
consecutive positive integers, each written with two readable digits; an
impossibility claim is accepted only when no run exists. Any valid row
is accepted.

## Examples

```
2
```

```
11 01
```

```
99
```

```
Glupenky Pierre
```

## Solution

Only the digits 0, 1, 6, 8 and 9 can be read upside down, so after the
turn only the numbers from 1 to 99 made of them can appear. Go through
1 … 99, count the current run of consecutive readable numbers, and stop
when it reaches n at some number r. Then print r, r − 1, …, r − n + 1
upside down: for each number its units digit turned first and its tens
digit turned second, so the turned row reads the run in increasing
order. If no run is long enough, the answer is `Glupenky Pierre`.
`O(100 + n)`.

The readable numbers are 1, 6, 8, 9, 10, 11, 16, 18, 19, 60, 61, 66, 68,
69, 80, 81, 86, 88, 89, 90, 91, 96, 98, 99; the longest runs, 8–11 and
88–91, have four numbers, so only n ≤ 4 has an answer.

Pitfalls:

- 6 and 9 swap when turned;
- keep the leading zero: 01 turned upside down is 10;
- 00 would turn into 0, which is not positive.

## Optimized solutions

The optimized C++ solution reads `n` with `getchar` and prints the
digits one by one with `putchar` instead of using `iostream` and
building a string: 88 KB instead of 368 KB, with the same time.

## Language notes

- The turned numbers are built from characters, so a leading zero stays.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2031_bruteforce.cpp](2031_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(100+n) | AC | 0.015 s | 368 KB | 11303664 |
| [2031_bruteforce.go](2031_bruteforce.go) | Go 1.14 x64 | bruteforce | O(100+n) | AC | 0.031 s | 1152 KB | 11303665 |
| [2031_bruteforce.java](2031_bruteforce.java) | Java 1.8 | bruteforce | O(100+n) | AC | 0.093 s | 440 KB | 11303530 |
| [2031_bruteforce.py](2031_bruteforce.py) | Python 3.12 x64 | bruteforce | O(100+n) | AC | 0.078 s | 420 KB | 11303666 |
| [2031_bruteforce.rs](2031_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(100+n) | AC | 0.015 s | 204 KB | 11303667 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2031_bruteforce_optimized.cpp](2031_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(100+n) | AC | 0.015 s | 88 KB | 11303668 |
