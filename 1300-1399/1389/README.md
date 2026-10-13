# 1389. Roadworks

[Timus 1389](https://acm.timus.ru/problem.aspx?space=1&num=1389) · difficulty 552 · dp

Original problem by Dmitry Ivankov and Alexander Ipatov, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 100 000 cities are joined by N − 1 two-way roads so that every
city can reach every other one: the roads form a tree. Close as many
roads as possible for repairs, with at most one closed road at every
city.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M = N − 1, then the M roads as pairs of cities.

## Output

The number K of closed roads, then the K roads written as in the input.

## Examples

### Example 1

Input:

```
4 3
1 2
2 3
3 4
```

Output:

```
2
1 2
3 4
```

## Solution

The closed roads form a matching, and a largest matching of a tree is
found greedily from the leaves. Take a leaf and its only neighbour: some
largest matching uses the road between them, since a matching that
uses another road at the neighbour can swap it for this one. So walk
the cities in reverse breadth-first order from city 1 and close the road
to the parent whenever both its ends are still free. The breadth-first
order replaces recursion, which can overflow the stack on a path of
100 000 cities. `O(N)`.

Pitfalls:

- the roads must be printed as written in the input and in input order;
  the judge appears to reject other orders of a correct answer, so the
  solutions mark the chosen roads and print them in one pass;
- a path of 100 000 cities can be too deep for recursion (generated test 1);
- a star allows a single road (test 03 and generated test 3).

The answers were compared on 300 random trees of up to 11 cities with a
search over all sets of roads. The tests are judged by a checker that
asks for the expected number of roads, each one written as in the input,
in input order, with no city on two of them.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1389_dp.cpp](1389_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.156 s | 6968 KB |
| [1389_dp.go](1389_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.078 s | 16820 KB |
| [1389_dp.java](1389_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 7304 KB |
| [1389_dp.py](1389_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.343 s | 49940 KB |
| [1389_dp.rs](1389_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 16272 KB |
