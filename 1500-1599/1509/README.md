# 1509. Domino Recognition

[Timus 1509](https://acm.timus.ru/problem.aspx?space=1&num=1509) · difficulty 3218 · geometry

Original problem by Ekaterina Ovechkina and Stanislav Vasiliev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A domino is an L × 2L rectangle (1 ≤ L ≤ 100) made of two squares, each
with 0 to 6 dots in the usual pattern. Take the square of half the side
around a square's centre: one dot sits in the centre, two dots in two
opposite corners of that small square, three add the centre, four take
all its corners, five add the centre, and six add the middles of its
two sides parallel to the long sides of the domino. A photo shows all N
dots (1 ≤ N ≤ 12) of one face-down domino at its real size, turned and
moved arbitrarily, with coordinates accurate to 0.0001. L is not given.
Print every possible pair A ≤ B of dot counts, in lexicographic order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the coordinates of the N dots.

## Output

The possible pairs "A B", one per line.

## Examples

### Example 1

Input:

```
2
1.12 2.2
7 -3.0001
```

Output:

```
0 2
1 1
```

## Solution

Try every pair A ≤ B with A + B = N. Build its dots for L = 1, with the
domino lying along the x axis, and look for a similarity that takes
them onto the photo. Take a photo dot g0 and the photo dot g1 farthest
from it. Treating points as complex numbers, for every ordered pair
(a, b) of template dots the map z ↦ g0 + (z − a)·(g1 − g0)/(b − a) sends
a to g0 and b to g1; its factor has modulus L, which must lie between 1
and 100. The pair fits when every template dot lands within a small
tolerance of a different photo dot. Repeat with the template mirrored.
A single dot can only be 0-1. With at most 12 dots the search is tiny.

The solutions accept the mirror image of every arrangement as well. The
remark that the domino lies face down does not settle which way the
picture is reflected; the judge accepts this reading.

Pitfalls:

- two dots fit both a 0-2 and a 1-1 domino, with different sizes
  (test 01);
- the bounds on L then decide: two dots 0.8 apart cannot be 1-1, and
  two dots 80 apart cannot be 0-2 (tests 03, 04, gen4);
- a single dot is only 0-1 (test 02);
- the domino can be turned by any angle and mirrored (tests 06, 07, 09,
  10);
- the coordinates carry an error of 1e-4, so compare with a tolerance
  that stays well below the 0.25 between dots when L = 1 (test 08,
  gen2).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1509_geometry.cpp](1509_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^5) | AC | 0.015 s | 224 KB |
| [1509_geometry.go](1509_geometry.go) | Go 1.14 x64 | geometry | O(N^5) | AC | 0.031 s | 1132 KB |
| [1509_geometry.java](1509_geometry.java) | Java 1.8 | geometry | O(N^5) | AC | 0.125 s | 676 KB |
| [1509_geometry.py](1509_geometry.py) | Python 3.12 x64 | geometry | O(N^5) | AC | 0.078 s | 740 KB |
| [1509_geometry.rs](1509_geometry.rs) | Rust 1.75 x64 | geometry | O(N^5) | AC | 0.015 s | 456 KB |
