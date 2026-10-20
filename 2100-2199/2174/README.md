# 2174. Pairing banknotes so that every pair sums to a prime

[Timus 2174](https://acm.timus.ru/problem.aspx?space=1&num=2174) · difficulty 939 · matching

Original problem by Ignat Nigmatullin, from the Ural School Programming Contest 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Split N banknotes, N even, into pairs so that the two values of every
pair add up to a prime, or report that it is impossible. Any valid
pairing is accepted. The limits are 1 second and 256 MB.

## Input

N, 2 ≤ N ≤ 500, then the values, 1 ≤ cᵢ ≤ 10⁶.

## Output

NO, or YES and N / 2 pairs.

## Checking

A checker verifies the verdict and that the pairs use exactly the given
notes with prime sums.

## Examples

### Example 1

Input:

```
8
6 2 4 5 2 3 1 5
```

Output:

```
YES
5 2
3 2
5 6
1 4
```

### Example 2

Input:

```
2
1 3
```

Output:

```
NO
```

## Solution

The only even prime is 2 = 1 + 1, so every other pair must join an odd
note with an even one. Let O be the number of odd notes, ones included,
and E the number of even notes. The pairs of two ones take away odd
notes two at a time, so exactly (O − E) / 2 of them are needed; if that
is negative or needs more ones than there are, the answer is NO. Ones
are all alike, so it does not matter which ones are paired together.

The remaining odd and even notes, equally many, form a bipartite graph
with an edge whenever the sum is prime, found with a sieve up to
2 · 10⁶. A perfect matching in it, found with Kuhn's augmenting paths in
O(N³), is the answer; if it does not exist the answer is NO.

In the second example 1 + 3 = 4 is not prime, and two odd notes cannot
be paired otherwise.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2174_matching.cpp](2174_matching.cpp) | G++ 13.2 x64 | matching | O(N^3 + C log log C) | AC | 0.015 s | 1752 KB |
| [2174_matching.go](2174_matching.go) | Go 1.14 x64 | matching | O(N^3 + C log log C) | AC | 0.031 s | 3248 KB |
| [2174_matching.java](2174_matching.java) | Java 1.8 | matching | O(N^3 + C log log C) | AC | 0.109 s | 2904 KB |
| [2174_matching.py](2174_matching.py) | Python 3.12 x64 | matching | O(N^3 + C log log C) | AC | 0.109 s | 4620 KB |
| [2174_matching.rs](2174_matching.rs) | Rust 1.75 x64 | matching | O(N^3 + C log log C) | AC | 0.046 s | 2116 KB |
