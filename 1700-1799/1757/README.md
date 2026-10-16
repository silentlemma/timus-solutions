# 1757. Gold Bars

[Timus 1757](https://acm.timus.ru/problem.aspx?space=1&num=1757) · difficulty 2343 · binary_search

Original problem by Vassily Burnin, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n bars; bar i weighs mᵢ grams and has fineness pᵢ, the grams
of gold in a kilogram of it. Any part of any bar may be taken. Cast a
bar of m grams and fineness p, or report that it cannot be done.

## Input

n, m and p (1 ≤ n ≤ 1000, 1 ≤ m ≤ 10⁶, 0 ≤ p ≤ 1000), then mᵢ and pᵢ
for each bar (1 ≤ mᵢ ≤ 1000, 0 ≤ pᵢ ≤ 1000).

## Output

`NO`, or `YES` and the grams xᵢ taken from each bar, with
|Σxᵢ − m| < 10⁻⁶ and |Σxᵢpᵢ/1000 − mp/1000| < 10⁻⁶. Any fitting
choice is accepted.

## Examples

### Example 1

Input:

```
4 150 750
100 1000
150 585
100 750
100 0
```

Output:

```
YES
75.000000000
0.000000000
50.000000000
25.000000000
```

### Example 2

Input:

```
1 100 1000
200 0
```

Output:

```
NO
```

## Solution

Lay the bars in a row from the poorest to the richest, a total of M
grams, and look at a window of m grams starting at s. Its gold G(s)
never decreases as s moves right, since the window drops poorer metal
and takes in richer, and it changes continuously. Any choice of m grams
holds at least as much gold as the window at s = 0 and at most as much
as the window at s = M − m. So the bar can be cast exactly when
M ≥ m and G(0) ≤ m·p ≤ G(M − m), both computed in whole numbers.

If so, a binary search over s finds where G(s) = m·p, and the parts
are the overlaps of the window with the bars: whole bars inside it and
at most two cut bars at its ends. G(s) takes one pass over the bars,
or a binary search on prefix sums of weight and gold, so the whole is
`O(n log n + K·n)` for K = 100 halvings of the range. Few cut bars
also keep the rounding of the printed parts far below 10⁻⁶.

In the first example the bars in order are 0, 585, 750 and 1000 fine.
The window at s = 0 holds 100 grams at 0 and 50 at 585, 29.25 grams of
gold; at the far end it holds 50 at 750 and 100 at 1000, 137.5. The
order needs 112.5, so the window stops inside: about 30.12 grams of the
585 bar, all of the 750 bar and about 19.88 of the 1000 bar. That is
another fitting answer than the example's.

Pitfalls:

- an order heavier than the whole store is impossible at any fineness;
- the yes-or-no decision must not depend on floating point: the edges
  G(0) and G(M − m) are whole sums;
- mixing many bars by fractions makes every part a long fraction, and
  1000 rounded parts can eat most of the 10⁻⁶ margin.

The answers agree with an independent accepted implementation on which
orders are possible, on 500 random stores, many with the fineness
right at or just past the edge, and every answer passes a checker for
the two conditions and the bar weights.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1757_binary_search.cpp](1757_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n log n + K n), K = 100 | AC | 0.015 s | 228 KB |
| [1757_binary_search.go](1757_binary_search.go) | Go 1.14 x64 | binary_search | O(n log n + K n), K = 100 | AC | 0.031 s | 1196 KB |
| [1757_binary_search.java](1757_binary_search.java) | Java 1.8 | binary_search | O(n log n + K n), K = 100 | AC | 0.171 s | 3280 KB |
| [1757_binary_search.py](1757_binary_search.py) | Python 3.12 x64 | binary_search | O(n log n + K n), K = 100 | AC | 0.078 s | 684 KB |
| [1757_binary_search.rs](1757_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n log n + K n), K = 100 | AC | 0.046 s | 268 KB |
