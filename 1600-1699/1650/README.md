# 1650. Billionaires

[Timus 1650](https://acm.timus.ru/problem.aspx?space=1&num=1650) · difficulty 185 · segment_tree

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
10¹¹). Then m and k (1 ≤ m ≤ 50000, 0 ≤ k ≤ 50000) and k lines
"day name destination" in increasing order of day. Names and cities are
up to 20 Latin letters, case-sensitive.

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1650_segment_tree.cpp](1650_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O((n + k) log C) | AC | 0.093 s | 20656 KB |
| [1650_segment_tree.go](1650_segment_tree.go) | Go 1.14 x64 | segment_tree | O((n + k) log C) | AC | 0.171 s | 18416 KB |
| [1650_segment_tree.java](1650_segment_tree.java) | Java 1.8 | segment_tree | O((n + k) log C) | AC | 0.203 s | 27324 KB |
| [1650_segment_tree.py](1650_segment_tree.py) | Python 3.12 x64 | segment_tree | O((n + k) log C) | AC | 1.062 s | 27776 KB |
| [1650_segment_tree.rs](1650_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O((n + k) log C) | AC | 0.031 s | 12940 KB |
