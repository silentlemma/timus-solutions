# 1761. Binary Palindrome

[Timus 1761](https://acm.timus.ru/problem.aspx?space=1&num=1761) · difficulty 1094 · strings

Original problem by Ilya Zvigintsev, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Write the numbers 1 to n in binary one after another. Find the length
of the longest palindrome in the resulting string of zeros and ones.

## Input

n in binary (1 ≤ n ≤ 2¹⁰⁰⁰⁰⁰⁰), so up to a million and one digits.

## Output

The length of the longest palindrome.

## Examples

### Example 1

Input:

```
101
```

Output:

```
5
```

### Example 2

Input:

```
10100
```

Output:

```
11
```

## Solution

Let n have k binary digits. Three numbers of k digits in a row give a
palindrome: 2^(k−1) + 5 = 1 0…0 101, then 2^(k−1) + 6 = 1 0…0 110, then
the first k − 2 digits of 2^(k−1) + 7 = 1 0…0 111, that is 1 0…0 1,
where each 0…0 has k − 4 zeros. Written out, 1 0…0 1011 0…0 1101 0…0 1
reads the same both ways and has 3k − 2 digits. It is present once n
reaches 2^(k−1) + 7, which holds when a one follows the leading digit
anywhere before the last three, or when those three are all ones.
Otherwise the same pattern one length lower gives 3(k − 1) − 2.

That nothing longer appears is checked rather than proved here: the
longest palindrome, found with Manacher's algorithm on the whole
string, matches the formula for every n up to 300 and, since adding
numbers can only make it longer, at both ends of every range of n with
one answer for every k from 6 to 20. Below 32 the pattern does not yet
hold, and the string is short enough to search directly. Reading the
digits is all the work: `O(k)`.

For n = 39 = 100111 the string ends in 100101 100110 100111, and
1001011001101001 is the palindrome of 16 = 3·6 − 2 digits.

Pitfalls:

- n has up to a million digits, so it is never turned into a number;
- the step from 3k − 5 to 3k − 2 comes at 2^(k−1) + 7, not at 2^(k−1);
- the formula fails below 32, for instance n = 20 gives 11, not 10.

The answers agree with an independent accepted implementation on 60
random inputs, including inputs of a million and one digits right
around 2^(k−1) + 7.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1761_strings.cpp](1761_strings.cpp) | G++ 13.2 x64 | strings | O(k) for k digits | AC | 0.046 s | 156 KB |
| [1761_strings.go](1761_strings.go) | Go 1.14 x64 | strings | O(k) for k digits | AC | 0.031 s | 1080 KB |
| [1761_strings.java](1761_strings.java) | Java 1.8 | strings | O(k) for k digits | AC | 0.125 s | 504 KB |
| [1761_strings.py](1761_strings.py) | Python 3.12 x64 | strings | O(k) for k digits | AC | 0.093 s | 3044 KB |
| [1761_strings.rs](1761_strings.rs) | Rust 1.75 x64 | strings | O(k) for k digits | AC | 0.031 s | 244 KB |
