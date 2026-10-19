# 2122. Total Hamming distance between subsequences of every length

[Timus 2122](https://acm.timus.ru/problem.aspx?space=1&num=2122) · difficulty 3528 · math, combinatorics

Original problem by Alexey Danilyuk and Oleg Merkurev, from the t.me/umnik_team contest, Petrozavodsk training camp, summer 2018.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For a binary string s of length n and every k from 1 to n, take all
subsequences of length k (chosen by positions) and add up the Hamming
distances over all their unordered pairs. Print the n sums modulo
40 961. The limits are 4 seconds and 256 MB.

## Input

The string s, 1 ≤ n ≤ 4000.

## Output

n numbers, the sums for k = 1 … n modulo 40 961.

## Examples

### Example 1

Input:

```
11000110111001
```

Output:

```
48 4056 15326 31033 20654 29362 32472 13700 21357 12217 20411 12456 212 0
```

### Example 2

Input:

```
000
```

Output:

```
0 0 0
```

## Solution

Fix k and a position j of the subsequences. If c_j of the C(n, k)
subsequences have a 1 at position j, that position contributes
c_j · (C(n, k) − c_j) differing pairs. Summing over j,

answer(k) = C(n, k) · Σ c_j − Σ c_j².

Σ c_j counts the ones inside all subsequences, and each 1 of s lies in
C(n − 1, k − 1) of them, so Σ c_j = (number of ones) · C(n − 1, k − 1). Only Σ c_j² needs work.

Instead of choosing positions, delete n − k of them one at a time. Each
subsequence then appears (n − k)! times, once per deletion order, so let
r_k(j) = c_j · (n − k)! count the deletion orders. Going from length
k + 1 to k (positions from 0), the element at position j stays there
when one of the k − j later elements is deleted, and the element at
position j + 1 moves to j when one of the first j + 1 is deleted:

r_k(j) = (k − j) · r_{k+1}(j) + (j + 1) · r_{k+1}(j + 1).

Starting from r_n = s, each length takes O(k), O(n²) in total. The other
terms are scaled the same way, and at the end the whole expression is
divided by ((n − k)!)². The modulus 40 961 is a prime above 4000, so
these factorials are invertible.

In the second example all subsequences are equal, so every sum is 0.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2122_math_combinatorics.cpp](2122_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(n^2) | AC | 0.031 s | 464 KB |
| [2122_math_combinatorics.go](2122_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(n^2) | AC | 0.046 s | 1272 KB |
| [2122_math_combinatorics.java](2122_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(n^2) | AC | 0.156 s | 740 KB |
| [2122_math_combinatorics.py](2122_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(n^2) | AC | 3.453 s | 1228 KB |
| [2122_math_combinatorics.rs](2122_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(n^2) | AC | 0.015 s | 308 KB |
