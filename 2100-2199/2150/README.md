# 2150. Splitting a dense friendship graph into pairs and triangles

[Timus 2150](https://acm.timus.ru/problem.aspx?space=1&num=2150) · difficulty 1139 · greedy, matching

Original problem by Semyon Trifochkin, from the Ural School Programming Contest 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n pupils, each friends with at least ⌈n / 2⌉ others, must be split into
groups of two or three in which everybody knows everybody. Print a
split or NO. Any valid split is accepted. The limits are 1 second and
256 MB.

## Input

n, 2 ≤ n ≤ 1000, then the symmetric friendship matrix.

## Output

NO, or YES, the number of groups and every group as its size and
members.

## Checking

A checker verifies that the groups cover every pupil once and that all
members of a group are friends.

## Examples

### Example 1

Input:

```
2
0 1
1 0
```

Output:

```
YES
1
2 1 2
```

### Example 2

Input:

```
5
0 1 0 1 1
1 0 1 0 1
0 1 0 1 1
1 0 1 0 1
1 1 1 1 0
```

Output:

```
YES
2
3 1 2 5
2 3 4
```

## Solution

The answer is always YES: a near-perfect matching exists, and an odd
pupil out can join one of its pairs.

Take a greedy maximal matching. The unmatched pupils are pairwise not
friends, or the greedy pass would have paired them, so all their
friends are matched. For two unmatched pupils u and v there is a pair
(a, b) with u friends with a and v friends with b, or the other way
round: otherwise every pair would get at most two of the edges from u
and v, at most n − 2 edges in total, while u and v have at least n
friends together. Replacing (a, b) by (u, a) and (v, b) adds one pair,
so the unmatched pupils are fixed two at a time.

If n is odd one pupil w is left. It has at least ⌈n / 2⌉ friends, more
than the (n − 1) / 2 pairs, so both pupils of some pair are its friends,
and that pair becomes a triangle with w. Every step scans the pairs once
per fixed pupil, O(n²) in total.

In the second example pupil 5 knows everybody, so the pair (1, 2) takes
it as a third member and (3, 4) stays a pair.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2150_greedy_matching.cpp](2150_greedy_matching.cpp) | G++ 13.2 x64 | greedy, matching | O(n^2) | AC | 0.031 s | 540 KB |
| [2150_greedy_matching.go](2150_greedy_matching.go) | Go 1.14 x64 | greedy, matching | O(n^2) | AC | 0.031 s | 6248 KB |
| [2150_greedy_matching.java](2150_greedy_matching.java) | Java 1.8 | greedy, matching | O(n^2) | AC | 0.156 s | 1532 KB |
| [2150_greedy_matching.py](2150_greedy_matching.py) | Python 3.12 x64 | greedy, matching | O(n^2) | AC | 0.187 s | 19168 KB |
| [2150_greedy_matching.rs](2150_greedy_matching.rs) | Rust 1.75 x64 | greedy, matching | O(n^2) | AC | 0.031 s | 3292 KB |
