# 1759. Long-Livers

[Timus 1759](https://acm.timus.ru/problem.aspx?space=1&num=1759) · difficulty 462 · implementation

Original problem by Alexander Ipatov, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A list of n people gives each one's date of birth, the date they became
the oldest living person and the date of death; each person's second
date is the previous person's date of death. Find who lived the most
days, counting both the day of birth and the day of death. On a tie,
name the one who died first.

## Input

n (1 ≤ n ≤ 100), then n lines of three dates `dd.mm.yyyy` between
01.01.1800 and 31.12.2009 in the Gregorian calendar, each later than
the one before it. All births differ, and so do all deaths.

## Output

The number of that person in the list.

## Examples

### Example 1

Input:

```
4
10.10.1873 27.12.1987 11.01.1988
18.11.1874 11.01.1988 14.02.1991
21.02.1875 14.02.1991 04.08.1997
29.08.1880 04.08.1997 16.04.1998
```

Output:

```
3
```

## Solution

Each date becomes a day number, and a life lasts death − birth + 1
days. The day number counts the year from March, so that 29 February,
when there is one, is the last day of the year: then the years before
year y hold 365·y days plus ⌊y/4⌋ − ⌊y/100⌋ + ⌊y/400⌋ leap days, and the
days before month m (March being 0) are ⌊(153·m + 2) / 5⌋, since March
to July and August to December hold 153 days each in the same pattern.
The list runs in order of death, so the first person to reach the
longest life is the answer. `O(n)`.

In the example the lives are 41731, 42457, 44725 and 42964 days long,
so the third person, born in 1875 and dead in 1997, lived longest.

Pitfalls:

- 1800 and 1900 are not leap years, while 2000 is;
- both the day of birth and the day of death count, which does not
  change the winner but does change the lengths;
- a tie goes to the earlier death, which is the earlier line.

The answers agree with a count based on a standard date library and
with an independent accepted implementation on 160 random lists,
including lists with ties and dates around the end of February in
1800, 1900 and 2000.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1759_implementation.cpp](1759_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB |
| [1759_implementation.go](1759_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1128 KB |
| [1759_implementation.java](1759_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1804 KB |
| [1759_implementation.py](1759_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 520 KB |
| [1759_implementation.rs](1759_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 232 KB |
