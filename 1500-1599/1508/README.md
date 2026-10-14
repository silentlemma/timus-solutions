# 1508. Japanese Puzzle

[Timus 1508](https://acm.timus.ru/problem.aspx?space=1&num=1508) · difficulty 1564 · dp

Original problem by Stanislav Vasiliev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

One line of a nonogram has L cells (1 ≤ L ≤ 400) and a clue of K group
lengths (0 ≤ K ≤ L): the black cells form K runs of these lengths, in
this order, with at least one empty cell between neighbours. Some cells
are already known to be empty ('.') or black ('X'), the rest are
unknown ('?'). Deduce everything that follows: mark a cell '.' or 'X'
when it has that colour in every line that fits, or print
"Impossible" when no line fits.

Time limit: 1 second. Memory limit: 64 MB.

## Input

L and K, a line with the K lengths (empty when K = 0), and the L known
cells.

## Output

The L cells after the deduction, or "Impossible".

## Examples

### Example 1

Input:

```
10 2
4 2
?????.?X??
```

Output:

```
?XXX?.?X?.
```

### Example 2

Input:

```
9 0

??????.X?
```

Output:

```
Impossible
```

## Solution

Number the groups from 0.
Let pre[i][j] tell whether the first i cells can hold the first j groups
and suf[i][j] whether the cells from i on can hold the groups from j on.
pre[i][j] holds when cell i − 1 can be empty and pre[i − 1][j] holds, or
when group j − 1 can end at cell i − 1: its cells contain no '.', and the
cell just before it can be empty with pre holding for the j − 1 groups
before that (or the group starts the line and is the first). suf is the
mirror image. A prefix count of the '.' cells checks a group's place in
`O(1)`.

The line fits at all when pre[L][K] holds. Cell c can be empty when it
is not 'X' and pre[c][j] and suf[c + 1][j] hold for some j. Cell c can
be black when some group j can sit on a span covering it: the span
holds no '.', the cells around it can be empty, pre gives the j groups
to its left and suf the rest to its right. Every possible span adds one
to its cells through a difference array. A cell that can be both is
'?'. `O(L·(K + 1))`.

Pitfalls:

- with K = 0 the line of lengths is empty, so read the input by tokens
  (tests 02, 04, 07, gen6);
- one known black cell is enough to make no groups impossible
  (tests 02, 04);
- count the empty separators between neighbouring groups when checking
  whether they fill the line exactly (test 05);
- a single group longer than half the line forces middle cells black
  (test 06);
- too many known black cells (test 09) or groups (gen5) give "Impossible".

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1508_dp.cpp](1508_dp.cpp) | G++ 13.2 x64 | dp | O(L * (K + 1)) | AC | 0.015 s | 584 KB |
| [1508_dp.go](1508_dp.go) | Go 1.14 x64 | dp | O(L * (K + 1)) | AC | 0.031 s | 1304 KB |
| [1508_dp.java](1508_dp.java) | Java 1.8 | dp | O(L * (K + 1)) | AC | 0.109 s | 752 KB |
| [1508_dp.py](1508_dp.py) | Python 3.12 x64 | dp | O(L * (K + 1)) | AC | 0.250 s | 2108 KB |
| [1508_dp.rs](1508_dp.rs) | Rust 1.75 x64 | dp | O(L * (K + 1)) | AC | 0.015 s | 412 KB |
