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

## Optimized solutions

C++/Go/Rust keep reverse-BFS leaf matching: a free deepest vertex can safely match its free parent, by the usual exchange argument. Replace per-vertex dynamic adjacency lists and duplicate endpoint arrays with uint32 head/to/next links. Road i uses directed edges 2i (input a→b) and2i+1 (b→a); xor1 reverses an edge, so these same records also recover the original printed orientation. Parent edge+1 uses zero as sentinel and lets traversal skip the reverse parent edge without another parent/visited array. BFS order is preallocated; mark used vertices by one byte. After BFS, links are never traversed again, so their previously unused high bits mark chosen roads without another array. A final input-order pass prints only marked roads with exact input orientation. All edge links are below200000, far below bit31; path100000 is iterative, not recursive. Time/space O(N), bounded streaming I/O, no full input or answer strings. All simple sources remain; Java/Python reuse admitted bases.

The accepted Rust 1.75 x64 run takes 0.078 s versus 0.031 s for the base and uses 2 768 KB versus 16272 KB.

The accepted base implementations [1389_dp.java](1389_dp.java), [1389_dp.py](1389_dp.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1389_dp.cpp](1389_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.156 s | 6968 KB | 11285891 |
| [1389_dp.go](1389_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.078 s | 16820 KB | 11285893 |
| [1389_dp.java](1389_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 7304 KB | 11285902 |
| [1389_dp.py](1389_dp.py) \* | Python 3.12 x64 | dp | O(N) | AC | 0.343 s | 49940 KB | 11285897 |
| [1389_dp.rs](1389_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 16272 KB | 11285909 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1389_dp_optimized.cpp](1389_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.031 s | 2536 KB | 11315786 |
| [1389_dp_optimized.go](1389_dp_optimized.go) | Go 1.14 x64 | dp | O(N) | AC | 0.046 s | 3948 KB | 11315793 |
| [1389_dp_optimized.rs](1389_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(N) | AC | 0.078 s | 2768 KB | 11315796 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
