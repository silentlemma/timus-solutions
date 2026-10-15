# 1635. Mnemonics and Palindromes

[Timus 1635](https://acm.timus.ru/problem.aspx?space=1&num=1635) · difficulty 201 · dp

Original problem by Igor Chevdar, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Split a string of lowercase letters into the fewest palindromes and
print their number and the pieces in order. Any optimal split is
accepted.

## Input

One non-empty string of lowercase Latin letters, at most 4000 long.

## Output

The least number of palindromes, then the pieces of an optimal split
separated by spaces.

## Examples

### Example 1

Input:

```
pasoib
```

Output:

```
6
p a s o i b
```

### Example 2

Input:

```
zzzqxx
```

Output:

```
3
zzz q xx
```

### Example 3

Input:

```
wasitacatisaw
```

Output:

```
1
wasitacatisaw
```

## Solution

Let dp[j] be the fewest palindromes for the prefix of length j; then
dp[r + 1] = min dp[l] + 1 over the palindromes s[l..r], and remembering
the l of the minimum restores the pieces.

C++, Go, Java and Rust enumerate the palindromes by expanding around
each of the 2n − 1 centres from left to right. That order is safe:
a palindrome s[l..r] has its centre at l or later, while every
palindrome ending at l − 1 has its centre before l, so dp[l] is already
final. `O(n²)` time in the worst case (one repeated letter), `O(n)`
memory.

Python cannot afford eight million palindromes one by one, so it works
with bitsets. The starts j of palindromes s[j..i] come from those for
i − 1: shift them down by one and keep the positions holding s[i], then
add i itself and i − 1 if s[i − 1] = s[i]. Moreover dp changes by at
most one per step (without its last letter, the last piece splits into
its first letter and a palindrome), so dp[i + 1] is dp[i] − 1, dp[i] or
dp[i] + 1. With a bitset of the positions for each dp value, two `and`
operations decide it, and the lowest common bit names the piece.
`O(n² / 64)` word operations.

Pitfalls:

- taking the longest palindrome first is not optimal: abaab needs two
  pieces, a and baab, not aba, a, b (test 06);
- the matrix of all n² palindrome flags is 16 MB as bytes; centre
  expansion needs none of it.

A checker accepts any optimal split; the answers match an independent
accepted implementation in the count on 100 random strings.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1635_dp.cpp](1635_dp.cpp) | G++ 13.2 x64 | dp | O(n²) | AC | 0.015 s | 676 KB |
| [1635_dp.go](1635_dp.go) | Go 1.14 x64 | dp | O(n²) | AC | 0.046 s | 1456 KB |
| [1635_dp.java](1635_dp.java) | Java 1.8 | dp | O(n²) | AC | 0.125 s | 796 KB |
| [1635_dp.py](1635_dp.py) | Python 3.12 x64 | dp | O(n²) | AC | 0.093 s | 2064 KB |
| [1635_dp.rs](1635_dp.rs) | Rust 1.75 x64 | dp | O(n²) | AC | 0.062 s | 304 KB |
