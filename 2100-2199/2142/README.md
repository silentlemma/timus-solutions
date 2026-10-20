# 2142. Paying red, blue and any mana with dual lands

[Timus 2142](https://acm.timus.ru/problem.aspx?space=1&num=2142) · difficulty 127 · greedy

Original problem by Valentin Zuev, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are A red lands, B blue lands and C dual lands; each gives one
mana, and a dual land gives red or blue as chosen. A spell needs X red
mana, Y blue mana and Z more of any color. Decide whether the lands are
enough. The limits are 1 second and 256 MB.

## Input

A, B, C, then X, Y, Z, all between 0 and 10⁹.

## Output

"It is a kind of magic" if the spell can be paid, otherwise "There are
no miracles in life".

## Examples

### Example 1

Input:

```
3 3 1
2 2 1
```

Output:

```
It is a kind of magic
```

### Example 2

Input:

```
5 6 5
6 5 6
```

Output:

```
There are no miracles in life
```

## Solution

Red lands should pay for red mana and blue lands for blue mana first,
since any land can pay the any-color part. What they leave unpaid,
max(0, X − A) + max(0, Y − B), has to come from the dual lands. After
that every remaining land of any kind can pay for the Z mana of any
color, so the second condition is A + B + C ≥ X + Y + Z. Both together
are necessary and sufficient. The sums reach 3 · 10⁹, beyond 32-bit
integers.

Pitfall (test 02, the second example): covering both colors is not enough.
Red needs 6 − 5 = 1 dual land, but in total 16 lands face 17 mana.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2142_greedy.cpp](2142_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.015 s | 124 KB |
| [2142_greedy.go](2142_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1088 KB |
| [2142_greedy.java](2142_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.109 s | 1620 KB |
| [2142_greedy.py](2142_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 416 KB |
| [2142_greedy.rs](2142_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.031 s | 228 KB |
