# 1333. Genie Bomber 2

[Timus 1333](https://acm.timus.ru/problem.aspx?space=1&num=1333) · difficulty 218 · geometry

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Up to 10 bombs fall on the unit square 0 ≤ x, y ≤ 1. Each one hits a
disc with center (x, y) and radius r, all of them between 0 and 1.
Print the share of the square that is hit by at least one bomb, in
percent, with an error of at most one percent.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines with x, y and r.

## Output

The percentage of the square that is hit.

## Checking

Our tests accept answers within 0.01 of the expected one. The samples
in the statement are themselves rounded a little: the second is about
80.746, not 80.743.

## Examples

### Example 1

Input:

```
1
0.5 0.5 0.5
```

Output:

```
78.539816
```

### Example 2

Input:

```
2
0.2 0.2 0.5
0.8 0.8 0.5
```

Output:

```
80.74292
```

## Solution

Cut the square into 20 000 thin vertical strips and take the line
through the middle of each. On that line every disc covers one interval
of y, clipped to [0, 1]. Sorting the intervals and walking along them
gives the length of their union. The sum of these lengths times the
width of a strip is the hit area. `O(S · N log N)` for S strips.

The error comes only from the edges of the discs, where the length of
the chord changes fast. Even so it stays around 10⁻⁵ percent here:
with a million strips the second sample changes by less than 10⁻⁵.
That is far inside the one percent allowed, so no exact formula for the
union of discs is needed.

Pitfalls:

- the discs may reach outside the square, and only the part inside
  counts (tests 02 and 05);
- discs can repeat or lie inside each other, and the union must count
  such areas once (test 07);
- there may be no bombs, or bombs of radius 0 (tests 03 and 06).

The answers were compared with counting a 700 × 700 grid of points on
60 random cases; the largest gap was 0.005 percent.

## Language notes

- All five solutions use the same number of strips.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1333_geometry.cpp](1333_geometry.cpp) | G++ 13.2 x64 | geometry | O(S·N log N) | AC | 0.031 s | 224 KB |
| [1333_geometry.go](1333_geometry.go) | Go 1.14 x64 | geometry | O(S·N log N) | AC | 0.046 s | 5944 KB |
| [1333_geometry.java](1333_geometry.java) | Java 1.8 | geometry | O(S·N log N) | AC | 0.187 s | 6560 KB |
| [1333_geometry.py](1333_geometry.py) | Python 3.12 x64 | geometry | O(S·N log N) | AC | 0.156 s | 504 KB |
| [1333_geometry.rs](1333_geometry.rs) | Rust 1.75 x64 | geometry | O(S·N log N) | AC | 0.046 s | 268 KB |
