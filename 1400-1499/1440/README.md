# 1440. Training Schedule

[Timus 1440](https://acm.timus.ru/problem.aspx?space=1&num=1440) · difficulty 668 · bruteforce

Original problem by Ekaterina Vasilyeva (idea and text) and Stanislav Vasiliev (programming), from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The Gryffindor quidditch team trains on fixed days of the week, for
example every Friday and Sunday. Training may take place from September
2 up to the day before the first match, and the match is between
September 2 and December 24. There must be from A to B trainings
(1 ≤ A ≤ B ≤ 200). Given the weekday of September 1 and the date of the
match, choose a set of weekdays that gives such a number of trainings,
or report that none exists.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The weekday of September 1 in English, the date of the match as
"Month Day", and A and B.

## Output

"Impossible", or the number of chosen weekdays followed by their names,
one per line, in any order. Any fitting set is accepted.

## Examples

### Example 1

Input:

```
Thursday
September 10
9 20
```

Output:

```
Impossible
```

### Example 2

Input:

```
Tuesday
October 7
12 14
```

Output:

```
Impossible
```

### Example 3

Input:

```
Friday
October 4
12 14
```

Output:

```
3
Monday
Wednesday
Saturday
```

## Solution

Count how many training days fall on each weekday: walk over the days
from September 2 to the eve of the match, at most 113 of them, adding
one to the weekday of each. A set of weekdays gives the sum of its
counts, and there are only 127 non-empty sets, so try them all and print
the first whose sum lies between A and B. `O(D + 2⁷ · 7)` for D days
before the match.

Pitfalls:

- a match on September 2 leaves no training day at all (test 04);
- 200 trainings never fit before Christmas (test 05);
- sometimes only one set fits, or all seven days are needed (tests 06,
  09, 10, 13);
- the months have different lengths: September 30 and October 1 are
  neighbours (tests 11, 12).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1440_bruteforce.cpp](1440_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.015 s | 404 KB |
| [1440_bruteforce.go](1440_bruteforce.go) | Go 1.14 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.031 s | 1164 KB |
| [1440_bruteforce.java](1440_bruteforce.java) | Java 1.8 | bruteforce | O(D + 2^7 · 7) | AC | 0.109 s | 1708 KB |
| [1440_bruteforce.py](1440_bruteforce.py) | Python 3.12 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.078 s | 428 KB |
| [1440_bruteforce.rs](1440_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.031 s | 220 KB |
