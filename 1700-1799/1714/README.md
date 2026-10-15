# 1714. Mnemonics and Palindromes 2

[Timus 1714](https://acm.timus.ru/problem.aspx?space=1&num=1714) · difficulty 3223 · constructive

Original problem by Igor Chevdar, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The complexity of a word is the least number of palindromes it splits
into. Print a word of n letters a and b with the greatest complexity.

## Input

n (1 ≤ n ≤ 1000).

## Output

Such a word. Any of them is accepted.

## Examples

### Example 1

Input:

```
6
```

Output:

```
aababb
```

## Solution

Over two letters, palindromes are easy to find, so a hard word must
avoid long ones. The word used here starts with aabab and repeats the
block bbaaba, then ends with a short tail chosen by n mod 6: nothing,
b, bb, bbaaababb, bbaa or bbaab. Each block adds two palindromes to
the least split. A few short lengths need their own words: ab for 2,
aababbaa for 8 and aababbaabab for 11. Up to 5 letters a prefix of
aabab will do. `O(n)`.

The complexity of these words is ⌊n/3⌋ + 1 for n ≥ 12, one more when
n ≡ 2 (mod 6). The smaller lengths give 1, 2, 2, 2, 2, 3, 3, 4, 4, 4,
5. An exhaustive search over all words confirms that this is the
greatest complexity for every n up to 20. A matching bound for larger
n is not proved here: the words are those of an independent accepted
implementation, and they agree with it for every n from 1 to 1000.

Pitfalls:

- the plain prefix rule fails at n = 2: aa is one palindrome, while ab
  needs two;
- at n = 8 the long tail does not fit yet, and at n = 11 the pattern
  falls one palindrome short, so those lengths keep searched words;
- any word with the greatest complexity is accepted, so the tests use
  a checker that counts the palindromes by dynamic programming.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1714_constructive.cpp](1714_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.031 s | 380 KB |
| [1714_constructive.go](1714_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1112 KB |
| [1714_constructive.java](1714_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.140 s | 1660 KB |
| [1714_constructive.py](1714_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 452 KB |
| [1714_constructive.rs](1714_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.031 s | 224 KB |
