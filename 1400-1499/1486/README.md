# 1486. Equal Squares

[Timus 1486](https://acm.timus.ru/problem.aspx?space=1&num=1486) · difficulty 621 · hashing

Original problem by Vladimir Yakovlev, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

In an N × M matrix of lowercase letters (1 ≤ N, M ≤ 500), find the
largest K such that two different K × K squares (they may overlap, but
not coincide) are equal, and print K and their top-left corners, or 0
if no two cells are equal.

Time limit: 2 seconds. Memory limit: 128 MB.

## Input

N and M, then N rows of M letters.

## Output

K, then the two corners as row and column, or just 0. Any pair is
accepted.

## Examples

### Example 1

Input:

```
5 10
ljkfghdfas
isdfjksiye
pgljkijlgp
eyisdafdsi
lnpglkfkjl
```

Output:

```
3
1 1
3 3
```

## Solution

Two different equal K × K squares contain two different equal
(K − 1) × (K − 1) squares, their top-left parts. So whether a pair of
size K exists is monotone in K, and binary search finds the largest K
in about nine checks.

A check hashes every K × K square in `O(NM)`: a rolling hash over each
row gives the hash of every window of K letters, and a second rolling
hash, with another base, runs down each column over those row hashes.
Equal squares give equal hashes. A repeated hash is confirmed by
comparing the two squares letter by letter, so a collision can only
cost time, never give a wrong answer. `O(NM log min(N, M))`.

Pitfalls:

- the two squares may overlap, as in a chessboard, where the best
  squares are one step apart (test 07);
- if no letter repeats, the answer is 0 alone (tests 02, 03, 05);
- a square matrix of one letter allows only K = N − 1, since two N × N
  squares would coincide; a longer one allows min(N, M) (gen4, test 06).

## Language notes

- The other languages pack two hashes modulo 10⁹ + 7 and 998244353 into
  one 64-bit key.

- Python labels squares exactly instead of hashing them. Every 2 × 2
  square gets the number of its class, a square of size 2s gets the
  class of its four corner squares of size s, and squares whose class
  has one member are dropped, since no larger repeated square has them
  as a corner. After the largest size p = 2ʲ with a repeat, a binary
  search between p and 2p labels each K × K square by its four corners
  of size p, which overlap and cover it. The classes live in
  open-addressing tables over flat arrays that compare all four labels,
  so no collision can give a wrong answer. It runs under PyPy, 0.41 s
  and 21 MB on the judge; earlier versions with rolling hashes exceeded
  the 2 s limit on the judge's tests 10 and 23, and one with a
  dictionary per group exceeded the 128 MB on test 23.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1486_hashing.cpp](1486_hashing.cpp) | G++ 13.2 x64 | hashing | O(NM log min(N, M)) | AC | 0.234 s | 7924 KB |
| [1486_hashing.go](1486_hashing.go) | Go 1.14 x64 | hashing | O(NM log min(N, M)) | AC | 0.718 s | 25556 KB |
| [1486_hashing.java](1486_hashing.java) | Java 1.8 | hashing | O(NM log min(N, M)) | AC | 0.671 s | 17900 KB |
| [1486_hashing.py](1486_hashing.py) | PyPy 3.10 x64 | hashing | O(NM log min(N, M)) | AC | 0.406 s | 21008 KB |
| [1486_hashing.rs](1486_hashing.rs) | Rust 1.75 x64 | hashing | O(NM log min(N, M)) | AC | 0.125 s | 7980 KB |
