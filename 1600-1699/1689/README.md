# 1689. Fisherman and Barbell

[Timus 1689](https://acm.timus.ru/problem.aspx?space=1&num=1689) · difficulty 915 · prefix_sums

Original problem by Stanislav Vasilyev, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A trough of length g holds n worms of length w that do not overlap. A
barbell of total length b has a plate of width p at each end. A worm
is hurt if any part of it lies under a plate. Place the barbell in the
trough to hurt as few worms as possible, and among those places take
the leftmost one.

## Input

g and w (1 ≤ w ≤ g ≤ 100000), b and p (1 ≤ p ≤ b/2 ≤ g/2), n
(1 ≤ n ≤ 100000), then the left ends of the worms, from 0 to g − w. All
values are integers.

## Output

The distance from the left end of the trough to the left end of the
barbell.

## Examples

### Example 1

Input:

```
1000 4
500 60
10
47 68 22 237 585 417 666 996 888 555
```

Output:

```
149
```

### Example 2

Input:

```
20 1
2 1
11
1 2 3 4 6 8 10 12 14 16 19
```

Output:

```
17
```

## Solution

A plate [a, a + p] hurts the worm [x, x + w] when they overlap by a
positive length: a < x + w and a + p > x. Merely touching does no
harm, as the second example shows. For integers that means
x − p + 1 ≤ a ≤ x + w − 1. The left plate starts at the barbell's
position s and the right one at s + b − p, so each worm is hurt for
two ranges of s. All endpoints are integers, so some integer s is
always among the best places.

Add +1 on both ranges in a difference array over s = 0, …, g − b,
and −1 on their intersection, so a worm under both plates counts once.
Prefix sums then give the number of hurt worms for every s. Take the
first minimum. `O(n + g)`.

Pitfalls:

- touching a worm does not hurt it, so the ranges are open at both
  ends (example 2);
- a long worm can lie under both plates at once; counting it twice
  changes the answer in test 04;
- clip the ranges to 0, …, g − b; when b = g only s = 0 exists
  (test 03).

The answers match a direct count for every position on 150 small cases
and an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1689_prefix_sums.cpp](1689_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(n + g) | AC | 0.078 s | 584 KB |
| [1689_prefix_sums.go](1689_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(n + g) | AC | 0.078 s | 3540 KB |
| [1689_prefix_sums.java](1689_prefix_sums.java) | Java 1.8 | prefix_sums | O(n + g) | AC | 0.093 s | 884 KB |
| [1689_prefix_sums.py](1689_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(n + g) | AC | 0.359 s | 11728 KB |
| [1689_prefix_sums.rs](1689_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(n + g) | AC | 0.046 s | 2712 KB |
