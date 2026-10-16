# 1796. Amusement Park

[Timus 1796](https://acm.timus.ru/problem.aspx?space=1&num=1796) · difficulty 111 · math

Original problem by Eugene Kurpilyansky (prepared by Egor Shchelkonogov), from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A teacher pays for some tickets with notes of 10, 50, 100, 500, 1000
and 5000 roubles. The money is enough for the tickets, but would no
longer be enough if any single note were taken away. Given the number
of notes of each kind and the ticket price, list every possible number
of tickets.

## Input

Six counts of notes, from the smallest to the largest, then the price.
All numbers are at most 1000, and the price is positive. At least one
answer exists.

## Output

The number of possible answers, then the answers in increasing order.

## Examples

### Example 1

Input:

```
0 2 0 0 0 0
10
```

Output:

```
5
6 7 8 9 10
```

### Example 2

Input:

```
1 2 0 0 0 0
10
```

Output:

```
1
11
```

## Solution

Let the sum be T and the smallest given note s. For k tickets the money
must be enough, k·price ≤ T. Without any one note it must not be, and
the smallest note is the hardest case: if T − s is too little, so is
the sum without any larger note. So T − s < k·price, and the
answers are all k from ⌊(T − s)/price⌋ + 1 to ⌊T/price⌋. `O(answers)`,
at most 5000 of them.

In the first example T = 100 and s = 50: without one note 50 roubles
must not be enough, so more than 5 tickets, and at most 10.

Pitfalls:

- the note to take away is the smallest one present, not the 10-rouble
  note in general;
- with a 5000-rouble note and a price of 1 there are 5000 answers on
  one line.

The answers agree with an independent accepted implementation on 300
random cases with few and with many notes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1796_math.cpp](1796_math.cpp) | G++ 13.2 x64 | math | O(answers) | AC | 0.031 s | 460 KB |
| [1796_math.go](1796_math.go) | Go 1.14 x64 | math | O(answers) | AC | 0.031 s | 1288 KB |
| [1796_math.java](1796_math.java) | Java 1.8 | math | O(answers) | AC | 0.109 s | 1964 KB |
| [1796_math.py](1796_math.py) | Python 3.12 x64 | math | O(answers) | AC | 0.078 s | 752 KB |
| [1796_math.rs](1796_math.rs) | Rust 1.75 x64 | math | O(answers) | AC | 0.015 s | 480 KB |
