# 1523. K-inversions

[Timus 1523](https://acm.timus.ru/problem.aspx?space=1&num=1523) · difficulty 296 · fenwick

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a permutation a1, …, an of 1 … n (1 ≤ n ≤ 20000), count its
k-inversions (2 ≤ k ≤ 10): index sequences i1 < i2 < … < ik with
ai1 > ai2 > … > aik. Print the count modulo 10⁹.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n and k, then the permutation.

## Output

The number of k-inversions modulo 10⁹.

## Examples

### Example 1

Input:

```
3 2
3 1 2
```

Output:

```
2
```

### Example 2

Input:

```
5 3
5 4 3 2 1
```

Output:

```
10
```

## Solution

Let ends[i] count the decreasing runs of length L that end at position
i; for L = 1 it is 1 everywhere. A run of length L + 1 ending at i is a
run of length L ending at some earlier position p with ap > ai, followed
by i. So each level is one pass from left to right with a Fenwick tree
over the values: query the sum over values above ai, then add ends[i]
at ai. Counting values from the top turns "above" into a prefix. k − 1
passes give `O(n·k·log n)`.

Pitfalls:

- k can exceed the length of the longest decreasing run, or even n, and
  then the answer is 0 (tests 04, 05, gen3);
- the counts grow like C(20000, 10), so reduce them modulo 10⁹ as
  they are added (gen2, gen5).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1523_fenwick.cpp](1523_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 596 KB |
| [1523_fenwick.go](1523_fenwick.go) | Go 1.14 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 4576 KB |
| [1523_fenwick.java](1523_fenwick.java) | Java 1.8 | fenwick | O(n * k * log n) | AC | 0.125 s | 3512 KB |
| [1523_fenwick.py](1523_fenwick.py) | Python 3.12 x64 | fenwick | O(n * k * log n) | AC | 0.562 s | 5172 KB |
| [1523_fenwick.rs](1523_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 1292 KB |
