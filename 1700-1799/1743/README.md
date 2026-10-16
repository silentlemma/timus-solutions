# 1743. Domino Sorting

[Timus 1743](https://acm.timus.ru/problem.aspx?space=1&num=1743) · difficulty 991 · greedy

Original problem by Artyom Ripatti and Petr Lezhankin, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Lay n dominoes in a column, one per row, turning any of them over, so
that the left numbers go up (not strictly) and the right numbers go
down. Print such a layout or report that there is none.

## Input

n (1 ≤ n ≤ 10⁵), then the two numbers of each domino (0 to 10⁶).

## Output

`YES` and the dominoes in order, or `NO`. Any fitting layout is
accepted.

## Examples

### Example 1

Input:

```
3
5 2
6 1
3 4
```

Output:

```
YES
1 6
2 5
3 4
```

### Example 2

Input:

```
4
1 5
7 1
3 8
5 6
```

Output:

```
YES
1 7
1 5
6 5
8 3
```

### Example 3

Input:

```
2
1 2
3 4
```

Output:

```
NO
```

## Solution

Read a domino as a range [low, high]. It lies either upright as (low,
high) or flipped as (high, low). The layout needs every two rows to
be in order: two upright dominoes fit when their ranges are nested, two
flipped ones too, and an upright and a flipped one when their ranges
overlap. So the upright dominoes form a chain of nested ranges, the
flipped ones another, and the innermost range of one chain must
overlap the innermost range of the other; then every upright range
overlaps every flipped one.

Sort the ranges by low end, longer first on ties. A nested chain is
then a subsequence whose high ends never rise, and splitting the list
into two such subsequences is done greedily: a range goes to the first
chain if it fits, otherwise to the second, otherwise there is no
layout. The first chain's last high end is always below the second's,
so this is the same as putting each range on the tightest chain, which
never fails when a split exists.

If both chains are used, their last, innermost ranges must overlap.
If neither contains the other, every split has the same innermost
pair; otherwise all ranges contain their intersection. Thus the check
decides. The first chain is printed upright and the second flipped and
reversed. `O(n log n)`.

In the second example the chains are [1, 7] ⊃ [1, 5] and [3, 8] ⊃
[5, 6], whose innermost ranges meet at 5.

Pitfalls:

- ranges that only touch at one number overlap;
- equal dominoes are nested in both directions, so ties need no special
  care beyond the sort order;
- one big range around two separate small ones has no layout: the two
  small ones would be the innermost ranges and do not overlap.

The checker verifies that the same dominoes are printed and that both
columns are sorted. The verdicts match a search over every way of
turning the dominoes on 500 random sets of up to 8, and an independent
accepted implementation on the large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1743_greedy.cpp](1743_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.187 s | 2348 KB |
| [1743_greedy.go](1743_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.203 s | 13216 KB |
| [1743_greedy.java](1743_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.218 s | 10432 KB |
| [1743_greedy.py](1743_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.437 s | 40804 KB |
| [1743_greedy.rs](1743_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.046 s | 7688 KB |
