# 1362. Classmates 2

[Timus 1362](https://acm.timus.ru/problem.aspx?space=1&num=1362) · difficulty 442 · dp

Original problem by Evgeny Krokhalev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An agency of N ≤ 100 000 employees is a tree: everyone but the director
has exactly one boss. Tanya has news, and anyone who knows it can call
their boss or one of their direct subordinates; a call takes one minute,
and one person makes one call at a time. Print the least number of
minutes until the whole agency knows. This is the tree version of
[1323](../1323/README.md).

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then N lines: line K lists the subordinates of employee K and ends
with 0. The last line holds Tanya's number.

## Output

The least number of minutes.

## Examples

### Example 1

Input:

```
10
2 3 0
4 5 7 0
6 9 0
0
0
8 10 0
0
0
0
0
2
```

Output:

```
5
```

## Solution

Calls go both up and down, so the boss is just one more neighbour. Root
the tree at Tanya; then the news enters every subtree once, through its
root.

Let time(v) be the minutes v needs to tell its whole subtree after
learning the news. If v calls its children in some order, the i-th
child hears at minute i and finishes at i + time(child). The best
order calls the slowest subtree first: sort the children's times in
decreasing order t₁ ≥ t₂ ≥ …, and time(v) = max(tᵢ + i). Swapping two
neighbours that are out of this order never hurts, which proves it.

The tree is walked in breadth-first order and the times are computed
from the leaves up, so even a chain of 100 000 needs no recursion.
`O(N log N)`.

Pitfalls:

- the director need not be the root: when Tanya is a subordinate, the news
  goes up and then down other branches (tests 03 and 04);
- a chain of 100 000 is too deep for recursion in most languages
  (generated test 2);
- a star of 100 000 needs 99 999 minutes, one call at a time (generated
  test 3).

The answers were compared with a search over all ways to make calls,
minute by minute, on 400 random trees of up to 8 employees.

## Language notes

- Java keeps the tree in flat arrays and reads the input byte by byte;
  Go reads it byte by byte too.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1362_dp.cpp](1362_dp.cpp) | G++ 13.2 x64 | dp | O(N log N) | AC | 0.171 s | 8896 KB |
| [1362_dp.go](1362_dp.go) | Go 1.14 x64 | dp | O(N log N) | AC | 0.093 s | 17784 KB |
| [1362_dp.java](1362_dp.java) | Java 1.8 | dp | O(N log N) | AC | 0.093 s | 6848 KB |
| [1362_dp.py](1362_dp.py) | Python 3.12 x64 | dp | O(N log N) | AC | 0.468 s | 33988 KB |
| [1362_dp.rs](1362_dp.rs) | Rust 1.75 x64 | dp | O(N log N) | AC | 0.031 s | 15320 KB |
