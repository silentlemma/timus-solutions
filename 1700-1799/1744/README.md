# 1744. The Captain's Squad

[Timus 1744](https://acm.timus.ru/problem.aspx?space=1&num=1744) · difficulty 1983 · constructive

Original problem by Artyom Ripatti, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each day three of n soldiers go on night duty, and no two soldiers may
be on duty together more than three times. Make a schedule for as many
days as possible.

## Input

An odd n (3 ≤ n ≤ 99).

## Output

The largest number of days k and the three soldiers of each day. Any
schedule of k days is accepted.

## Examples

### Example 1

Input:

```
3
```

Output:

```
3
1 2 3
2 3 1
3 1 2
```

### Example 2

Input:

```
5
```

Output:

```
10
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5
```

## Solution

Each day puts three pairs of soldiers together, and each of the
n(n − 1)/2 pairs may be together three times, so there are at most
n(n − 1)/2 days. That many days are possible: number the soldiers
0 … n − 1 and take the triples i, i + d, i + 2d modulo n for every i
and every d from 1 to (n − 1)/2.

A pair of soldiers whose numbers differ by δ meets twice as neighbours
in a triple, in the first two or last two positions for the d with
δ = ±d, and once as the ends of a triple, for the d with δ = ±2d.
Since n is odd, each δ matches exactly one d of the first kind and,
as 2 can be divided out modulo n, exactly one of the second, so every
pair meets exactly three times. The three soldiers of a triple differ
because d and 2d are not multiples of n. `O(n²)`.

For n = 3 this gives the first example: d = 1 and the three rotations
of 1, 2, 3.

Pitfalls:

- the same three soldiers may go on duty on several days;
- the order of the soldiers in a day does not matter.

The checker verifies the number of days, the soldiers and the pair
counts; the schedule was checked for every odd n from 3 to 99.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1744_constructive.cpp](1744_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 380 KB |
| [1744_constructive.go](1744_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1228 KB |
| [1744_constructive.java](1744_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.125 s | 2028 KB |
| [1744_constructive.py](1744_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 836 KB |
| [1744_constructive.rs](1744_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.015 s | 320 KB |
