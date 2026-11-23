# 1480. Coupons

[Timus 1480](https://acm.timus.ru/problem.aspx?space=1&num=1480) · difficulty 471 · constructive

Original problem by Sergey Pupyrev, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Arrange the numbers 1 … N² (2 ≤ N ≤ 50) in an N × N table so that the
largest sum of two cells sharing a side is as small as possible. Print
that sum and a table reaching it; written row by row in order, the sum
would be 2N² − 1.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The smallest possible largest sum, then N rows of the table. Any
fitting table is accepted.

## Examples

### Example 1

Input:

```
2
```

Output:

```
6
1 4
3 2
```

## Solution

Put V=N² and t=⌊N/2⌋. Colour the table like a chessboard. In reading
order place V,V−1,… on the even colour and 1,2,… on the odd colour.
The counters partition 1…V without repetition. Every edge joins the two
colours. For odd N, direct indexing gives horizontal sums V or V+1
and downward large/small sums V+(N+1)/2. For N=2t, horizontal sums
are at most V+2 and the largest vertical sum is V+t+1. The pair at
(row0,column0) and (row1,column0) attains V+t+1 in both cases.
Thus this construction has exactly that maximum. Its running time
is Θ(N²), as required by the output size; the two counters need O(1)
working storage apart from language-specific output buffering.

### Why no arrangement does better

We use the following grid fact: for a set A in one chessboard colour,
with |A|≤t², its open neighbourhood satisfies

|N(A)|−|A| ≥ ⌈√|A|⌉.

The boundary-sensitive proof follows below. Suppose every edge sum
were at most V+t. The t² largest labels occupy an independent set S:
two of them already sum to more than V+t. Their neighbours can only
have labels at most t²+t−1, so there are at most t²+t−1 neighbours.
Split S into its two colour classes A0,A1. Their neighbourhoods have
different colours and do not overlap. The grid fact gives
|N(S)|−|S|≥√|A0|+√|A1|≥√|S|=t, a contradiction. Therefore V+t+1
is a lower bound and our construction is optimal.

### Proof of the grid fact

For a nonempty finite one-colour set X in the infinite square lattice,
[the bipartite isoperimetric inequality](https://arxiv.org/html/1710.10232#S4.SS3)
gives |N(X)|−|X|≥⌈2√|X|⌉+1 (Example4.7, equation4.22).
It cannot be applied directly at the table boundary; the following
reflection and crossing arguments account for those missing neighbours.

First suppose A misses one horizontal and one vertical border. Reflect
the table so these are the bottom and right borders. Write s=|A|,
d=|N(A)|−s. Let a and b count points of A and N(A) on the top and
left axes, counting their common corner twice; let α,β indicate that
corner in A,N(A). Reflect in both axes and identify repetitions. Then
|X|=4s−2a+α and D=|N(X)|−|X|=4d+2(a−b)+β−α.
Shifting A down or right injects it into N(A) away from the respective
axis, so each axis count is at most d. The infinite inequality implies
d≥1. If α=1, then β=0, b≥a and a≤2d; hence
4s−2a+1≤(2d−1)² and s≤d². If α=0 and p of the two axes meet A,
then b≥a+p, a≤pd, β≤1 and β=0 for p=0. Substitution gives respectively
s≤(d−1/4)², s≤d²−d/2+1/4, or s≤d²−d+1 for p=0,1,2.
Each is at most d². The same bound holds if every component has this
property: join A points sharing a neighbour, so different components
have disjoint neighbourhoods, and sum sᵢ≤dᵢ² to obtain s≤d².

Now put B=N(A), C=opposite colour minus B. The regions R=A∪B and
Q=C∪N(C) are disjoint. If both have paths between the same opposite
borders, then d≥t. To see this, transpose to left-to-right paths.
Disjoint simple crossings are vertically ordered; reflect so R is above Q.
Every column has an R point above a Q point. In an alternating column,
each run of A points has one extra vertical neighbour, except that an
A-coloured endpoint removes one. For even N every column contributes
nonnegative excess; in the t columns with an A-coloured bottom endpoint,
zero excess would make R a bottom suffix, contradicting that ordering.
These columns therefore contribute at least1. For odd N, the t or t+1
columns with opposite-coloured endpoints contribute at least1; in the
others Q prevents a run reaching both ends, so the excess is nonnegative.
Horizontal neighbours can only add to B. Thus in either case d≥t.

Finally let |A|≤t² and suppose a component spans opposite borders but
d<t. C is nonempty, and d_C≤d+ε, where ε is the difference of the two
colour-class sizes: 0 for even N and ±1 for odd N. A C component cannot
cross perpendicular to the A component by planar separation. A parallel
crossing would give d≥t as above. Otherwise all C components satisfy
the reflection bound, giving 1≤d_C and |C|≤(d+ε)². This is impossible:
for N=2t, |C|≥t²−t+1>(t−1)²; for N=2t+1 with A the majority colour,
|C|≥t²+t+1>t²; with A the minority colour,
|C|≥t²+t+2>(t−2)². If t−2<1 the latter case already contradicts
1≤d_C≤t−2. Hence a spanning set has d≥t and s≤t²≤d² too.
This proves the grid fact for all N; finite regression checks do not
replace this argument.

## Optimized solutions

C++ and Go emit the identical checkerboard construction using only the increasing small counter and decreasing large counter. An 8192-byte output block replaces per-number formatting calls; there is no table or whole-output string. Go reads and writes through standard handles and converts each value in a four-byte digit array. Time is Θ(N²), required by the answer size; extra working space is O(1). All original files remain; Java, Python and Rust reuse their admitted implementations. General optimality follows from the boundary-sensitive reflection and crossing proof above; the small-grid exhaustive checks are separate regression evidence.

The accepted base implementations [1480_constructive.java](1480_constructive.java), [1480_constructive.py](1480_constructive.py), [1480_constructive.rs](1480_constructive.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1480_parsing_implementation_optimized.rs`. Preserve the chessboard construction but write each number into one persistent bounded output buffer. Neither per-cell decimal strings nor the complete answer are stored.

Accepted #11329180 (Rust 1.75 x64): **0.015 s / 84 KB**. Archived comparison: `1480_constructive.rs` (Rust 1.75 x64) — 0.031 s / 256 KB (#11286708).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1480_constructive.cpp](1480_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 128 KB | 11286681 |
| [1480_constructive.go](1480_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.031 s | 1108 KB | 11286689 |
| [1480_constructive.java](1480_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.125 s | 1640 KB | 11286700 |
| [1480_constructive.py](1480_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.078 s | 432 KB | 11286697 |
| [1480_constructive.rs](1480_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.031 s | 256 KB | 11286708 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1480_constructive_optimized.cpp](1480_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N²) | AC | 0.015 s | 100 KB | 11315374 |
| [1480_constructive_optimized.go](1480_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N²) | AC | 0.015 s | 276 KB | 11315828 |
| [1480_parsing_implementation_optimized.rs](1480_parsing_implementation_optimized.rs) | Rust 1.75 x64 | parsing, implementation | O(n^2) time; O(1) state + bounded I/O buffers | AC | 0.015 s | 84 KB | 11329180 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
