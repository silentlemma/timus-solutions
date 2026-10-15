# 1646. Godzilla Strikes Back!

[Timus 1646](https://acm.timus.ru/problem.aspx?space=1&num=1646) · difficulty 891 · strings

Original problem by Ivan Burmistrov, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two DNA samples are given. On each of m days a new sample is made by
gluing two earlier samples together (the second after the first). Count
the occurrences of a given pattern in the last sample, modulo 10⁹ + 7.

## Input

The pattern (at most 100 letters `ACGT`), the two first samples (at most
10 letters each), m (1 ≤ m ≤ 100), then m pairs: on day k the numbers of
the two samples glued, each from 1 to k + 1.

## Output

The number of occurrences modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
AGA
A
G
4
1 2
2 1
3 1
5 4
```

Output:

```
2
```

### Example 2

Input:

```
A
CT
AG
2
1 1
3 3
```

Output:

```
0
```

## Solution

Samples double in length each day at most, so the last one can have
about 2¹⁰⁰ letters; it is never built. For each sample keep only its
number of occurrences modulo 10⁹ + 7 and its first and last L − 1
letters, where L is the pattern length (or the whole sample if it is
shorter).

Gluing A and B keeps every occurrence inside A and inside B and adds
those that cross the seam. Such an occurrence starts in the last L − 1
letters of A and ends in the first L − 1 letters of B, so they are
exactly the occurrences in the short string tail(A) + head(B): neither
part alone is long enough to hold the pattern. The new head is the first
L − 1 letters of head(A) + head(B), the new tail the last L − 1 letters
of tail(A) + tail(B), which stays right when a sample is shorter than
L − 1. `O(m · L²)`.

Pitfalls:

- the count overflows any integer type: 2¹⁰⁰ copies of `A` hold 2¹⁰⁰
  occurrences of `A` (test 04);
- a sample shorter than L − 1 must be kept whole; taking its last L − 1
  letters with a negative index cuts it (test 06);
- with a one-letter pattern the kept ends are empty and nothing crosses
  a seam.

The answers match an independent accepted implementation on 400 random
tests and a direct count on small ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1646_strings.cpp](1646_strings.cpp) | G++ 13.2 x64 | strings | O(m · L²) | AC | 0.015 s | 436 KB |
| [1646_strings.go](1646_strings.go) | Go 1.14 x64 | strings | O(m · L²) | AC | 0.031 s | 1168 KB |
| [1646_strings.java](1646_strings.java) | Java 1.8 | strings | O(m · L²) | AC | 0.140 s | 2144 KB |
| [1646_strings.py](1646_strings.py) | Python 3.12 x64 | strings | O(m · L²) | AC | 0.109 s | 532 KB |
| [1646_strings.rs](1646_strings.rs) | Rust 1.75 x64 | strings | O(m · L²) | AC | 0.015 s | 280 KB |
