# 1421. Credit Operations

[Timus 1421](https://acm.timus.ru/problem.aspx?space=1&num=1421) · difficulty 539 · greedy

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

## Optimized solutions

Rust keeps the same balanced water-level greedy and its exchange proof. Store input/residual sums in16 bits (at most32000) and each matrix credit in a byte (at most100). Fixed arrays need10000 matrix bytes and400 bytes for row/column sums at N≤100, without row vectors or per-number strings. Reject a row/column above100N as a necessary check, still perform every subsequent feasibility check, and skip zero rows. For each nonzero row, binary search up to the current largest residual, compute its capped takes, distribute the small tie remainder and reduce the columns immediately. If the level L is positive, lowering it to L − 1 gives one extra unit from each eligible column. Minimality of L guarantees enough such units. At L = 0 the row already receives exactly its required sum.

To see why the exact chosen row preserves feasibility, compare its target residuals with those of any feasible matrix after this row. A residual above its target is at least L, and one below its target is at most L − 1. This follows by clamping L or L − 1 to the interval allowed by each column and the cell cap. Some later row therefore has more in the excess column than in the deficit column. Exchange one unit between these two columns in the current and later rows, in opposite directions. The bounds and margins hold, and the two residuals approach their targets. Repeat to reach the exact greedy residual vector.

Require all residual columns to vanish before printing YES; no partial matrix is printed if a row fails. C-runtime character I/O with a C entry point streams bounded integers directly. Complexity remains O(N² log S), with S=max(2, largest initial column sum), storage O(N²) bounded by the fixed limits. All simple files remain; C++/Go/Java/Python reuse their admitted bases.

The accepted Rust 1.75 x64 run takes 0.062 s versus 0.031 s for the base and uses 84 KB versus 336 KB.

The accepted base implementations [1421_greedy.cpp](1421_greedy.cpp), [1421_greedy.go](1421_greedy.go), [1421_greedy.java](1421_greedy.java), [1421_greedy.py](1421_greedy.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1421_greedy.cpp](1421_greedy.cpp) | G++ 13.2 x64 | greedy | O(N^2 log S) | AC | 0.015 s | 268 KB | 11286140 |
| [1421_greedy.go](1421_greedy.go) | Go 1.14 x64 | greedy | O(N^2 log S) | AC | 0.031 s | 1188 KB | 11286141 |
| [1421_greedy.java](1421_greedy.java) | Java 1.8 | greedy | O(N^2 log S) | AC | 0.093 s | 832 KB | 11286146 |
| [1421_greedy.py](1421_greedy.py) \* | Python 3.12 x64 | greedy | O(N^2 log S) | AC | 0.171 s | 760 KB | 11286142 |
| [1421_greedy.rs](1421_greedy.rs) | Rust 1.75 x64 | greedy | O(N^2 log S) | AC | 0.031 s | 336 KB | 11286147 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1421_greedy_optimized.rs](1421_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(N² log S) | AC | 0.062 s | 84 KB | 11315704 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
