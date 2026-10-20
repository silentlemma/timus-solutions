# 2161. A knight who wins every duel whatever the others buy

[Timus 2161](https://acm.timus.ru/problem.aspx?space=1&num=2161) · difficulty 754 · greedy

Original problem by Aleksey Bykov, from the Ural Team Programming Contest 2021.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n knights has attack aᵢ, shield dᵢ and gᵢ coins; one coin adds
one point to the attack or to the shield, and nobody knows how the
others spend theirs. Every pair of knights fights once; a knight is
crushed when the rival's attack is at least their shield, and wins when
the rival is crushed and they are not. Find a knight who can buy
equipment that wins all fights whatever the others do, or print −1. The
limits are 1.5 seconds and 256 MB.

## Input

n, 1 ≤ n ≤ 10⁵, then the triples aᵢ, dᵢ, gᵢ, each between 0 and 10⁹.

## Output

The number of that knight, or −1.

## Examples

### Example 1

Input:

```
2
100 4 5
1 2 8
```

Output:

```
-1
```

### Example 2

Input:

```
3
5 2 2
4 1 10
10 4 0
```

Output:

```
2
```

## Solution

Rival j can reach attack aⱼ + gⱼ or shield dⱼ + gⱼ, and knight i must be
safe against both extremes. So i needs a shield above
A = max over j ≠ i of (aⱼ + gⱼ) and an attack of at least
D = max over j ≠ i of (dⱼ + gⱼ). Knight i manages it exactly when

max(0, A + 1 − dᵢ) + max(0, D − aᵢ) ≤ gᵢ.

The maxima over everybody but i come from the two largest values of
each kind and the position of the largest. At most one knight can pass,
since such a knight beats everybody else. With no rivals the maxima are
missing and a lone knight wins. The work is O(n), with 64-bit sums.

In the first example knight 1 can raise the shield only to 9, and
knight 2 can raise the attack to 9 as well, so knight 1 is not safe;
knight 2 cannot reach a shield above 105.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2161_greedy.cpp](2161_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.203 s | 2556 KB |
| [2161_greedy.go](2161_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.203 s | 6900 KB |
| [2161_greedy.java](2161_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.156 s | 7484 KB |
| [2161_greedy.py](2161_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.265 s | 32468 KB |
| [2161_greedy.rs](2161_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.015 s | 8320 KB |
