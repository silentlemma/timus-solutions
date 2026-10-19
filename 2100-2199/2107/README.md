# 2107. Completing a jump rule that repeats after k seconds

[Timus 2107](https://acm.timus.ru/problem.aspx?space=1&num=2107) · difficulty 1488 · dp, graphs

Original problem by Alexey Danilyuk, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Dancers stand on platforms 1 … n, and every second each dancer on
platform i jumps to platform f(i). Some values of f are fixed, the others
(given as 0) may be chosen freely. Choose them so that after k seconds
every dancer is back on the starting platform, or report that it is
impossible. Any valid completion is accepted. The limits are 2 seconds
and 150 MB.

## Input

n and k, 1 ≤ n ≤ 35, 1 ≤ k ≤ 10⁹, then f(1) … f(n), 0 ≤ f(i) ≤ n.

## Output

"No", or "Yes" and the completed f.

## Checking

A checker verifies that the printed f keeps the fixed values and returns
everyone home after k seconds.

## Examples

### Example 1

Input:

```
3 4
1 2 3
```

Output:

```
Yes
1 2 3
```

### Example 2

Input:

```
3 4
0 0 0
```

Output:

```
Yes
1 2 3
```

### Example 3

Input:

```
3 1
2 2 2
```

Output:

```
No
```

### Example 4

Input:

```
2 666
2 0
```

Output:

```
Yes
2 1
```

### Example 5

Input:

```
2 777
2 0
```

Output:

```
No
```

## Solution

Everyone is home after k seconds exactly when f is a permutation whose
cycle lengths all divide k. So two fixed values with the same target give
"No", and a cycle already closed by the fixed values must have a length
dividing k.

The rest of the fixed edges form disjoint paths; a platform with an open
value and no incoming edge is a path of one vertex. Completing f means
joining the paths into cycles: the end of each path points to the start
of the next one in its group. So the paths have to be split into groups
whose total number of vertices divides k.

Only the lengths of the paths matter, so a state is a count of how many
paths of every length are still unused, encoded in a mixed radix. The
product of (count + 1) over the lengths with total at most 35 stays below
a thousand states. A group is any non-empty sub-state whose total divides
k. To avoid counting the same split in different orders, the group for a
state must contain a path of the largest length present in it; a state is
solvable when such a group leaves a solvable remainder. The stored choices
are then replayed to build the cycles from the actual paths.

In the fourth example 1 → 2 is a path of two vertices and 666 is even, so
the cycle 1 → 2 → 1 works; for 777 it does not.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2107_dp_graphs.cpp](2107_dp_graphs.cpp) | G++ 13.2 x64 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.015 s | 464 KB |
| [2107_dp_graphs.go](2107_dp_graphs.go) | Go 1.14 x64 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.031 s | 1144 KB |
| [2107_dp_graphs.java](2107_dp_graphs.java) | Java 1.8 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.125 s | 576 KB |
| [2107_dp_graphs.py](2107_dp_graphs.py) | Python 3.12 x64 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.093 s | 936 KB |
| [2107_dp_graphs.rs](2107_dp_graphs.rs) | Rust 1.75 x64 | dp, graphs | O(S^2 n) with S < 10^3 states | AC | 0.031 s | 268 KB |
