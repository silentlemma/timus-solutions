# 1961. Cantonese Dialect

[Timus 1961](https://acm.timus.ru/problem.aspx?space=1&num=1961) · difficulty 875 · math

Original problem from Open Ural FU Personal Contest 2013 | by Alexander Ipatov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A population has N objects, of which an unknown number M belong to a
specified class. A uniform sample of n distinct objects contains exactly
m members of that class. Choose the integer M, 0≤M≤N, maximizing the
probability of this observation. If several values maximize it, choose
the largest. Sampling is without replacement. Limits: 1 second, 64 MB.

## Input

Three integers n,m,N, in that order: 1≤n≤N≤10⁸ and 0≤m≤n.

## Output

One integer M, the largest maximizer.

## Checking

Outputs are compared token by token.

## Examples

```
10 1 200
```

```
20
```

## Solution

For the sample, m(N+1)=201 and floor(201/10)=20, so the answer is 20.

For a candidate M, the probability is

P(M)=C(M,m)·C(N−M,n−m)/C(N,n).

It is positive exactly on m≤M≤N−n+m. The denominator is independent of M.
Do not evaluate these huge binomial coefficients. Instead compare adjacent
feasible candidates:

P(M+1)/P(M) = (M+1)/(M+1−m) · (N−M−n+m)/(N−M).

The denominators are positive on such a step. Subtracting the cross
products shows that this ratio is at least one exactly when

m(N+1)−n(M+1)≥0.

Thus the probabilities increase, may have one equal adjacent pair, then
decrease. The largest maximizing index is

M = min(N, floor(m(N+1)/n)).

When 0<m<n and m(N+1)/n is an integer q, the two equal maxima are q−1
and q; integer division returns the required larger one. For example,
n=2,m=1,N=3 gives probability 2/3 at both M=1 and M=2, so output 2.

The formula is feasible. For m<n, its quotient is at least m. Also
m(N+1)/n=(N+1)−(n−m)(N+1)/n<N−n+m+1, so its floor is at most N−n+m.
If m=n, the quotient is N+1 and the cap returns N, which makes every
sample successful. If m=0, it returns zero. If n=N, the entire population
was observed and the answer is exactly m, as the formula also gives.

`O(1)` time and `O(1)` space: one multiplication, integer division and cap.

Use N+1, not N, and choose the upper tie. Do not replace the model by
independent sampling with replacement. The largest intermediate product
is 10⁸(10⁸+1)=10,000,000,100,000,000: it exceeds both int32 and exact
binary64 integer precision, but fits signed int64. Keep the multiplication
and division integral. For n=N=10⁸,m=99,999,999, floating-point rounding
can incorrectly return 10⁸ even though the observed full population fixes
M=99,999,999. The cap at N matters when m=n.

## Language notes

C++ uses int64_t, Go 1.14 int64, Java 8 long and Rust 1.75 u64. Parameters
are already wide before multiplication. Python integers are exact.
Rust uses only the standard library. All versions use ordinary integer
division on nonnegative operands; no special negative rounding is needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1961_math.cpp](1961_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB |
| [1961_math.go](1961_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1140 KB |
| [1961_math.java](1961_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1592 KB |
| [1961_math.py](1961_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.109 s | 400 KB |
| [1961_math.rs](1961_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.062 s | 228 KB |
