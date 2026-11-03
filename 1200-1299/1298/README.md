# 1298. Cover Every Square by Knight Moves

[Timus 1298](https://acm.timus.ru/problem.aspx?space=1&num=1298) · difficulty 234 · backtracking

Original problem: folklore (prepared by Den Raskovalov), from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

On an N × N board (1 ≤ N ≤ 8), find a knight's tour: a path of knight
moves that visits every square exactly once. Print the squares in
order, as a letter for the column and a number for the row, or
`IMPOSSIBLE` if there is no tour.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

N² squares, one per line, or `IMPOSSIBLE`.

## Checking

Validate the output as a witness: exactly N² distinct in-board squares,
each consecutive displacement a knight move. Different correct tours are
allowed; do not compare their text or assume the same tie order. Both new
programs passed all eight repository inputs in Java 8 and CPython 3.12,
covering every allowed value N=1..8. The actual 16 outputs and exit codes
were re-read and checked independently. For `IMPOSSIBLE`, a separate plain
search enumerated every start and legal path for N≤4, using 30102 recursive
calls in total, without symmetry, degree ordering or isolated-vertex pruning.
Both sources also have their own exact-byte Accepted submissions.

## Examples

### Example 1

Input:

```
3
```

Output:

```
IMPOSSIBLE
```

### Example 2

Input:

```
5
```

Output:

```
a1
c2
e1
d3
e5
c4
d2
e4
c5
a4
b2
d1
e3
d5
b4
a2
c1
e2
c3
b1
a3
b5
d4
b3
a5
```

## Solution

View each board square as a vertex, with edges for legal knight moves.
Let `V=N²`. The simple versions perform depth-first backtracking from every
starting square. Mark the current square, append it to the path, and try
every unvisited neighbor; undo the mark and append when that branch fails.
A path of V vertices is a tour. If every branch from every start fails,
there is no tour. This proves completeness independently of the move order.

Warnsdorff's rule tries neighbors with fewer currently free onward moves
first. It changes only the order: no branch is omitted. It often finds
a witness quickly, but is not a polynomial-time guarantee. A coarse
worst-case bound is `O(V·8^V)` time and `O(V)` storage, since each square
has at most eight neighbors and recursion depth is at most V. The entire
allowed range is small (`V≤64`) and is checked explicitly below.

N=1 has the one-square tour a1. N=2,3,4 have no tour; plain exhaustive
search proves their impossibility. For N=5,6,7,8, actual output supplies
a full tour. A tour need not be closed and may start at any square.
Do not treat the heuristic's empirical behavior as an asymptotic proof.

## Optimized solutions

The two `_optimized` files keep the same complete Warnsdorff-ordered
backtracking algorithm but represent legal neighbors and unvisited squares
as bit masks. Number `(column,row)` by `column*N+row`. Candidate moves are
`adjacency[v] & remaining`; the next-degree is the number of set bits in
`adjacency[w] & remaining`. Only up to eight candidate moves need ordering.

Two sound reductions remove unnecessary search. First, reflections in both
axes and transposition preserve knight moves. Reflect a start to distances
from its nearest edges, then transpose so column≤row. Therefore every
starting-square orbit has a representative in
`0≤column≤row<ceil(N/2)`, and testing only these representatives is complete.
Second, when more than one vertex remains, an isolated vertex in the
remaining induced graph makes a continuation impossible: a path through
all remaining vertices cannot connect it to another remaining vertex.
The single remaining vertex is exempt from this test.

Python uses integer masks and `bit_count`, avoiding repeated coordinate
tuple generation and free-neighbor lists. Java uses `long` masks and
primitive per-depth candidate/degree arrays, avoiding ArrayList nodes,
per-move coordinate arrays, comparator objects and Scanner. At N=8 all
64 bits are needed: Java explicitly uses `-1L` for the full mask, since
shifting a long by 64 would otherwise shift by zero. Bit 63 being signed
does not invalidate bit counting or trailing-zero extraction.

These reductions preserve completeness, not a polynomial bound. A coarse
bound including every isolated-vertex scan is `O(V²·8^V)` time. For V≤64,
masks and per-depth workspaces occupy `O(V)` bounded-size words/objects,
with depth at most V; generalizing to larger boards would also require
accounting for variable-size integer masks. No tours or answers are stored
in the sources.

Exact-source Accepted Python time is 0.062 versus 0.171 s (63.7% faster),
but memory is 636 versus 544 KB (16.9% more). Java uses 396 versus 7116 KB
(94.4% less memory), with time 0.125 versus 0.156 s (19.9% less). Both
qualify by at least one metric; all five simple sources remain unchanged.

## Language notes

The original five implementations retain their readable coordinate-based
search and existing accepted tours. The two mask versions may print a
different valid order. The table names the actually accepted runtime;
the new Python source was accepted with CPython 3.12, not PyPy.

Both admitted new versions still miss the first-place target in at least
one metric, so both rows carry a star. The C++ base already meets the
agreed top-15%-or-first-ten criterion in both metrics. Go and Rust have no
eligible competing authors in the filtered snapshot: their bases give
formal coverage, not evidence of superiority. Comparisons use each source's
own same-language simple base, with no artificial optimized copies.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1298_backtracking.cpp](1298_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(V·8^V) | AC | 0.015 s | 216 KB | 11284706 |
| [1298_backtracking.go](1298_backtracking.go) | Go 1.14 x64 | backtracking | O(V·8^V) | AC | 0.015 s | 4468 KB | 11284709 |
| [1298_backtracking.java](1298_backtracking.java) | Java 1.8 | backtracking | O(V·8^V) | AC | 0.156 s | 7116 KB | 11284720 |
| [1298_backtracking.py](1298_backtracking.py) | Python 3.12 x64 | backtracking | O(V·8^V) | AC | 0.171 s | 544 KB | 11284718 |
| [1298_backtracking.rs](1298_backtracking.rs) | Rust 1.75 x64 | backtracking | O(V·8^V) | AC | 0.015 s | 244 KB | 11284723 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1298_backtracking_optimized.py](1298_backtracking_optimized.py) \* | Python 3.12 x64 | backtracking | O(V²·8^V) | AC | 0.062 s | 636 KB | 11308531 |
| [1298_backtracking_optimized.java](1298_backtracking_optimized.java) \* | Java 1.8 | backtracking | O(V²·8^V) | AC | 0.125 s | 396 KB | 11308542 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
