# 1650. Billionaires

[Timus 1650](https://acm.timus.ru/problem.aspx?space=1&num=1650) · difficulty 174 · segment_tree

Original problem by Pavel Atnashev, from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n billionaires with known fortunes start in given cities. Over m days
they travel: a trip on day d leaves in the evening and arrives the next
morning, so it counts from day d + 1. For each city, count the days on
which its billionaires together were strictly the richest of all
cities, and list the cities with at least one such day, sorted by name.

## Input

n (1 ≤ n ≤ 10000), then n lines "name city fortune" (fortunes from 1 to
10¹¹). Then m and k (1 ≤ m ≤ 50000, 0 ≤ k ≤ 50000) and k lines "day name
destination" (1 ≤ day ≤ m − 1) in increasing order of day; nobody
travels more than once a day. Names and cities are up to 20 Latin
letters, case-sensitive.

## Output

"city days" for every city that led on at least one day, in plain
character order (ABC…Zabc…z).

## Examples

### Example 1

Input:

```
5
Abramovich London 15000000000
Deripaska Moscow 10000000000
Potanin Moscow 5000000000
Berezovsky London 2500000000
Khodorkovsky Chita 1000000000
25 9
1 Abramovich Anadyr
5 Potanin Courchevel
10 Abramovich Moscow
11 Abramovich London
11 Deripaska StPetersburg
15 Potanin Norilsk
20 Berezovsky Tbilisi
21 Potanin StPetersburg
22 Berezovsky London
```

Output:

```
Anadyr 5
London 14
Moscow 1
```

## Solution

Give every city that ever appears an index and keep a segment tree over
the city totals. Each node stores the largest total below it, how many
leaves reach it, and one of those leaves, so the root tells at once
whether one city is strictly ahead and which. A trip is two point
updates: the fortune leaves one city and joins another.

Between two travel days the leader does not change, so the days are
counted in blocks: before applying the trips of day d, the current
leader (if it is unique) gets the days from the last counted day to d;
after the last trip it gets the days up to m. Totals reach 10¹⁵, so
they are 64-bit. `O((n + k) log C)` for C cities.

Pitfalls:

- a tie at the top means nobody leads that day (test 03), so the input
  may produce no output at all;
- trips on day d still leave day d to the old city;
- the order is by character codes, so uppercase names come before all
  lowercase ones (test 05).

The answers match a day-by-day count on 60 random histories and an
independent accepted implementation on generated tests. That
implementation goes wrong when someone "travels" to the city they are
already in, which the judge's tests evidently never contain; the
program here treats such a trip as staying put.

## Optimized solutions

The optimized C++ solution reads the trips one at a time and applies
each as soon as it is read, instead of storing them all first: a trip
brings at most one new city, so the tree is sized from the start for the
starting cities plus k. One map from a name to the city and fortune
replaces two, a node keeps the index of its single leading city, or a
tie mark, instead of a count of leaves, the tree is built bottom-up from
the starting totals, and an update stops climbing as soon as a node
keeps its maximum and its leader, since nothing above it can change
then. Names are read with `scanf` into buffers of 21 bytes instead of
with `iostream`: {1650_segment_tree_optimized.cpp}.

The optimized Go solution reads the trips one at a time and applies each
as soon as it is read, instead of storing them all first: a trip brings
at most one new city, so the tree is sized from the start for the
starting cities plus k. One map from a name to the city and fortune
replaces two, a node keeps the index of its single leading city, or a
tie mark, instead of a count of leaves, the tree is built bottom-up from
the starting totals, and an update stops climbing as soon as a node
keeps its maximum and its leader, since nothing above it can change
then. The words come from a `bufio.Scanner` instead of `fmt.Fscan`:
{1650_segment_tree_optimized.go}.

The optimized Java solution reads the trips one at a time and applies
each as soon as it is read, instead of storing them all first: a trip
brings at most one new city, so the tree is sized from the start for the
starting cities plus k. One map from a name to the city and fortune
replaces two, a node keeps the index of its single leading city, or a
tie mark, instead of a count of leaves, the tree is built bottom-up from
the starting totals, and an update stops climbing as soon as a node
keeps its maximum and its leader, since nothing above it can change
then. The tokens are read line by line instead of collecting the whole
input in a `StringBuilder` first: {1650_segment_tree_optimized.java}.

The optimized Python solution reads the trips one at a time and applies
each as soon as it is read, instead of storing them all first: a trip
brings at most one new city, so the tree is sized from the start for the
starting cities plus k. One map from a name to the city and fortune
replaces two, a node keeps the index of its single leading city, or a
tie mark, instead of a count of leaves, the tree is built bottom-up from
the starting totals, and an update stops climbing as soon as a node
keeps its maximum and its leader, since nothing above it can change
then. The input is read line by line, one record per line, instead of
all at once: {1650_segment_tree_optimized.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1650_segment_tree_optimized.cpp`: time reduction -49.60%; memory
  reduction +50.94%; base: `1650_segment_tree.cpp`.

- `1650_segment_tree_optimized.go`: time reduction +45.61%; memory
  reduction +1.04%; base: `1650_segment_tree.go`.

- `1650_segment_tree_optimized.java`: time reduction -15.27%; memory
  reduction +46.58%; base: `1650_segment_tree.java`.

- `1650_segment_tree_optimized.py`: time reduction +1.51%; memory
  reduction +41.56%; base: `1650_segment_tree.py`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1650_segment_tree.cpp](1650_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O((n + k) log C) | AC | 0.125 s | 20700 KB | 11304018 |
| [1650_segment_tree.go](1650_segment_tree.go) | Go 1.14 x64 | segment_tree | O((n + k) log C) | AC | 0.171 s | 18416 KB | 11288517 |
| [1650_segment_tree.java](1650_segment_tree.java) | Java 1.8 | segment_tree | O((n + k) log C) | AC | 0.203 s | 27324 KB | 11288519 |
| [1650_segment_tree.py](1650_segment_tree.py) | Python 3.12 x64 | segment_tree | O((n + k) log C) | AC | 1.062 s | 27776 KB | 11288518 |
| [1650_segment_tree.rs](1650_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O((n + k) log C) | AC | 0.046 s | 13036 KB | 11304019 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1650_segment_tree_optimized.cpp](1650_segment_tree_optimized.cpp) \* | G++ 13.2 x64 | segment_tree | O((n + k) log C) | AC | 0.187 s | 10156 KB | 11307264 |
| [1650_segment_tree_optimized.go](1650_segment_tree_optimized.go) \* | Go 1.14 x64 | segment_tree | O((n + k) log C) | AC | 0.093 s | 18224 KB | 11307269 |
| [1650_segment_tree_optimized.java](1650_segment_tree_optimized.java) \* | Java 1.8 | segment_tree | O((n + k) log C) | AC | 0.234 s | 14596 KB | 11307271 |
| [1650_segment_tree_optimized.py](1650_segment_tree_optimized.py) \* | Python 3.12 x64 | segment_tree | O((n + k) log C) | AC | 1.046 s | 16232 KB | 11307267 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
