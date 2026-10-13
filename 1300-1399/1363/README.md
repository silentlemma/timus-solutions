# 1363. Halftones

[Timus 1363](https://acm.timus.ru/problem.aspx?space=1&num=1363) · difficulty 5112 · greedy

Original problem: idea by Pavel Atnashev, prepared by Evgeny Krokhalev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A grey picture A of N × M pixels, 75 ≤ N, M ≤ 300, with brightness from
0 to 255, has to be printed in black and white: every pixel of B is 0
or 255. For every pixel (i, j), take the window of pixels (k, l) with
|k − i| ≤ 10 and |l − j| ≤ 10 that lie inside the picture. The average
of B − A over that window must be at most 20 in absolute value. Print
any such B.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then N lines of M brightness values.

## Output

N lines of M numbers, each 0 or 255.

## Examples

### Example 1

Input:

```
3 3
255 255 0
0 0 255
254 0 253
```

Output:

```
255 255 0
0 0 255
255 0 255
```

## Solution

Round each row on its own, carrying the error along it. Keep e, the
sum of B − A over the pixels of the row done so far. At the next pixel,
subtract its brightness from e; if that drops below −127, print white
and add 255. Then e stays within [−127, 127] at every step. The error
of any stretch of the row is the difference of two such sums: at most
254, and at most 127 if the stretch starts where the row's scan began.

A window has r ≥ 11 rows and c ≥ 11 columns, and its error is the sum
of its row stretches:

- a window away from the left and right borders is 21 wide, and a
  stretch error of 254 is well below the allowed 20 · 21 = 420 per row;
- a window at a side border can be only 11 wide, allowing 220 per row,
  less than 254. So the rows are scanned in alternate directions; then
  in every other row the stretch touches the start of the scan and errs
  by at most 127. With r ≥ 11 rows,
  ⌈r/2⌉ · 254 + ⌊r/2⌋ · 127 ≤ 220 · r.

`O(N · M)`.

Pitfalls:

- scanning every row from the left is not enough: a picture of the
  single grey 46 that is 97 wide puts the window at the right border
  off by 22.8 on average (generated test 2);
- the example breaks the size limits on purpose and only shows the
  format.

The tests are judged by a checker that tests every window with 2D
prefix sums; the same checker rejects the one-direction rounding on
generated test 2.

## Language notes

- All five solutions use the same integer rounding.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1363_greedy.cpp](1363_greedy.cpp) | G++ 13.2 x64 | greedy | O(N·M) | AC | 0.062 s | 848 KB |
| [1363_greedy.go](1363_greedy.go) | Go 1.14 x64 | greedy | O(N·M) | AC | 0.031 s | 1536 KB |
| [1363_greedy.java](1363_greedy.java) | Java 1.8 | greedy | O(N·M) | AC | 0.109 s | 3568 KB |
| [1363_greedy.py](1363_greedy.py) | Python 3.12 x64 | greedy | O(N·M) | AC | 0.156 s | 6956 KB |
| [1363_greedy.rs](1363_greedy.rs) | Rust 1.75 x64 | greedy | O(N·M) | AC | 0.031 s | 1636 KB |
