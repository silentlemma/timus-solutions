# 1831. Tsyfirkin's Lesson

[Timus 1831](https://acm.timus.ru/problem.aspx?space=1&num=1831) · difficulty 2244 · probability

Original problem by Evgeny Kurpilyansky (idea by Alexander Ipatov), from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A pupil adds two numbers in a column, right to left. Writing a digit or
a carry mark takes one second. Adding two numbers takes one second if
one of them is 0 or 1 and two seconds otherwise, but a sum already
computed in this lesson, in either order, is recalled in one second. At
each place the pupil adds the two digits, adds the incoming carry if
there is one, writes the last digit and marks a carry if needed; a
carry out of the last place is written as a digit. For two random
k-digit numbers without leading zeros, find the expected time.

## Input

k (1 ≤ k ≤ 5000).

## Output

The expected time, with absolute or relative error at most 10⁻⁶.

## Examples

### Example 1

Input:

```
2
```

Output:

```
7.51530864
```

## Solution

Split the time by linearity of expectation.

- Every place writes one digit and computes one digit sum: 2k seconds,
  plus one more second for each digit sum of two digits above 1 that is
  met for the first time.
- Every carry is marked, and then either added to the next place (one
  second, since one of the addends is 1) or, out of the last place,
  written: two seconds per carry.

The carries form a Markov chain. With random digits 0 … 9 a carry
appears with chance 45/100 without an incoming carry and 55/100 with
one; at the leading place the digits are 1 … 9 and the chances are
45/81 and 53/81. Iterating the chance of a carry place by place gives
the expected number of carries.

A pair {a, b} of digits from 2 … 9 shows up at a lower place with
chance 2/100 (1/100 if a = b) and at the leading place with chance
2/81 (1/81), independently across places. So it is met at least once
with chance 1 − (1 − q)^(k−1)(1 − r), and the 36 such pairs add these
chances. `O(k)`.

For k = 2: 4 seconds for writing and summing, carries 0.45 and 0.6
that add 2·1.05 = 2.1, and pairs met for the first time add 1.41531,
in total 7.51531.

Pitfalls:

- the leading digits are never 0, so the leading place has its own
  carry and pair chances;
- a sum with 0 or 1 never costs two seconds, so only pairs of digits
  from 2 … 9 are remembered in a way that matters;
- adding the carry is a separate one-second sum.

The values agree with an exhaustive count over all pairs of numbers for
k up to 3 and with an independent accepted implementation for all
tested k.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1831_probability.cpp](1831_probability.cpp) | G++ 13.2 x64 | probability | O(k) | AC | 0.015 s | 148 KB |
| [1831_probability.go](1831_probability.go) | Go 1.14 x64 | probability | O(k) | AC | 0.031 s | 1080 KB |
| [1831_probability.java](1831_probability.java) | Java 1.8 | probability | O(k) | AC | 0.125 s | 1828 KB |
| [1831_probability.py](1831_probability.py) | Python 3.12 x64 | probability | O(k) | AC | 0.093 s | 524 KB |
| [1831_probability.rs](1831_probability.rs) | Rust 1.75 x64 | probability | O(k) | AC | 0.031 s | 252 KB |
