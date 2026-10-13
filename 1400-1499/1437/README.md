# 1437. Gasoline Station

[Timus 1437](https://acm.timus.ru/problem.aspx?space=1&num=1437) · difficulty 493 · bfs

Original problem by Alexey Lakhtin, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three cans hold from 0 to 255 litres each. The pump can only fill a can
to the brim, petrol may be poured from one can into another until the
first is empty or the second is full, and nothing may be spilled. Only
after all pouring, some of the cans are emptied into the tank. How many
different positive volumes can the tank receive?

Time limit: 1 second. Memory limit: 64 MB.

## Input

The three capacities, one per line.

## Output

The number of volumes.

## Examples

### Example 1

Input:

```
0
3
4
```

Output:

```
6
```

## Solution

Search all states (x, y, z) of the cans from all empty, with three
moves to fill a can and six moves to pour one can into another. After
any move some can is empty or full, so only a few tens of thousands of
the 256³ states can be reached. Every reached state gives the sums of
its non-empty subsets of cans as volumes for the tank; count the
distinct positive ones. `O(S)` for S reachable states, at most about
3·2·256².

Pitfalls:

- zero litres does not count (tests 01, 03);
- a can that is already full cannot take more, so in the example 5
  litres cannot be made (test 01);
- equal cans only ever hold full loads (test 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1437_bfs.cpp](1437_bfs.cpp) | G++ 13.2 x64 | bfs | O(S) | AC | 0.031 s | 16164 KB |
| [1437_bfs.go](1437_bfs.go) | Go 1.14 x64 | bfs | O(S) | AC | 0.046 s | 10572 KB |
| [1437_bfs.java](1437_bfs.java) | Java 1.8 | bfs | O(S) | AC | 0.156 s | 20420 KB |
| [1437_bfs.py](1437_bfs.py) | Python 3.12 x64 | bfs | O(S) | AC | 0.406 s | 17212 KB |
| [1437_bfs.rs](1437_bfs.rs) | Rust 1.75 x64 | bfs | O(S) | AC | 0.062 s | 3104 KB |
