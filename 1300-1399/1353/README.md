# 1353. Milliard Vasya's Function

[Timus 1353](https://acm.timus.ru/problem.aspx?space=1&num=1353) · difficulty 103 · dp

Original problem by Denis Musin, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given S, 1 ≤ S ≤ 81, count the integers from 1 to 10⁹ whose digit sum
is S.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number S.

## Output

The count.

## Examples

### Example 1

Input:

```
1
```

Output:

```
10
```

## Solution

Every number below 10⁹ is a string of nine digits once leading zeros are
added, and leading zeros do not change the digit sum. So count digit
strings: ways[s] after k digits is the number of k-digit strings with
sum s, and each new digit d from 0 to 9 moves ways[s] into s + d. After
nine digits, ways[S] counts the numbers from 0 to 999 999 999 with sum
S. Zero has sum 0, so it is never counted, and 10⁹ itself, with digit
sum 1, adds one when S = 1. `O(9 · 81 · 10)`.

Pitfalls:

- 10⁹ is in the range: S = 1 gives 10, not 9 (test 01);
- from S = 10 on, a single digit can no longer carry the whole sum, so
  plain stars and bars overcounts (test 07);
- the counts are symmetric, ways[s] = ways[81 − s], and the largest is
  45 433 800 at S = 40 and 41, which fits in 32 bits.

The same table for 10⁶ in place of 10⁹ was compared with counting the
digit sums of every number up to 10⁶.

## Language notes

- All five solutions build the table digit by digit in the same way.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1353_dp.cpp](1353_dp.cpp) | G++ 13.2 x64 | dp | O(9·81·10) | AC | 0.015 s | 200 KB |
| [1353_dp.go](1353_dp.go) | Go 1.14 x64 | dp | O(9·81·10) | AC | 0.031 s | 1124 KB |
| [1353_dp.java](1353_dp.java) | Java 1.8 | dp | O(9·81·10) | AC | 0.109 s | 1584 KB |
| [1353_dp.py](1353_dp.py) | Python 3.12 x64 | dp | O(9·81·10) | AC | 0.093 s | 444 KB |
| [1353_dp.rs](1353_dp.rs) | Rust 1.75 x64 | dp | O(9·81·10) | AC | 0.015 s | 228 KB |
