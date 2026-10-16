# 1779. The Great Team

[Timus 1779](https://acm.timus.ru/problem.aspx?space=1&num=1779) · difficulty 339 · constructive

Original problem by Ivan Burmistrov, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Build a friendship graph on n students in which no three students have
the same number of friends, or report that none exists.

## Input

n (3 ≤ n ≤ 200).

## Output

The number of friendly pairs and the pairs, or −1 if no graph fits. Any
fitting graph is accepted.

## Examples

### Example 1

Input:

```
4
```

Output:

```
2
1 3
3 4
```

## Solution

Join students i and j whenever i + j > n. Student i is then a friend of
the i students n − i + 1, …, n, less themselves when they are among
them, that is, when 2i > n. So student i has i friends for i ≤ n/2
and i − 1 friends for i > n/2: the counts run 1, 2, … up to the middle
and on after it, and only one count, the middle one, is shared, by two
students. A graph therefore always exists and −1 is never printed.
`O(n²)`.

For four students this joins 1–4, 2–3, 2–4 and 3–4, with 1, 2, 2 and 3
friends, which fits as well as the example's answer.

Pitfalls:

- n − 1 friends and 0 friends cannot both occur, so the counts 0 to
  n − 1 can never all be different, and two students must share one;
- the graph may be dense, about n²/4 pairs, so the output is large;
- the answer is not unique, so the checker counts the friends itself.

The construction passes the checker for every n from 3 to 200, and so
does an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1779_constructive.cpp](1779_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 292 KB |
| [1779_constructive.go](1779_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.015 s | 2140 KB |
| [1779_constructive.java](1779_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.109 s | 2568 KB |
| [1779_constructive.py](1779_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.093 s | 1952 KB |
| [1779_constructive.rs](1779_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.015 s | 644 KB |
