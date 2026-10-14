# 1537. Ents

[Timus 1537](https://acm.timus.ru/problem.aspx?space=1&num=1537) · difficulty 283 · dp

Original problem by Sergey Pupyrev, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The first ent learns two words. Every ent who has learned w words teaches
them to one old and one young ent who cannot speak yet; then the elves
teach the old one one more word, so it ends with w + 1 words, and the
young one w more, so it ends with 2w. This goes on forever. Count the
ents who know exactly K words, modulo P (K ≤ 10⁷, P ≤ 10⁹).

Time limit: 1 second. Memory limit: 64 MB.

## Input

K and P.

## Output

The number of ents who know exactly K words, modulo P.

## Examples

### Example 1

Input:

```
4 10
```

Output:

```
2
```

## Solution

Let f(w) be the number of ents who know w words. Every ent but the first
was taught by one parent, as its old pupil (w − 1 words) or its young one
(w / 2 words, only for even w), so f(2) = 1 and
f(w) = f(w − 1) + f(w / 2) for even w, f(w) = f(w − 1) for odd w. An odd
w adds nothing, so g(m) = f(2m) = f(2m + 1) satisfies g(1) = 1 and
g(m) = g(m − 1) + g(⌊m / 2⌋), and the answer is g(⌊K / 2⌋), or 0 for
K = 1. If B(n) counts partitions of n into powers of two, then
g(m) = B(2m) / 2 for m ≥ 1. These counts grow too large to keep exactly,
so the recurrence is evaluated modulo P.

One pass over m up to K / 2 = 5·10⁶ does it; only the values up to K / 4
are looked up again, so only those are stored (an array of 2.5·10⁶
numbers). A sum of two residues is at most 2(P − 1) ≤ 1,999,999,998,
which fits a signed 32-bit integer; the compiled solutions use 64-bit sums.
`O(K)` time and `O(K)` space.

Pitfalls:

- K = 1: nobody knows one word (test 02);
- P = 1 makes every answer 0 (test 04);
- reduce each sum modulo P: the exact counts grow beyond fixed-width
  integers, although each sum of two residues fits 32 bits (tests 06, 07);
- g(m) is half of B(2m): for K = 4, the answer is 2, while B(4) = 4
  (test 01);
- Python runs under PyPy: K = 10⁷ takes about 0.8 s with CPython and
  about 0.17 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1537_dp.cpp](1537_dp.cpp) | G++ 13.2 x64 | dp | O(K) | AC | 0.046 s | 9684 KB |
| [1537_dp.go](1537_dp.go) | Go 1.14 x64 | dp | O(K) | AC | 0.109 s | 11700 KB |
| [1537_dp.java](1537_dp.java) | Java 1.8 | dp | O(K) | AC | 0.140 s | 11368 KB |
| [1537_dp.py](1537_dp.py) | PyPy 3.10 x64 | dp | O(K) | AC | 0.203 s | 20812 KB |
| [1537_dp.rs](1537_dp.rs) | Rust 1.75 x64 | dp | O(K) | AC | 0.046 s | 9836 KB |
