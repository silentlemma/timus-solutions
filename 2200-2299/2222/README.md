# 2222. Most knights on a 3 × N board whose attack graph is a tree

[Timus 2222](https://acm.timus.ru/problem.aspx?space=1&num=2222) · difficulty 1870 · dp

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place as many knights as possible on a 3 × N board so that the graph
of knights that attack each other is a tree: connected and without
cycles. Print any optimal placement. The limits are 1 second and
256 MB.

## Input

N, 1 ≤ N ≤ 10⁵.

## Output

Three rows of N zeros and ones.

## Examples

### Example 1

Input:

```
3
```

Output:

```
0 1 1
1 0 1
1 1 1
```

### Example 2

Input:

```
2
```

Output:

```
1 0
0 0
0 1
```

## Solution

A knight attacks at most two columns away, so the board is filled column
by column with a profile DP over the last two columns. A state records
which of those six cells hold knights and which of them are already
connected to each other through earlier knights, relabelled in a
canonical order. Adding a column with a mask of knights joins each new
knight to the knights it attacks in the two previous columns; a join
inside one component would close a cycle and is forbidden, and a
component that leaves the profile without touching the new column is
only allowed if it is the whole finished tree, which moves to a
special finished state that accepts only empty columns. All states
reachable this way are generated once as a small automaton.

The DP keeps the most knights for every state, column by column. After
a few columns the vector of scores shifts by exactly 2 in every
reachable state at each step, and from then on every later step is the
same max-plus update, so the DP stops and the same choices are reused
for all remaining columns. The answer is the best state whose profile is
one component, and the placement is restored backwards through the
stored choices.

The first example puts 7 knights on the 3 × 3 board: the center attacks
nothing and stays empty, and the eight outer cells form a single cycle
of knight moves, so one of them is left out.

The automaton has a fixed size, so this takes O(N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2222_dp.cpp](2222_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 924 KB |
| [2222_dp.go](2222_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 2080 KB |
| [2222_dp.java](2222_dp.java) | Java 1.8 | dp | O(N) | AC | 0.171 s | 4124 KB |
| [2222_dp.py](2222_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.203 s | 8336 KB |
| [2222_dp.rs](2222_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 1656 KB |
