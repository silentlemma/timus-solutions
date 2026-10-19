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

n ≤ 20, then the n replies, each a name of Latin letters, possibly with
`+one`.

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2100_implementation.cpp](2100_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 404 KB |
| [2100_implementation.go](2100_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB |
| [2100_implementation.java](2100_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.156 s | 1596 KB |
| [2100_implementation.py](2100_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 420 KB |
| [2100_implementation.rs](2100_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 236 KB |
