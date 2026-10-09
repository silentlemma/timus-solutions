# 1032. Choosing numbers whose sum is a multiple of N

[Timus 1032](https://acm.timus.ru/problem.aspx?space=1&num=1032) · difficulty 301 · prefix_sums, math

Original problem from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `N` positive integers (`1 ≤ N ≤ 10 000`, each at most 15 000, repeats
allowed), choose one or more of them whose sum is divisible by `N`. If there
is no such choice, print 0.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `N` numbers, one per line.

## Output

The number of chosen numbers, then the chosen numbers one per line, in any
order; or 0.

## Checking

Any valid choice is accepted. The checker verifies that every number is
used at most as many times as it is given, that at least one number is
chosen and that the sum is a multiple of `N`.

## Examples

### Example 1

Input:

```
4
3
8
6
1
```

Output:

```
1
8
```

### Example 2

Input:

```
1
15000
```

Output:

```
1
15000
```

## Solution

**A choice always exists**, and it can even be a block of consecutive
numbers. Look at the `N + 1` prefix sums `S_0 = 0, S_1, ..., S_N` modulo
`N`. They take at most `N` different values, so by the **pigeonhole
principle** two of them are equal, `S_i ≡ S_j (mod N)` with `i < j`; then
`a_{i+1} + ... + a_j = S_j - S_i` is a multiple of `N`.

Walk through the numbers keeping the prefix sum modulo `N` and the first
position where each remainder appeared (remainder 0 at position 0). The
first repeated remainder gives the block. `O(N)`.

So the answer 0 is never needed.

Pitfalls:

- the remainder 0 must be "seen" at position 0, so that a prefix that is
  itself a multiple of `N` is found;
- the numbers in the output are the values, not their positions;
- `N = 1`: any single number works.

## Language notes

The same pass everywhere.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1032_prefix_sums.cpp](1032_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 232 KB |
| [1032_prefix_sums.go](1032_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 1368 KB |
| [1032_prefix_sums.java](1032_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.156 s | 944 KB |
| [1032_prefix_sums.py](1032_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.093 s | 2608 KB |
| [1032_prefix_sums.rs](1032_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 464 KB |
