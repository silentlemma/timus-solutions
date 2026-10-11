# 1304. Parallelepiped

[Timus 1304](https://acm.timus.ru/problem.aspx?space=1&num=1304) · difficulty 1873 · bruteforce

Original problem from the Second Ural Team Student Programming Championship, Yekaterinburg, April 3–4, 1998.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An axis-aligned box A has opposite corners (0, 0, 0) and (u, v, w),
with 0 < u, v, w < 1000. There are 1 to 50 points, which need not lie
in A, and no two of them share a line parallel to a face of A, so all
their x, all their y and all their z coordinates
are different. Find the largest box G with edges parallel to A's that
lies inside A and has no point strictly inside it (points on its
surface are allowed). Print its volume rounded to two decimals, halves
rounded up.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

u, v and w; then n; then n lines with the coordinates of the points.
All numbers have at most two decimals.

## Output

The volume of G with two decimals.

## Examples

### Example 1

Input:

```
1.0 1.0 1.0
1
0.5 0.5 0.5
```

Output:

```
0.50
```

## Solution

Every coordinate is read as a whole number of hundredths, so volumes
are exact integers in millionths and the final rounding is exact too.

A largest box cannot be pushed outwards, so each of its six faces lies
on a face of A or touches a point. The search goes as follows:

- the two x faces are chosen from 0, u and the points' x, at most
  52 · 51 / 2 pairs;
- only the points strictly between them in x can stop the box; call
  them P;
- the lower y face lies on 0 or on a point of P;
- the upper y face then sweeps down from v. At each position, the
  points of P strictly between the two y faces cut [0, w] into gaps,
  and the widest gap gives the best height.

As the upper face reaches a point's y, that point leaves the slab
and the two gaps around its z merge into one. A doubly linked list over
the sorted z values does each merge in constant time once the node is
located, and the widest gap only grows. Points with z equal to 0 or w
never split a gap and are left out of the list.

For k points between a pair of x faces there are O(k²) gap merges;
the sum of k² over all pairs is about n⁴ / 12, half a million for n = 50.
Two cheap bounds cut this further: for each x1 the x2 are tried from
the widest, and a pair or a lower y face is dropped as soon as even
the full height and depth could not beat the best box so far.

Pitfalls:

- points on the surface of A, even in a corner, do not cut anything
  (tests 02 and 03);
- a point may lie outside A; it can never be inside G, so it is dropped
  before the search, and otherwise its x would give G a face beyond A
  (tests 09, 10, gen6);
- the rounding is half up: a volume of exactly 0.005 prints as 0.01
  (test 07), and a float product can land just below such a half;
- the volume reaches almost 10⁹, which is 10¹⁵ millionths, so the
  integers need 64 bits (test 06).

The results were compared with a direct check of every pair of x faces
and every pair of y faces on 200 small random inputs, many of them with
points on the faces of A.

## Language notes

- Python runs the same sweep with dictionaries as the linked list.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1304_bruteforce.cpp](1304_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n^4 log n) | AC | 0.031 s | 256 KB |
| [1304_bruteforce.go](1304_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n^4 log n) | AC | 0.062 s | 6564 KB |
| [1304_bruteforce.java](1304_bruteforce.java) | Java 1.8 | bruteforce | O(n^4 log n) | AC | 0.187 s | 7084 KB |
| [1304_bruteforce.py](1304_bruteforce.py) | Python 3.12 x64 | bruteforce | O(n^4 log n) | AC | 0.468 s | 832 KB |
| [1304_bruteforce.rs](1304_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(n^4 log n) | AC | 0.046 s | 364 KB |
