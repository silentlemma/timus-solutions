# 2125. Extending a sequence by its lowest-degree polynomial

[Timus 2125](https://acm.timus.ru/problem.aspx?space=1&num=2125) · difficulty 3087 · math

Original problem by Alexey Danilyuk and Oleg Merkurev, from the t.me/umnik_team contest, Petrozavodsk training camp, summer 2018.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The complexity of a sequence a₁ … aₙ is the smallest degree of a
polynomial p with p(x) ≡ aₓ modulo 998 244 353 for x = 1 … n. Extend the
given sequence by m more terms so that the complexity of the whole
sequence is as small as possible, and print the new terms. The limits
are 4 seconds and 128 MB.

## Input

n and m, 1 ≤ n ≤ 10⁵, 1 ≤ m ≤ 8 · 10⁵, then a₁ … aₙ.

## Output

b_{n+1} … b_{n+m}.

## Examples

### Example 1

Input:

```
5 10
1 4 9 16 25
```

Output:

```
36 49 64 81 100 121 144 169 196 225
```

### Example 2

Input:

```
3 3
0 0 0
```

Output:

```
0 0 0
```

### Example 3

Input:

```
5 10
1 2 4 8 16
```

Output:

```
31 57 99 163 256 386 562 794 1093 1471
```

### Example 4

Input:

```
3 1
2 1 0
```

Output:

```
998244352
```

## Solution

Over the field modulo the prime there is exactly one polynomial of
degree below n through the n given points, and every polynomial through
them has at least its degree. Continuing with that polynomial keeps the
complexity, so the answer is its values at n + 1 … n + m.

With the nodes at 0 … n − 1 (shifted by one), Lagrange's formula for an
integer t ≥ n is

p(t) = t! / (t − n)! · Σᵢ wᵢ / (t − i), with
wᵢ = aᵢ · (−1)^{n−1−i} / (i! (n − 1 − i)!).

The sum is a convolution of the sequence w with the sequence 1/k, so one
number-theoretic transform of length about 2n + m gives all m values at
once; factorials and their inverses come from a single pass. The modulus
998 244 353 = 119 · 2²³ + 1 has the roots of unity the transform needs.
The work is O((n + m) log(n + m)).

In the first example the squares are continued by the polynomial x²:
36, 49, … 225.

## Language notes

The Python solution runs under PyPy with the same transform on flat
arrays of 32-bit numbers. An earlier version multiplied the sequences
packed into huge decimal numbers; under CPython it exceeded the time
limit on test 14, and under PyPy the decimal module is pure Python and
far slower.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2125_math.cpp](2125_math.cpp) | G++ 13.2 x64 | math | O((n + m) log(n + m)) | AC | 0.250 s | 19288 KB |
| [2125_math.go](2125_math.go) | Go 1.14 x64 | math | O((n + m) log(n + m)) | AC | 0.281 s | 41732 KB |
| [2125_math.java](2125_math.java) | Java 1.8 | math | O((n + m) log(n + m)) | AC | 1.687 s | 16320 KB |
| [2125_math.py](2125_math.py) | PyPy 3.10 x64 | math | O((n + m) log(n + m)) | AC | 1.343 s | 57604 KB |
| [2125_math.rs](2125_math.rs) | Rust 1.75 x64 | math | O((n + m) log(n + m)) | AC | 0.187 s | 49012 KB |
