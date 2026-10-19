# 2069. The best route with at most two turns

[Timus 2069](https://acm.timus.ru/problem.aspx?space=1&num=2069) · difficulty 226 · greedy

Original problem by Oleg Merkurev, prepared by Alexander Borzunov, from the Ural Regional School Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city is a grid of n vertical and m horizontal streets, and every street
has its own popularity. A route goes along the streets from the upper
left corner to the lower right one, and its coolness is the smallest
popularity among the streets on which it covers a non-zero distance. Find
the largest possible coolness. The limits are 1 second and 64 MB.

## Input

n and m, 2 ≤ n, m ≤ 10⁵, then the n popularities of the vertical streets
from left to right and the m popularities of the horizontal streets from
top to bottom, one per line, each from 1 to 10⁹.

## Output

The largest coolness.

## Examples

### Example 1

Input:

```
2 3
4
8
2
7
3
```

Output:

```
4
```

### Example 2

Input:

```
4 3
12
4
12
3
21
5
16
```

Output:

```
12
```

## Solution

Let v₁ … vₙ be the vertical streets and h₁ … hₘ the horizontal ones; the
route starts where v₁ meets h₁ and ends where vₙ meets hₘ. Its first
step goes along v₁ or h₁, and its last step along vₙ or hₘ, so there are
four cases.

- It starts on v₁ and ends on hₘ. The coolness is at most min(v₁, hₘ),
  and going down v₁ and then right along hₘ reaches it.
- It starts on h₁ and ends on vₙ: at most min(h₁, vₙ), reached by going
  right and then down.
- It starts on h₁ and ends on hₘ. To change rows the route must move
  along some vertical street, so the coolness is at most
  min(h₁, max v, hₘ). Going right along h₁ to the best vertical street,
  down it and right along hₘ reaches this bound.
- It starts on v₁ and ends on vₙ: symmetrically min(v₁, max h, vₙ).

Every route falls into one of the cases and each bound is reached, so
the answer is the largest of the four values, found in O(n + m).

In the first example the first two cases give min(4, 3) = 3 and
min(2, 8) = 2, while the last one goes down v₁ = 4, right along h₂ = 7
and down v₂ = 8, with coolness 4.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2069_greedy.cpp](2069_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.140 s | 988 KB |
| [2069_greedy.go](2069_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.062 s | 5704 KB |
| [2069_greedy.java](2069_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.140 s | 1344 KB |
| [2069_greedy.py](2069_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.109 s | 21716 KB |
| [2069_greedy.rs](2069_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.031 s | 6328 KB |
