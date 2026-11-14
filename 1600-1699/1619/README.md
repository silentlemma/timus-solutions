# 1619. Big Brother

[Timus 1619](https://acm.timus.ru/problem.aspx?space=1&num=1619) · difficulty 717 · math

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

During a year the elder brother gets K one-euro coins and the younger
one gets M, one coin at a time, in a uniformly random order. The elder
gets angry if at some moment the younger has more money. For each of N
cases (N ≤ 2004, 0 ≤ K, M ≤ 10⁴) print the probability that he never
does, with an error of at most 10⁻⁶.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines `K M`.

## Output

The probabilities, one per line.

## Examples

### Example 1

Input:

```
3
1 0
0 1
1 1
```

Output:

```
1
0
0.5
```

## Solution

The orders are lattice paths with K steps of one kind and M of the
other, C(K + M, M) of them. If M > K the younger ends ahead, so the
answer is 0. Otherwise the bad paths are those that at some moment have
the younger one coin ahead; reflecting its prefix through the first bad
moment turns it into a path with K + 1 and M − 1 coins, one to one, so
there are C(K + M, M − 1) bad paths. The probability is

1 − C(K + M, M − 1) / C(K + M, M) = 1 − M / (K + 1) = (K − M + 1) / (K + 1).

`O(1)` per case.

Pitfalls:

- equal amounts are fine: only being strictly ahead angers the elder,
  so K = M = 1 gives 1/2, not 0 (example);
- K = M = 0 gives 1, and M > K gives exactly 0 (test 03).

The formula matches counting all orders for every K, M ≤ 8.

## Optimized solutions

Read the integers from buffered input and write each probability to eight decimal places. The time remains linear in the number of pairs.

Go submission 11321910 took 0.015 s and used 328 KB. The simple version took 0.015 s and used 1184 KB.

Java submission 11317935 took 0.062 s and used 500 KB. The simple version took 0.156 s and used 4196 KB.

Python submission 11317944 took 0.062 s and used 372 KB. The simple version took 0.062 s and used 800 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321893 · Rust 1.75 x64 №11321911 · Go 1.14 x64 №11322083 · Java 1.8 №11322084 · Python 3.12 x64 №11322085.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1619_math.cpp](1619_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 124 KB | 11321893 |
| [1619_math.go](1619_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1184 KB | 11322083 |
| [1619_math.java](1619_math.java) | Java 1.8 | math | O(N) | AC | 0.156 s | 4196 KB | 11322084 |
| [1619_math.py](1619_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 800 KB | 11322085 |
| [1619_math.rs](1619_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.001 s | 252 KB | 11321911 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1619_math_optimized.go](1619_math_optimized.go) \* | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 328 KB | 11321910 |
| [1619_math_optimized.java](1619_math_optimized.java) \* | Java 1.8 | math | O(N) | AC | 0.062 s | 500 KB | 11317935 |
| [1619_math_optimized.py](1619_math_optimized.py) \* | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 372 KB | 11317944 |

\* The marked solutions can improve their target rankings.
