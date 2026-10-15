# 1645. Ski Race

[Timus 1645](https://acm.timus.ru/problem.aspx?space=1&num=1645) · difficulty 200 · fenwick

Original problem by Eugene Kurpilyansky and Alexey Samsonov, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Skiers 1 to n start one after another, 30 seconds apart, and the final
table ranks them by their own time. Only the order of finishing is
known. For each skier find the best and the worst place they could
take.

## Input

n (1 ≤ n ≤ 2000), then the skiers in the order they finished.

## Output

For each skier i, the best and the worst possible place.

## Examples

### Example 1

Input:

```
6
3 5 1 4 2 6
```

Output:

```
3 6
4 6
1 4
2 5
1 3
1 6
```

## Solution

Compare skier i with skier j:

- j started later and finished earlier: j was surely faster;
- j started earlier and finished later: j was surely slower;
- otherwise either is possible: only the order of finishing is known,
  not the times, so the gaps between finishes can make up for the
  30-second gaps between starts or not.

So the best place is one plus the number of later starters who finished
earlier, and the worst is one plus everyone except the earlier starters
who finished later. Let e be the number of earlier starters who also
finished earlier, and p the finishing position of skier i. The later
starters who finished earlier number p − 1 − e, so the best place is
p − e, and the worst place is (n − i) + e + 1: all later starters plus
the e earlier ones. A Fenwick tree over finishing positions, filled in
starting order, gives e for each skier. `O(n log n)`.

Pitfalls:

- an early finish is not an early place: in the example skier 1
  finishes third behind two later starters, so third place is the best
  possible;
- finishing in starting order decides nothing, every place stays open
  (test 03); finishing in reverse decides everything (test 04).

The answers match an independent accepted implementation on 90 random
races.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1645_fenwick.cpp](1645_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n log n) | AC | 0.015 s | 204 KB |
| [1645_fenwick.go](1645_fenwick.go) | Go 1.14 x64 | fenwick | O(n log n) | AC | 0.031 s | 1176 KB |
| [1645_fenwick.java](1645_fenwick.java) | Java 1.8 | fenwick | O(n log n) | AC | 0.093 s | 652 KB |
| [1645_fenwick.py](1645_fenwick.py) | Python 3.12 x64 | fenwick | O(n log n) | AC | 0.093 s | 852 KB |
| [1645_fenwick.rs](1645_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n log n) | AC | 0.046 s | 268 KB |
