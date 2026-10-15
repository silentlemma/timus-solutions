# 1727. Znaika's Magic Numbers

[Timus 1727](https://acm.timus.ru/problem.aspx?space=1&num=1727) · difficulty 200 · greedy

Original problem by Ivan Burmistrov, from the Ural Regional School Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find a set of distinct positive integers below 10⁵ whose digits add up
to n in total, or print −1 if there is none.

## Input

n (0 < n < 10⁵).

## Output

The size of the set and then its numbers, or −1. Any fitting set is
accepted.

## Examples

### Example 1

Input:

```
17
```

Output:

```
3
7 12 43
```

## Solution

A set always exists: the digits of all numbers from 1 to 99 999 add up
to 5 · 45 · 10⁴ = 2 250 000, far more than n.

Go down from 99 999 and take each number whose digit sum still fits in
what is left of n. Large numbers have digit sums near 45 and use up
most of n quickly; when the rest gets small, the greedy skips ahead to
numbers with small digit sums, such as 20 000 or 10 000, and at the
very end the one-digit numbers 9, 8, …, 1 can make any rest up to 45.
The digit sums are built up front as s(i) = s(i / 10) + i mod 10.
`O(10⁵)`.

For n = 17 the greedy prints 98 000, which alone has digit sum 17. Any
set with the right total is accepted.

Pitfalls:

- −1 is never the answer;
- the numbers must be distinct and below 10⁵, so 99 999 can be used
  only once;
- for n = 99 999 the set has 3261 numbers, so the output should be
  built in one piece.

The greedy reaches exactly n for every n from 1 to 99 999, checked one
by one. The checker verifies the range, the distinctness and the total
of the digits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1727_greedy.cpp](1727_greedy.cpp) | G++ 13.2 x64 | greedy | O(10⁵) | AC | 0.015 s | 616 KB |
| [1727_greedy.go](1727_greedy.go) | Go 1.14 x64 | greedy | O(10⁵) | AC | 0.031 s | 2268 KB |
| [1727_greedy.java](1727_greedy.java) | Java 1.8 | greedy | O(10⁵) | AC | 0.125 s | 2196 KB |
| [1727_greedy.py](1727_greedy.py) | Python 3.12 x64 | greedy | O(10⁵) | AC | 0.093 s | 1636 KB |
| [1727_greedy.rs](1727_greedy.rs) | Rust 1.75 x64 | greedy | O(10⁵) | AC | 0.046 s | 1096 KB |
