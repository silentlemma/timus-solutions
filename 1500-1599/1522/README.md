# 1522. Factory

[Timus 1522](https://acm.timus.ru/problem.aspx?space=1&num=1522) · difficulty 1764 · greedy

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N toys (1 ≤ N ≤ 10⁵) each pass through machines A, B and C in this
order, taking ai, bi and ci time units (each from 1 to 10⁶); every
machine handles one toy at a time, and the toys may go in any order,
the same on all machines. Machine B is fast: max bi ≤ min ai or
max bi ≤ min ci. Find the smallest time to finish all toys and an order
that achieves it.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then ai, bi and ci for each toy.

## Output

The smallest finishing time, then an optimal order of the toys. Any
optimal order is accepted.

## Examples

### Example 1

Input:

```
5
3 1 6
1 1 2
5 2 5
7 1 4
10 2 8
```

Output:

```
33
2 1 3 5 4
```

### Example 2

Input:

```
1
5 4 7
```

Output:

```
16
1
```

## Solution

When B is dominated like this, the line behaves like two machines with
times ai + bi and bi + ci, and Johnson's rule for two machines gives
an optimal order: first the toys with ai + bi < bi + ci, by increasing
ai + bi, then the rest by decreasing bi + ci. Simulate the order to get
the time: each machine starts a toy when both the machine and the
toy's previous stage are free. `O(N log N)`.

Pitfalls:

- the rule relies on the condition on B; the general three-machine
  problem is much harder;
- B can be dominated by C instead of A (test 04, gen2);
- toys with equal combined times may go in either group (tests 03, 05);
- the total reaches about 3·10¹¹, beyond 32 bits (gen3);
- many orders can be optimal, so the tests use a checker (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1522_greedy.cpp](1522_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.187 s | 4564 KB |
| [1522_greedy.go](1522_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.062 s | 9752 KB |
| [1522_greedy.java](1522_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.281 s | 10816 KB |
| [1522_greedy.py](1522_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.343 s | 50996 KB |
| [1522_greedy.rs](1522_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.078 s | 11432 KB |
