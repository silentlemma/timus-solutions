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

Work with the row after rotation. Every number there is between 1 and
99, and its two digits, including a possible leading zero, belong to
`0,1,6,8,9`. Scan these integers in increasing order. Keep the length of
the current consecutive run of readable numbers, resetting it to zero at
an unreadable number. Once its length reaches `n` at integer `r`, the
target interval `[r-n+1,r]` is available.

To produce its preimage, visit target integers from `r` down to `r-n+1`.
For each one, map its units digit first and its tens digit second through the
rotation map. Append these as characters, preserving width two. If the scan
finishes without a run of length `n`, report impossibility.

### Correctness

The digit map is an involution: applying it twice recovers each readable digit.
Our row is therefore the inverse rotation of the chosen target interval.
The whole-row reversal restores increasing target order, and the reversal and
mapping inside each word restores that target's two digits. Thus the result
rotates to exactly the chosen positive consecutive integers.

Conversely, any valid printed row must rotate to a positive consecutive interval
inside `[1,99]` consisting only of readable digits. The complete scan visits
every integer in that interval consecutively, so its run length reaches `n`.
Consequently a failed scan proves that no answer exists.

The readable positive targets are
`1,6,8,9,10,11,16,18,19,60,61,66,68,69,80,81,86,88,89,90,91,96,98,99`.
Their longest runs are `[8,11]` and `[88,91]`, each of length four.
Hence exactly lengths one through four are feasible; the program
discovers runs instead of using this cutoff as a special case.

The first sample `11 01` rotates to `10 11`. Our program may instead print
`60 80`, which rotates to `08 09` and is equally valid. For the second sample,
length 99 exceeds the maximum run length, so the required phrase is correct.

The scan tests at most 99 integers and emits `n` words on success: `O(100+n)`
time, `O(1)` scan state and `O(n)` buffered output. The fixed two-digit universe
keeps the enumeration work constant.

Pitfalls:

- Rotate the whole row, reversing both word order and digit order.
- Swap `6` and `9`; merely reversing characters is insufficient.
- Keep both printed digits, including leading zero.
- Exclude zero from the target interval.
- An alternative valid interval need not match the sample tokens.

## Language notes

All ports append mapped digit characters rather than converting a
rotated number to an integer, preserving zeros. The map contains a
marker for unreadable digits. Rust computes descending targets as
`r-offset`; the found run guarantees `r ≥ n`, so unsigned subtraction is
safe. No large integers or floating point are needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2031_bruteforce.cpp](2031_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(100+n) | AC | 0.015 s | 372 KB |
| [2031_bruteforce.go](2031_bruteforce.go) | Go 1.14 x64 | bruteforce | O(100+n) | AC | 0.015 s | 1092 KB |
| [2031_bruteforce.java](2031_bruteforce.java) | Java 1.8 | bruteforce | O(100+n) | AC | 0.109 s | 472 KB |
| [2031_bruteforce.py](2031_bruteforce.py) | Python 3.12 x64 | bruteforce | O(100+n) | AC | 0.078 s | 472 KB |
| [2031_bruteforce.rs](2031_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(100+n) | AC | 0.015 s | 200 KB |
