# 1180. Who wins when stones are taken in powers of two

[Timus 1180](https://acm.timus.ru/problem.aspx?space=1&num=1180) · difficulty 89 · games

Original problem by Dmitry Filimonenkov, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N ≤ 10²⁵⁰` stones. Two players take turns removing a power of
two (1, 2, 4, 8, …) stones; whoever takes the last stone wins. Say who
wins with best play, and if it is the first player, the smallest number
of stones the first move can take and still win.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, with up to 251 digits.

## Output

`2`, or `1` and the smallest winning first move.

## Examples

### Example 1

Input:

```
8
```

Output:

```
1
2
```

## Solution

No power of two is divisible by 3, so from a multiple of 3 every move
leaves a pile that is not a multiple of 3. From any other pile, taking 1
or 2 stones, the remainder modulo 3, leaves a multiple of 3. Zero is a
multiple of 3, so the player who always leaves a multiple of 3 takes the
last stone. The second player wins exactly when `N` is divisible by 3;
otherwise the first player wins, and the smallest winning move is
`N mod 3`, because no move of 1 or 2 other than that one leaves a
multiple of 3. `N mod 3` is the digit sum modulo 3. `O(digits)`.

Pitfalls:

- `N` has up to 251 digits, so it cannot be read as a number;
- the winning move must be the smallest one, and both 1 and 2 are powers
  of two, so the remainder itself is it.

The answers were checked against a direct game search for every `N` up to
399.

## Language notes

- All languages add up the digits modulo 3 while reading them as text.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1180_games.cpp](1180_games.cpp) | G++ 13.2 x64 | games | O(digits) | AC | 0.015 s | 384 KB |
| [1180_games.go](1180_games.go) | Go 1.14 x64 | games | O(digits) | AC | 0.015 s | 1104 KB |
| [1180_games.java](1180_games.java) | Java 1.8 | games | O(digits) | AC | 0.125 s | 1568 KB |
| [1180_games.py](1180_games.py) | Python 3.12 x64 | games | O(digits) | AC | 0.078 s | 400 KB |
| [1180_games.rs](1180_games.rs) | Rust 1.75 x64 | games | O(digits) | AC | 0.015 s | 212 KB |
