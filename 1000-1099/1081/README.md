# 1081. The K-th binary string without two adjacent ones

[Timus 1081](https://acm.timus.ru/problem.aspx?space=1&num=1081) · difficulty 269 · dp

Original problem by Emil Kelevedzhiev, from the Informatics Tournament of the Winter Mathematical Festival, Varna 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Consider all strings of length `N` (`0 < N < 44`) made of 0 and 1 with no
two adjacent ones, sorted lexicographically. Print the `K`-th of them
(`0 < K < 10^9`), or `-1` if there are fewer than `K`.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` and `K`.

## Output

The string, or `-1`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 1
```

Output:

```
000
```

## Solution

Let `count[r]` be the number of valid strings of length `r`: a string
starts either with 0 and any valid rest, or with `10` and any valid rest,
so `count[r] = count[r − 1] + count[r − 2]` with `count[0] = 1` and
`count[1] = 2`, the Fibonacci numbers.

Build the answer from the left. If the previous character is 1, this one
must be 0. Otherwise the strings with 0 here come first in the order, and
there are `count[rest]` of them, where `rest` is the number of positions
after this one (the 0 does not restrict the next character). If
`K ≤ count[rest]`, write 0; otherwise subtract `count[rest]` from `K` and
write 1. If `K > count[N]` from the start, print `-1`. `O(N)`.

Pitfalls:

- `count[43] = 1 134 903 170` is larger than any `K`, so for `N = 43`
  there is always an answer; the counts are kept in 64-bit integers
  anyway;
- after a 1 the next character is forced and `K` is not changed;
- the strings are counted from `K = 1`, the all-zero string.

The answers were checked against the sorted list of all valid strings for
`N ≤ 20`, and for longer strings by computing the rank of the answer back
from a memoised count.

## Language notes

- Python grows the `count` list with `append` until it reaches `N`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1081_dp.cpp](1081_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 200 KB |
| [1081_dp.go](1081_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.015 s | 1084 KB |
| [1081_dp.java](1081_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1640 KB |
| [1081_dp.py](1081_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 476 KB |
| [1081_dp.rs](1081_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 216 KB |
