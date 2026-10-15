# 1709. Penguin-Avia

[Timus 1709](https://acm.timus.ru/problem.aspx?space=1&num=1709) · difficulty 153 · dsu

Original problem by Alexander Ipatov, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An airline flies between some pairs of n airports, given as a
symmetric 0/1 matrix. The new network must connect every airport to
every other, possibly with changes, and use as few flights as any
connected network can. Cancelling a flight costs d, opening one costs
a. Find the cheapest change and print it as a matrix with d for a
cancelled flight, a for a new one and 0 elsewhere.

## Input

n (2 ≤ n ≤ 100), then d and a (1 ≤ d, a ≤ 10⁶), then n rows of the
matrix.

## Output

The least sum, then the n × n plan, symmetric. Any optimal plan is
accepted.

## Examples

### Example 1

Input:

```
6
2 3
011000
101000
110000
000011
000101
000110
```

Output:

```
7
0d0000
d00000
000a00
00a0d0
000d00
000000
```

## Solution

A connected network with the fewest flights is a spanning tree with
n − 1 flights. If the tree keeps k of the m old flights, the plan
cancels m − k and opens n − 1 − k, so more kept flights is cheaper
whatever d and a are. The kept flights form a forest inside the old
network, so k is at most n − c, where c is the number of its connected
parts, and a spanning forest reaches it.

So build a spanning forest with a disjoint-set union: an old flight
between two different trees is kept, any other is cancelled. Then
join the c trees with c − 1 new flights from airport 1 to one airport
of every other tree. The sum is d(m − n + c) + a(c − 1). `O(n²)`.

Pitfalls:

- the sum reaches 4851 · 10⁶ when all flights exist, which needs
  64 bits (test 04);
- a new flight between two trees never doubles an old one, as an old
  flight would have joined them already;
- the matrix rows are written without spaces.

A checker accepts any optimal plan. It checks the sum, the symmetry,
that d and a stand only on old and on missing flights, and that the
result is a spanning tree. The answers match an independent accepted
implementation on 800 random graphs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1709_dsu.cpp](1709_dsu.cpp) | G++ 13.2 x64 | dsu | O(n²) | AC | 0.015 s | 464 KB |
| [1709_dsu.go](1709_dsu.go) | Go 1.14 x64 | dsu | O(n²) | AC | 0.031 s | 1188 KB |
| [1709_dsu.java](1709_dsu.java) | Java 1.8 | dsu | O(n²) | AC | 0.093 s | 796 KB |
| [1709_dsu.py](1709_dsu.py) | Python 3.12 x64 | dsu | O(n²) | AC | 0.093 s | 656 KB |
| [1709_dsu.rs](1709_dsu.rs) | Rust 1.75 x64 | dsu | O(n²) | AC | 0.015 s | 288 KB |
