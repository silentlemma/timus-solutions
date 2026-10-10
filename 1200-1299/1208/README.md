# 1208. The most legendary teams without a shared member

[Timus 1208](https://acm.timus.ru/problem.aspx?space=1&num=1208) · difficulty 214 · bitmask

Original problem by Leonid Volkov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `K ≤ 18` legendary teams of three programmers each, and some
programmers have been in more than one of them. A programmer can play for
only one team, so find the largest number of teams that can take part
together, that is with no programmer in two of them.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`K`, then the three names of each team, up to 20 lowercase letters each.

## Output

The largest number of teams that can take part.

## Examples

### Example 1

Input:

```
7
gerostratos scorpio shamgshamg
zaitsev silverberg cousteau
zaitsev petersen shamgshamg
clipper petersen shamgshamg
clipper bakirelli vasiliadi
silverberg atn dolly
knuth dijkstra bellman
```

Output:

```
4
```

## Solution

Two teams clash when they share a member, and the answer is the largest
set of teams with no clash between them. For each team keep a bit mask
of the teams it clashes with, itself included. For a set of teams given
as a mask, look at its lowest team: either it stays home, leaving the set
without it, or it plays, leaving the set without it and without every
team it clashes with. So

`best(S) = max(best(S without i), 1 + best(S minus clash(i)))`, `i` the
lowest team in `S`.

Both smaller sets are smaller numbers, so the table can be filled for
all `2^K` masks in increasing order. `O(2^K + K²)`.

Pitfalls:

- a team clashes with itself, which removes it when it is taken;
- the same programmer can be in many teams, so clashes are not just
  between neighbours in the list.

The answers were compared with a separately written solution on 200
random inputs and on teams drawn from pools of 3 to 1000 programmers.

## Language notes

- Python evaluates the same recursion lazily with `functools.lru_cache`,
  which only visits the sets that can actually arise; the other
  languages fill the whole table.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1208_bitmask.cpp](1208_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K + K²) | AC | 0.015 s | 976 KB |
| [1208_bitmask.go](1208_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K + K²) | AC | 0.062 s | 3204 KB |
| [1208_bitmask.java](1208_bitmask.java) | Java 1.8 | bitmask | O(2^K + K²) | AC | 0.109 s | 2688 KB |
| [1208_bitmask.py](1208_bitmask.py) | Python 3.12 x64 | bitmask | O(2^K + K²) | AC | 0.078 s | 456 KB |
| [1208_bitmask.rs](1208_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K + K²) | AC | 0.046 s | 684 KB |
