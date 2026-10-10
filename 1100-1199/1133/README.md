# 1133. Finding a term of a Fibonacci-like sequence from two other terms

[Timus 1133](https://acm.timus.ru/problem.aspx?space=1&num=1133) · difficulty 224 · number_theory

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An integer sequence, infinite both ways, satisfies
`F(k + 2) = F(k + 1) + F(k)` for every `k`. Given `F(i)` and `F(j)` for
`i ≠ j`, find `F(n)`. All indices are in `[−1000, 1000]`, and every term
from the smallest to the largest of `i, j, n` is within `±2·10⁹`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Five integers: `i`, `F(i)`, `j`, `F(j)`, `n`.

## Output

`F(n)`.

## Examples

### Example 1

Input:

```
3 5 -1 4 5
```

Output:

```
12
```

## Solution

Let `i < j` (swap the pairs otherwise). Every term is a fixed integer
combination of `F(i)` and `F(i + 1)`: `F(j) = A·F(i) + B·F(i + 1)`, where
`A` and `B` are Fibonacci numbers found by stepping the pair of
coefficients from `(1, 0)` and `(0, 1)` for `j − i` steps. So the unknown
`F(i + 1) = (F(j) − A·F(i)) / B`, and then the sequence is walked forward
or backward from `i` to `n` with `F(k − 1) = F(k + 1) − F(k)`.

The trouble is size: `B` can be the 2000th Fibonacci number, far beyond
64 bits, while the answer is small. So everything is done modulo the
prime `P = 4294967291`. It is larger than the `4·10⁹ + 1` possible
answers, so the residue of `F(n)` determines it: a residue above `P / 2`
stands for a negative value. It is below `2³²`, so the product of two
residues fits in an unsigned 64-bit integer. The division is a
multiplication by `B^(P−2)`, which works because no Fibonacci number with
index from 1 to 2000 is divisible by `P` (checked directly). Linear in
the width `W` of the index range: at most 4000 steps.

Pitfalls:

- the intermediate values `A` and `B` are huge even though every input
  and the answer are small; plain 64-bit arithmetic overflows;
- `n` can be outside the range from `i` to `j`, on either side;
- the given indices may come in either order;
- the zero sequence allows indices 2000 apart, so the walk has up to 2000
  steps.

The answers were compared with an exact big-integer computation on every
test and on 200 random queries, which also checked that the inputs meet
the `±2·10⁹` limit.

## Language notes

- All languages use the same modulus and walk.
- Java has no unsigned 64-bit type, but `Long.remainderUnsigned` reduces
  the wrapped product correctly.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1133_number_theory.cpp](1133_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(W) | AC | 0.015 s | 128 KB |
| [1133_number_theory.go](1133_number_theory.go) | Go 1.14 x64 | number_theory | O(W) | AC | 0.015 s | 1064 KB |
| [1133_number_theory.java](1133_number_theory.java) | Java 1.8 | number_theory | O(W) | AC | 0.156 s | 1688 KB |
| [1133_number_theory.py](1133_number_theory.py) | Python 3.12 x64 | number_theory | O(W) | AC | 0.078 s | 436 KB |
| [1133_number_theory.rs](1133_number_theory.rs) | Rust 1.75 x64 | number_theory | O(W) | AC | 0.015 s | 220 KB |
