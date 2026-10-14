# 1521. War Games 2

[Timus 1521](https://acm.timus.ru/problem.aspx?space=1&num=1521) · difficulty 121 · fenwick

Original problem by Ilya Grebnov, Nikita Rybak and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N soldiers (1 ≤ N ≤ 100000), numbered 1 to N, march in a circle. In
each round one soldier leaves: first soldier K (1 ≤ K ≤ N), then each
time the soldier K places ahead of the one who left last, counting only
those still marching. Print the soldiers in the order they leave.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and K.

## Output

The numbers of the soldiers in the order they leave.

## Examples

### Example 1

Input:

```
5 3
```

Output:

```
3 1 5 2 4
```

## Solution

Number the soldiers still marching 0, 1, … in circle order. If the last
one to leave had rank r among them, the next one has rank
(r + K − 1) mod (soldiers left), since the leaver's place is taken by
the soldier behind. A Fenwick tree holds 1 for each soldier still
marching; descending it by powers of two finds the soldier of a given
rank in `O(log N)`, and removing a soldier is a point update.
`O(N log N)` in all.

Pitfalls:

- deleting from a plain list costs `O(N)` per round, `O(N²)` in all,
  too slow for 100000 soldiers (gen1);
- K = 1 sends the soldiers out in order (test 03, gen5);
- K = N starts from the last soldier (test 04, gen4).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1521_fenwick.cpp](1521_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.031 s | 2136 KB |
| [1521_fenwick.go](1521_fenwick.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.062 s | 2460 KB |
| [1521_fenwick.java](1521_fenwick.java) | Java 1.8 | fenwick | O(N log N) | AC | 0.171 s | 5016 KB |
| [1521_fenwick.py](1521_fenwick.py) | Python 3.12 x64 | fenwick | O(N log N) | AC | 0.640 s | 12028 KB |
| [1521_fenwick.rs](1521_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.031 s | 2512 KB |
