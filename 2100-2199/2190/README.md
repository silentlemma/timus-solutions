# 2190. Fewest boulder moves to make heaps proportional

[Timus 2190](https://acm.timus.ru/problem.aspx?space=1&num=2190) · difficulty 1229 · math, sorting

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are N heaps of sᵢ boulders. One minute adds or removes a single
boulder. Find the least time after which the heaps follow the
proportion p₁ : … : p_N, not all of them empty. The limits are 2 seconds
and 256 MB.

## Input

N, 2 ≤ N ≤ 10⁵, then s₁ … s_N and p₁ … p_N, all between 1 and 10⁹.

## Output

The least number of minutes.

## Examples

### Example 1

Input:

```
2
21 34
2 3
```

Output:

```
2
```

## Solution

Divide every pᵢ by their greatest common divisor to get qᵢ. A
nonempty set of heaps in that proportion is exactly k · qᵢ for an
integer k ≥ 1, so the answer is the minimum over k of

cost(k) = Σ |sᵢ − k qᵢ| = Σ qᵢ · |sᵢ / qᵢ − k|.

This is a weighted sum of distances from k to the points sᵢ / qᵢ with
weights qᵢ, a convex function minimized over the reals at a weighted
median: sort the ratios, comparing a / b with c / d as a · d against
c · b in 64 bits, and take the first ratio where the running weight
reaches half the total. The best integer is then the floor of that
ratio or one more, and the floor is skipped when it is zero. Both
candidates lie within 1 of the real minimum, so each cost is below
cost(1) + Σqᵢ ≤ 2 · 10¹⁴ and fits in 64 bits.

In the example the ratios are 10.5 and 11.33, the second one carries
weight 3 of 5 and is the median, and k = 11 gives 22 and 33 at a cost
of 1 + 1.

The sort makes it O(N log N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2190_math_sorting.cpp](2190_math_sorting.cpp) | G++ 13.2 x64 | math, sorting | O(N log N) | AC | 0.203 s | 1564 KB |
| [2190_math_sorting.go](2190_math_sorting.go) | Go 1.14 x64 | math, sorting | O(N log N) | AC | 0.078 s | 5848 KB |
| [2190_math_sorting.java](2190_math_sorting.java) | Java 1.8 | math, sorting | O(N log N) | AC | 0.140 s | 2732 KB |
| [2190_math_sorting.py](2190_math_sorting.py) | Python 3.12 x64 | math, sorting | O(N log N) | AC | 0.875 s | 24836 KB |
| [2190_math_sorting.rs](2190_math_sorting.rs) | Rust 1.75 x64 | math, sorting | O(N log N) | AC | 0.062 s | 5304 KB |
