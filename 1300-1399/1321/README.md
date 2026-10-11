# 1321. Floor Indicator

[Timus 1321](https://acm.timus.ru/problem.aspx?space=1&num=1321) · difficulty 1361 · math

Original problem: idea by Leonid Volkov, prepared by Pavel Egorov and Igor Goldberg, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A building has floors 1 to N, where 4 < N < 10⁹⁹⁹. The elevator display
has one place per digit of N, each made of up to seven segments, and
shows the floor number without leading zeros. A segment that never
lights for any floor of the building is not installed. A faulty segment
is stuck on or stuck off.

A technician may enter the elevator at any floor and ride it, watching
the display, until every faulty segment is found or all are known to
work. Print the smallest number of spans between floors the ride needs.

The digits look like this: 0 lights all but the middle segment, 1 the
two right ones, 6 has its top segment and 9 its bottom one, and 7 is
the top and both right segments.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The number N.

## Output

The smallest number of spans.

## Examples

### Example 1

Input:

```
10
```

Output:

```
8
```

## Solution

A segment is checked once the ride shows it both lit and unlit, and a
ride from L to R shows every floor in between, so the task is the
shortest range of floors [L, R] where every installed segment is lit
somewhere and unlit somewhere. A place that is not used yet, like the
tens on floors 1 to 9, is blank: all its segments are unlit.

Let N have D digits. The leading place must change during the ride, so
the range crosses a multiple of 10^(D−1). If it crosses only one, the
lower places pass from 9 to 0. The place right below the leading one
changes the least, and it then shows a run of digits that runs down
from 9 and up from 0. Only digit 2 leaves the lower right segment unlit
and only 5 and 6 leave the upper right one unlit, so the shortest good
runs are 6, 7, 8, 9, 0, 1, 2 and 9, 0, 1, 2, 3, 4, 5. Each costs five
blocks of 10^(D−2) floors plus one. Without reaching 2 above the
crossing, the run has to be 2, …, 9, 0, which costs seven blocks plus
one. A single crossing only works for the leading place when its digit
is 1: blank and 1 differ in exactly the two segments that are installed
there. Reaching digit 2 after the crossing needs N to start with 12 or
more.

With a leading digit of 2 or more, the leading place needs at least
three states. Blank, 1, 2 is enough when N starts with 2 or 3. From 4
on, the upper left segment is installed as well, and the shortest runs
are blank to 4 or 1 to 5. A run of k states costs (k − 2) · 10^(D−1) + 1
floors, and its middle blocks show every lower digit. One-digit
buildings need floors 1 to 5. All together:

- N < 10: 4;
- N starts with 1 and the second digit is 2 or more: 5 · 10^(D−2) + 1;
- N starts with 10 or 11: 7 · 10^(D−2) + 1;
- N starts with 2 or 3: 10^(D−1) + 1;
- N starts with 4 or more: 3 · 10^(D−1) + 1.

The answer is a digit, then zeros, then 1. `O(D)`.

Pitfalls:

- N has up to 999 digits, so it is read as a string (tests 14 to 16);
- with 10 or 11 floors the ride cannot reach floor 12 and has to start
  at floor 2 (tests 01 and 05);
- for two-digit N the answer has no zeros: 8 for 10 and 6 for 12
  (tests 01 and 04).

The formula was compared with a sliding window over all floors for
every N up to 399 and 60 random N up to 30 000.

## Language notes

- Python computes the number with its big integers; the other languages
  write the digit, the zeros and the final 1 as text.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1321_math.cpp](1321_math.cpp) | G++ 13.2 x64 | math | O(D) | AC | 0.015 s | 380 KB |
| [1321_math.go](1321_math.go) | Go 1.14 x64 | math | O(D) | AC | 0.031 s | 1100 KB |
| [1321_math.java](1321_math.java) | Java 1.8 | math | O(D) | AC | 0.125 s | 1584 KB |
| [1321_math.py](1321_math.py) | Python 3.12 x64 | math | O(D) | AC | 0.093 s | 432 KB |
| [1321_math.rs](1321_math.rs) | Rust 1.75 x64 | math | O(D) | AC | 0.046 s | 220 KB |
