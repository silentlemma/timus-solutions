# 2100. Count the guests and avoid thirteen

[Timus 2100](https://acm.timus.ru/problem.aspx?space=1&num=2100) · difficulty 29 · implementation

Original problem by Alexey Danilyuk, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A couple invites n friends; a reply `name+one` means the friend comes
with a partner. Everyone sits at one table with the couple, and if
exactly 13 would sit there, a dummy is added. Every seat costs $100.
Output the cost of the dinner. The limits are 1 second and 64 MB.

## Input

1 ≤ n ≤ 20, then the n replies, each a name of at most 20 Latin letters,
possibly with `+one`.

## Output

The cost in dollars.

## Examples

### Example 1

Input:

```
3
Ted+one
Robin
Barney
```

Output:

```
600
```

### Example 2

Input:

```
6
Alice+one
Bob+one
carl
Debora+one
Enrique+one
FRED+one
```

Output:

```
1400
```

## Solution

Start with the two hosts, add 2 for a reply ending in `+one` and 1
otherwise, turn 13 into 14, and multiply by 100.

In the second example 2 + 5 · 2 + 1 = 13 people would sit, so a dummy
joins them: 1400.

## Optimized solutions

The optimized C++ solution reads the replies with `scanf` into a buffer
of 25 bytes instead of `iostream` and counts those that contain `+`,
since only a reply ending in `+one` has one: 128 KB instead of 396 KB,
with the same time.

The optimized Java solution reads the input in 1 KB blocks and, like the
C++ one, counts the `+` signs in the replies byte by byte instead of
using `Scanner` and strings: 0.093 s instead of 0.140 s and 364 KB
instead of 1572 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2100_implementation.cpp](2100_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 396 KB | 11303533 |
| [2100_implementation.go](2100_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB | 11294707 |
| [2100_implementation.java](2100_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1572 KB | 11303534 |
| [2100_implementation.py](2100_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 420 KB | 11294708 |
| [2100_implementation.rs](2100_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 236 KB | 11294714 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2100_implementation_optimized.cpp](2100_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303968 |
| [2100_implementation_optimized.java](2100_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 364 KB | 11303969 |
