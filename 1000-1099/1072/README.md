# 1072. The shortest route between two computers through IP subnets

[Timus 1072](https://acm.timus.ru/problem.aspx?space=1&num=1072) · difficulty 502 · bfs, graphs

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

## Language notes

- C++ reads an address with `scanf("%u")` and `".%u"` for the four parts;
  the other languages split the token at the dots.
- Java keeps the addresses in `int`, which overflows into negative values
  for high addresses, but `AND` and equality do not care.
- Python stores the subnets of a computer in a set and tests
  `isdisjoint`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1072_bfs.cpp](1072_bfs.cpp) | G++ 13.2 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 208 KB |
| [1072_bfs.go](1072_bfs.go) | Go 1.14 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 1180 KB |
| [1072_bfs.java](1072_bfs.java) | Java 1.8 | bfs | O(N^2 · K^2) | AC | 0.078 s | 776 KB |
| [1072_bfs.py](1072_bfs.py) | Python 3.12 x64 | bfs | O(N^2 · K^2) | AC | 0.078 s | 612 KB |
| [1072_bfs.rs](1072_bfs.rs) | Rust 1.75 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 224 KB |
