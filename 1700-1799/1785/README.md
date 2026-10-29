# 1785. Lost in Localization

[Timus 1785](https://acm.timus.ru/problem.aspx?space=1&num=1785) · difficulty 16 · implementation

Original problem: folklore, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A game names the size of an army by a word instead of a number: 1–4
is "few", 5–9 "several", 10–19 "pack", 20–49 "lots", 50–99 "horde",
100–249 "throng", 250–499 "swarm", 500–999 "zounds", and 1000 or more
"legion". Print the word for a given number of monsters.

## Input

n (1 ≤ n ≤ 2000).

## Output

The word for n.

## Examples

### Example 1

Input:

```
7
```

Output:

```
several
```

### Example 2

Input:

```
40
```

Output:

```
lots
```

## Solution

Keep the lower ends of the ranges from the largest down, 1000, 500,
250, 100, 50, 20, 10, 5, 1, next to their words. Skip the ends that are
above n; the first one that is not gives the word. `O(1)`.

In the examples 7 passes 1000 down to 10 and stops at 5, "several";
40 stops at 20, "lots".

Pitfalls:

- the ends belong to the larger word: 5 is "several", 1000 is
  "legion";
- every n from 1000 to 2000 is "legion".

The answers agree with an independent accepted implementation on every
n from 1 to 2000.

## Optimized solutions

The optimized C++ solution looks the word up in the same table, but
reads with `scanf` and prints with `puts` instead of `iostream`: 116 KB
instead of 376 KB, with the same time.

The optimized Java solution parses the numbers byte by byte from
`System.in` instead of using `Scanner`: 0.093 s instead of 0.125 s and
340 KB instead of 1600 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1785_implementation.cpp](1785_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 376 KB | 11303506 |
| [1785_implementation.go](1785_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1080 KB | 11289797 |
| [1785_implementation.java](1785_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1600 KB | 11303507 |
| [1785_implementation.py](1785_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 424 KB | 11289798 |
| [1785_implementation.rs](1785_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 228 KB | 11289801 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1785_implementation_optimized.cpp](1785_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303636 |
| [1785_implementation_optimized.java](1785_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 340 KB | 11303777 |
