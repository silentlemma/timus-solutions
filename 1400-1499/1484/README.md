# 1484. Film Rating

[Timus 1484](https://acm.timus.ru/problem.aspx?space=1&num=1484) · difficulty 629 · math

Original problem by Vladimir Yakovlev, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A film's rating is the mean of integer votes from 1 to 10, rounded to
one decimal with halves going up (7.55 shows as 7.6). It now shows X
after N votes (1 ≤ X, Y ≤ 10 with one decimal, 1 ≤ N ≤ 10⁶). Find the
fewest new votes that make the rating show at most Y whatever the
earlier votes were, or print "Impossible".

Time limit: 1 second. Memory limit: 64 MB.

## Input

X, Y and N.

## Output

The number of votes, or "Impossible".

## Examples

### Example 1

Input:

```
9.5 2.0 12
```

Output:

```
86
```

## Solution

Work in tenths: x = 10X and y = 10Y. A sum S of N votes shows x exactly
when (2x − 1)N ≤ 20S < (2x + 1)N, and the votes allow N ≤ S ≤ 10N. If no
integer S fits both, no set of votes shows X, and the answer is
"Impossible": one vote, for example, can never show 7.1.

The new votes should all be 1, and the worst case is the largest
fitting S. After k such votes the rating shows at most y when
20(S + k) < (2y + 1)(N + k), that is (2y − 19)·k > 20S − (2y + 1)N.
Since Y ≥ 1, 2y − 19 is positive, so the smallest k is 0 when the right
side is already negative and (20S − (2y + 1)N) div (2y − 19) + 1
otherwise. `O(1)`.

Pitfalls:

- a rating that N votes cannot show is "Impossible", even if the target
  would be easy (tests 02, 09);
- 7.55 rounds up to 7.6, so the bounds are half-open and best kept in
  integers (test 07);
- the answer reaches 179 000 001 for a million tens brought down to 1.0
  (test 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1484_math.cpp](1484_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 132 KB |
| [1484_math.go](1484_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1076 KB |
| [1484_math.java](1484_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1636 KB |
| [1484_math.py](1484_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 456 KB |
| [1484_math.rs](1484_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 232 KB |
