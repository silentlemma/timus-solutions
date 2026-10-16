# 1801. The Revolution Cup

[Timus 1801](https://acm.timus.ru/problem.aspx?space=1&num=1801) · difficulty 4973 · graphs

Original problem by Magaz Asanov, from the NEERC 2010 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

g·t teams lie in t pots of g teams each, and every team belongs to a
political party. Split them into g groups of t teams so that each group
has exactly one team from every pot and no two teams of the same party.
Print any such split, or report that there is none.

## Input

g and t (1 ≤ g, t ≤ 100), then the pots one after another, separated
by empty lines, each line a team name and its party name. Names are
up to 10 lowercase letters, and team names are all different.

## Output

"No", or "Yes" followed by the g groups, each preceded by an empty line
and listing its t team names one per line.

## Examples

### Example 1

Input:

```
2 3
cavalry red
guard white

infantry red
guerilla green

czechs white
gunners latvia
```

Output:

```
Yes

cavalry
guerilla
czechs

guard
infantry
gunners
```

### Example 2

Input:

```
2 2
cavalry red
guard white

czechs white
cossacks white
```

Output:

```
No
```

## Solution

Make a bipartite multigraph with the pots on one side and the parties on
the other, and every team an edge between its pot and its party. A
group is a colour: colour the edges with g colours so that no vertex
sees a colour twice. Every pot has exactly g edges, so it then sees
every colour once, and a party sees each colour at most once. By
König's theorem a bipartite graph can be coloured with as many colours
as its largest degree, so the answer is "No" exactly when some party
has more than g teams.

The colouring is built edge by edge. For an edge from pot u to party v,
take a colour a free at u and a colour b free at v. If they differ,
follow the path from u that alternates colours b and a. In a bipartite
graph it cannot end at v, which has no b edge. Swapping a and b along
it frees b at u, and the new edge gets colour b. The path visits each
pot at most once, so it has at most 2t + 1 edges. `O(g·t·(g + t))`.

In the first example the two red teams, cavalry and infantry, go to
different groups, and so do the white ones, guard and czechs.

Pitfalls:

- the check of party sizes is all it takes to answer "No";
- a plain greedy choice of colours gets stuck, so recolouring along
  alternating paths is needed;
- the empty lines between pots in the input are best skipped by reading
  words.

The checker requires every team once, one team from each pot in every
group and distinct parties within a group. All solutions pass it on
hundreds of small draws and on full draws of 100 pots with tight,
loose and overfull parties, and they agree on "No" with an independent
accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1801_graphs.cpp](1801_graphs.cpp) | G++ 13.2 x64 | graphs | O(g t (g + t)) | AC | 0.015 s | 5440 KB |
| [1801_graphs.go](1801_graphs.go) | Go 1.14 x64 | graphs | O(g t (g + t)) | AC | 0.046 s | 12424 KB |
| [1801_graphs.java](1801_graphs.java) | Java 1.8 | graphs | O(g t (g + t)) | AC | 0.140 s | 10672 KB |
| [1801_graphs.py](1801_graphs.py) | Python 3.12 x64 | graphs | O(g t (g + t)) | AC | 0.156 s | 13072 KB |
| [1801_graphs.rs](1801_graphs.rs) | Rust 1.75 x64 | graphs | O(g t (g + t)) | AC | 0.031 s | 9652 KB |
