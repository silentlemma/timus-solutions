# 1564. Counting Ones

[Timus 1564](https://acm.timus.ru/problem.aspx?space=1&num=1564) · difficulty 680 · binary_search

Original problem by Sergey Pupyrev, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Petya climbs the stairs of a skyscraper from floor 1 and counts the
digits 1 on the floor numbers on the way. Given the count k
(1 ≤ k ≤ 10¹⁸), print the floor where the last of these ones was
counted, or `Petr lies` if no floor gives exactly k ones.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number k.

## Output

The floor number or `Petr lies`.

## Examples

### Example 1

Input:

```
4
```

Output:

```
11
```

### Example 2

Input:

```
3
```

Output:

```
Petr lies
```

## Solution

Let f(x) be the number of ones in 1, …, x. It counts place by place: at
place p (1, 10, 100, …) the numbers up to x hold ⌊x / 10p⌋ full blocks
of 10p numbers with p ones there each, and the last, partial block adds
p ones if its digit at that place is above 1, the rest of x below the
place plus 1 if the digit is 1, and nothing if it is 0.

f only grows, so the floor where the k-th one was counted is the first x
with f(x) ≥ k, found by binary search over 1 … 10¹⁸ (f(10¹⁸) is about
1.8·10¹⁸). If f(x) is larger than k, floor x brought several ones at
once and the count k was never seen, so Petya lies. The search takes
about 60 steps of O(log x) each. The results were checked against
walking the floors one by one for all counts up to 25000.

Pitfalls:

- a floor such as 11 adds two ones at once, so some counts never occur
  (the second example);
- the answer for k = 10¹⁸ is near 5.2·10¹⁷, and the place values reach
  10¹⁷, so the fixed-width solutions need 64-bit arithmetic (test 05);
- a count one short of the total at a floor full of ones is a lie
  (test 08).

## Optimized solutions

The digit DP constructs the floor from left to right. For each possible next digit, it counts the ones contributed by the whole block of completions and either skips the block or descends into it. A floor can add several ones at once, so the final count must match exactly.

Python 3.12 x64, submission 11318528. Time 0.078 → 0.078 s, memory 428 → 436 KB.

Java 1.8, submission 11318559. Time 0.109 → 0.125 s, memory 1564 → 396 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321883 · Go 1.14 x64 №11322261 · Java 1.8 №11322262 · Python 3.12 x64 №11322264 · Rust 1.75 x64 №11322265.

Go constructs the floor number one decimal digit at a time, skipping whole blocks by counting the occurrences of the digit one. Go 1.14 x64, submission 11322873. Time 0.015 → 0.031 s, memory 1060 → 316 KB.

Rust reconstructs the floor digit by digit, counting how many ones each skipped decimal prefix contributes. Rust 1.75 x64, submission 11323309. Time 0.015 → 0.031 s, memory 216 → 44 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1564_binary_search.cpp](1564_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(log^2 k) | AC | 0.001 s | 112 KB | 11321883 |
| [1564_binary_search.go](1564_binary_search.go) | Go 1.14 x64 | binary_search | O(log^2 k) | AC | 0.015 s | 1060 KB | 11322261 |
| [1564_binary_search.java](1564_binary_search.java) | Java 1.8 | binary_search | O(log^2 k) | AC | 0.109 s | 1564 KB | 11322262 |
| [1564_binary_search.py](1564_binary_search.py) | Python 3.12 x64 | binary_search | O(log^2 k) | AC | 0.078 s | 428 KB | 11322264 |
| [1564_binary_search.rs](1564_binary_search.rs) | Rust 1.75 x64 | binary_search | O(log^2 k) | AC | 0.015 s | 216 KB | 11322265 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1564_dp.py](1564_dp.py) \* | Python 3.12 x64 | dp | O(log k) | AC | 0.078 s | 436 KB | 11318528 |
| [1564_dp.java](1564_dp.java) | Java 1.8 | dp | O(log k) | AC | 0.125 s | 396 KB | 11318559 |
| [1564_dp.go](1564_dp.go) \* | Go 1.14 x64 | dp | O(log k) | AC | 0.031 s | 316 KB | 11322873 |
| [1564_dp.rs](1564_dp.rs) \* | Rust 1.75 x64 | dp | O(log k) | AC | 0.031 s | 44 KB | 11323309 |

\* The marked versions have room to improve in the ratings.
