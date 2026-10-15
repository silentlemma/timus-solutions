# 1706. Cipher Message 2

[Timus 1706](https://acm.timus.ru/problem.aspx?space=1&num=1706) · difficulty 678 · strings

Original problem by Dmitry Ivankov, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Take a string s of length n and a key k < n. For every position i,
look at the k characters starting at i, wrapping around to the start
of s when the end is reached, and count the distinct non-empty
substrings of that window. Print the n counts.

## Input

k (1 ≤ k ≤ 1000) on the first line, s on the second: lowercase Latin
letters, its length n with k < n ≤ 4000.

## Output

The n counts, separated by spaces.

## Examples

### Example 1

Input:

```
3
abaccc
```

Output:

```
5 6 5 3 5 6
```

## Solution

Repeat s so that every window is a plain slice [a, a + k). Count each
distinct substring of a window at its leftmost start j. Starting at j,
the window holds the lengths 1 … a + k − j, and a length is already
taken exactly when some earlier start j′ of the window, a ≤ j′ < j,
shares at least that many characters with j. So the window's count is
the sum over j of a + k − j minus best[j], the longest common prefix
of j with an earlier start in the window, clipped at zero.

Go over a from right to left. When a becomes a window's left end,
only one new earlier start, a itself, enters every best[j], so best[j]
is raised to lcp(a, j) for j = a + 1 … a + k − 1. These prefixes
come from the previous step: lcp(a, a + d) is lcp(a + 1, a + 1 + d)
+ 1 when the characters at a and a + d match, and 0 otherwise, so one
array indexed by the distance d holds them. Each step costs O(k), and
the sweep starts k positions beyond the last window so that the
prefixes that matter are already exact. `O((n + k) · k)` time,
`O(n + k)` memory.

Pitfalls:

- windows wrap around the end of s; four copies of s keep every
  comparison of the sweep inside the text;
- a suffix automaton per window also works, but costs about n · k
  automaton steps with 26-way transitions;
- k = 1 gives a 1 for every position (test 02).

The answers match an independent accepted implementation on random
strings over two, three and all letters, a Fibonacci word and periodic
strings.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1706_strings.cpp](1706_strings.cpp) | G++ 13.2 x64 | strings | O((n + k) k) | AC | 0.015 s | 272 KB |
| [1706_strings.go](1706_strings.go) | Go 1.14 x64 | strings | O((n + k) k) | AC | 0.046 s | 1292 KB |
| [1706_strings.java](1706_strings.java) | Java 1.8 | strings | O((n + k) k) | AC | 0.109 s | 972 KB |
| [1706_strings.py](1706_strings.py) | Python 3.12 x64 | strings | O((n + k) k) | AC | 1.734 s | 1224 KB |
| [1706_strings.rs](1706_strings.rs) | Rust 1.75 x64 | strings | O((n + k) k) | AC | 0.031 s | 408 KB |
