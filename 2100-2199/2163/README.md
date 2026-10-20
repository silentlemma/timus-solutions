# 2163. Possible values of one cell given row and column sums

[Timus 2163](https://acm.timus.ru/problem.aspx?space=1&num=2163) · difficulty 1184 · math

Original problem by Semyon Trifochkin, from the Ural School Programming Contest 2021.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A matrix of non-negative integers has known row sums r₁ … rₙ and column
sums c₁ … cₘ. Count the values the cell in row a and column b can take
over all such matrices; the answer is 0 if no matrix exists. The limits
are 1 second and 256 MB.

## Input

n and m, 1 ≤ n, m ≤ 1000, a and b, the row sums, then the column sums,
each from 0 to 10⁹.

## Output

The number of possible values.

## Examples

### Example 1

Input:

```
1 2
1 1
15
5 10
```

Output:

```
1
```

### Example 2

Input:

```
2 2
2 2
10 15
12 13
```

Output:

```
11
```

## Solution

A matrix exists exactly when the row sums and the column sums have the
same total T: then the classic greedy fill along the rows and columns
builds one. Now fix the cell to x. It needs x ≤ rₐ and x ≤ c_b. The rest
of row a, rₐ − x, has to go to the other columns, whose sums add up to
T − c_b, and likewise c_b − x has to fit into the other rows, T − rₐ;
both say x ≥ rₐ + c_b − T. Under these conditions the remaining part is
again a matrix with matching totals and one cell kept at zero, which the
same greedy fill can build. So the values form the interval from
max(0, rₐ + c_b − T) to min(rₐ, c_b), and the answer is its length,
which is at least 1. The sums need 64 bits. The work is O(n + m).

In the second example T = 25, r₂ = 15 and c₂ = 13, so the cell takes
the values 3 … 13, eleven of them.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2163_math.cpp](2163_math.cpp) | G++ 13.2 x64 | math | O(n + m) | AC | 0.015 s | 448 KB |
| [2163_math.go](2163_math.go) | Go 1.14 x64 | math | O(n + m) | AC | 0.015 s | 1104 KB |
| [2163_math.java](2163_math.java) | Java 1.8 | math | O(n + m) | AC | 0.093 s | 376 KB |
| [2163_math.py](2163_math.py) | Python 3.12 x64 | math | O(n + m) | AC | 0.093 s | 472 KB |
| [2163_math.rs](2163_math.rs) | Rust 1.75 x64 | math | O(n + m) | AC | 0.031 s | 228 KB |
