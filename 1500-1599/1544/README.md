# 1544. Classmates 3

[Timus 1544](https://acm.timus.ru/problem.aspx?space=1&num=1544) · difficulty 1252 · graphs

Original problem: folklore, prepared by Sergey Pupyrev for the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 50 computers form a connected network; each runs the European (E)
or the Japanese (J) protocol. Asking a computer to switch protocol
switches it together with everything reachable from it through
computers on its old protocol. Find the fewest requests that leave all
computers on one protocol, and list them as "computer protocol".

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, the N protocols, then the M links.

## Output

K, then the K requests. Any optimal list is accepted.

## Examples

### Example 1

Input:

```
5 5
E E E J J
1 2
1 3
1 4
4 2
5 2
```

Output:

```
1
1 J
```

## Solution

Glue linked computers with the same protocol into regions. A request
recolours one region, which then merges with all neighbouring regions,
since they all have the other protocol. In the graph of regions,
switching the same region again and again absorbs one more ring of
regions each time, so a region with eccentricity e finishes the job in e
requests; the best choice is a centre of the region graph, and the
answer is its radius. A breadth-first search from every region finds it
in `O(R·(R + M))` for R regions.

That no plan beats the radius was checked by a breadth-first search over
all 2^N protocol states on 300 random networks of up to 10 computers;
every answer matched.

Pitfalls:

- in this construction, the requests must alternate the protocol of
  the chosen computer, starting with the other protocol (tests 04, 07);
- the best region may run either protocol (test 06);
- a network on one protocol needs 0 requests (tests 02, 03);
- several optimal plans exist, so the tests use a checker (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1544_graphs.cpp](1544_graphs.cpp) | G++ 13.2 x64 | graphs | O(R * (R + M)) | AC | 0.015 s | 208 KB |
| [1544_graphs.go](1544_graphs.go) | Go 1.14 x64 | graphs | O(R * (R + M)) | AC | 0.031 s | 1192 KB |
| [1544_graphs.java](1544_graphs.java) | Java 1.8 | graphs | O(R * (R + M)) | AC | 0.109 s | 776 KB |
| [1544_graphs.py](1544_graphs.py) | Python 3.12 x64 | graphs | O(R * (R + M)) | AC | 0.093 s | 748 KB |
| [1544_graphs.rs](1544_graphs.rs) | Rust 1.75 x64 | graphs | O(R * (R + M)) | AC | 0.015 s | 260 KB |
