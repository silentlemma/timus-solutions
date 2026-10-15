# 1707. Hypnotoad's Secret

[Timus 1707](https://acm.timus.ru/problem.aspx?space=1&num=1707) · difficulty 1900 · fenwick

Original problem by Dmitry Ivankov, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

States are numbers 0 … n − 1. Each of m laws produces the eye states
(sᵢ, tᵢ) = ((s₀ + iΔs) mod n, (t₀ + iΔt) mod n) for i = 0 … k − 1.
Each of p experiments produces q device states (aⱼ, bⱼ, cⱼ, dⱼ) by the
same kind of rule. For a device state, xⱼ = 1 if some eye state has s
between aⱼ and bⱼ and t between cⱼ and dⱼ, both bounds included, and
xⱼ = 0 otherwise.

## Input

n and m (1 ≤ n ≤ 5000, 1 ≤ m ≤ 1000), then m lines s₀ t₀ Δs Δt k
(0 ≤ s₀, t₀, |Δs|, |Δt| ≤ n − 1, 1 ≤ k ≤ 567). Then p (1 ≤ p ≤ 345)
and p lines a₀ b₀ c₀ d₀ Δa Δb Δc Δd q with the same bounds on the
starts and steps and 1 ≤ q ≤ 345.

## Output

One line per experiment: for q ≤ 20 the digits x₀ … x_{q−1} without
spaces, for q > 20 the number (Σ 7ʲ xⱼ) mod 200904040963.

## Examples

### Example 1

Input:

```
3 3
0 1 0 0 1
1 2 0 0 1
2 0 0 0 1
5
0 0 1 1 0 0 0 0 5
1 1 0 0 0 0 0 0 3
0 1 0 0 0 0 0 0 345
1 2 1 1 0 0 0 1 4
1 2 1 1 0 0 0 1 3
```

Output:

```
11111
000
0
0110
011
```

## Solution

The eye states are at most 567000 points of the n × n grid, and every
device state asks whether an axis-parallel rectangle holds one of
them. That is answered by counting: with C(x, y) the number of points
with s ≤ x and t ≤ y, the rectangle [a, b] × [c, d] holds
C(b, d) − C(a − 1, d) − C(b, c − 1) + C(a − 1, c − 1) points, and a
corner with a negative coordinate counts 0.

All corners are known in advance, so they are answered offline. Sweep
t from 0 to n − 1: add the points of row t to a Fenwick tree over s,
then read C(x, t) for every corner in that row as a prefix sum of the
tree. A full table of C would take 25 million counts, too much memory,
while the sweep keeps only the tree and one count per corner. With
P points and Q = 4 · Σq corners it runs in `O((P + Q) log n + n)`.

Pitfalls:

- the steps can be negative, so the remainders must be brought into
  0 … n − 1;
- the bounds of a range can come in either order, aⱼ > bⱼ included;
- the hash puts x₀ at the lowest power, 7⁰;
- the Python solution keeps points and corners in compact arrays,
  sorted by row with a counting sort: lists of integer objects reach
  about 77 MB here, over the 64 MB limit.

The answers match an independent accepted implementation on random
laws and experiments on small grids, on the largest sizes, and on few
slow laws with thin rectangles, where zeros and ones mix.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1707_fenwick.cpp](1707_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((P + Q) log n + n) | AC | 0.078 s | 14752 KB |
| [1707_fenwick.go](1707_fenwick.go) | Go 1.14 x64 | fenwick | O((P + Q) log n + n) | AC | 0.093 s | 40324 KB |
| [1707_fenwick.java](1707_fenwick.java) | Java 1.8 | fenwick | O((P + Q) log n + n) | AC | 0.187 s | 20128 KB |
| [1707_fenwick.py](1707_fenwick.py) | Python 3.12 x64 | fenwick | O((P + Q) log n + n) | AC | 3.046 s | 19836 KB |
| [1707_fenwick.rs](1707_fenwick.rs) | Rust 1.75 x64 | fenwick | O((P + Q) log n + n) | AC | 0.062 s | 24072 KB |
