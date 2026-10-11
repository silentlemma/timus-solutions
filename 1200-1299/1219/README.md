# 1219. A million letters with no letter, pair or triple too common

[Timus 1219](https://acm.timus.ru/problem.aspx?space=1&num=1219) · difficulty 121 · constructive

Original problem by Pavel Atnashev and Leonid Volkov, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Print 1,000,000 lowercase Latin letters such that every letter occurs at
most 40,000 times, every two consecutive letters at most 2,000 times and
every three consecutive letters at most 100 times.

Time limit: 1 second. Memory limit: 64 MB.

## Input

There is no input.

## Output

One line with the letters.

## Checking

Any sequence that meets the three limits is accepted.

## Examples

There is no input, and the statement gives no example output.

## Solution

Spread the million letters as evenly as possible. There are 26 letters,
`26² = 676` pairs and `26³ = 17,576` triples, so a perfectly even spread
gives about 38,462, 1,479 and 57 occurrences, all under the limits.

A de Bruijn sequence of order 3 over 26 letters is a cycle of 17,576
letters in which every triple appears exactly once as three consecutive
letters, going around the cycle. Repeating it end to end keeps every
window of three letters a window of the cycle, so after about 57 copies
every triple appears 56 or 57 times, every pair 26 times as often and
every letter 676 times as often: at most 38,532, 1,482 and 57 here. The
cycle comes from the classic construction that joins the Lyndon words
whose length divides 3, in lexicographic order. `O(L)` for `L = 10⁶`.

Pitfalls:

- the windows that cross from one copy to the next are cyclic windows of
  the sequence, so they do not break the balance;
- a random sequence would probably pass too, but its largest triple count
  would only be about 90, close to the limit.

The output was checked against all three limits, and the counts above are
its actual maxima.

## Language notes

- All languages generate the cycle with the same recursive construction
  and write the whole line at once.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1219_constructive.cpp](1219_constructive.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.001 s | 1184 KB |
| [1219_constructive.go](1219_constructive.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.015 s | 2624 KB |
| [1219_constructive.java](1219_constructive.java) | Java 1.8 | constructive | O(L) | AC | 0.062 s | 8868 KB |
| [1219_constructive.py](1219_constructive.py) | Python 3.12 x64 | constructive | O(L) | AC | 0.078 s | 3224 KB |
| [1219_constructive.rs](1219_constructive.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.001 s | 2404 KB |
