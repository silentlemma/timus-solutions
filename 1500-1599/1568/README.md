# 1568. Train Car Sorting

[Timus 1568](https://acm.timus.ru/problem.aspx?space=1&num=1568) · difficulty 1575 · constructive

Original problem by Sergey Pupyrev, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A train of 1 ≤ N ≤ 10000 cars numbered 1 … N in some order is sorted by
gluings: at a fork each car goes left or right, keeping their order,
and then the left part is glued in front of the right part. Find the
fewest gluings that put the cars in order 1 … N and print the order
before and after each of them.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the order of the cars.

## Output

The number K of gluings, then K + 1 lines with the orders. Any shortest
sequence is accepted.

## Examples

### Example 1

Input:

```
5
5 1 3 2 4
```

Output:

```
2
5 1 3 2 4
1 2 5 3 4
1 2 3 4 5
```

### Example 2

Input:

```
6
6 5 2 4 1 3
```

Output:

```
3
6 5 2 4 1 3
6 4 1 5 2 3
6 1 2 3 4 5
1 2 3 4 5 6
```

## Solution

Cut the numbers 1 … N into the fewest runs v, v + 1, …, w that already
stand left to right in the train; a new run starts wherever car v + 1
stands before car v. Number the runs 0 … r − 1.

A gluing is the reverse of a riffle shuffle, and an order comes from the
sorted one by k riffle shuffles exactly when it has at most 2^k such
runs (rising sequences) — a known fact about shuffling cards. So the
least number of gluings is K = ⌈log₂ r⌉, which a search over all
gluings confirmed for every order of up to 6 cars.

The gluings themselves are a radix sort on the run numbers: gluing b
sends the cars whose run number has bit b set to the right. After the
gluings for bits 0 … b, the cars stand sorted by the low b + 1 bits of
their run numbers and keep their old order on ties, so after all K the
runs stand in order and each run is already in order inside. `O(N log N)`.

Pitfalls:

- several shortest answers exist, and the solutions' answer to the first
  example differs from the statement's (a checker checks the moves);
- a sorted train needs no gluing: print 0, then its order
  (tests 03, 04);
- 2^13 runs need 13 gluings and one run more needs 14 (tests gen3,
  gen4).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1568_constructive.cpp](1568_constructive.cpp) | G++ 13.2 x64 | constructive | O(N log N) | AC | 0.046 s | 208 KB |
| [1568_constructive.go](1568_constructive.go) | Go 1.14 x64 | constructive | O(N log N) | AC | 0.031 s | 3168 KB |
| [1568_constructive.java](1568_constructive.java) | Java 1.8 | constructive | O(N log N) | AC | 0.093 s | 5580 KB |
| [1568_constructive.py](1568_constructive.py) | Python 3.12 x64 | constructive | O(N log N) | AC | 0.125 s | 6612 KB |
| [1568_constructive.rs](1568_constructive.rs) | Rust 1.75 x64 | constructive | O(N log N) | AC | 0.046 s | 2124 KB |
