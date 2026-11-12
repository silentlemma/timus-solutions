# 1072. The shortest route between two computers through IP subnets

[Timus 1072](https://acm.timus.ru/problem.aspx?space=1&num=1072) · difficulty 504 · bfs, graphs

Original problem by Evgeny Kobzev, from the Ural State University Personal Contest Online, February 2001, Students Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` computers (`2 ≤ N ≤ 90`) have up to 5 network interfaces each; an
interface is an IP address and a subnet mask (some ones followed by
zeros). Two interfaces are in one subnet when `IP1 AND mask1` equals
`IP2 AND mask2`. A packet goes directly between computers that share a
subnet, and from one subnet to another only through a computer with
interfaces in both. Find a path through the fewest computers between two
given computers.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`; then for each computer the number of interfaces `K` and `K` lines
with an IP address and a mask in dotted form; then the numbers of the two
computers.

## Output

`Yes` and the computers of the path in order, or `No` if there is no path.

## Checking

Any shortest path is accepted. The checker verifies that the path goes
from the first computer to the second, that every two neighbours on it
share a subnet, and that it has as few computers as possible.

## Examples

### Example 1

Input:

```
6
2
10.0.0.1 255.0.0.0
192.168.0.1 255.255.255.0
1
10.0.0.2 255.0.0.0
3
192.168.0.2 255.255.255.0
212.220.31.1 255.255.255.0
212.220.35.1 255.255.255.0
1
212.220.31.2 255.255.255.0
2
212.220.35.2 255.255.255.0
195.38.54.65 255.255.255.224
1 
195.38.54.94 255.255.255.224
1 6
```

Output:

```
Yes
1 3 5 6
```

## Solution

Reduce every interface to the number `IP AND mask`. Two computers are
joined when they have an equal number among their interfaces; a hop
between joined computers is exactly one direct transfer, and a computer
in the middle of a path has interfaces in the subnets on both sides of
it. So the task is a shortest path in this graph of computers, and a
breadth-first search from the first computer finds it. Following the
recorded parents back from the second computer gives the path.
`O(N^2 · K^2)`.

Pitfalls:

- the subnet test uses each interface's own mask: `10.0.0.77/255.0.0.0`
  and `10.0.0.5/255.255.255.0` are in one subnet, because both give
  `10.0.0.0`, while `10.1.0.1/255.0.0.0` and `10.1.0.2/255.255.0.0` are
  not, although each address lies inside the other range;
- masks `0.0.0.0` and `255.255.255.255` are allowed and need no special
  case;
- the addresses are 32-bit unsigned numbers; a signed type works too, as
  long as only equality is compared.

The path lengths were checked against Floyd–Warshall on the same graph,
built separately with the masks checked for the ones-then-zeros form.

## Optimized solutions

The Go incidence-list BFS indexes each subnet value by its member computers instead of comparing all pairs of interfaces. When a computer is taken from the BFS queue, expand each of its subnets and visit every unvisited member. The first expansion comes from a computer of minimum distance, so all members receive their shortest possible next-step distance. Delete that subnet’s membership list afterwards; a later expansion cannot improve any route. Each interface is processed a constant number of times, giving expected O(N·K) time with the hash map and O(N·K) space. Parents recover a shortest path. Duplicate interfaces are harmless, and identical endpoints return the one-computer path.

The accepted Go 1.14 x64 run takes 0.031 s versus 0.015 s for the base and uses 280 KB versus 1180 KB.

The accepted base implementations [1072_bfs.cpp](1072_bfs.cpp), [1072_bfs.java](1072_bfs.java), [1072_bfs.py](1072_bfs.py), [1072_bfs.rs](1072_bfs.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

All five ordinary-input BFS base files are preserved. The new Go version parses addresses directly into unsigned 32-bit values and uses standard input/output handles. Equality compares IP AND its own mask, not the pair (IP AND mask, mask); different masks may therefore describe matching subnet values. The existing C++, Java, Python and Rust files also cover the fast set under the saved ranking admission rules.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1072_bfs.cpp](1072_bfs.cpp) | G++ 13.2 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 208 KB | 11278927 |
| [1072_bfs.go](1072_bfs.go) | Go 1.14 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 1180 KB | 11278929 |
| [1072_bfs.java](1072_bfs.java) | Java 1.8 | bfs | O(N^2 · K^2) | AC | 0.078 s | 776 KB | 11278935 |
| [1072_bfs.py](1072_bfs.py) \* | Python 3.12 x64 | bfs | O(N^2 · K^2) | AC | 0.078 s | 612 KB | 11278931 |
| [1072_bfs.rs](1072_bfs.rs) | Rust 1.75 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 224 KB | 11278936 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1072_bfs_optimized.go](1072_bfs_optimized.go) \* | Go 1.14 x64 | bfs | O(N·K) | AC | 0.031 s | 280 KB | 11314790 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
