# 1233. Where a number stands in dictionary order

[Timus 1233](https://acm.timus.ru/problem.aspx?space=1&num=1233) · difficulty 907 · math

Original problem by Andrew Stankevich, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Write the numbers 1 to N in lexicographic order, as strings: for N = 11
that is 1, 10, 11, 2, 3, …, 9. Given K and M (1 ≤ K, M ≤ 10⁹), find the
smallest N for which K stands at place M, or report that there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

K and M.

## Output

The smallest such N, or 0 if there is none.

## Examples

### Example 1

Input:

```
2 4
```

Output:

```
11
```

### Example 2

Input:

```
2 1
```

Output:

```
0
```

## Solution

Take N ≥ K and count the numbers that come no later than K.

- **Not longer than K.** For each length l, these are the numbers from
  `10^(l−1)` up to the first l digits of K. All of them are at most K, so
  every N ≥ K contains them; their count B is the place of K when N = K.
- **Longer than K.** A number of length `len(K) + j` comes before K
  exactly when it is less than `K·10^j`, so there are `K·10^j − 10^(len(K)+j−1)`
  of them for each j ≥ 1.

As N grows past K, the place of K rises by one exactly when N itself is
one of the longer numbers before K. So if M < B there is no answer, if
M = B the answer is K, and otherwise N is the (M − B)-th longer number
before K in increasing order: subtract whole lengths, then count into the
first length that is not used up. Parsing all prefixes processes
`1 + 2 + ... + len(K)` digits; the longer-length loop takes `O(log M)`
iterations (at most nine under these limits). With unit-cost integer
arithmetic, the total time is `O((log K)^2 + log M)`.

Pitfalls:

- a power of ten has no longer number before it, so its place never
  changes (tests 04, 08, 11);
- N can be far beyond 32 bits: for K = 100000001 only `10^j` numbers of
  each longer length come before it, and for M = 10⁹ the answer has 18
  digits (test 10);
- the number of longer lengths depends on M, so a time bound based only
  on parsing K misses this work (tests 09, 10).

## Language notes

- C++, Go, Java and Rust use signed 64-bit integers; Python uses
  arbitrary-precision integers. `K·10^j` stays below 10¹⁸ because the loop
  ends within nine lengths when K is not a power of ten.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1233_math.cpp](1233_math.cpp) | G++ 13.2 x64 | math | O((log K)^2 + log M) | AC | 0.015 s | 200 KB |
| [1233_math.go](1233_math.go) | Go 1.14 x64 | math | O((log K)^2 + log M) | AC | 0.031 s | 1084 KB |
| [1233_math.java](1233_math.java) | Java 1.8 | math | O((log K)^2 + log M) | AC | 0.109 s | 460 KB |
| [1233_math.py](1233_math.py) | Python 3.12 x64 | math | O((log K)^2 + log M) | AC | 0.078 s | 456 KB |
| [1233_math.rs](1233_math.rs) | Rust 1.75 x64 | math | O((log K)^2 + log M) | AC | 0.046 s | 232 KB |
