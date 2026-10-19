# 1904. Reversing Absolute Folds

[Timus 1904](https://acm.timus.ru/problem.aspx?space=1&num=1904) · difficulty 478 · math, sorting

Original problem by Alexander Ipatov, from Ural Championship 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For a real input x, apply k operations in order: replace the current
value y by |y−aᵢ|. Describe every x whose final value is at most 1.
Return the set as sorted, nonintersecting closed intervals with integer
endpoints. The original x can be negative. Limits: 1 second and 64 MB.

## Input

First k, with 1 ≤ k ≤ 10. Then k integer references a₁,…,aₖ in forward
processing order, with −1000 ≤ aᵢ ≤ 1000.

## Output

Print the number of intervals and then one pair l ≤ r per line, in
increasing order. A single point is allowed; print 0 for an empty set.
Include boundary points whose final value equals 1.

## Checking

Tests use `tokens` and compare the sorted connected components exactly.
Overlapping or touching intervals are merged into a single closed component.

## Examples

```
3
0 4 2
```

```
4
-7 -5
-3 -1
1 3
5 7
```

## Solution

Work backward from the accepted final range [0,1]. Suppose a desired
output interval of one operation is [l,r]. Absolute values cannot be
negative, so discard the interval if r < 0; otherwise clip l to max(l,0).
The full preimage under `z = |y−a|` is

`[a−r, a−l] ∪ [a+l, a+r]`.

Apply this to every current interval, sort the resulting intervals and
merge all intersections, including shared endpoints. Repeat for
aₖ,aₖ₋₁,…,a₁. Each intermediate variable is the output of an absolute
value, so clipping the desired output at each inversion is necessary.
After the last inversion, retain negative original inputs; do not clip
the final answer to nonnegative values.

The invariant is that the current union contains exactly the values
that pass through the already reversed suffix of operations successfully.
The two reflected branches are precisely all solutions of one absolute
value constraint. Intersecting its output with [0,∞) removes impossible
values, while sorting and merging preserve the union. Induction through
all operations gives exactly the required original inputs.

All initial endpoints and reference values are integers. Reflection,
translation, clipping at zero and union preserve integer endpoints.
Every accepted original reading satisfies `|x| ≤ 1 + Σ|aᵢ| ≤ 10001`,
so ordinary signed 32-bit integers suffice.

At most twice as many intervals arise at a step. With at most `2^k`
candidates and sorting at each level, time is `O(k·2^k)` and auxiliary
space is `O(2^k)`. Here k ≤ 10. An empty union remains empty.

For the sample, reversing a₃=2 gives [1,3]. Reversing a₂=4 gives
[1,3] and [5,7]. Reversing a₁=0 adds their negative reflections,
producing the four shown components.

## Language notes

All five sources sort interval pairs by left, then right endpoint.
Python uses CPython 3.12. Parse signed references in every language.
Java mutates only the right endpoint of a newly constructed merged interval.

Merge when the next left endpoint is at most the previous right endpoint;
this describes real intervals. Preserve isolated points. Negative references
can eliminate every possible intermediate output: for example [0,−2]
has no calm input, while [2,−1] accepts only x=2.

The answers agree with evaluating the chain forwards on 4025 cases,
among them 1725 with an empty answer and 915 with isolated points; the
largest tests have 512 separate intervals.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1904_math_sorting.cpp](1904_math_sorting.cpp) | G++ 13.2 x64 | math, sorting | O(k 2^k) | AC | 0.015 s | 436 KB |
| [1904_math_sorting.go](1904_math_sorting.go) | Go 1.14 x64 | math, sorting | O(k 2^k) | AC | 0.031 s | 1252 KB |
| [1904_math_sorting.java](1904_math_sorting.java) | Java 1.8 | math, sorting | O(k 2^k) | AC | 0.140 s | 2764 KB |
| [1904_math_sorting.py](1904_math_sorting.py) | Python 3.12 x64 | math, sorting | O(k 2^k) | AC | 0.093 s | 540 KB |
| [1904_math_sorting.rs](1904_math_sorting.rs) | Rust 1.75 x64 | math, sorting | O(k 2^k) | AC | 0.015 s | 260 KB |
