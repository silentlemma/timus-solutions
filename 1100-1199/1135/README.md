# 1135. Counting the turns of recruits facing each other until the row is stable

[Timus 1135](https://acm.timus.ru/problem.aspx?space=1&num=1135) · difficulty 160 · math

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 30000` recruits stand in a row, each facing left (`<`) or right
(`>`). Every second, all pairs of neighbours facing each other (`><`) turn
around at once. Count the pair turns until nothing changes, or print `NO`
if it never stops.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then exactly `N` characters `<` and `>` spread over lines of up to
255 characters.

## Output

The number of pair turns.

## Examples

### Example 1

Input:

```
6
>><<><
```

Output:

```
7
```

## Solution

A turning pair `><` becomes `<>`: as far as the directions go, it is a
swap of two neighbours. Each such swap removes exactly one pair of
recruits (not necessarily neighbours) where a `>` stands before a `<`,
and creates none. The row is stable exactly when no `><` is left, that is
when every `<` stands before every `>`, which has no such pairs at all.
So the process always stops, `NO` is never printed, and the number of
turns equals the number of pairs with `>` before `<`. One pass counts
them: keep the number of `>` seen so far and add it at every `<`. `O(N)`.

Pitfalls:

- the row is split over several lines, possibly with empty ones, so read
  characters until `N` of them are found;
- the answer reaches `15000² = 2.25·10⁸`, still within 32 bits, but 64-bit
  counters cost nothing;
- the order of turns inside a second does not matter for the count.

The answers were compared with a second-by-second simulation on 200
random rows of up to 300 recruits.

## Language notes

- All languages skip the line breaks and keep the same running count.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1135_math.cpp](1135_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 132 KB |
| [1135_math.go](1135_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1100 KB |
| [1135_math.java](1135_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 532 KB |
| [1135_math.py](1135_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 420 KB |
| [1135_math.rs](1135_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 248 KB |
