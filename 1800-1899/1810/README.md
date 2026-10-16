# 1810. Antiequations

[Timus 1810](https://acm.timus.ru/problem.aspx?space=1&num=1810) · difficulty 4022 · math

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the vectors x in {0, 1, 2}ⁿ such that every one of k linear forms
modulo 3 differs from its given value: aᵢ₁x₁ + … + aᵢₙxₙ ≢ bᵢ (mod 3)
for all i.

## Input

k and n (1 ≤ k, n ≤ 30), then k lines aᵢ₁ … aᵢₙ bᵢ with values from 0
to 2.

## Output

The number of solutions.

## Examples

### Example 1

Input:

```
3 3
2 2 1 1
2 1 0 0
1 2 2 2
```

Output:

```
8
```

### Example 2

Input:

```
4 3
2 2 1 1
2 1 0 0
1 2 2 2
1 0 1 2
```

Output:

```
6
```

## Solution

Look at y = Ax instead of x. If A has rank r over GF(3), every y in the
image of A comes from exactly 3^(n−r) vectors x, so the answer is
3^(n−r) times the number of image vectors y with yᵢ ≠ bᵢ for all i.
Gaussian elimination on the transposed matrix gives a basis of its null
space, the vectors w orthogonal to every column; y lies in the image
exactly when its syndrome, the list of products w·y, is zero.

Each yᵢ has two allowed values, so there are 2ᵏ ≤ 2³⁰ candidate vectors
y, too many to try, but they split into two halves of at most 2¹⁵
choices each. The syndrome is additive: list the syndromes of all
choices for the first half, and for every choice of the second half
count the first-half syndromes equal to minus its syndrome. A syndrome
over GF(3) of at most 30 coordinates is kept as two bit masks, the
coordinates equal to 1 and to 2. Then addition takes a few bitwise
operations, and negation swaps the masks. `O(nk min(n,k) + 2^(k/2) · k)`.

In the first example 8 of the 27 assignments avoid all three values;
the second example adds one more antiequation and leaves 6.

Pitfalls:

- equal or proportional rows are dependent; each image vector has
  multiple preimages exactly when r < n;
- a row of zeros with bᵢ = 0 rules out everything;
- the answer can reach 3³⁰ and needs 64 bits.

The answers agree with a direct count over all 3ⁿ assignments on 100
small systems, and with an independent accepted implementation on
square, low-rank, repetitive and narrow systems with 30 antiequations.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1810_math.cpp](1810_math.cpp) | G++ 13.2 x64 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.015 s | 748 KB |
| [1810_math.go](1810_math.go) | Go 1.14 x64 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.109 s | 6272 KB |
| [1810_math.java](1810_math.java) | Java 1.8 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.156 s | 3500 KB |
| [1810_math.py](1810_math.py) | Python 3.12 x64 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.171 s | 10228 KB |
| [1810_math.rs](1810_math.rs) | Rust 1.75 x64 | math | O(nk min(n,k) + 2^(k/2) k) | AC | 0.031 s | 1540 KB |
