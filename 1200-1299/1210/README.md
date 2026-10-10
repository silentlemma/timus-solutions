# 1210. The cheapest climb through levels of planets

[Timus 1210](https://acm.timus.ru/problem.aspx?space=1&num=1210) · difficulty 170 · dp

Original problem by Leonid Volkov, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Planets are arranged in levels 0 to `N < 30`, at most 30 per level, and
level 0 holds a single planet, the traveller's home. Links lead only from
a planet of one level to planets of the next, and each costs an integer
from `−32768` to `32767`; a negative cost means the spirit guarding it
pays the traveller. Find the cheapest route from home to any planet of
level `N`; it may be negative. A route is known to exist.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` blocks separated by lines holding `*`. Block `i` starts
with the number of planets on level `i`; then, for each of them, a line
of pairs "planet of level `i − 1`, cost" ended by `0`.

## Output

The least total cost.

## Examples

### Example 1

Input:

```
3
2
1 15 0
1 5 0
*
3
1 -5 2 10 0
1 3 0
2 40 0
*
2
1 1 2 5 3 -5 0
2 -19 3 -20 0
```

Output:

```
-1
```

## Solution

The map is layered and every link climbs one level, so there are no
cycles and negative costs do no harm: the cheapest way to a planet is the
cheapest way to one of the planets linking to it plus that link. Keep the
cheapest cost for every planet of the current level, starting with 0 for
home, and build the next level's costs from the incoming links listed in
its block. The answer is the smallest cost on level `N`. `O(L)` for `L`
links.

Pitfalls:

- a planet may have no incoming link at all, or only links from
  unreachable planets; such a planet must stay unreachable instead of
  passing on a generous link from it;
- the `*` lines are only separators and can be skipped when reading
  numbers;
- the total stays below `30 · 32768` in absolute value, so 32-bit integers
  are enough.

The answers were compared with a separately written solution on 300
random maps, half of them with unreachable planets.

## Language notes

- Python and Rust filter the `*` tokens out of the input stream; the
  other languages skip them in their number readers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1210_dp.cpp](1210_dp.cpp) | G++ 13.2 x64 | dp | O(L) | AC | 0.031 s | 384 KB |
| [1210_dp.go](1210_dp.go) | Go 1.14 x64 | dp | O(L) | AC | 0.031 s | 1220 KB |
| [1210_dp.java](1210_dp.java) | Java 1.8 | dp | O(L) | AC | 0.140 s | 5668 KB |
| [1210_dp.py](1210_dp.py) | Python 3.12 x64 | dp | O(L) | AC | 0.125 s | 3276 KB |
| [1210_dp.rs](1210_dp.rs) | Rust 1.75 x64 | dp | O(L) | AC | 0.046 s | 732 KB |
