# 1535. The Hobbit or There and Back Again

[Timus 1535](https://acm.timus.ru/problem.aspx?space=1&num=1535) · difficulty 497 · constructive

Original problem by Alexander Ipatov, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Bilbo leaves city 1, visits each of the cities 2 … N once and returns to
city 1 (2 ≤ N ≤ 50000). Entering city P from city Q costs P·Q gold.
Print a visiting order of minimal total cost and one of maximal total
cost.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

Two lines with N numbers each, starting with 1: the cheapest order and
the dearest one. Any optimal orders are accepted.

## Examples

### Example 1

Input:

```
4
```

Output:

```
1 4 2 3
1 3 4 2
```

## Solution

The cost of a cyclic order is the sum of products of its neighbours,
including the closing edge back to city 1. Put D(i,j)=N²−ij. This matrix
is nonnegative and symmetric. For i<j<k<l,

(Dᵢⱼ+Dₖₗ)−(Dᵢₖ+Dⱼₗ)=(k−j)(i−l)<0,

(Dᵢₖ+Dⱼₗ)−(Dᵢₗ+Dⱼₖ)=(j−i)(k−l)<0.

These are the Supnick inequalities. For D, the minimum tour lists the
odd labels in ascending order followed by the even labels in descending
order. The maximum tour alternates two arms. Each D-tour costs N³ minus
the original product sum, so these tours maximize and minimize that sum,
respectively. [Supnick’s tour extrema](https://doi.org/10.1016/S0166-218X(99)00148-1)

For the maximum product sum, output 1, 3, 5, … upward and then the even
labels downward to 2. To construct the minimum, start at N and set
q=⌊(N−1)/2⌋. For k=1…q, one arm takes aₖ=k+1 for odd k and N−k
for even k. The other takes bₖ=k for odd k and N−k+1 for even k.
Join N,a₁,…,a_q, the one unused middle value if N is even, then
b_q,…,b₁. The middle value for even N is 2⌊N/4⌋+1. Rotate this cycle
to start at 1. Reading it backwards gives the maximum D-tour
1, N−1, 3, N−3, …, N−2, 2, N, which proves the minimum-product
construction. N=2 and N=3 are immediate because there is only one
undirected cyclic edge set.

The simple programs explicitly keep the arms and rotate the resulting
cycle. They take O(N) time and O(N) auxiliary space. The distinct fast
versions generate the same indices directly with bounded output buffers.

Both output lines start with 1. Include the closing edge in the cost
and print each city once.

## Optimized solutions

C++, Go and Rust compute the old two-arm cycle directly rather than keeping visited flags, both arms, the cycle, rotated order and formatted strings. Let q=⌊(N−1)/2⌋. Emit 1,N, then aₖ=k+1 for odd k or N−k for even k, k=1…q. For even N>2, the one unused middle value is 2⌊N/4⌋+1. Finish with bₖ=k for odd k or N−k+1 for even k, traversing k=q…2; b₁=1 is already first. N=2 simply emits 1,2. This is the same original arm construction, indexed without storage. The maximum-cost order still emits odds upward and evens downward. Bounded 8192-byte output gives O(N) time and O(1) extra space. All simple sources remain; Java/Python reuse admitted bases. Independent exact subset DP checks both extrema through N=14 as regression evidence; general optimality follows from the Supnick reduction in the simple explanation.

The accepted Rust 1.75 x64 run takes 0.046 s versus 0.031 s for the base and uses 232 KB versus 4376 KB.

The accepted base implementations [1535_constructive.java](1535_constructive.java), [1535_constructive.py](1535_constructive.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1535_constructive.cpp](1535_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1700 KB | 11287470 |
| [1535_constructive.go](1535_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 7060 KB | 11287471 |
| [1535_constructive.java](1535_constructive.java) \* | Java 1.8 | constructive | O(N) | AC | 0.140 s | 11176 KB | 11287473 |
| [1535_constructive.py](1535_constructive.py) \* | Python 3.12 x64 | constructive | O(N) | AC | 0.109 s | 8752 KB | 11287472 |
| [1535_constructive.rs](1535_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 4376 KB | 11287474 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1535_constructive_optimized.cpp](1535_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 100 KB | 11315377 |
| [1535_constructive_optimized.go](1535_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 936 KB | 11315379 |
| [1535_constructive_optimized.rs](1535_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 232 KB | 11315380 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
