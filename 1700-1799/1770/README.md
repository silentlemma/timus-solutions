# 1770. The Party of Ural Champions

[Timus 1770](https://acm.timus.ru/problem.aspx?space=1&num=1770) · difficulty 1719 · graphs

Original problem by Igor Chevdar, from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city has n crossroads joined by two-way roads into a connected
network. A road may carry one board, seen only by drivers going one way
along it. A table gives, for every ordered pair of crossroads, the
fewest boards a driver must see going from the first to the second.
Build a road network with boards that gives exactly this table, or
report that none exists.

## Input

n (2 ≤ n ≤ 300), then the n × n table with entries from 0 to n − 1 and
zeros on the diagonal.

## Output

`NO`, or `YES` and n rows of n characters: 0 for no road between i and
j, 1 for a road on which nothing is seen going from i to j, 2 for a road
whose board is seen going from i to j. Any fitting network is accepted.

## Examples

### Example 1

Input:

```
5
0 1 1 1 1
1 0 1 0 1
0 0 0 0 0
2 1 2 0 2
0 0 0 0 0
```

Output:

```
YES
00202
00210
11001
02000
10100
```

### Example 2

Input:

```
2
0 1
1 0
```

Output:

```
NO
```

## Solution

A road from i to j costs 0 or 1 boards each way, and the trip from i to
j can always take it, so a road is only possible where it costs at
least the table both ways. Since one road shows at most one board, the
table's pair (i to j, j to i) must be (0, 0), (1, 0) or (0, 1), that is,
add up to at most 1; we choose road costs equal to the table's entries.

Put in every such road. With all road costs at least the table, every
trip costs at least the table too, as long as the table itself obeys
the triangle inequality, and adding roads only lowers costs; so this
network gives the smallest costs any network can give. The table is
possible exactly when this network reproduces it, which also makes the
network connected. The costs come from Floyd–Warshall in `O(n³)`; the
Python solution instead searches from each crossroad level by level,
with the crossroads of one cost kept as bit masks.

In the first example crossroads 3 and 5 can reach any crossroad without
seeing a board: a free road joins them, and roads from 1 and 2 lead into
both with a board seen on the way in. Crossroad 4 gets only a road to 2, with a
board seen on the way out, and 1 and 4 see each other's boards too
often for a road. The program also keeps the road from 2 to 5, which
the example leaves out; both networks give the table.

Pitfalls:

- a pair with 1 both ways cannot have a road, since a road has only
  one board;
- a table can fail the triangle inequality, which the comparison
  catches;
- the answer is a network, not a unique one, so the checker recomputes
  the table from the printed roads.

The answers agree with an independent accepted implementation, checked
on both sides, on 100 random cases: tables of random networks of up to
8 and of 300 crossroads, random small tables and tables with one entry
changed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1770_graphs.cpp](1770_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^3) | AC | 0.093 s | 692 KB |
| [1770_graphs.go](1770_graphs.go) | Go 1.14 x64 | graphs | O(n^3) | AC | 0.125 s | 3164 KB |
| [1770_graphs.java](1770_graphs.java) | Java 1.8 | graphs | O(n^3) | AC | 0.171 s | 7360 KB |
| [1770_graphs.py](1770_graphs.py) | Python 3.12 x64 | graphs | O(n^3) | AC | 0.250 s | 7252 KB |
| [1770_graphs.rs](1770_graphs.rs) | Rust 1.75 x64 | graphs | O(n^3) | AC | 0.062 s | 2560 KB |
