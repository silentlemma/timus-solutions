# 1526. Martian Plates

[Timus 1526](https://acm.timus.ru/problem.aspx?space=1&num=1526) · difficulty 1326 · dp

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dinner consists of t/2 dishes (2 ≤ t ≤ 200, t even) chosen from n
kinds (1 ≤ n ≤ 10), with repeats allowed. A waiter brings dishes and
takes empty plates away; plates stack, and only the top plate can be taken.
m pairs (0 ≤ m ≤ 100) "i j" forbid bringing dish j while a plate of
dish i is anywhere on the table. Count the schedules of t items
(bringing a dish of some kind, or taking the top plate away) modulo p
(2 ≤ p ≤ 10⁴).

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

p, t, n and m, then the m pairs.

## Output

The number of schedules modulo p.

## Examples

### Example 1

Input:

```
10000 4 2 1
1 2
```

Output:

```
7
```

### Example 2

Input:

```
9999 6 10 2
2 3
6 7
```

Output:

```
4866
```

## Solution

A schedule is a forest of plates: each plate has the plates brought
while it lay on the table nested over it. Whether a dish may be
brought depends only on the set of kinds still allowed, which starts
as all kinds and, over a plate of kind x, shrinks to its part that x
does not forbid. So let F[S][q] count the schedules of q dishes with
the set S allowed. The first plate is some x in S with a dishes over
it, counted by F[S ∩ after(x)][a], and the other q − 1 − a dishes
follow it with S still allowed:
F[S][q] = Σ over a of G[S][a] · F[S][q − 1 − a], with
G[S][a] = Σ over x in S of F[S ∩ after(x)][a]. Only sets reachable from
the full set are needed; a smaller set comes first, and a set may
refer to itself at a smaller q. At most 2¹⁰ sets give
`O(2^n·t·(n+t))`.

Pitfalls:

- a pair forbids the dish while the other plate lies anywhere on the
  table, not only on top (test 04, gen2);
- the pair "i j" forbids bringing j over i, not the other way round
  (test 08);
- a dish can be forbidden over itself, and then its plates never stack
  (test 05);
- all 1024 sets of kinds can come up (test 04, gen2);
- the same pair may be given twice (test 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1526_dp.cpp](1526_dp.cpp) | G++ 13.2 x64 | dp | O(2^n * t * (n + t)) | AC | 0.001 s | 244 KB |
| [1526_dp.go](1526_dp.go) | Go 1.14 x64 | dp | O(2^n * t * (n + t)) | AC | 0.031 s | 1208 KB |
| [1526_dp.java](1526_dp.java) | Java 1.8 | dp | O(2^n * t * (n + t)) | AC | 0.140 s | 2992 KB |
| [1526_dp.py](1526_dp.py) | Python 3.12 x64 | dp | O(2^n * t * (n + t)) | AC | 0.109 s | 748 KB |
| [1526_dp.rs](1526_dp.rs) | Rust 1.75 x64 | dp | O(2^n * t * (n + t)) | AC | 0.015 s | 276 KB |
