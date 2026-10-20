# 2217. Reaching a palindrome by sorting substrings of a binary string

[Timus 2217](https://acm.timus.ru/problem.aspx?space=1&num=2217) · difficulty 1109 · prefix_sums

Original problem by Timofey Imaev, from the ICPC Ural Regional Contest qualifier 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A binary string S of length N may have any of its substrings sorted
into non-decreasing order, any number of times. Can it become a
palindrome? The limits are 1 second and 256 MB.

## Input

N, 1 ≤ N ≤ 10⁵, then S.

## Output

YES or NO.

## Examples

### Example 1

Input:

```
12
010110110100
```

Output:

```
YES
```

### Example 2

Input:

```
1
1
```

Output:

```
YES
```

### Example 3

Input:

```
2
10
```

Output:

```
NO
```

## Solution

Sorting a substring only moves zeros to the left, and it can be done
one adjacent swap "10" → "01" at a time. So a string T with the same
counts is reachable exactly when every prefix of T has at least as many
zeros as the same prefix of S.

A palindrome has as many zeros in its first k characters as in its last
k. For a reachable palindrome P, the first k characters of P hold at
least as many zeros as those of S, and the last k at most as many as
those of S, since zeros only leave the end. So for every k up to N / 2:

zeros in the last k characters of S ≥ zeros in the first k characters.

Also, for even N the zeros pair up, so their count must be even; for
odd N the middle character takes care of the parity. These two
conditions are also sufficient: the palindrome that pushes zeros as far
left as the pairing allows is then reachable, which was confirmed
exhaustively for every string up to length 12.

One scan from both ends keeps the running difference of the two zero
counts and fails when it turns negative.

In the third example "10" has one zero, an odd count on an even length,
so the answer is NO.

This takes O(N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2217_prefix_sums.cpp](2217_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 436 KB |
| [2217_prefix_sums.go](2217_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 1552 KB |
| [2217_prefix_sums.java](2217_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 996 KB |
| [2217_prefix_sums.py](2217_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.093 s | 388 KB |
| [2217_prefix_sums.rs](2217_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.031 s | 244 KB |
