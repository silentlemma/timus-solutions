# 2133. Counting runs of tall buildings under height updates

[Timus 2133](https://acm.timus.ru/problem.aspx?space=1&num=2133) · difficulty 2053 · fenwick

Original problem by Nikita Sivukhin, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n buildings stand in a row. Queries either change the height of one
building or ask, for a level x, for the number of maximal runs of
consecutive buildings that are at least x floors high. The limits are
3 seconds and 256 MB.

## Input

n, 1 ≤ n ≤ 10⁵, the heights, then q, 1 ≤ q ≤ 10⁵, and the queries
"1 i x" (set the height of building i to x) and "2 x", all heights and
levels between 1 and 10⁹.

## Output

The number of runs for every query of the second kind.

## Examples

### Example 1

Input:

```
7
3 6 5 2 6 1 4
6
2 3
1 6 4
2 3
2 5
1 4 10
2 5
```

Output:

```
3
2
2
1
```

## Solution

At a level x the buildings of height at least x form runs, and every
pair of neighbours that are both tall enough joins two of them. So the
number of runs is the number of buildings with h ≥ x minus the number
of neighbouring pairs with min(hᵢ, hᵢ₊₁) ≥ x.

Read all queries first and compress every height and level that occurs.
A Fenwick tree over the compressed values holds +1 at the height of each
building and −1 at the minimum of each neighbouring pair; the answer
for x is the sum over all values from x up. Changing a height moves the
building's +1 and the −1 of its at most two pairs, a constant number of
updates. Everything takes O((n + q) log(n + q)).

In the example at level 3 the buildings 3 6 5 | 2 | 6 | 1 | 4 form three
runs: 3 6 5, 6 and 4.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2133_fenwick.cpp](2133_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((n + q) log(n + q)) | AC | 0.109 s | 3292 KB |
| [2133_fenwick.go](2133_fenwick.go) | Go 1.14 x64 | fenwick | O((n + q) log(n + q)) | AC | 0.156 s | 18028 KB |
| [2133_fenwick.java](2133_fenwick.java) | Java 1.8 | fenwick | O((n + q) log(n + q)) | AC | 0.171 s | 6748 KB |
| [2133_fenwick.py](2133_fenwick.py) | Python 3.12 x64 | fenwick | O((n + q) log(n + q)) | AC | 1.843 s | 65740 KB |
| [2133_fenwick.rs](2133_fenwick.rs) | Rust 1.75 x64 | fenwick | O((n + q) log(n + q)) | AC | 0.078 s | 10488 KB |
