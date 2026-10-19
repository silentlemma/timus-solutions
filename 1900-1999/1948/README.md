# 1948. The First Impossible Return

[Timus 1948](https://acm.timus.ru/problem.aspx?space=1&num=1948) · difficulty 1216 · math

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose a real x. At second i+1, for i=0,1,…, the signed displacement on a
line is a(x+i)²+b(x+i)+c. For each coefficient triple, find the smallest
positive integer k for which no real choice of x makes the sum of the
first k displacements zero. Each k may use its own x; the path need not
avoid returning earlier. Limits: 1 second, 64 MB.

## Input

t, 1≤t≤1000, followed by t triples of integers a,b,c.
0<a<10⁹ and |b|,|c|<10⁹; both absolute bounds are strict.

## Output

One answer k per triple. The statement requests `Infinity` if no such k
exists or the answer exceeds 10¹⁸. Under the specified bounds this case
is impossible, as proved below; every output is an integer.

## Checking

Outputs are compared token by token.

## Examples

```
2
1 -2 1
1 1 -6
```

```
2
9
```

## Solution

The total displacement is a quadratic in x with positive leading
coefficient ak. Complete its square using the mean of 0,…,k−1:

Σ_{i=0}^{k−1} f(x+i)
= ak·(x+(k−1)/2+b/(2a))²
+ k·(a(k²−1)/12+c−b²/(4a)).

A real zero exists precisely when the minimum is nonpositive. Therefore
returning is possible exactly when

k² ≤ 1 + 3b²/a² − 12c/a.

The right side is fixed. To avoid both floating-point rounding at exact
squares and products beyond 64 bits, compute nested integer floors:

s = floor(3b²/a) − 12c.

If s<0, even k=1 is impossible, so return 1. Indeed the real quantity
3b²/a−12c lies in [s,s+1), hence is negative. Otherwise s≥0 and define

T = 1 + floor(s/a).

For integer m and positive integer a, floor((z−m)/a) equals
floor((floor(z)−m)/a). Applying this with z=3b²/a and m=12c shows that
T is exactly floor(1+3b²/a²−12c/a). An integer square satisfies the
original inequality exactly when it is at most T. Thus the answer is
floor(sqrt(T))+1, including when T is a perfect square.

Python uses exact integer square root. The other languages binary-search
the first k in [1,2000000000] with k²>T. This predicate is monotone and
the upper endpoint always satisfies it. The search therefore returns the
first impossible second, proving the algorithm.

O(t log U) time, U=2000000000, with at most 31 binary-search iterations
per case. The arithmetic core needs O(1) space; implementations that store
the input or output use O(t) space. Python's exact integer square root
also fits this upper bound for these fixed-size integers.

The parameter x is real, not integral. The strict failure test is k²>T;
equality still permits a repeated real root. Negative b is harmless after
squaring. A negative s gives answer 1. Avoid signed 32-bit products and
do not confuse a separate suitable x for each k with one x for every k.

## Language notes

Use signed 64-bit coefficients, products and search bounds in native
languages. 3b²≤2999999994000000003, s≤3000000005999999991, and
T≤3000000005999999992. Search squares are at most 4000000000000000000,
below 2⁶³−1. Check s<0 before the second division, so native truncation
agrees with floor; the first numerator is always nonnegative. Do not
form a²k² or use a floating square root. Python's integers and isqrt are exact.

Since a≥1, the real bound on k² is at most
1+3·999999999²+12·999999999=3000000005999999992<2000000000².
So k≤2000000000<10¹⁸ always exists; no `Infinity` branch is needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1948_math.cpp](1948_math.cpp) | G++ 13.2 x64 | math | O(t log U) | AC | 0.015 s | 444 KB |
| [1948_math.go](1948_math.go) | Go 1.14 x64 | math | O(t log U) | AC | 0.031 s | 1156 KB |
| [1948_math.java](1948_math.java) | Java 1.8 | math | O(t log U) | AC | 0.078 s | 500 KB |
| [1948_math.py](1948_math.py) | Python 3.12 x64 | math | O(t log U) | AC | 0.078 s | 908 KB |
| [1948_math.rs](1948_math.rs) | Rust 1.75 x64 | math | O(t log U) | AC | 0.015 s | 284 KB |
