# 2048. Classifying years by Friday-the-thirteenth counts

[Timus 2048](https://acm.timus.ru/problem.aspx?space=1&num=2048) · difficulty 901 · implementation

Original problem by Alexander Ipatov, prepared by Oleg Dolgorukov, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For every year from A to B of the Gregorian calendar count the months
whose 13th day is a Friday, and for each k from 0 to 12 report how many
years have exactly k such months. A year is leap when it is divisible by
400, or by 4 but not by 100; February then has 29 days. The limits are 1
second and 64 MB.

## Input

Two integers A and B, 1919 ≤ A ≤ B ≤ 10⁹.

## Output

Thirteen lines `k: count` for k = 0, …, 12 in increasing order, zero
counts included.

## Checking

Outputs are compared token by token.

## Examples

```
2015 2016
```

```
0: 0
1: 1
2: 0
3: 1
4: 0
5: 0
6: 0
7: 0
8: 0
9: 0
10: 0
11: 0
12: 0
```

In 2015 the matching dates are February 13, March 13 and November 13, so
one year belongs to bucket three. In 2016 only May 13 matches, placing
one year in bucket one. Every other bucket is zero; all thirteen labels
still appear.

## Solution

### Build one calendar period

Number weekdays from Monday zero through Sunday six. January 1 of year 1
is Monday in the proleptic Gregorian calendar. Track the weekday `w` of
a month's first day. Its thirteenth day has weekday `(w+12) mod 7`, so
it matches when this equals Friday, four. After processing the month,
advance `w` by its actual length modulo seven.

Simulate years `1..400` and save `type[y-1]`, the number of matching
months in year `y`. Count these four hundred types into a
thirteen-element histogram `cycle`. February receives the extra day only
under the complete leap rule.

The leap pattern repeats every 400 years. Such a period contains
`400/4-400/100+400/400=97` leap years and `400*365+97=146097=7*20871`
days. Thus the weekday of the next period's first day is unchanged. The
same month lengths and starting weekdays recur, proving that each year's
type repeats with period 400.

### Histograms of prefixes of years

Let `F(t)` be the thirteen counts for years `1..t`. Write `t=400q+r`
with `0≤r<400`. Start with `q*cycle`, then add one to the bucket of each
of the first `r` saved types. The requested histogram is `F(B)-F(A-1)`
component by component.

### Correctness

The month recurrence starts at a known weekday and advances by exactly
the number of days in each month. By induction it obtains the weekday of
every thirteenth day and the exact annual type for the simulated period.
The 400-year day total and repeated leap rule prove these types valid in
every later period.

Years `1..t` split into `q` disjoint full periods and a prefix of `r`
years. Each full period contributes `cycle`; the saved prefix
contributes exactly its year types. Therefore the formula computes
`F(t)`. Subtracting the years through `A-1` from those through `B`
retains exactly the inclusive interval `A..B` in every bucket.

For period length `C=400`, time is `O(C*12+C+13)` and auxiliary space is
`O(C+13)`. Both are constant with respect to the width of the requested
year interval. No loop visits the years from `A` to `B`.

## Language notes

- The thirteenth is twelve days after the first; the offset is not thirteen.
- The saved array starts at year one, so its year index is `(year-1) mod 400`.
- Subtract `F(A-1)`, including when the endpoints coincide.
- Divisibility by four alone is insufficient: 2100 is ordinary, while
  2000 and 2400 are leap.
- Print zero buckets and count years, not matching months.

All five ports construct the calendar once, reuse it for both prefix
histograms and emit all labels. The compiled ports use 64-bit histogram
counts; Python uses integers. No runtime date library or hardcoded
distribution is needed by the solutions.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2048_implementation.cpp](2048_implementation.cpp) | G++ 13.2 x64 | implementation | O(C*12+C+13) | AC | 0.015 s | 400 KB |
| [2048_implementation.go](2048_implementation.go) | Go 1.14 x64 | implementation | O(C*12+C+13) | AC | 0.031 s | 1120 KB |
| [2048_implementation.java](2048_implementation.java) | Java 1.8 | implementation | O(C*12+C+13) | AC | 0.093 s | 492 KB |
| [2048_implementation.py](2048_implementation.py) | Python 3.12 x64 | implementation | O(C*12+C+13) | AC | 0.078 s | 640 KB |
| [2048_implementation.rs](2048_implementation.rs) | Rust 1.75 x64 | implementation | O(C*12+C+13) | AC | 0.031 s | 240 KB |
