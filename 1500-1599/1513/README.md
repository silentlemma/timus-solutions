# 1513. Lemon Tale

[Timus 1513](https://acm.timus.ru/problem.aspx?space=1&num=1513) · difficulty 381 · dp

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text uses the word "lemon" N times (1 ≤ N ≤ 10000). Some of them may be
replaced by "banana", so that no more than K lemons (0 ≤ K ≤ N) stand in
a row. Count the ways to do it, exactly.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and K.

## Output

The number of ways.

## Examples

### Example 1

Input:

```
5 2
```

Output:

```
24
```

## Solution

Let a[i] count the lines of i words with no run of more than K lemons.
A valid line of i words is a valid line of i − 1 words with one more
word, lemon or banana, which gives 2·a[i − 1], except for the lines
whose new lemon makes a run of exactly K + 1: those are a valid line of
i − K − 2 words, a banana and K + 1 lemons, so
a[i] = 2·a[i − 1] − a[i − K − 2] for i > K, with a[−1] = 1 for the line
made of lemons only, and a[i] = 2^i for i ≤ K. There is no modulus, so
the numbers are big integers; Python, Go and Java have them, and C++
and Rust keep base-10⁹ limbs. `O(N²)` digit operations at worst.

Pitfalls:

- the answer is exact and reaches 2^10000, about 3000 digits (tests 04,
  07);
- K = 0 leaves a single line of bananas (test 05);
- K = 1 gives Fibonacci numbers (test 06);
- the subtraction needs the line of i − K − 2 words even when that is
  −1 words, the case of K + 1 lemons in a row (test 01, gen3).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1513_dp.cpp](1513_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.046 s | 14844 KB |
| [1513_dp.go](1513_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.062 s | 9884 KB |
| [1513_dp.java](1513_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.156 s | 12788 KB |
| [1513_dp.py](1513_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 8152 KB |
| [1513_dp.rs](1513_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.031 s | 15176 KB |
