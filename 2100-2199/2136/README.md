# 2136. Fewest bricks that stop a rectangle sliding down a chimney

[Timus 2136](https://acm.timus.ru/problem.aspx?space=1&num=2136) · difficulty 2330 · two_pointers

Original problem by Nikita Sivukhin, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A chimney is a grid of h rows and width w. Row i has lᵢ bricks on the
left and rᵢ on the right, and the free cells between them form a
non-empty segment. An a × b rectangle starts above the chimney and moves
one cell at a time, never overlapping a brick, trying to get out below.
Add the fewest bricks, keeping every row's free segment non-empty, so
that it cannot pass. The limits are 1 second and 256 MB.

## Input

h and w, 1 ≤ h ≤ 10⁵, 3 ≤ w ≤ 10⁹, then a and b, 1 ≤ a ≤ 10⁹,
2 ≤ b ≤ 10⁹, then the pairs lᵢ, rᵢ with lᵢ, rᵢ ≥ 1 and lᵢ + rᵢ < w.

## Output

The fewest bricks.

## Examples

### Example 1

Input:

```
7 5
1 2
2 1
1 1
1 1
1 1
2 1
1 1
1 1
```

Output:

```
1
```

## Solution

While the rectangle covers a fixed set of a rows it can slide sideways
freely within their common free part. A step down from rows i … i + a − 1
to rows i + 1 … i + a keeps the columns, so those columns must be free
in all a + 1 rows i … i + a. With L and R the largest left and right
brick counts in such a window of a + 1 rows, the step is possible
exactly when L + R + b ≤ w. Rows above and below the chimney are empty,
so windows near the top are shorter, and the rectangle gets through
exactly when every window allows its step.

To block it, one window must get L + R ≥ w − b + 1. Adding bricks to a
single row raises L or R one by one, and every row keeps a free cell
because b ≥ 2, so the answer is max(0, w − b + 1 − max over windows of
(L + R)). The windows of a + 1 rows are scanned with two monotone deques
for the maxima, in O(h).

In the example the window of the first two rows has L + R = 3, while
w − b + 1 = 4, so one more brick in one of these rows blocks the way.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2136_two_pointers.cpp](2136_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(h) | AC | 0.046 s | 444 KB |
| [2136_two_pointers.go](2136_two_pointers.go) | Go 1.14 x64 | two_pointers | O(h) | AC | 0.031 s | 6324 KB |
| [2136_two_pointers.java](2136_two_pointers.java) | Java 1.8 | two_pointers | O(h) | AC | 0.140 s | 2188 KB |
| [2136_two_pointers.py](2136_two_pointers.py) | PyPy 3.10 x64 | two_pointers | O(h) | AC | 0.250 s | 18588 KB |
| [2136_two_pointers.rs](2136_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(h) | AC | 0.046 s | 3176 KB |
