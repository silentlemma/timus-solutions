# 2143. Seating a group with no two members side by side

[Timus 2143](https://acm.timus.ru/problem.aspx?space=1&num=2143) · difficulty 672 · dp, bitmask

Original problem by Alexey Kungurtsev, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A plane has n rows of seats A B C | D E F with an aisle in the middle,
and some seats are taken. Two seats are adjacent when they are on the
same side of the aisle and both their rows and their letters differ by
at most one. Seat a group of k people on free seats so that no two of
them are adjacent, or report that it is impossible. Any valid seating is
accepted. The limits are 0.5 seconds and 256 MB.

## Input

n and k, 1 ≤ n ≤ 100, 1 ≤ k ≤ 6n, then n rows like ".**|_|**." with
"." for a free seat and "*" for a taken one. There are at least k free
seats.

## Output

"PORAZHENIE", or "POBEDA" and k seats such as 1A.

## Checking

A checker verifies the verdict and that the seats are free, distinct
and pairwise non-adjacent.

## Examples

### Example 1

Input:

```
2 2
.**|_|**.
**.|_|***
```

Output:

```
POBEDA
1A
2C
```

### Example 2

Input:

```
2 3
...|_|***
***|_|***
```

Output:

```
PORAZHENIE
```

## Solution

The two sides of the aisle never touch, so each side is a separate n × 3
grid where adjacency is the king's move. Any subset of a valid seating
is valid, so it is enough to find the largest valid seating on each
side and check that together they have at least k seats.

On one side the seats of a row form a 3-bit mask. A mask is allowed in
a row when it uses only free seats and has no two neighbouring bits, and
two masks fit in consecutive rows when no bit of one is in the same or a
neighbouring column of a bit of the other: (m | m << 1 | m >> 1) & m′ = 0.
A DP over rows and the mask of the last row keeps the largest number of
people and the previous mask, so the best seating is rebuilt from the
last row. There are 8 masks, so the work is O(64 n).

In the second example the three free seats 1A, 1B and 1C hold at most
two people, 1A and 1C, so three cannot be seated.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2143_dp_bitmask.cpp](2143_dp_bitmask.cpp) | G++ 13.2 x64 | dp, bitmask | O(n) | AC | 0.015 s | 412 KB |
| [2143_dp_bitmask.go](2143_dp_bitmask.go) | Go 1.14 x64 | dp, bitmask | O(n) | AC | 0.031 s | 1184 KB |
| [2143_dp_bitmask.java](2143_dp_bitmask.java) | Java 1.8 | dp, bitmask | O(n) | AC | 0.140 s | 1756 KB |
| [2143_dp_bitmask.py](2143_dp_bitmask.py) | Python 3.12 x64 | dp, bitmask | O(n) | AC | 0.109 s | 780 KB |
| [2143_dp_bitmask.rs](2143_dp_bitmask.rs) | Rust 1.75 x64 | dp, bitmask | O(n) | AC | 0.015 s | 264 KB |
