# 1827. Indigenous Wars

[Timus 1827](https://acm.timus.ru/problem.aspx?space=1&num=1827) · difficulty 1191 · hashing

Original problem by Dmitry Ivankov, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The natives date days by the number of stars in the night sky. Their
book records each war as x, the stars on its first day, y, the stars on
its last day, and d, its length in days. Given the stars seen i days
ago for each of the last n days, mark every day on which some recorded
war could have been going on.

## Input

n (2 ≤ n ≤ 10⁵), then a₁, …, aₙ, where aᵢ is the number of stars i
days ago (0 ≤ aᵢ ≤ 2·10⁸), then m (1 ≤ m ≤ 10⁵) and m lines x, y, d
(0 ≤ x, y ≤ 2·10⁸, 2 ≤ d ≤ 50).

## Output

A string of n digits: the i-th is 1 if a war could have been going on i
days ago, and 0 otherwise.

## Examples

### Example 1

Input:

```
6
6 5 4 3 2 1
3
2 4 3
4 5 2
1 6 5
```

Output:

```
011110
```

## Solution

A war of d days that ended k days ago began k + d − 1 days ago, so it
fits there exactly when a at k + d − 1 is x and a at k is y. Lengths are
at most 50, so for each length d that occurs in the book, put the pairs
(x, y) of its wars into a hash set and slide over all k, looking up
(a at k + d − 1, a at k). Each hit covers the days k … k + d − 1: keep,
for every k, the oldest day covered by a war ending there, and one
sweep marks every day below the running maximum. That is at most
49·n lookups, `O(50·n + m)`.

Python does the lookups for one length at once with `map` over two
shifted lists, packs the hits into a big-integer bitmask and smears it
over d days with O(log d) shifts and ors.

In the example the war (2, 4, 3) fits 5 to 3 days ago and (4, 5, 2)
fits 3 to 2 days ago, while (1, 6, 5) would need 6 stars 2 days ago.

Pitfalls:

- the first day of a war is further in the past, so x is matched with
  the larger number of days ago;
- with every count equal, each war matches everywhere, so looking up
  wars position by position from their first-day counts is quadratic;
- a war can be longer than the whole record.

The answers agree with an independent accepted implementation on a few
hundred random records and on the full-size ones in the tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1827_hashing.cpp](1827_hashing.cpp) | G++ 13.2 x64 | hashing | O(50 n + m) | AC | 0.484 s | 5944 KB |
| [1827_hashing.go](1827_hashing.go) | Go 1.14 x64 | hashing | O(50 n + m) | AC | 0.187 s | 10820 KB |
| [1827_hashing.java](1827_hashing.java) | Java 1.8 | hashing | O(50 n + m) | AC | 0.234 s | 6812 KB |
| [1827_hashing.py](1827_hashing.py) | Python 3.12 x64 | hashing | O(50 n + m) | AC | 0.828 s | 42112 KB |
| [1827_hashing.rs](1827_hashing.rs) | Rust 1.75 x64 | hashing | O(50 n + m) | AC | 0.093 s | 8892 KB |
