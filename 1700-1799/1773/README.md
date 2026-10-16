# 1773. Metro to Every Home

[Timus 1773](https://acm.timus.ru/problem.aspx?space=1&num=1773) · difficulty 850 · constructive

Original problem by Alexander Ipatov (prepared by Marina Mukhacheva), from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n strips of wallpaper of equal width and height h each carry a straight
segment from the left edge, at height l, to the right edge, at height r.
A strip may be turned upside down. Put all strips side by side so that
the segments form one straight line across the wall.

## Input

h and n (1 ≤ h ≤ 100000, 1 ≤ n ≤ 50000), then l and r for each strip
(0 ≤ l, r ≤ h).

## Output

The strip numbers from left to right, with a minus before a strip that
is turned over, or 0 if no order works. Any fitting order is accepted.

## Examples

### Example 1

Input:

```
5 3
3 2
2 1
2 1
```

Output:

```
-3 1 2
```

### Example 2

Input:

```
5 3
3 2
2 1
3 2
```

Output:

```
0
```

## Solution

Turning a strip over changes its ends to h − r on the left and h − l on
the right, so its rise d = r − l stays the same. All strips must have
the same d, and the left ends of the strips in order are then start,
start + d, …, start + (n − 1)·d. A strip with left end x can take the
place of x or, turned over, of h − d − x.

If a strip can take two places i and j, then x and h − d − x both lie
on the line, so i + j is the same for every such strip: places pair up
as i and K − i, and only strips of the same pair compete. So strips with
one possible place go first, each to its place, and then each strip
with two places takes whichever is still free; if any strip finds no
place, this start fails. The start itself has two candidates: the
strip with the most extreme end, lowest when d > 0 and highest when
d < 0, either starts the line with it or, turned over, ends it with the
opposite extreme. A flat line is checked at the two heights of the
first strip. `O(n)`.

In the first example d = −1. The extreme end is 4, from strip 2 or 3
turned over, so the line starts at 4: strip 3 turned over takes 4 to 3,
strip 1 takes 3 to 2 and strip 2 takes 2 to 1.

Pitfalls:

- turning a strip over does not change its slope, so differing slopes
  are hopeless;
- a strip whose two left ends coincide must not be counted twice;
- the order is not unique, so the checker joins the strips itself.

The answers agree with a search over all orders and turnings on about
500 random cases of up to 5 strips, and with an independent accepted
implementation, checked both ways, on 100 cases of up to 50000 strips.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1773_constructive.cpp](1773_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.093 s | 1060 KB |
| [1773_constructive.go](1773_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.078 s | 6100 KB |
| [1773_constructive.java](1773_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.140 s | 6076 KB |
| [1773_constructive.py](1773_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.296 s | 34732 KB |
| [1773_constructive.rs](1773_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 4816 KB |
