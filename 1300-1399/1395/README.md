# 1395. Pascal vs. C++. Version 2

[Timus 1395](https://acm.timus.ru/problem.aspx?space=1&num=1395) · difficulty 2289 · hashing

Original problem by Ilya Grebnov, Dmitry Kovalioff and Nikita Rybak, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A harder version of problem 1452. From N ≤ 10 000 numbers between 1 and
10⁹, choose as many different values as possible that are consecutive
terms of an increasing arithmetic progression, in any order. Print
their number and their positions.

Time limit: 1 second. Memory limit: 4 MB.

## Input

N, then the N numbers.

## Output

The largest number of elements, then their positions in any order.

## Examples

### Example 1

Input:

```
6
7 3 2 3 5 9
```

Output:

```
4
4 5 1 6
```

## Solution

With 4 MB there is no room for the usual table over all pairs, so the
solutions walk the progressions directly. Keep each distinct value once,
with its first position, in an open-addressing hash table of 2¹⁵ slots,
and sort the values. For every pair i < j with d = a[j] − a[i]:

- stop the row of pairs once a[i] + best·d is beyond the largest value:
  a longer progression from a[i] cannot fit, and d only grows;
- skip the pair if a[j] + d is missing, as two terms never beat the
  best, or if a[i] − d is present, as the progression is walked from
  its smallest term;
- otherwise walk a[j] + d, a[j] + 2d, … while the values exist.

Each pair of neighbours in a progression starts at most one walk step,
so the work is `O(N²)` look-ups, with a single look-up for most pairs.
Sums go past 2³¹, so they are kept in 64 bits.

Pitfalls:

- repeated values count once (example 1 and test 04);
- one value repeated gives a single element (test 02);
- a set with no three-term progression keeps the best at 2, so the
  pruning is weakest there (generated test 8, numbers whose base 3
  digits are 0 and 1);
- a[j] + d can pass 2³¹ near the upper limit (test 05 and generated
  test 5).

The answers were compared on 3 000 random short sequences with a search
over all pairs. The tests are judged by a checker that asks for the
expected count and checks that the positions give distinct values in
one progression.

## Language notes

- The statement allows only C, C++ and Pascal, but the Timus submit form
  also offers Rust 1.75, so there are C++ and Rust solutions; Go, Python
  and Java cannot be submitted.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1395_hashing.cpp](1395_hashing.cpp) | G++ 13.2 x64 | hashing | O(N^2) | AC | 0.453 s | 504 KB |
| [1395_hashing.rs](1395_hashing.rs) | Rust 1.75 x64 | hashing | O(N^2) | AC | 0.500 s | 1276 KB |
