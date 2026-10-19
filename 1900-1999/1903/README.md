# 1903. Counting Sorted Selections

[Timus 1903](https://acm.timus.ru/problem.aspx?space=1&num=1903) · difficulty 941 · combinatorics

Original problem by Alex Samsonov, prepared by Alexander Fetisov, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n distinct identities, each assigned a class. Select exactly t
identities including a specified identity k. Their order must be
nondecreasing by class, and k must be able to occupy position x.
Equal-class identities can be ordered arbitrarily. Count possible sets,
not orders, modulo P = 10⁹+7. Limits: 1 second and 64 MB.

## Input

First n and t, with 1 ≤ t < n ≤ 5000. Then n classes cᵢ, each from 1
to 5000. Finally k and x, with 1 ≤ k ≤ n and 1 ≤ x ≤ t. Identity k
is its index in the original input, not its rank after sorting.

## Output

One integer: the number of valid sets modulo 10⁹+7.

## Checking

Compare the single integer token exactly; tests use `tokens` judging.

## Examples

### Example 1

```
5 3
2 1 1 3 1
2 3
```

```
1
```

### Example 2

```
4 2
1 1 1 1
1 2
```

```
3
```

## Solution

Fix v = cₖ. Count L classes strictly below v and G classes strictly
above v. The identified identity belongs to neither category. Among
the t−1 other selected identities, let a be lower and b be higher.

In sorted order the equal-class block occupies positions a+1 through
t−b. Therefore k can occupy x exactly when `a ≤ x−1` and `b ≤ t−x`.
Ties need no permutation factor: we only require that one ordering exists.

Start with all `C(n−1,t−1)` sets containing k. Remove the sets with
too many lower identities:

`A = Σ(a=x…min(L,t−1)) C(L,a) C(n−1−L,t−1−a)`.

Also remove the sets with too many higher identities:

`B = Σ(b=t−x+1…min(G,t−1)) C(G,b) C(n−1−G,t−1−b)`.

Each term chooses exactly the specified number from one strict class
group and chooses the rest freely from its complement, including ties.
The two bad families are disjoint: belonging to both would give
`a+b ≥ x+(t−x+1) = t+1`, although only t−1 other identities are selected.
The answer is `C(n−1,t−1) − A − B`, normalized modulo P.

This counts every containing set once initially. A set is removed
exactly when its equal-class block misses x, and disjointness prevents
double removal. Every remaining set can place k at x within that block,
which proves the result.

Precompute factorials and inverse factorials through n−1. Because P is
prime and n < P, all these factorials are invertible. Use one modular
power `factorial[n−1]^(P−2)` and fill inverse factorials backward.
Then `C(N,r) = N! / (r!(N−r)!)` takes constant time modulo P;
define it as zero if r is outside [0,N].

There are at most n terms in each sum. Time is `O(n + log P)` and space
is `O(n)`; P is fixed, so the time is linear in n. Sorting is unnecessary.

In the first sample, the third selected position can have class 1 only
if all three chosen identities have class 1. Those are identities 2, 3,
and 5. In the second, identity 1 can be second beside any of the other
three equal-class identities, yielding three sets, not six orders.

## Language notes

All five versions use the same two disjoint bad-family sums. C++, Go,
Java and Rust use 64-bit products, reducing modulo P between products;
multiplying three residues before reduction would overflow. Normalize
subtractions immediately. Python uses CPython 3.12 and modular `pow`.

Pitfalls: use strict class comparisons, always include identity k,
allow all tie positions, preserve identity distinctions and handle
empty summation ranges. A unique minimum cannot occupy position 2.

The answers agree with listing all 47 013 labelled subsets on 9117 small
queries.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1903_combinatorics.cpp](1903_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n + log P) | AC | 0.015 s | 428 KB |
| [1903_combinatorics.go](1903_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n + log P) | AC | 0.031 s | 1232 KB |
| [1903_combinatorics.java](1903_combinatorics.java) | Java 1.8 | combinatorics | O(n + log P) | AC | 0.093 s | 540 KB |
| [1903_combinatorics.py](1903_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n + log P) | AC | 0.078 s | 1588 KB |
| [1903_combinatorics.rs](1903_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n + log P) | AC | 0.046 s | 264 KB |
