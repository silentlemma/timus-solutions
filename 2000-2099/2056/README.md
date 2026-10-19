# 2056. Determine the scholarship category

[Timus 2056](https://acm.timus.ru/problem.aspx?space=1&num=2056) · difficulty 41 · implementation

Folklore problem, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A student passed n exams with grades from 3 to 5. Name the scholarship:
`None` if there is any 3, otherwise `Named` if all grades are 5,
otherwise `High` if the average is at least 4.5, and `Common` in all
other cases. The limits are 1 second and 64 MB.

## Input

The number of exams n, 1 ≤ n ≤ 10, and then n lines with one grade each.

## Output

One word, case-sensitive.

## Checking

Outputs are compared token by token.

## Examples

```
3
5
5
4
```

```
High
```

```
3
3
3
3
```

```
None
```

For the first example the sum is fourteen and `2·14≥9·3`, so the average
exceeds 4.5. There is no three and not every grade is five, hence
`High`. In the second example a three is present, so the
highest-priority rule gives `None`.

## Solution

Scan all grades, keeping their sum `S` and minimum `q`, initially zero
and five. After any prefix these are exactly its sum and minimum: adding
the new grade updates the sum, and taking the smaller value updates the
minimum. Thus after all `n` grades, `q=3` holds exactly when some grade
is three. In this case output `None` before considering any average.

Otherwise `q=5` holds exactly when every grade is five, since five is
the largest allowed grade; output `Named`. If neither condition holds,
there are only fours and fives, including at least one four. The next
rule applies exactly when `S/n≥4.5`, which is equivalent to the integer
comparison `2S≥9n` because `n>0`. Output `High` if it holds and `Common`
otherwise. These conditions implement the four rules in their required
order, are exhaustive and mutually exclusive, proving correctness.

A three overrides even a high average. All fives must produce `Named`
rather than `High`. The average threshold is inclusive, so one four and
one five give `High`. Do not truncate an integer average. With one exam,
grades three, four and five produce `None`, `Common` and `Named`
respectively. Preserve output capitalization.

## Language notes

One pass takes `O(n)` time and `O(1)` working state. Python and Rust
also retain `O(n)` input text/tokens; the other versions stream buffered
input. All arithmetic is exact integer arithmetic: `S≤50`, `2S≤100` and
`9n≤90`. Every port uses the same three statistics, and no floating-point
division is needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2056_implementation.cpp](2056_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 420 KB |
| [2056_implementation.go](2056_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.046 s | 1096 KB |
| [2056_implementation.java](2056_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.109 s | 452 KB |
| [2056_implementation.py](2056_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 472 KB |
| [2056_implementation.rs](2056_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 224 KB |
