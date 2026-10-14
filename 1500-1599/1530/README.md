# 1530. Ones and Zeroes

[Timus 1530](https://acm.timus.ru/problem.aspx?space=1&num=1530) · difficulty 879 · greedy

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two binary sequences A and B of length n (1 ≤ n ≤ 10⁵) are compatible
when A XOR B = A + B. Given a pair (p, q), find the first compatible pair
after it, ordering pairs by the first sequence and then by the second;
if there is none, print the first compatible pair overall.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, then p and q, each on its own line, possibly with trailing spaces.

## Output

The two sequences of the answer, each on its own line.

## Examples

### Example 1

Input:

```
1
0
0
```

Output:

```
0
1
```

### Example 2

Input:

```
2
01
10
```

Output:

```
10
00
```

## Solution

Adding two binary numbers gives their XOR exactly when there is no
carry, that is, when no position holds a 1 in both. The answer either
keeps a = p with the smallest compatible b above q, or takes the next a.

With a = p, the best b agrees with q up to some position j, has 1 at j
where q has 0, and zeros after it. The kept part of q must avoid the
ones of p, so j lies before the first position where p and q both hold
1, and b may put 1 at j only if p has 0 there. The largest such j gives
the smallest b. If there is none, a must grow: the next binary sequence
after p turns its last 0 into 1 and clears the rest, and b = 0…0 fits
any a. If p is all ones, start over at the pair of all zeros. `O(n)`.

Pitfalls:

- "+" adds the sequences as binary numbers, so compatible means no
  common 1 (all tests);
- p and q themselves may clash, and then q's tail cannot be kept
  (test 05);
- when p is all ones nothing comes after it, so the answer wraps
  around (tests 03, 04, gen3);
- the lines may end with spaces, so read the input by tokens (test 06).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1530_greedy.cpp](1530_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.031 s | 816 KB |
| [1530_greedy.go](1530_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 2380 KB |
| [1530_greedy.java](1530_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 6292 KB |
| [1530_greedy.py](1530_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.078 s | 1040 KB |
| [1530_greedy.rs](1530_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 740 KB |
