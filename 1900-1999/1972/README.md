# 1972. Longest Nonrepeating Walk Between Two Bitsets

[Timus 1972](https://acm.timus.ru/problem.aspx?space=1&num=1972) · difficulty 3339 · constructive

Original problem by Idea by Alexander Ipatov, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A configuration is a subset of n independently switchable options. Start
at a given subset and finish at another, changing exactly one option at
each step. No configuration may occur twice. Maximize the number of
configurations visited, counting both endpoints, and print such a sequence.
The endpoints differ and a solution exists. Limits: 1 second, 64 MB.

## Input

n, 1≤n≤16. Each of the next two lines describes an endpoint: k followed
by its k enabled option indices, where 0≤k≤n and 1≤a₁<…<aₖ≤n.

## Output

First print the maximum count m, then m configurations in traversal order,
each in the same count-and-increasing-indices format. The first and last
must equal the input endpoints. Any optimal sequence is accepted.

## Checking

A checker verifies that each step changes exactly one option, that no
configuration repeats and that the path has the largest possible length:
2ⁿ for endpoints of different parity, 2ⁿ − 1 otherwise. Any such path is
accepted.

## Examples

```
2
0
2 1 2
```

```
3
0
1 2
2 1 2
```

## Solution

Represent subsets as n-bit integers. Configurations form the n-dimensional
hypercube: an edge flips one bit. Color a vertex by the parity of its number
of set bits. Every edge changes color. The two color classes each have
2ⁿ⁻¹ vertices, so an opposite-color path can use at most all 2ⁿ vertices;
an equal-color path can use at most 2ⁿ−1. We construct both bounds.

### Split into two smaller cubes

Maintain endpoints a,b and a mask of free dimensions; all other bits
are fixed within this subproblem. With one free dimension, return both
endpoints if distinct, or just the endpoint if equal. The equal case is
needed only as a recursive leaf.

Otherwise choose a differing dimension d. Removing d splits the cube
into the half containing a and the half containing b. Choose any other
free dimension e and set u=a XOR 2ᵉ, v=u XOR 2ᵈ. Construct a path from
a to u in the first half, followed by a path from v to b in the second.
The concatenation joins u to v by flipping exactly d.

There is one necessary exception: if v=b and at least three dimensions
are free, choose a different e. Equality means the original endpoints
differed in exactly d and e, so any alternative remaining dimension makes
v distinct from b. With exactly two dimensions, allow equality: the second
half then contributes its single endpoint.

### Why the construction is complete and optimal

a and u always have opposite parity. By induction their half-cube path
visits all 2ⁿ⁻¹ vertices. Since flipping d changes parity again, v has
the same parity as a. If a and b had opposite parity, so do v and b;
their path also visits the entire second half, yielding 2ⁿ vertices.

If a and b had equal parity, v and b do too. The exception rule keeps
them distinct whenever that half has dimension at least two. Induction
gives 2ⁿ⁻¹−1 vertices there; in the two-dimensional parent, the equal
one-dimensional leaf gives one, the same formula. Total length is 2ⁿ−1.
The halves are disjoint, so no vertex repeats. Recursion changes only
free dimensions, preserves endpoints and terminates. Both upper bounds
are therefore attained.

Building the mask sequence takes `O(2^n)` time and `O(2^n)` storage;
recursion depth is `O(n)`. Formatting all enabled-index lists takes
`O(n·2^n)` time. Versions that buffer output use up to `O(n·2^n)` space
including text; the numeric path itself remains `O(2^n)`.

In the example the empty set and {1,2} both have even parity. Four
configurations cannot be visited between these endpoints, but three can:
empty → {2} → {1,2}. The two steps flip option 2 and then option 1.
Thus the printed length three meets the bound.

The answer counts configurations, not transitions. Equal endpoint parity
usually needs 2ⁿ−1, not a shortest path. Do not let v=b in a recursive
half of dimension at least two: a one-vertex result would waste many
vertices. The one-dimensional equal-endpoint leaf is intentional.
Always remove the split bit from both recursive masks. Output indices
in increasing order and generate large test answers instead of storing
them as static fixtures, even when the input is tiny.

## Language notes

All five versions use integer masks and extract the lowest set bit.
Rust uses wrapping negation for unsigned masks; C++ uses unsigned masks,
and Go, Java and Python use nonnegative signed or arbitrary-size values.
Java stores the path in a preallocated array. Depth at most 16 needs no
special recursion-limit adjustment.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1972_constructive.cpp](1972_constructive.cpp) | G++ 13.2 x64 | constructive | O(n*2^n) | AC | 0.078 s | 684 KB |
| [1972_constructive.go](1972_constructive.go) | Go 1.14 x64 | constructive | O(n*2^n) | AC | 0.125 s | 5908 KB |
| [1972_constructive.java](1972_constructive.java) | Java 1.8 | constructive | O(n*2^n) | AC | 0.187 s | 11420 KB |
| [1972_constructive.py](1972_constructive.py) | Python 3.12 x64 | constructive | O(n*2^n) | AC | 0.328 s | 10276 KB |
| [1972_constructive.rs](1972_constructive.rs) | Rust 1.75 x64 | constructive | O(n*2^n) | AC | 0.062 s | 3456 KB |
