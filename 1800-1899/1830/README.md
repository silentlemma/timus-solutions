# 1830. Help in the RNOS

[Timus 1830](https://acm.timus.ru/problem.aspx?space=1&num=1830) · difficulty 952 · math

Original problem by Evgeny Kurpilyansky (idea by Stanislav Vasiliev), from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A help system has pages 1, …, n. F1 opens or closes page 1. Every page
but the last has buttons that open or close the next page, but only the
least detailed open page, the one with the smallest number, is visible
and usable. Find the fewest button presses that turn one set of open
pages into another.

## Input

n (1 ≤ n ≤ 50), then the starting and the wanted sets as strings of n
zeros and ones, the i-th character telling whether page i is open.

## Output

The fewest presses.

## Examples

### Example 1

Input:

```
3
111
000
```

Output:

```
5
```

## Solution

This is the Chinese rings puzzle. In any state there are at most two
moves: flip page 1, or flip the page right after the first open one.
Read page i as bit i − 1 of a binary word. Then these are exactly the
two kinds of steps of the reflected Gray code, which flips bit 0 on
every other step and otherwise the bit just above the lowest set bit.
So all 2ⁿ states lie on one path in Gray code order, and the place of a
state on it is its word decoded from Gray code: the xor of the word and
all its right shifts. The answer is the difference of the two places.
`O(n)`.

In the example 111 is the word 7, whose place is 7 xor 3 xor 1 = 5,
and 000 is at place 0: five presses.

Pitfalls:

- the first character is page 1, the lowest bit, so the string is read
  backwards;
- the answer reaches 2⁵⁰ − 1, which needs 64-bit integers;
- a breadth-first search over 2⁵⁰ states is hopeless.

The answers agree with a breadth-first search for n up to 9 and with an
independent accepted implementation on random pairs of up to 50 pages.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1830_math.cpp](1830_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 132 KB |
| [1830_math.go](1830_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1076 KB |
| [1830_math.java](1830_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1588 KB |
| [1830_math.py](1830_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 476 KB |
| [1830_math.rs](1830_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 232 KB |
