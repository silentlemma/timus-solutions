# 1676. Mortal Kombat

[Timus 1676](https://acm.timus.ru/problem.aspx?space=1&num=1676) · difficulty 1707 · matching

Original problem by Magaz Asanov (prepared by Alexander Ipatov), from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N monsters must each fight a different one of M Earth fighters, and the
fighters must win every fight; a 0/1 matrix tells which fighter beats
which monster. For every pair (monster i, fighter j), print 1 if
choosing that pair as the first fight makes a full winning assignment
impossible, and 0 otherwise.

## Input

N and M (1 ≤ N ≤ 300, N ≤ M ≤ 1500), then N rows of M digits.

## Output

The N × M matrix of answers.

## Examples

### Example 1

Input:

```
4 4
1111
1000
1111
1111
```

Output:

```
1000
0111
1000
1000
```

### Example 2

Input:

```
4 5
10000
10000
10000
10000
```

Output:

```
11111
11111
11111
11111
```

## Solution

A pair is fine exactly when it belongs to some matching of all monsters
to fighters who beat them. Kuhn's algorithm finds one such matching; if
it fails for some monster, every pair is impossible.

Otherwise monster i keeps its own fighter m(i), and may take a fighter
j that beats it in two more ways:

- j is free, and i simply switches;
- j belongs to monster k, which takes another fighter that beats it:
  the one i gives up (closing a cycle), a free one, or the fighter of a
  third monster, which must then move on in the same way.

With an arrow k → k₂ when k can take the fighter of k₂, this means: k
reaches i, or k reaches a monster that some free fighter beats (k itself
included). The reachability among the N monsters comes from a search
from each of them (bitset transitive closure in Python), so the whole is
`O(N² · M)`.

Pitfalls:

- a fighter who beats nobody gives a column of ones (test 05); a monster
  nobody beats makes the whole answer ones (test 04);
- with no full assignment the answer is all ones, even for pairs where
  the fighter wins (example 2);
- the rows are digits without spaces.

The answers match a search over all full assignments on 600 random small
inputs, and an independent accepted implementation on large ones.

## Language notes

- Python keeps each row as one big integer and runs Kuhn's search with
  the unvisited fighters as a bit set, so a step takes the next
  candidate straight from adj[u] & unseen.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1676_matching.cpp](1676_matching.cpp) | G++ 13.2 x64 | matching | O(N^2 M) | AC | 0.078 s | 2528 KB |
| [1676_matching.go](1676_matching.go) | Go 1.14 x64 | matching | O(N^2 M) | AC | 0.078 s | 7576 KB |
| [1676_matching.java](1676_matching.java) | Java 1.8 | matching | O(N^2 M) | AC | 0.406 s | 10656 KB |
| [1676_matching.py](1676_matching.py) | Python 3.12 x64 | matching | O(N^2 M) | AC | 0.296 s | 3976 KB |
| [1676_matching.rs](1676_matching.rs) | Rust 1.75 x64 | matching | O(N^2 M) | AC | 0.046 s | 4120 KB |
