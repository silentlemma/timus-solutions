# 2068. Parity of the number of splits

[Timus 2068](https://acm.timus.ru/problem.aspx?space=1&num=2068) · difficulty 108 · games

Original problem by Alexey Danilyuk, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n heaps of nuts, each with an odd number of nuts. Two players
take turns; a move splits one heap into three non-empty heaps, each again
with an odd number of nuts. A player who cannot move loses. Daenerys
moves first, then Stannis. Find the winner under optimal play. The limits
are 1 second and 64 MB.

## Input

An odd n, 1 ≤ n ≤ 777, then n odd heap sizes from 1 to 54321.

## Output

`Daenerys` if she wins, otherwise `Stannis`.

## Examples

### Example 1

Input:

```
1
3
```

Output:

```
Daenerys
```

### Example 2

Input:

```
3
1 1 1
```

Output:

```
Stannis
```

### Example 3

Input:

```
5
777 313 465 99 1
```

Output:

```
Daenerys
```

## Solution

No strategy matters here. A move replaces one heap by three, so the
number of heaps grows by exactly two, and the total number of nuts never
changes. The game is over exactly when every heap holds one nut: a heap
of 3 or more odd nuts can always be split as 1 + 1 + (a − 2). At that
point there are as many heaps as nuts, so the number of moves made is
always (S − n) / 2, the sum of (aᵢ − 1) / 2 over the heaps.

Daenerys makes the odd-numbered moves, so she wins exactly when this
number is odd. In the third example the heaps give 388 + 156 + 232 + 49
+ 0 = 825 moves, which is odd. The work is O(n).

## Language notes

The sum is at most 777 · 27160 and fits a 32-bit integer; it is kept in
64 bits anyway in C++ and Java.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2068_games.cpp](2068_games.cpp) | G++ 13.2 x64 | games | O(n) | AC | 0.015 s | 124 KB |
| [2068_games.go](2068_games.go) | Go 1.14 x64 | games | O(n) | AC | 0.031 s | 1108 KB |
| [2068_games.java](2068_games.java) | Java 1.8 | games | O(n) | AC | 0.093 s | 440 KB |
| [2068_games.py](2068_games.py) | Python 3.12 x64 | games | O(n) | AC | 0.093 s | 368 KB |
| [2068_games.rs](2068_games.rs) | Rust 1.75 x64 | games | O(n) | AC | 0.031 s | 248 KB |
