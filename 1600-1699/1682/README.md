# 1682. Crazy Professor

[Timus 1682](https://acm.timus.ru/problem.aspx?space=1&num=1682) · difficulty 537 · dsu

Original problem by Pavel Egorov, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The numbers 1, 2, 3, … are written one by one. A new number a is joined
to every earlier number b with b + a² ≡ 0 or a + b² ≡ 0 (mod k). Print
the number after which the graph first has a cycle, or −1 if it never
does.

## Input

k (1 ≤ k ≤ 100000).

## Output

That number.

## Examples

### Example 1

Input:

```
2
```

Output:

```
5
```

## Solution

Whether two numbers are joined depends only on their residues. Every
residue r has the partner s = −r² mod k, and all numbers with residue
r are joined to all numbers with residue s. If s ≠ r, two numbers of
each residue already form a 4-cycle; if s = r, three numbers of residue
r form a triangle. Both happen by the number 3k, so a cycle always
appears and −1 is never printed.

So simulate. Keep the numbers written so far grouped by residue and a
disjoint-set union over the numbers. For a new number a with residue r,
the earlier neighbours are the numbers with residue −r² mod k, together
with those whose residue s satisfies s² ≡ −r; the residues s with a
given −s² mod k are listed in advance. Add the edges one by one: an
edge between two numbers already in one tree closes the first cycle,
and a is the answer. Any other edge joins two trees, which happens
fewer than 3k times in total, so the work is `O(k log k)`.

Pitfalls:

- the two conditions can name the same residue; take it once, or the
  same edge counts twice and makes a false cycle;
- for k = 1 every pair is joined and the answer is 3;
- r · r approaches 10¹⁰, beyond 32 bits, so square residues in 64-bit
  arithmetic.

The answers match an independent accepted implementation for every
k ≤ 299 and for 34 larger k.

## Optimized solutions

C++, Go and Rust retain the residue-class simulation but replace nested vectors with flat chains. Precompute F(s)=−s² mod k, a head per target residue and one next pointer per residue. A second head array and one next pointer per written number enumerate earlier numbers of a residue. For new a, first process class F(a mod k), then the reverse-square classes pointing to a mod k, skipping F(a mod k) there. This is exactly the union of the two congruence conditions, without per-number copying, sorting or duplicate edges. Use32-bit indices and signed32-bit DSU parents, with a negative component size at roots, union by size and path compression. Grow the vertex arrays only as numbers are written; do not allocate every possible vertex in advance. Squares are computed in 64 bits because (k−1)² can exceed 32 bits. The implementation uses the bound 3k from the triangle k, 2k, 3k. For k ≥ 3, F(1) = k − 1, so those two residue classes form a four-cycle once each appears twice, by 2k − 1. Before the first cycle every processed edge joins two trees, so fewer than3k edges succeed; the reverse residue lists are traversed at most three times each. Time O(k α(k)), space O(k+a) for a≤3k. Rust also uses bounded C-runtime I/O and a C entry point. All simple files remain; Java/Python reuse bases.

The accepted base implementations [1682_dsu.java](1682_dsu.java), [1682_dsu.py](1682_dsu.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1682_dsu.cpp](1682_dsu.cpp) | G++ 13.2 x64 | dsu | O(k log k) | AC | 0.062 s | 7344 KB | 11288833 |
| [1682_dsu.go](1682_dsu.go) | Go 1.14 x64 | dsu | O(k log k) | AC | 0.062 s | 15044 KB | 11288837 |
| [1682_dsu.java](1682_dsu.java) \* | Java 1.8 | dsu | O(k log k) | AC | 0.218 s | 26412 KB | 11288842 |
| [1682_dsu.py](1682_dsu.py) | Python 3.12 x64 | dsu | O(k log k) | AC | 0.359 s | 27804 KB | 11288840 |
| [1682_dsu.rs](1682_dsu.rs) | Rust 1.75 x64 | dsu | O(k log k) | AC | 0.109 s | 12944 KB | 11288844 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1682_dsu_optimized.cpp](1682_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O(k α(k)) | AC | 0.015 s | 3076 KB | 11315690 |
| [1682_dsu_optimized.go](1682_dsu_optimized.go) \* | Go 1.14 x64 | dsu | O(k α(k)) | AC | 0.031 s | 6364 KB | 11315699 |
| [1682_dsu_optimized.rs](1682_dsu_optimized.rs) \* | Rust 1.75 x64 | dsu | O(k α(k)) | AC | 0.015 s | 3380 KB | 11315696 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
