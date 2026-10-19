# 2005. The Shortest Allowed Five-Stop Route

[Timus 2005](https://acm.timus.ru/problem.aspx?space=1&num=2005) · difficulty 94 · bruteforce

Original problem by Mikhail Rubinchik. (Prepared by Oleg Merkurev), from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Visit five locations exactly once, starting at 1 and finishing at 5.
Location 3 must not be the penultimate stop. Given distances between
every pair, find a route of minimum total distance and its length. Any
optimal allowed route is acceptable.

## Input

A 5 by 5 integer distance matrix. Every entry is between 0 and 10000,
diagonal entries are zero, distances are symmetric and satisfy the
triangle inequality: `d[i][j]≤d[i][k]+d[k][j]`. Time limit 0.5 seconds,
memory 64 MB.

## Output

On the first line print the minimum total distance. On the second print
the five location numbers in visiting order, separated by spaces. Ties
may be resolved arbitrarily.

## Checking

A checker verifies that the route is allowed, that the printed length is
its length and that it is optimal; any optimal route is accepted.

## Examples

```
0 2600 3800 2600 2500
2600 0 5300 3900 4400
3800 5300 0 1900 4500
2600 3900 1900 0 3700
2500 4400 4500 3700 0
```

```
13500
1 2 3 4 5
```

The displayed route costs `2600+5300+1900+3700=13500`; its penultimate
stop is 4, so it obeys the restriction.

## Solution

Only the order of locations 2, 3 and 4 varies. Their six permutations
contain two ending in 3, which are forbidden. The four remaining routes
are `1,2,3,4,5`, `1,3,2,4,5`, `1,3,4,2,5` and `1,4,3,2,5`. Sum the four
consecutive distances for each and retain a cheapest route together with
its cost.

The programs enumerate the first and last intermediate locations,
requiring them to differ and excluding 3 as the last. The middle
location is the remaining one. Internally these locations have
zero-based indices 1, 2, 3, whose sum is 6; subtracting the selected
endpoints recovers the middle index. This visits every allowed
permutation exactly once and no forbidden permutation. Every required
answer is among these four candidates, so choosing their minimum proves
optimality. Updating the saved cost and route together ensures that the
printed route has the printed length.

Time `O(1)` and memory `O(1)`, since there are always five locations,
four candidates and four edges per candidate. Each sum is at most 40000,
so signed 32-bit integers suffice. No shortest-path preprocessing is
needed for the given metric distances.

The restriction concerns the penultimate stop, not the second or third
stop. Keep location 5 last and location 1 first. Zero distances and tied
optima are legal. Initialize the best cost so zero can win; 10000 is not
a valid upper bound for a whole route. Convert internal zero-based
indices back to 1..5 in the output.

## Language notes

All five languages evaluate the same four candidates and consume all 25
matrix entries. Fixed arrays are used where convenient; Python uses
small lists. The saved route is preserved independently of later
candidates.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2005_bruteforce.cpp](2005_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.031 s | 432 KB |
| [2005_bruteforce.go](2005_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1108 KB |
| [2005_bruteforce.java](2005_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 432 KB |
| [2005_bruteforce.py](2005_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.093 s | 508 KB |
| [2005_bruteforce.rs](2005_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 224 KB |
