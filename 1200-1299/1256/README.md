# 1256. The cemetery guard

[Timus 1256](https://acm.timus.ru/problem.aspx?space=1&num=1256) · difficulty 2233 · geometry

Original problem by Alexander Petrov (prepared by Alexander Mironenko), from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two dogs sit on chains of length R4 at two posts. The guard's house is
R1 from the first post and R2 from the second; the posts are R3 apart
(0 ≤ R1, R2, R3 ≤ 20000, 1 ≤ R4 ≤ 20000). The guard leaves the house,
puts a bowl somewhere each dog can reach and comes back. Find the shortest
such walk, with three digits after the point. The return counts: in the
example the walk is 1750 there and 1750 back.

Time limit: 1 second. Memory limit: 64 MB.

## Input

R1, R2, R3 on the first line (possibly fractional), the integer R4 on
the second.

## Output

The length of the shortest walk.

## Examples

### Example 1

Input:

```
1000 2000 1000
250
```

Output:

```
3500.000
```

## Solution

Each dog reaches a disk of radius R = R4 around its post. Put post A at
the origin, post B at (R3, 0) and the house H at distances R1 and R2
from them. The walk is H → P → Q → H with P in disk A and Q in disk B;
the other order is the same walk backwards.

If the house is inside one of the disks, the guard feeds that dog at the
door and only walks to the other disk and back:
2 · max(0, max(R1, R2) − R).

Otherwise fix P. If the segment from P to H crosses disk B, the second
bowl goes on the way home and the rest of the walk is just |PH|.
If not, Q lies on circle B; the walk P → Q → H is taken at 24 points of
the circle and then refined by golden-section search next to the best
of them.

The whole length |HP| + (best way from P through disk B to H) is convex
in P: the sum |PQ| + |QH| is convex in the pair (P, Q), and taking the
least value over Q in a convex disk keeps it convex. So a golden-section
search over x of golden-section searches over y inside disk A finds the
least value. With S = 70 steps per search and K = 24 samples this is
`O(S² · (K + S))`, about a million distances in the worst case.

Pitfalls:

- the house may be inside one disk or both (tests 02, 03);
- coincident posts, R3 = 0 (test 04), need special handling to avoid
  division by zero;
- for collinear points (tests 01, 06, 07), rounding may make the squared
  house height slightly negative;
- the input distances may be fractional (test 11).

The answers were compared with a dense grid search over both bowls on
150 random cases and with an independent search over angles on the two
circles on 200 more.

## Language notes

- All languages run the same nested searches.
- C++ takes π as `acos(-1)`, since `M_PI` is not standard.
- Java reads the numbers with `StreamTokenizer`, which accepts the
  fractional ones, and prints with `Locale.ROOT` to get a decimal point.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1256_geometry.cpp](1256_geometry.cpp) | G++ 13.2 x64 | geometry | O(S² · (K + S)) | AC | 0.062 s | 204 KB |
| [1256_geometry.go](1256_geometry.go) | Go 1.14 x64 | geometry | O(S² · (K + S)) | AC | 0.078 s | 1104 KB |
| [1256_geometry.java](1256_geometry.java) | Java 1.8 | geometry | O(S² · (K + S)) | AC | 0.734 s | 3888 KB |
| [1256_geometry.py](1256_geometry.py) | Python 3.12 x64 | geometry | O(S² · (K + S)) | AC | 0.734 s | 800 KB |
| [1256_geometry.rs](1256_geometry.rs) | Rust 1.75 x64 | geometry | O(S² · (K + S)) | AC | 0.046 s | 288 KB |
