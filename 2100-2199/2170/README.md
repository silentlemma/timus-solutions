# 2170. Time to merge juice in pairs over aligned power-of-two blocks

[Timus 2170](https://acm.timus.ru/problem.aspx?space=1&num=2170) · difficulty 1404 · dp, prefix_sums

Original problem by Vadim Barinov, from the Ural School Programming Contest 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

2ᴺ vessels hold one litre each at temperatures tᵢ. A query takes the 2ᵖ
vessels from l on and merges them in rounds, pouring every second vessel
into its left neighbour; a pair is poured as soon as both of its parts
have settled. Mixing volumes V₁, V₂ at t₁, t₂ gives
t = (V₁t₁ + V₂t₂) / (V₁ + V₂) and takes (|t − t₁| V₁ + |t − t₂| V₂)
seconds. Answer Q such queries. The limits are 3 seconds and 512 MB.

## Input

N and Q, 1 ≤ N ≤ 18, 1 ≤ Q ≤ 10⁵, the temperatures, 0 ≤ tᵢ ≤ 10⁵, then
the queries l, p with l + 2ᵖ − 1 ≤ 2ᴺ.

## Output

The time of every query.

## Examples

### Example 1

Input:

```
2 2
1 2 3 4
2 1
1 2
```

Output:

```
1.0
5.0
```

## Solution

The merges always join two halves of equal volume V. Then t is their
average, and the time is V |t₁ − t₂|, the absolute difference of the two
heat amounts V t₁ and V t₂, that is, of the sums of the original
temperatures in the two halves. Both halves are finished independently,
so a block of size 2ᵖ starting at l takes

T(l, p) = max(T(l, p − 1), T(l + 2ᵖ⁻¹, p − 1)) + |S(left half) − S(right half)|,

with T(l, 0) = 0 and S from prefix sums. Queries can start anywhere, so
the table is filled for every start and every p: N · 2ᴺ values, about
4.7 million, each in O(1). The times are integers, and every query is a
lookup.

In the example the block 1 … 4 first merges (1, 2) and (3, 4) in 1
second each, then the halves with sums 3 and 7 in 4 more, 5 in total.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2170_dp_prefix_sums.cpp](2170_dp_prefix_sums.cpp) | G++ 13.2 x64 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.125 s | 36892 KB |
| [2170_dp_prefix_sums.go](2170_dp_prefix_sums.go) | Go 1.14 x64 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.046 s | 50324 KB |
| [2170_dp_prefix_sums.java](2170_dp_prefix_sums.java) | Java 1.8 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.265 s | 44600 KB |
| [2170_dp_prefix_sums.py](2170_dp_prefix_sums.py) | PyPy 3.10 x64 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.421 s | 62776 KB |
| [2170_dp_prefix_sums.rs](2170_dp_prefix_sums.rs) | Rust 1.75 x64 | dp, prefix_sums | O(N 2^N + Q) | AC | 0.062 s | 43200 KB |
