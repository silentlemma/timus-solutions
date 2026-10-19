# 2120. Expected weight of a random labelled tree with some degrees fixed

[Timus 2120](https://acm.timus.ru/problem.aspx?space=1&num=2120) · difficulty 1821 · math, probability

Original problem by Alexey Danilyuk, from the t.me/umnik_team contest, Petrozavodsk training camp, summer 2018.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The weight of a tree on vertices 1 … n is the sum over its edges (u, v)
of u · s(u) + v · s(v), where s(u) is the size of the part containing u
after the edge is removed. Some vertices have a fixed degree, the others
any degree. Pick a tree with these degrees uniformly at random and print
the integer part of its expected weight. The limits are 2 seconds and
64 MB.

## Input

n, 2 ≤ n ≤ 10⁶, then a₁ … aₙ: a fixed degree from 1 to n − 1, or −1 for
any degree. The sum of |aᵢ| is at most 2n − 2.

The expectation requires at least one compatible tree; the original statement
does not explicitly guarantee this. If every degree is fixed, their sum must
equal 2n − 2: for example, n = 3 with degrees 1, 1, 1 meets the listed bounds
but has no tree and no defined expected weight. With any free vertex, the
absolute-sum bound already ensures existence.

## Output

The integer part of the expected weight.

## Examples

### Example 1

Input:

```
5
1 -1 -1 -1 -1
```

Output:

```
67
```

### Example 2

Input:

```
5
-1 -1 -1 -1 1
```

Output:

```
52
```

### Example 3

Input:

```
4
1 1 1 3
```

Output:

```
42
```

### Example 4

Input:

```
4
1 1 2 2
```

Output:

```
38
```

## Solution

Group the terms by vertex. Removing the d edges of a vertex v splits the
other n − 1 vertices into d branches, and on each edge v keeps all
vertices except its branch, so the sizes s(v) over its edges add up to
d · n − (n − 1). Hence the weight depends only on the degrees:

W = Σ v · (n (d_v − 1) + 1) = n(n + 1)/2 + n · Σ v (d_v − 1).

By Prüfer codes the number of trees with degrees d₁ … dₙ is
(n − 2)! / ∏ (d_v − 1)!, which does not change when the free vertices
swap their degrees. So all free vertices have the same expected
d_v − 1, and these values add up to R = n − 2 − Σ (fixed d_v − 1). With
c free vertices whose labels sum to S, linearity of expectation gives

E = n(n + 1)/2 + n · Σ_fixed v (d_v − 1) + n · R · S / c.

This formula applies when c > 0. If c = 0, omit the last term, as in test
05; feasibility then requires R = 0.

Only the last term can be fractional; its integer part is computed exactly
with integer division. C++, Go and Python split R · S into a quotient and
a remainder by c before multiplying by n. Java and Rust instead split S
by c before multiplying by n · R. Both methods avoid overflow in signed
64-bit arithmetic. Do not discard the remainder before multiplication:
tests 12 and 13 exercise fractional expectations. The work is O(n).

In the third example the degrees are fixed, Σ v (d_v − 1) = 4 · 2 = 8, and
W = 10 + 4 · 8 = 42.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2120_math_probability.cpp](2120_math_probability.cpp) | G++ 13.2 x64 | math, probability | O(n) | AC | 0.156 s | 448 KB |
| [2120_math_probability.go](2120_math_probability.go) | Go 1.14 x64 | math, probability | O(n) | AC | 0.062 s | 1088 KB |
| [2120_math_probability.java](2120_math_probability.java) | Java 1.8 | math, probability | O(n) | AC | 0.171 s | 572 KB |
| [2120_math_probability.py](2120_math_probability.py) | Python 3.12 x64 | math, probability | O(n) | AC | 0.468 s | 3036 KB |
| [2120_math_probability.rs](2120_math_probability.rs) | Rust 1.75 x64 | math, probability | O(n) | AC | 0.015 s | 280 KB |
