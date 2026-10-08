# 1003. First contradictory parity answer

[Timus 1003](https://acm.timus.ru/problem.aspx?space=1&num=1003) · difficulty 386 · dsu, hashing

Original problem from the Central European Olympiad in Informatics 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There is an unknown sequence of `L` bits (`L ≤ 10^9`). You get `q ≤ 5000`
statements in order; statement `i` says that the number of ones among the bits
`l..r` (1-based, `l ≤ r`) is even or odd.

Find the largest `X` such that some bit sequence satisfies the first `X`
statements. If all statements can hold at once, `X = q`.

The input holds several such tests.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Tests one after another. A test is a line with `L`, a line with `q`, and `q`
lines `l r even` or `l r odd`. A line `-1` ends the input.

## Output

For every test, one line with `X`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
3
1 2 odd
3 4 even
1 4 even
-1
```

Output:

```
2
```

### Example 2

Input:

```
8
4
1 8 even
1 4 odd
5 8 odd
2 3 even
3
2
1 3 odd
1 3 even
-1
```

Output:

```
4
1
```

## Solution

Let `P(k)` be the parity of the number of ones among the first `k` bits, with
`P(0) = 0`. A statement about `l..r` says `P(l-1) xor P(r) = 0` (even) or `1`
(odd). Conversely, any values of `P` with `P(0) = 0` come from exactly one
bit sequence. So the statements are consistent exactly when the equations
`P(a) xor P(b) = w` have a solution.

Process the statements in order with a disjoint set union over prefix
positions that also stores, for every node, the parity relative to its parent.
`find` returns the root and the parity of the node relative to it. For a new
equation, if both ends are in the same set the equation must agree with the
parities already known; otherwise the two sets are merged with the right
parity on the new edge. The first equation that disagrees gives `X`.

Positions go up to `10^9`, but at most `2q` of them appear: they are mapped to
consecutive ids with a hash map. With path compression and union by rank the
work is `O(q · α(q))` per test.

Pitfalls:

- the equations are about prefixes `l-1` and `r`, not about `l` and `r`;
- after the first contradiction the rest of the test still has to be read;
- a test may have no statements at all.

## Language notes

- **C++**: `std::unordered_map<int, int>` for the ids; a recursive `find` is
  fine, the trees are shallow with union by rank.
- **Go**: `map[int]int` and a recursive `find` with path compression.
- **Python**: an iterative `find` that compresses the path and recomputes the
  parities of the nodes on it.
- **Java**: arrays of size `2q` per test, `HashMap<Integer, Integer>` for the
  ids, iterative `find`.
- **Rust**: `HashMap<i64, usize>` with `entry().or_insert_with()` to create
  nodes; iterative `find`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1003_dsu_hashing.cpp](1003_dsu_hashing.cpp) | G++ 13.2 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.015 s | 632 KB |
| [1003_dsu_hashing.go](1003_dsu_hashing.go) | Go 1.14 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.046 s | 3420 KB |
| [1003_dsu_hashing.java](1003_dsu_hashing.java) | Java 1.8 | dsu, hashing | O(q·α(q)) per test | AC | 0.109 s | 4788 KB |
| [1003_dsu_hashing.py](1003_dsu_hashing.py) | Python 3.12 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.093 s | 4388 KB |
| [1003_dsu_hashing.rs](1003_dsu_hashing.rs) | Rust 1.75 x64 | dsu, hashing | O(q·α(q)) per test | AC | 0.001 s | 1268 KB |
