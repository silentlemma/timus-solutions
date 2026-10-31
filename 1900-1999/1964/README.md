# 1964. Chinese Dialects

[Timus 1964](https://acm.timus.ru/problem.aspx?space=1&num=1964) · difficulty 172 · math

Original problem from Open Ural FU Personal Contest 2013 | by Alexander Ipatov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A universe has n distinct elements. For k subsets, only lower bounds
a_i on their sizes are known: subset i must contain at least a_i
elements. Find the smallest possible number of elements belonging to
all k subsets simultaneously. The subsets may overlap arbitrarily.
Limits: 1 second, 64 MB.

## Input

n,k on the first line, with 1≤n≤10⁹ and 2≤k≤20. The second line gives
k integers a_i, each satisfying 1≤a_i≤n.

## Output

One integer: the minimum possible size of the intersection of all k sets.

## Checking

Outputs are compared token by token.

## Examples

```
1000000000 2
800000000 800000000
```

```
600000000
```

```
1000000000 2
500000000 500000000
```

```
0
```

## Solution

In the first example each set can omit at most 200,000,000 elements.
Even if these omissions are disjoint, they cover only 400,000,000 of
the 1,000,000,000 elements. The remaining 600,000,000 must be in both
sets, and disjoint omissions attain this number. In the second example
the two sets can partition the universe into halves, leaving no common
element.

Work with complements. Write b_i=n−a_i. At most b_i elements can be
absent from set i. An element outside the common intersection must be
absent from at least one set. The union of all complements has size
at most min(n,Σb_i), so the intersection has size at least

max(0,n−Σb_i) = max(0,Σa_i−(k−1)n).

This bound is attainable, not merely necessary. Label the elements
0,…,n−1 cyclically. Give the first complement the first b_1 consecutive
labels, the next complement the following b_2 labels, and so on, wrapping
around modulo n. Each b_i<n, so that complement has exactly b_i distinct
elements and the corresponding original set has exactly a_i elements.
These exact sizes also satisfy the required lower bounds.

If Σb_i<n, the assigned complements are disjoint and their union has
Σb_i elements. If Σb_i≥n, the consecutive walk visits all n labels, so
the union is the entire universe. In both cases its size is min(n,Σb_i),
and the common intersection reaches the lower bound.

The program only computes this number. Start with n, subtract each
n−a_i, then clamp the final result to zero. Constructing the actual
subsets is useful for the proof but unnecessary for the output.

`O(k)` time and `O(k)` space in these implementations, which keep the
k input values. The accumulator itself uses `O(1)` extra space.

The size bounds are lower bounds, not exact observations or probabilities.
Do not assume independent membership, add pairwise intersections, or use
only the smallest set. Negative lower bounds on the intersection mean
zero. Although the final answer is at most n, intermediate sums can
approach 20·10⁹ and the subtraction can go below −2³¹. Use signed 64-bit
arithmetic. When all a_i=n, the answer is n, not zero.

## Optimized solutions

The optimized C++ solution reads with `scanf` instead of `iostream` and
subtracts each `n − a_i` from the accumulator as soon as it is read,
instead of keeping the k values in a vector, so it needs `O(1)` space;
the accumulator is still a signed 64-bit integer (`long long`), since up
to 20 deficits of up to 10⁹ each are subtracted:
{1964_math_optimized.cpp}.

The optimized Java solution computes the same number, but reads the
input with `BufferedReader` and `StringTokenizer` instead of `Scanner`,
whose regular expressions take time and memory to set up:
{1964_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1964_math_optimized.cpp`: time reduction +51.61%; memory reduction
  +73.53%; base: `1964_math.cpp`.

- `1964_math_optimized.java`: time reduction +25.60%; memory reduction
  +68.20%; base: `1964_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1964_math.rs](1964_math.rs).

C++ uses int64_t, Go 1.14 int64, Java 8 long and Rust 1.75 i64. Rust
must not use unsigned arithmetic for the possibly negative accumulator.
Python 3.12 uses exact integers. All versions read the k values once.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1964_math.cpp](1964_math.cpp) | G++ 13.2 x64 | math | O(k) | AC | 0.031 s | 408 KB | 11292204 |
| [1964_math.go](1964_math.go) | Go 1.14 x64 | math | O(k) | AC | 0.031 s | 1120 KB | 11292206 |
| [1964_math.java](1964_math.java) | Java 1.8 | math | O(k) | AC | 0.125 s | 1648 KB | 11304242 |
| [1964_math.py](1964_math.py) | Python 3.12 x64 | math | O(k) | AC | 0.078 s | 476 KB | 11304244 |
| [1964_math.rs](1964_math.rs) | Rust 1.75 x64 | math | O(k) | AC | 0.031 s | 236 KB | 11292211 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1964_math_optimized.cpp](1964_math_optimized.cpp) | G++ 13.2 x64 | math | O(k) | AC | 0.015 s | 108 KB | 11307259 |
| [1964_math_optimized.java](1964_math_optimized.java) | Java 1.8 | math | O(k) | AC | 0.093 s | 524 KB | 11307263 |
