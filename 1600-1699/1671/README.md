# 1671. Anansi's Cobweb

[Timus 1671](https://acm.timus.ru/problem.aspx?space=1&num=1671) · difficulty 108 · dsu

Original problem by Dmitry Poletaev (prepared by Alex Samsonov), from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cobweb has N knots and M threads between pairs of knots. Q of the
threads are cut one by one in a given order. After each cut, print how
many pieces (connected parts) the web falls into.

## Input

N and M (2 ≤ N ≤ 100000, 1 ≤ M ≤ 100000), the M threads as pairs of
different knots, then Q (1 ≤ Q ≤ M) and the numbers of the threads to
cut, all different.

## Output

The Q numbers of pieces, separated by spaces.

## Examples

### Example 1

Input:

```
4 4
1 2
2 3
1 3
3 4
3
2 4 3
```

Output:

```
1 2 3
```

### Example 2

Input:

```
3 1
1 2
1
1
```

Output:

```
3
```

## Solution

Cutting is hard to follow, but joining is easy with a disjoint set
union, so the process runs backwards. Start from the web as it is after
all the cuts: join every thread that is never cut. Then go through the
cuts from the last to the first: the current number of pieces is the
answer after that cut, and then the thread goes back in. Each join that
connects two different sets lowers the count by one. With path
compression this is `O((N + M) α(N))`.

Pitfalls:

- the same two knots may be joined by several threads, and cutting one
  of them changes nothing (test 03);
- the answer after a cut is the count before putting that thread back.

The answers match a recount of the pieces by search after every cut on
200 small random webs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1671_dsu.cpp](1671_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + M) alpha(N)) | AC | 0.218 s | 2716 KB |
| [1671_dsu.go](1671_dsu.go) | Go 1.14 x64 | dsu | O((N + M) alpha(N)) | AC | 0.031 s | 5912 KB |
| [1671_dsu.java](1671_dsu.java) | Java 1.8 | dsu | O((N + M) alpha(N)) | AC | 0.140 s | 6400 KB |
| [1671_dsu.py](1671_dsu.py) | Python 3.12 x64 | dsu | O((N + M) alpha(N)) | AC | 0.265 s | 35132 KB |
| [1671_dsu.rs](1671_dsu.rs) | Rust 1.75 x64 | dsu | O((N + M) alpha(N)) | AC | 0.031 s | 11476 KB |
