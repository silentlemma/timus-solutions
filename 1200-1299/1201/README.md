# 1201. A month calendar with one date in brackets

[Timus 1201](https://acm.timus.ru/problem.aspx?space=1&num=1201) · difficulty 364 · implementation

Original problem by Alexander Klepinin, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a date between the years 1600 and 2400, print the calendar of its
month: seven rows, Monday to Sunday, with one column per week and the
given date in square brackets. Leap years follow the Gregorian rule.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The day, the month and the year.

## Output

Exactly seven lines in the layout of the examples. Each row starts with
`mon` … `sun`; every week takes five characters, the last week four, and
a day is right-aligned in two characters after two spaces. The given date
replaces the space before it and the space after it with `[` and `]`.

## Examples

### Example 1

Input:

```
16 3 2002
```

Output:

```
mon        4   11   18   25
tue        5   12   19   26
wed        6   13   20   27
thu        7   14   21   28
fri   1    8   15   22   29
sat   2    9  [16]  23   30
sun   3   10   17   24   31
```

### Example 2

Input:

```
1 3 2002
```

Output:

```
mon        4   11   18   25
tue        5   12   19   26
wed        6   13   20   27
thu        7   14   21   28
fri [ 1]   8   15   22   29
sat   2    9   16   23   30
sun   3   10   17   24   31
```

## Solution

Count the days from 1 January of year 1, a Monday in the Gregorian
calendar, to the first of the month: `365·(y−1)` plus the leap days
`⌊(y−1)/4⌋ − ⌊(y−1)/100⌋ + ⌊(y−1)/400⌋` plus the lengths of the earlier
months of the year. The remainder modulo 7 is the row of the first day,
and the month needs `⌈(first + days)/7⌉` columns. Then each cell is just
the day number `7·column + row − first + 1` when it falls inside the
month. `O(1)`.

Pitfalls:

- 1900 is not a leap year but 2000 is;
- a month can need four, five or six columns;
- the widths are fixed even where a cell is empty, so rows that end
  before the last week keep their trailing spaces; the expected outputs
  of these tests are compared character by character;
- a one-digit date in brackets keeps its padding: `[ 1]`.

The calendars were compared with a separately written solution on 605
dates, among them the ends of the range and several Februaries.

## Language notes

- All languages build each row cell by cell with the same widths.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1201_implementation.cpp](1201_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 196 KB |
| [1201_implementation.go](1201_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1124 KB |
| [1201_implementation.java](1201_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1752 KB |
| [1201_implementation.py](1201_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 560 KB |
| [1201_implementation.rs](1201_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 252 KB |
