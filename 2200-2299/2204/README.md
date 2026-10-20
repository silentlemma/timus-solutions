# 2204. Choosing exam dates that block the fewest trips

[Timus 2204](https://acm.timus.ru/problem.aspx?space=1&num=2204) · difficulty 1321 · dp, two_pointers

Original problem by Ivan Kogut, from the University Academic School Olympiad in Informatics 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n exams can be taken on one of two day ranges, and the exams
come in order without overlapping. There are m disjoint trips, also in
order. A trip is lost if it shares a day with a chosen exam range.
Choose the ranges to keep as many trips as possible. The limits are
1 second and 256 MB.

## Input

n and m, 1 ≤ n, m ≤ 10⁵, then the two ranges of each exam and the
ranges of the trips, days up to 10⁹.

## Output

The largest number of trips kept.

## Examples

### Example 1

Input:

```
3 5
3 5 7 9
43 50 51 58
100 103 111 114
6 6
47 47
101 101
103 103
112 112
```

Output:

```
4
```

## Solution

Minimize the number of lost trips instead. The trips that meet a day
range form a contiguous block of the sorted trips, found with two
pointers that only move forward, since the ranges come in increasing
order.

The DP keeps, for each option of the current exam, the fewest trips
lost so far and the index of the last trip that this option blocks.
The only overlap between consecutive exams is a single long trip that
meets both chosen ranges: it can only be the last trip blocked by the
previous range and the first one blocked by the next. So when an option
blocks c trips, its cost is c plus the better of the two previous
costs, each reduced by one if its last blocked trip is this option's
first. A trip that reaches across three exams also covers the middle
one, so it is subtracted at each step and still counted once.

In the example the first two exams can avoid every trip, and the last
one blocks either the trips on days 101 and 103 or the trip on day 112,
so one trip is lost and four are kept.

This takes O(n + m).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2204_dp_two_pointers.cpp](2204_dp_two_pointers.cpp) | G++ 13.2 x64 | dp, two_pointers | O(n + m) | AC | 0.109 s | 2084 KB |
| [2204_dp_two_pointers.go](2204_dp_two_pointers.go) | Go 1.14 x64 | dp, two_pointers | O(n + m) | AC | 0.062 s | 20120 KB |
| [2204_dp_two_pointers.java](2204_dp_two_pointers.java) | Java 1.8 | dp, two_pointers | O(n + m) | AC | 0.125 s | 2716 KB |
| [2204_dp_two_pointers.py](2204_dp_two_pointers.py) | Python 3.12 x64 | dp, two_pointers | O(n + m) | AC | 0.546 s | 62660 KB |
| [2204_dp_two_pointers.rs](2204_dp_two_pointers.rs) | Rust 1.75 x64 | dp, two_pointers | O(n + m) | AC | 0.062 s | 13792 KB |
