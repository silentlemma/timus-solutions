# 1421. Credit Operations

[Timus 1421](https://acm.timus.ru/problem.aspx?space=1&num=1421) · difficulty 544 · greedy

Original problem by Ilya Grebnov, Dmitry Kovalioff and Nikita Rybak, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Fill an N × N matrix (2 ≤ N ≤ 100) with integers from 0 to 100 so that
row i sums to SR[i] and column j sums to SC[j] (each sum from 0 to
32 000, the two totals equal). Print "YES" and any such matrix, or "NO"
if there is none.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

N, then the N row sums, then the N column sums.

## Output

"NO", or "YES" and the matrix.

## Examples

### Example 1

Input:

```
4
267 157 188 259
193 320 346 12
```

Output:

```
YES
100 55 100 12
0 70 87 0
0 95 93 0
93 100 66 0
```

## Solution

Fill the rows one by one, each time taking the credits from the columns
that still need the most. For a row that needs r, lower all column
needs towards a common level L: column j gives min(100, max(0, SC[j] −
L)). The amount given shrinks as L grows, so binary search finds the
lowest L that gives at most r, and the few missing units come one each
from columns standing exactly at L. If even L = 0 gives less than r,
the answer is "NO".

Why this never spoils a solution: suppose some matrix exists but its
first row leaves column j with at least 2 more than column k, while the
row could still take one more from j and gives something to k. The rest
of column j then sums to more than the rest of column k, so some lower
row has more in j than in k. Moving one unit from k to j in the first
row and back in that row keeps all sums and bounds and makes the
remaining needs strictly more even. Repeating this reaches the balanced
row that the greedy builds, and the remaining problem depends only on
the multiset of column needs, so the greedy keeps a solution whenever
one exists. `O(N² log S)`.

Pitfalls:

- every row and column can fit on its own while two rows together
  cannot, so simple per-line checks are not enough (test 06);
- any valid matrix is accepted, so the tests use a checker (test 01);
- a row needing more than 100 per column is impossible at once
  (tests 03, 08).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1421_greedy.cpp](1421_greedy.cpp) | G++ 13.2 x64 | greedy | O(N^2 log S) | AC | 0.015 s | 268 KB |
| [1421_greedy.go](1421_greedy.go) | Go 1.14 x64 | greedy | O(N^2 log S) | AC | 0.031 s | 1188 KB |
| [1421_greedy.java](1421_greedy.java) | Java 1.8 | greedy | O(N^2 log S) | AC | 0.093 s | 832 KB |
| [1421_greedy.py](1421_greedy.py) | Python 3.12 x64 | greedy | O(N^2 log S) | AC | 0.171 s | 760 KB |
| [1421_greedy.rs](1421_greedy.rs) | Rust 1.75 x64 | greedy | O(N^2 log S) | AC | 0.031 s | 336 KB |
