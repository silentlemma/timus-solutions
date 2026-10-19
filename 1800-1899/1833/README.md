# 1833. Hopes of Rowing

[Timus 1833](https://acm.timus.ru/problem.aspx?space=1&num=1833) · difficulty 2007 · matching

Original problem by Alexander Ipatov (prepared by Evgeny Kurpilyansky), from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n canoeists formed m prize-winning two-person crews. Pay each canoeist
a non-negative bonus so that the two members of every prize crew get at
least k together, spending as little as possible in total.

## Input

n, k, m (2 ≤ n ≤ 500, 1 ≤ k ≤ 10000, 0 ≤ m ≤ 100000), then m crews as
pairs of distinct canoeists, each crew listed once.

## Output

The bonus of every canoeist, with absolute error at most 10⁻⁶. Any
optimal payment is accepted.

## Examples

### Example 1

Input:

```
4 1000 4
1 2
1 3
2 4
3 4
```

Output:

```
146.5
853.5
853.5
146.5
```

## Solution

This is the linear relaxation of vertex cover: minimise Σxᵥ with
xᵤ + xᵥ ≥ k on every crew. It always has a half-integral optimum, and
one is found through the doubled graph: make a left and a right copy of
every canoeist and join u on the left to v on the right, and v on the
left to u on the right, for every crew. A minimum vertex cover C of
this bipartite graph gives xᵥ = k/2 for each copy of v in C. Every crew
is covered twice over in the doubled graph, so it gets at least k, and
the total k·|C|/2 is optimal because any fractional solution, divided
by k and copied to both sides, is a fractional cover of the bipartite
graph, whose optimum is the integral |C|.

By König's theorem, C comes from a maximum matching: search alternating
paths from the free left copies; the left copies not reached and the
right copies reached form C. The matching takes `O(n·m)` with Kuhn's
augmenting paths, and Python uses Hopcroft–Karp.

In the example the crews form the cycle 1–2–4–3–1, an even cycle, and
the cover gives every canoeist 500: total 2000, the same as the sample
answer 146.5 + 853.5 + 853.5 + 146.5.

Pitfalls:

- paying only 0 or k costs more: on a triangle three halves, 1.5k in
  total, beat two whole k;
- canoeists in no crew get 0;
- many optimal payments exist, so the answer is checked by its total
  and the crews.

All answers have the least total found by trying every payment with
values 0, k/2 and k for up to 9 canoeists, and agree in total with an
independent accepted implementation on the large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1833_matching.cpp](1833_matching.cpp) | G++ 13.2 x64 | matching | O(n m) | AC | 0.093 s | 1364 KB |
| [1833_matching.go](1833_matching.go) | Go 1.14 x64 | matching | O(n m) | AC | 0.140 s | 6008 KB |
| [1833_matching.java](1833_matching.java) | Java 1.8 | matching | O(n m) | AC | 0.218 s | 7396 KB |
| [1833_matching.py](1833_matching.py) | Python 3.12 x64 | matching | O(n m) | AC | 0.218 s | 17380 KB |
| [1833_matching.rs](1833_matching.rs) | Rust 1.75 x64 | matching | O(n m) | AC | 0.046 s | 4260 KB |
