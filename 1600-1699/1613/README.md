# 1613. For Fans of Statistics

[Timus 1613](https://acm.timus.ru/problem.aspx?space=1&num=1613) · difficulty 141 · binary_search

Original problem by Alexander Ipatov, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n cities (n ≤ 69 999) each carried some number of passengers, below
10⁹. For each of q queries (q ≤ 69 999) `l r x`, tell whether some
city numbered from l to r carried exactly x passengers. Print a string
of q characters, `1` for yes and `0` for no.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, the n counts, q, then q lines `l r x`.

## Output

The string of answers.

## Examples

### Example 1

Input:

```
5
1234567 666666 3141593 666666 4343434
5
1 5 3141593
1 5 578202
2 4 666666
4 4 7135610
1 1 1234567
```

Output:

```
10101
```

## Solution

Sort the pairs (count, city number). The cities with count x then form
one block, sorted by number. For a query, a binary search finds the
first pair not less than (x, l): the answer is yes if its count is x and
its city is at most r. `O((n + q) log n)`.

Pitfalls:

- the answer is one string without separators;
- the city must be found at or after l, not merely somewhere with count
  x (test 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1613_binary_search.cpp](1613_binary_search.cpp) | G++ 13.2 x64 | binary_search | O((n + q) log n) | AC | 0.171 s | 748 KB |
| [1613_binary_search.go](1613_binary_search.go) | Go 1.14 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 5876 KB |
| [1613_binary_search.java](1613_binary_search.java) | Java 1.8 | binary_search | O((n + q) log n) | AC | 0.140 s | 1964 KB |
| [1613_binary_search.py](1613_binary_search.py) | Python 3.12 x64 | binary_search | O((n + q) log n) | AC | 0.343 s | 26612 KB |
| [1613_binary_search.rs](1613_binary_search.rs) | Rust 1.75 x64 | binary_search | O((n + q) log n) | AC | 0.062 s | 3692 KB |
