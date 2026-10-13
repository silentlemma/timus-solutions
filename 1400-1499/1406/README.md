# 1406. Next Number

[Timus 1406](https://acm.timus.ru/problem.aspx?space=1&num=1406) · difficulty 344 · greedy

Original problem by Alexander Ipatov, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A K-digit number N, K ≤ 2000, possibly with leading zeros, is given.
Print the smallest K-digit number greater than N with the same sum of
digits, again with leading zeros, or -1 if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N with all its K digits.

## Output

The next number, or -1.

## Examples

### Example 1

Input:

```
113
```

Output:

```
122
```

### Example 2

Input:

```
0050
```

Output:

```
0104
```

## Solution

A larger number with the same sum agrees with N up to some position,
has a larger digit there, and the digits after it give back what that
digit took. The next number changes as late a position as possible and
raises its digit by exactly one, so look for the rightmost digit below 9
with a positive sum after it. Raise it by one and rebuild the tail with
that sum minus one in its smallest form: zeros first and the sum pushed
to the end, nines from the right. If no digit qualifies, the answer is
-1. `O(K)`.

Pitfalls:

- leading zeros are part of the number and must be kept (example 2 and
  test 09);
- 0, 9 and numbers like 1000 have no next number (tests 05 to 07, and
  generated test 3, the largest number of its sum);
- the number has up to 2000 digits, far beyond fixed-width integer types;
  Python's `int` supports arbitrary precision, but leading zeros still
  require preserving the width (test 09).

The answers were compared with counting up number by number on 2 000
random numbers of up to five digits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1406_greedy.cpp](1406_greedy.cpp) | G++ 13.2 x64 | greedy | O(K) | AC | 0.015 s | 376 KB |
| [1406_greedy.go](1406_greedy.go) | Go 1.14 x64 | greedy | O(K) | AC | 0.031 s | 1088 KB |
| [1406_greedy.java](1406_greedy.java) | Java 1.8 | greedy | O(K) | AC | 0.125 s | 1576 KB |
| [1406_greedy.py](1406_greedy.py) | Python 3.12 x64 | greedy | O(K) | AC | 0.093 s | 552 KB |
| [1406_greedy.rs](1406_greedy.rs) | Rust 1.75 x64 | greedy | O(K) | AC | 0.062 s | 200 KB |
