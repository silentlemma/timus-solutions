# 2123. Counting ways to make a mass with two weights of each fast-growing type

[Timus 2123](https://acm.timus.ru/problem.aspx?space=1&num=2123) · difficulty 1040 · dp

Original problem by Alexey Danilyuk, from the t.me/umnik_team contest, Petrozavodsk training camp, summer 2018.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n types of weights with masses a₁ … aₙ, each type at least
twice as heavy as the previous one, and two weights of every type.
Count the ways to make the mass W exactly; ways differ by how many
weights of some type are used. The limits are 4 seconds and 256 MB.

## Input

n and W, 1 ≤ n ≤ 60, 0 ≤ W ≤ 4 · 10¹⁸, then a₁ … aₙ with 1 ≤ a₁,
2aᵢ ≤ aᵢ₊₁ and aₙ ≤ 10¹⁸.

## Output

The number of ways.

## Examples

### Example 1

Input:

```
5 100
2 5 10 21 49
```

Output:

```
3
```

## Solution

Write the number of weights of type i as 1 + xᵢ with xᵢ ∈ {−1, 0, 1}.
With S the total of all masses, a way is a choice of xᵢ with
Σ xᵢ aᵢ = W − S. Flipping every sign maps the solutions for a value to
those for its negation, so it is enough to count the representations of
r = |W − S| (and W > 2S has none).

Go from the heaviest type down, keeping the reachable residuals with
their numbers of ways. Before type i is used, a residual r has to be
covered by types 1 … i, so r ≤ Sᵢ, the sum of a₁ … aᵢ. Choosing xᵢ
turns r into r or r − aᵢ, and by the same sign symmetry r − aᵢ can be
replaced by |r − aᵢ|; r + aᵢ is never small enough, since the lighter
types sum to less than aᵢ. With these growth conditions only all xᵢ = 0
give 0, so a residual 0 is one way and goes straight to the answer.

The residuals are kept sorted. Staying keeps the order, r − aᵢ for
r > aᵢ keeps it as well, and aᵢ − r for r ≤ aᵢ reverses it, so the next
list is a three-way merge of sorted streams, with equal residuals added
up. Each type at least halves the bound on the residuals and at most
doubles a number of ways, so a residual and its count fit together in
one 64-bit word. The number of residuals can grow like the Fibonacci
numbers, but it is limited by Sᵢ + 1 and stays within the limits.

In the example the three ways are 2 · 5 + 2 · 10 + 21 + 49,
2 + 2 · 49 and 2 · 2 + 5 + 2 · 21 + 49.

## Language notes

The Python solution keeps the residuals as bitsets over blocks of
masses, with the numbers of ways stored as binary bit planes, so a step
is a few shifts and masks and a bit-sliced addition. When the lightest
types form an exact doubling chain u, 2u, 4u, …, the number of ways to
finish with them is a hyperbinary count, a term of Stern's diatomic
sequence, which is computed directly instead of expanding the chain.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2123_dp.cpp](2123_dp.cpp) | G++ 13.2 x64 | dp | O(n R), R the largest number of residuals | AC | 0.031 s | 564 KB |
| [2123_dp.go](2123_dp.go) | Go 1.14 x64 | dp | O(n R), R the largest number of residuals | AC | 0.046 s | 1292 KB |
| [2123_dp.java](2123_dp.java) | Java 1.8 | dp | O(n R), R the largest number of residuals | AC | 0.109 s | 620 KB |
| [2123_dp.py](2123_dp.py) | Python 3.12 x64 | dp | O(n R), R the largest number of residuals | AC | 0.078 s | 1304 KB |
| [2123_dp.rs](2123_dp.rs) | Rust 1.75 x64 | dp | O(n R), R the largest number of residuals | AC | 0.031 s | 360 KB |
