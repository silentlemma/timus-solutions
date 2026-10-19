# 1879. GOV-internship 2

[Timus 1879](https://acm.timus.ru/problem.aspx?space=1&num=1879) · difficulty 1461 · greedy

Original problem by Mikhail Rubinchik, from the Ural Regional School Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The distance from a cyclic string s to a shorter string t is the sum
of the Hamming distances from t to every substring of s of t's length,
including the ones that wrap around the end of s. Both strings may
contain question marks. Replace every question mark by a letter so
that the distance is as small as possible, and print it. Letters are
numbers from 1 to 100 000, and 0 stands for a question mark.

## Input

The length n of s (1 ≤ n ≤ 100 000) and its n numbers, then the length
m of t and its m numbers.

## Output

The smallest distance.

## Examples

### Example 1

Input:

```
5
2 1 1 0 2
4
3 0 3 0
```

Output:

```
14
```

## Solution

A cyclic string of length n has n substrings of length m, one starting
at each position. For a fixed position j of t, the starts run over all
n positions of s, so every pair (position of s, position of t) is
compared exactly once. The distance is therefore n·m minus the number
of pairs with equal letters, Σ a(c)·b(c) over letters c, where a(c) and b(c)
count c in s and t. The order of letters does not matter at all.

Now put x(c) question marks of s and y(c) of t on letter c. The equal
pairs grow by Σ (x(c)·b(c) + y(c)·a(c) + x(c)·y(c)). For fixed y this is
linear in x, so the best x puts all p question marks of s on one
letter. In the same way all q question marks of t go to one letter.
With one letter for both the gain is p·b(c) + q·a(c) + p·q, and with two
different letters it is at most p·max b + q·max a. That bound is
reached when the two maxima are at different letters, and is beaten by
the first case otherwise. The answer is n·m − Σ a(c)b(c) minus the larger
gain. `O(n + m + letters)`.

In the example the counts are a: 2 → 2, 1 → 2 with one question mark,
and b: 3 → 2 with two. No letters match, and the best gain is 6, for
example with all question marks turned into 2. The answer is
20 − 6 = 14.

Pitfalls:

- the cyclic substrings make every pair meet exactly once, so neither
  positions nor the order of letters matter;
- splitting the question marks of one string between letters never
  helps;
- the distance reaches 10¹⁰, so 64-bit integers are needed.

The answers match a search over all replacements and all cyclic
substrings on 3000 small random cases, and an independent accepted
implementation on 90 large ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1879_greedy.cpp](1879_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m + L) | AC | 0.125 s | 1752 KB |
| [1879_greedy.go](1879_greedy.go) | Go 1.14 x64 | greedy | O(n + m + L) | AC | 0.031 s | 3796 KB |
| [1879_greedy.java](1879_greedy.java) | Java 1.8 | greedy | O(n + m + L) | AC | 0.125 s | 2108 KB |
| [1879_greedy.py](1879_greedy.py) | Python 3.12 x64 | greedy | O(n + m + L) | AC | 0.156 s | 20668 KB |
| [1879_greedy.rs](1879_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m + L) | AC | 0.046 s | 4716 KB |
