# 1187. Survey cross tables with percents that add up to 100

[Timus 1187](https://acm.timus.ru/problem.aspx?space=1&num=1187) · difficulty 2051 · strings

Original problem by Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A survey has up to 100 questions with 2 to 10 one-character answers each,
and up to 10000 recorded answers in all. For each requested pair of
questions, print a cross table: how many people gave each pair of
answers, with row and column totals, and under every number its percent
of the row total and of the column total. Percents are whole numbers,
each rounded down or up from the exact value, so that the percents of a
row (or column) without its total add up to exactly 100; a percent of a
zero total is printed as `-`. The layout of the table is fixed to the
character.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The survey name, the questions with their answers, `#`, one line of
answer codes per person, `#`, the requested tables, `#`.

## Output

For every table: a title, both questions copied, an empty line and a
table of 6-character cells; tables are separated by an empty line.

## Checking

Any rounding is accepted if every percent rounds its exact value down or
up, rows and columns without totals add up to 100%, totals show `100%`
and zero totals show `-`; every other character must match exactly.

## Examples

### Example 1

Input:

```
New Year Phone Survey for ACM ICPC
Q01 Hello!
 H Hello!
 Y Yes!
 * Uhm...
 . (silence)
 @ (other)
Q02 How are you?
 H Hello!
 Y Yes!
 F Fine!
 Q Who are you?
 @ (other)
BYE Happy New Year!
 Y You too.
 * (censored)
 @ (other)
 . (hang up)
#
.@.
HH@
.@.
YFY
HQ*
H@.
YYY
.H@
HFY
HH@
#
Q01 Q02 Health vs greeting style
Q02 BYE Politeness matrix
#
```

Output:

```
New Year Phone Survey for ACM ICPC - Health vs greeting style
Q01 Hello!
 H Hello!
 Y Yes!
 * Uhm...
 . (silence)
 @ (other)
Q02 How are you?
 H Hello!
 Y Yes!
 F Fine!
 Q Who are you?
 @ (other)

       Q02:H Q02:Y Q02:F Q02:Q Q02:@ TOTAL
 Q01:H     2     0     1     1     1     5
         40%    0%   20%   20%   20%  100%
         66%    0%   50%  100%   33%   50%
 Q01:Y     0     1     1     0     0     2
          0%   50%   50%    0%    0%  100%
          0%  100%   50%    0%    0%   20%
 Q01:*     0     0     0     0     0     0
           -     -     -     -     -     -
          0%    0%    0%    0%    0%    0%
 Q01:.     1     0     0     0     2     3
         33%    0%    0%    0%   67%  100%
         34%    0%    0%    0%   67%   30%
 Q01:@     0     0     0     0     0     0
           -     -     -     -     -     -
          0%    0%    0%    0%    0%    0%
 TOTAL     3     1     2     1     3    10
         30%   10%   20%   10%   30%  100%
        100%  100%  100%  100%  100%  100%

New Year Phone Survey for ACM ICPC - Politeness matrix
Q02 How are you?
 H Hello!
 Y Yes!
 F Fine!
 Q Who are you?
 @ (other)
BYE Happy New Year!
 Y You too.
 * (censored)
 @ (other)
 . (hang up)

       BYE:Y BYE:* BYE:@ BYE:. TOTAL
 Q02:H     0     0     3     0     3
          0%    0%  100%    0%  100%
          0%    0%  100%    0%   30%
 Q02:Y     1     0     0     0     1
        100%    0%    0%    0%  100%
         33%    0%    0%    0%   10%
 Q02:F     2     0     0     0     2
        100%    0%    0%    0%  100%
         67%    0%    0%    0%   20%
 Q02:Q     0     1     0     0     1
          0%  100%    0%    0%  100%
          0%  100%    0%    0%   10%
 Q02:@     0     0     0     3     3
          0%    0%    0%  100%  100%
          0%    0%    0%  100%   30%
 TOTAL     3     1     3     3    10
         30%   10%   30%   30%  100%
        100%  100%  100%  100%  100%
```

## Solution

Count the pairs into a table and append the row totals as one more
column and the column totals as one more row; the corner holds the number
of people.

For rounding, take a row (or column) of values `v` with total `T`. Round
every percent `100·v/T` down. The sum falls short of 100 by some `d`, and
since the dropped fractions add up to exactly `d`, at least `d` values
have a fraction. Raise the `d` values with the largest fractions by one.
This is done for every row and column without its total, including the
totals row and the totals column themselves, while the totals cells get
`100%` (or `-` if their total is zero). `O(people + table size)` per table.

The rest is careful printing: every cell is right-aligned to width 6, the
second and third lines of a row start with 6 blanks, and the questions
are copied exactly as in the input.

Pitfalls:

- the totals must not be in the vectors that add up to 100, or every sum
  would be 200;
- the sample rounds 2/3 down and 1/3 up in one column, which is just
  another valid choice, so outputs differ from it and a checker is
  needed;
- a row whose total is zero still gets column-wise percents, which are 0%
  unless the column total is zero too.

Every output was validated by the checker on 100 random surveys, and the
same checker accepted the output of a separately written solution there.

## Language notes

- All languages round the same way: a stable sort by remainder raises
  the largest remainders first and, among equal ones, the earlier cell,
  so all five print the same tables.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1187_strings.cpp](1187_strings.cpp) | G++ 13.2 x64 | strings | O(people + table) per table | AC | 0.015 s | 1008 KB |
| [1187_strings.go](1187_strings.go) | Go 1.14 x64 | strings | O(people + table) per table | AC | 0.031 s | 4656 KB |
| [1187_strings.java](1187_strings.java) | Java 1.8 | strings | O(people + table) per table | AC | 0.265 s | 10196 KB |
| [1187_strings.py](1187_strings.py) | Python 3.12 x64 | strings | O(people + table) per table | AC | 0.125 s | 2564 KB |
| [1187_strings.rs](1187_strings.rs) | Rust 1.75 x64 | strings | O(people + table) per table | AC | 0.031 s | 1296 KB |
