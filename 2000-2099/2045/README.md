# 2045. Prescribing the number of distinct palindromes

[Timus 2045](https://acm.timus.ru/problem.aspx?space=1&num=2045) · difficulty 478 · constructive

Original problem by Mikhail Rubinchik, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each integer `i` from `1` to `n`, construct a word of length `n`
over the lowercase Latin alphabet with exactly `i` different nonempty
palindromic substrings, or report that no such word exists. Substrings
are contiguous. Equal substring values count once even if they occur at
different positions. A palindrome reads the same in both directions.

## Input

One integer `1≤n≤2000`. Time limit: 0.5 seconds; memory limit: 64 MB.

## Output

Print `n` lines in order. Line `i` has the form `i : word` or `i : NO`.
Every printed word must have exactly `n` lowercase letters and exactly
`i` distinct nonempty palindromes.

Any valid word is accepted. The checker verifies the number and order of
lines, the colon, length, alphabet, and actual distinct palindrome count
using a palindromic tree. It accepts `NO` only when `i<min(n,3)`; it
does not compare the word with a fixed construction.

## Checking

A checker verifies the format, the length and the letters of each word
and counts its distinct palindromes with an eertree; `NO` is accepted
only when no word exists. Any valid words are accepted.

## Examples

```
4
```

```
1 : NO
2 : NO
3 : abca
4 : bbca
```

A four-letter word cannot have only one or two different palindromes. In
`abca` the only ones are the letters `a,b,c`. In `bbca` they are
`b,c,a,bb`. These are example choices; the programs may print other
valid words.

## Solution

The first two lengths need separate handling. For `n=1` use `a`. For
`n=2`, one distinct palindrome is impossible and `aa` supplies two: `a`
and `aa`.

For `n≥3`, print `NO` for targets one and two. For every `3≤i≤n`, set
`k=i-3`. Print `k` copies of `a` followed by the first `n-k` characters
of the infinite periodic word `bcdbcdbcd…`.

### Correctness

First, every word of length at least three has at least three distinct
palindromes. If it uses three or more letters, their one-letter
substrings suffice. If it uses only one letter, its first one, two and
three letters give three different palindromes. If it uses exactly two
letters, both singletons occur; either equal adjacent letters give a
third palindrome of length two, or all adjacent letters differ and the
first three letters form a palindrome. For length two the minimum is
two: distinct letters give two singletons, while equal letters give the
singleton and the pair. Thus the impossible targets are precisely
`i<min(n,3)`.

For the construction, `n-k=n-i+3≥3`, so the tail contains all of
`b,c,d`. It has no palindromes of length two or three: adjacent letters
and letters two positions apart differ. Every longer palindrome has a
central palindrome of length two or three, obtained by repeatedly
removing its equal endpoints. Consequently the tail has exactly its
three single-letter palindromes.

The initial run contributes exactly the distinct strings `a,a²,…,a^k`.
For `k=0` it contributes none. A substring crossing the boundary starts
with `a` and ends in `b,c` or `d`, so it cannot be a palindrome. These
two sets are disjoint, and the total is `k+3=i`. The length is
`k+(n-k)=n`. Together with the small cases and the lower bound, this
proves every printed word and every `NO`.

### Complexity

Each word takes `O(n)` construction and output time. There are `n` rows,
so total time is `O(n^2)` and auxiliary space is `O(n)` when rows are
written immediately. For large `n`, `n-2` words of length `n` must be
printed, so the output alone requires `Ω(n^2)` time.

Pitfalls:

- Count distinct strings, not palindrome occurrences or partitions.
- Keep at least three tail characters, including at target `i=n`.
- The tail alphabet must exclude the run letter; a binary alternating
  tail creates longer palindromes.
- Treat `n=1` and `n=2` separately.
- A checker must accept valid words different from the example or the
  production construction.

## Language notes

All five ports build a periodic tail once and write one row at a time.
C++, Go, Python and Rust combine a repeated prefix with a tail prefix.
Java fills one character array per row. Buffered output avoids
per-character writes; no port retains the quadratic complete answer in
memory. CPython 3.12 is selected.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2045_constructive.cpp](2045_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.031 s | 1088 KB |
| [2045_constructive.go](2045_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 5888 KB |
| [2045_constructive.java](2045_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.156 s | 5140 KB |
| [2045_constructive.py](2045_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.203 s | 692 KB |
| [2045_constructive.rs](2045_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 956 KB |
