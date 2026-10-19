# 2061. Counting rich binary words

[Timus 2061](https://acm.timus.ru/problem.aspx?space=1&num=2061) · difficulty 3176 · strings, bruteforce

Original problem by Mikhail Rubinchik, from the Palindromic Contest of July 11, 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A word of length n is rich when it contains exactly n distinct nonempty
palindromes as substrings. For every length i from 1 to n, count the
rich words of length i over a two-letter alphabet. The limits are 1
second and 64 MB.

## Input

One integer n, 1 ≤ n ≤ 61.

## Output

n lines: the number of rich binary words of length 1, 2, …, n.

## Checking

Outputs are compared token by token.

## Examples

### Example 1

Input:

```
4
```

Output:

```
2
4
8
16
```

## Solution

The input has only 61 possible values, and the counts grow to about
3·10¹², far too many words to list in a second. So the counts are
computed once, offline, and the programs print the first n of them
from a table. The interesting part is how the table is computed.

Appending a letter to a word adds at most one new distinct palindrome:
any new palindrome is a suffix, and if two suffixes `U` and `V`,
`|U| > |V|`, were new, then `V`, a palindromic suffix of the palindrome
`U`, would also be its prefix and so would already occur earlier. A
word of length L therefore has at most L distinct palindromes, and it
has exactly L of them only if each of its letters added a new one. So
every prefix of a rich word is rich, and the rich words form a tree in
which each word is a rich word plus one letter.

A depth-first search walks this tree. It keeps an eertree of the
current word: one node per distinct palindrome, a suffix link to its
longest proper palindromic suffix, and transitions `c: P → cPc`. To
try a letter c, follow suffix links from the longest palindromic suffix
until the letter before it equals c; the result plus c on both sides is
the new longest palindromic suffix. If that node already exists, the
word with c is not rich and the branch is cut; otherwise the node is
created, the search goes deeper, and on return the node and the
transition are removed again. Every step costs O(L) at most, the depth
is at most 61, and memory stays tiny.

Swapping the two letters maps rich words to rich words, so the search
starts with the letter 0 and doubles every count. The words of length
20 with first letter 0 split the work into independent parts for
several threads. The whole search visits about 10¹³ words and takes
about an hour and a half on 22 threads. Its results agree with the
sequence A216264 of the OEIS for every length up to 60.
[2061_strings_bruteforce_table.py](2061_strings_bruteforce_table.py) is the
same search in Python: far too slow for all 61 lengths, it checks the
first ones in seconds.

The example: all 16 words of length 4 are rich; the first poor words
appear at length 8, for instance 00101100.

## Language notes

The largest count, 2 966 632 985 826, needs 64-bit integers. Each
program keeps the table as a constant and prints its first n entries.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2061_strings_bruteforce.cpp](2061_strings_bruteforce.cpp) | G++ 13.2 x64 | strings, bruteforce | O(n) | AC | 0.001 s | 132 KB |
| [2061_strings_bruteforce.go](2061_strings_bruteforce.go) | Go 1.14 x64 | strings, bruteforce | O(n) | AC | 0.001 s | 1048 KB |
| [2061_strings_bruteforce.java](2061_strings_bruteforce.java) | Java 1.8 | strings, bruteforce | O(n) | AC | 0.046 s | 1524 KB |
| [2061_strings_bruteforce.py](2061_strings_bruteforce.py) | Python 3.12 x64 | strings, bruteforce | O(n) | AC | 0.046 s | 400 KB |
| [2061_strings_bruteforce.rs](2061_strings_bruteforce.rs) | Rust 1.75 x64 | strings, bruteforce | O(n) | AC | 0.015 s | 208 KB |
