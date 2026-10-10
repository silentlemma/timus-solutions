# 1152. The least damage from monsters on balconies around a hall

[Timus 1152](https://acm.timus.ru/problem.aspx?space=1&num=1152) · difficulty 155 · bitmask

Original problem by Evgeny Bryzgalov, from the Ural Team Programming Championship, Perm, April 2001, English round.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` balconies, `3 ≤ N ≤ 20`, stand in a circle, each with 1 to 100
monsters. One shot destroys three neighbouring balconies (balcony `N`
neighbours balcony 1). After every shot, every monster still alive deals
one unit of damage. Shots go on until no monsters remain. Find the least
total damage.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then the numbers of monsters on the balconies.

## Output

The least total damage.

## Examples

### Example 1

Input:

```
7
3 4 2 2 1 4 1
```

Output:

```
9
```

## Solution

The state is the set of balconies still occupied, a mask of `N` bits.
From a state, a shot at balcony `i` clears `i − 1`, `i` and `i + 1` and
leaves the set `rest`; it costs the number of monsters in `rest`, and then
the best play from `rest` follows. So with `damage(∅) = 0`

`damage(mask) = min over shots that hit something of alive(rest) + damage(rest)`.

Only states reachable from the full circle matter: their cleared parts are
unions of runs of three neighbours, and for `N = 20` there are just 15126
of them. Memoized recursion visits only those, with `N` shots each, and
the depth is at most `⌈N / 3⌉`. Shots that hit no occupied balcony are
skipped; they never help.

Pitfalls:

- the circle wraps around, so the shot at balcony 1 also clears balcony
  `N`;
- the damage after the last shot is zero, since nothing is left;
- the order of shots matters, because large groups should fall early.

The answers were compared with a bottom-up table over all `2^N` subsets
on 120 random inputs with up to 13 balconies and on every test with 20.

## Language notes

- All languages memoize the same recursion; Python keeps the memo in a
  cache keyed by the mask, the others in an array of `2^N` entries.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1152_bitmask.cpp](1152_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(S·N²) | AC | 0.015 s | 3868 KB |
| [1152_bitmask.go](1152_bitmask.go) | Go 1.14 x64 | bitmask | O(S·N²) | AC | 0.031 s | 10052 KB |
| [1152_bitmask.java](1152_bitmask.java) | Java 1.8 | bitmask | O(S·N²) | AC | 0.125 s | 5356 KB |
| [1152_bitmask.py](1152_bitmask.py) | Python 3.12 x64 | bitmask | O(S·N²) | AC | 0.625 s | 2420 KB |
| [1152_bitmask.rs](1152_bitmask.rs) | Rust 1.75 x64 | bitmask | O(S·N²) | AC | 0.001 s | 1592 KB |
