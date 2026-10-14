# 1533. Fat Hobbits

[Timus 1533](https://acm.timus.ru/problem.aspx?space=1&num=1533) · difficulty 979 · matching

Original problem by Alexander Ipatov, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N hobbits (2 ≤ N ≤ 100) have distinct weights. Some pairs were weighed
against each other, and every hobbit knows all results, including what
follows from chains of them. A hobbit refuses to go if a hobbit known to
be lighter goes too. Find a largest group in which no hobbit is known to
be heavier than another.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then an N × N matrix of zeros and ones: a 1 in row i, column j means
hobbit i was weighed against hobbit j and turned out heavier.

## Output

The size of the group, then the numbers of its hobbits on one line. Any
largest group is accepted.

## Examples

### Example 1

Input:

```
2
0 1
0 0
```

Output:

```
1
2
```

### Example 2

Input:

```
3
0 0 0
0 0 0
0 0 0
```

Output:

```
3
1 2 3
```

## Solution

Close the weighings transitively (Floyd–Warshall on booleans); the
result is a strict partial order, and the task asks for its largest
antichain. By Dilworth's theorem that size equals the least number of
chains covering all hobbits, which is N minus a maximum matching in the
bipartite graph with a "heavier" and a "lighter" copy of every hobbit
and an edge i → j whenever i outweighs j. Kuhn's algorithm finds the
matching.

To list the hobbits, follow König's construction: start at the unmatched
heavier copies and walk alternating paths (any edge to a lighter copy,
then its matching edge back). Heavier copies not reached and lighter
copies reached form a minimum vertex cover; a hobbit with neither copy
in it is in the antichain, and there are exactly N minus the matching of
them. Two such hobbits cannot be comparable, since the edge between them
would be uncovered. `O(N³)`.

Pitfalls:

- the order has to be closed first: in test 03 hobbit 1 is heavier than
  hobbit 3 only through hobbit 2 (also tests 05, 07);
- the answer is not simply the lightest or the heaviest hobbits: in
  test 04 the middle layer of four wins over both single hobbits;
- several largest groups exist, so the tests use a checker (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1533_matching.cpp](1533_matching.cpp) | G++ 13.2 x64 | matching | O(N^3) | AC | 0.015 s | 204 KB |
| [1533_matching.go](1533_matching.go) | Go 1.14 x64 | matching | O(N^3) | AC | 0.046 s | 1244 KB |
| [1533_matching.java](1533_matching.java) | Java 1.8 | matching | O(N^3) | AC | 0.093 s | 588 KB |
| [1533_matching.py](1533_matching.py) | Python 3.12 x64 | matching | O(N^3) | AC | 0.093 s | 852 KB |
| [1533_matching.rs](1533_matching.rs) | Rust 1.75 x64 | matching | O(N^3) | AC | 0.046 s | 300 KB |
