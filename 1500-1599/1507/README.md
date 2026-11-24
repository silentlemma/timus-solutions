# 1507. Difficult Decision

[Timus 1507](https://acm.timus.ru/problem.aspx?space=1&num=1507) · difficulty 447 · math

Original problem by Evgeny Krokhalev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given an n × n matrix A (2 ≤ n ≤ 50) of integers from 0 to 100, decide
whether the matrix B = A^(n(n−1)) + A^(n(n−1)+1) + … + A^(n(n+1)) has
a zero entry.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, then the n rows of A.

## Output

"No" if B has a zero entry, otherwise "Yes".

## Examples

### Example 1

Input:

```
2
0 7
15 30
```

Output:

```
Yes
```

### Example 2

Input:

```
3
100 35 40
0 22 0
10 11 0
```

Output:

```
No
```

## Solution

The entries are huge, but only whether they are zero matters, and with
non-negative entries a sum is zero only when all its terms are, and a
product only when a factor is. So treat A as a directed graph with an edge i → j where the entry
is non-zero: (A^k)[i][j] is non-zero exactly when some walk of length k
leads from i to j, and B has no zero exactly when every j is reached
from every i by a walk with length between n(n−1) and n(n+1).

Keep each row of a boolean matrix as a bitmask, so a product ORs the
rows of the second factor picked by the bits of the first. Compute
A^(n(n−1)) by repeated squaring, then take the 2n + 1 consecutive powers
one multiplication at a time and OR them together. About 125 products
of `O(n²)` word operations.

In fact the answer is "Yes" exactly when the graph is strongly
connected: a check of every graph with n ≤ 4 and of random ones up to
n = 12 found no exception. The window of 2n + 1 consecutive lengths
covers every residue of a cycle structure, so even a single cycle,
whose powers are never positive, passes.

Pitfalls:

- the formula is given only as a picture in the statement: the powers
  run from n(n−1) to n(n+1);
- the real values overflow 64-bit integers, so compute only zero or
  non-zero (test 06);
- a single cycle has no positive power, yet B has no zero (tests 03, 07);
- a one-way link between two parts, or a vertex with no edge out or no
  edge in, gives zeros (tests 04, 08, gen3).

## Optimized solutions

The graph version tests strong connectivity by reaching every vertex from vertex 0 in both the graph and its transpose. This is sufficient for the original matrix formula: for any vertices u and v, choose a simple path of length p ≤ n−1 and a directed cycle through u of length c ≤ n. Put L = n(n−1). Repeating that cycle before the path gives a walk of length p + k·c; choose the smallest nonnegative k making it at least L. Its length is less than L + c and therefore lies inside [n(n−1), n(n+1)]. Conversely, a positive entry for each pair implies reachability and hence strong connectivity. Scanning the matrix takes O(n²) time. The two searches use O(n) machine words of graph storage because n ≤ 50, so each row fits one bitmask.

## Language notes

The matrix-power base files are preserved in all five languages. The graph versions store rows as bitmasks. Python reads all input tokens at once, so its input buffering takes O(n²) space despite the O(n) graph representation. Go uses standard handles; Rust uses bounded C-runtime I/O and a C entry point to avoid standard-library startup. The exact Go and Rust sources also passed Windows-target compilation before submission.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1507_math.cpp](1507_math.cpp) | G++ 13.2 x64 | math | O(n^3) | AC | 0.015 s | 188 KB | 11287289 |
| [1507_math.go](1507_math.go) | Go 1.14 x64 | math | O(n^3) | AC | 0.031 s | 1184 KB | 11287290 |
| [1507_math.java](1507_math.java) | Java 1.8 | math | O(n^3) | AC | 0.171 s | 524 KB | 11287292 |
| [1507_math.py](1507_math.py) | Python 3.12 x64 | math | O(n^3) | AC | 0.140 s | 740 KB | 11287291 |
| [1507_math.rs](1507_math.rs) | Rust 1.75 x64 | math | O(n^3) | AC | 0.046 s | 256 KB | 11287293 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1507_graphs.cpp](1507_graphs.cpp) | G++ 13.2 x64 | graphs | O(n²) | AC | 0.015 s | 108 KB | 11314642 |
| [1507_graphs.go](1507_graphs.go) | Go 1.14 x64 | graphs | O(n²) | AC | 0.015 s | 288 KB | 11314641 |
| [1507_graphs.java](1507_graphs.java) | Java 1.8 | graphs | O(n²) | AC | 0.093 s | 392 KB | 11314637 |
| [1507_graphs.py](1507_graphs.py) | Python 3.12 x64 | graphs | O(n²) | AC | 0.093 s | 584 KB | 11314647 |
| [1507_graphs.rs](1507_graphs.rs) | Rust 1.75 x64 | graphs | O(n²) | AC | 0.046 s | 48 KB | 11314650 |
