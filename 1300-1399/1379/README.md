# 1379. Cups Transportation

[Timus 1379](https://acm.timus.ru/problem.aspx?space=1&num=1379) · difficulty 581 · graphs

Original problem by Pavel Egorov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A truck weighing 3000 kg must bring as many cups as it can, 100 g each
and no more than the 10 000 000 ordered, from junction 1 to junction N,
N ≤ 500, within 24 hours. Every two-way road has a travel time in
minutes and a largest allowed weight of the truck in grams. Print the
largest number of cups.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then M lines: the ends of a road, its time and its weight
limit.

## Output

The number of cups.

## Examples

### Example 1

Input:

```
3 3
1 2 10 3000220
2 3 20 3000201
1 3 1 3000099
```

Output:

```
2
```

### Example 2

Input:

```
1 0
```

Output:

```
10000000
```

## Solution

A heavier truck can use fewer roads, so whether it arrives in time only
gets worse as the load grows. A route's weight limit equals that of
some road, so binary search over the road limits of at least
3 000 000 g. For each one, Dijkstra's algorithm uses only the roads
that bear that weight and never keeps a time over 1440 minutes. With
the heaviest weight W that arrives in time, the answer is
min(10 000 000, ⌊(W − 3 000 000) / 100⌋). `O((N + M log M) · log M)`.

Pitfalls:

- with N = 1 the cups are already at the venue: all 10 000 000 of them
  (example 2);
- exactly 24 hours, 1440 minutes, is still in time (test 03);
- the fastest way may bear less than a slower one (test 05);
- a road bearing exactly the empty truck allows no cups at all
  (test 06);
- roads can take no time (test 07).

The answers were compared with trying every simple path on 400 random
graphs of up to 6 junctions.

## Language notes

- Python needs PyPy: a chain of short roads inside a complete graph of
  day-long ones makes searches scan many roads, about 0.5 s with
  CPython and 0.25 s with PyPy.
- Java keeps its heap as an array of plain longs, time and vertex packed
  in one number: a priority queue of small arrays exceeded the time limit
  on the judge's test 46.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1379_graphs.cpp](1379_graphs.cpp) | G++ 13.2 x64 | graphs | O((N + M log M) · log M) | AC | 0.265 s | 7532 KB |
| [1379_graphs.go](1379_graphs.go) | Go 1.14 x64 | graphs | O((N + M log M) · log M) | AC | 0.515 s | 23772 KB |
| [1379_graphs.java](1379_graphs.java) | Java 1.8 | graphs | O((N + M log M) · log M) | AC | 0.500 s | 11512 KB |
| [1379_graphs.py](1379_graphs.py) | PyPy 3.10 x64 | graphs | O((N + M log M) · log M) | AC | 0.500 s | 58564 KB |
| [1379_graphs.rs](1379_graphs.rs) | Rust 1.75 x64 | graphs | O((N + M log M) · log M) | AC | 0.046 s | 15788 KB |
