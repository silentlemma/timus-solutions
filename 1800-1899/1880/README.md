# 1880. Psych Up's Eigenvalues

[Timus 1880](https://acm.timus.ru/problem.aspx?space=1&num=1880) · difficulty 30 · two_pointers, hashing

Original problem by Denis Mukhametianov, from the Ural Regional School Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of the three players of a team has a list of "own" numbers. A
number is the team's own if it is in all three lists. How many such
numbers are there?

## Input

Three blocks: the length n of a list (1 ≤ n ≤ 4000), then its n
distinct positive numbers up to 10⁹ in increasing order.

## Output

The number of numbers in all three lists.

## Examples

### Example 1

Input:

```
5
13 20 22 43 146
4
13 22 43 146
5
13 43 67 89 146
```

Output:

```
3
```

## Solution

The lists are sorted, so walk them together with one pointer each. If
the three current numbers are equal, count one. Then move every pointer
that stands at the smallest of them; when any list runs out, stop. The
Python solution intersects three sets instead. `O(n)`.

In the example 13, 43 and 146 are in all three lists, while 20, 22,
67 and 89 are missing from at least one.

Pitfalls:

- a number in only two of the lists does not count;
- after a match all three pointers move, and otherwise only the ones
  at the minimum, or the walk can skip a common number;
- the walk stops as soon as one list is exhausted.

The counts agree with an independent accepted implementation on 50
random teams.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1880_two_pointers.cpp](1880_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.031 s | 244 KB |
| [1880_two_pointers.go](1880_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n) | AC | 0.046 s | 1364 KB |
| [1880_two_pointers.java](1880_two_pointers.java) | Java 1.8 | two_pointers | O(n) | AC | 0.109 s | 540 KB |
| [1880_hashing.py](1880_hashing.py) | Python 3.12 x64 | hashing | O(n) | AC | 0.078 s | 1860 KB |
| [1880_two_pointers.rs](1880_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.046 s | 492 KB |
