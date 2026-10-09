# 1061. The cheapest window of free buffers

[Timus 1061](https://acm.timus.ru/problem.aspx?space=1&num=1061) · difficulty 666 · prefix_sums

Original problem from the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` buffers (`1 ≤ N ≤ 100000`), each locked (`*`) or holding a
value from 0 to 9. Choose `K` consecutive buffers (`1 ≤ K ≤ 10000`), none
of them locked, with the smallest total value, and print the number `L`
of the first one; among equal totals the smallest `L`. Print `0` if no
such window exists.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` and `K`, then the `N` states, 80 characters per line (the last line
may be shorter).

## Output

`L`, or `0`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
100 53
2165745216091853477755800393859785807207523169954341**7363*9*94664808*4777717089
09825185827659480548
```

Output:

```
0
```

### Example 2

Input:

```
100 10
2165745216091853477755800393859785807207523169954341**7363*9*94664808*4777717089
09825185827659480548
```

Output:

```
36
```

## Solution

Two prefix sums over the buffers: the total value and the number of
locked buffers among the first `i`. A window `[L, L + K − 1]` is allowed
when the lock count does not change across it, and its value is a
difference of the value sums. Checking all `N − K + 1` windows from left
to right and keeping a strictly smaller value gives the smallest `L`
among the cheapest. `O(N)`.

Pitfalls:

- `K > N`: no window at all, the answer is `0`;
- ties: keep the first window, so replace the best only on a strictly
  smaller value;
- the states are split over lines of 80 characters: read characters and
  skip the line breaks;
- locked buffers have no value; they only block windows.

## Language notes

- **C++**, **Go**, **Java**: the states are read character by character
  after the two numbers.
- **Python**, **Rust**: the whole input is split into words and the rows
  are joined.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1061_prefix_sums.cpp](1061_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 1372 KB |
| [1061_prefix_sums.go](1061_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 2700 KB |
| [1061_prefix_sums.java](1061_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.093 s | 1600 KB |
| [1061_prefix_sums.py](1061_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.109 s | 9248 KB |
| [1061_prefix_sums.rs](1061_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.015 s | 2196 KB |
