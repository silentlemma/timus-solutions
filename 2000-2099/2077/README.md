# 2077. Shortest unique abbreviations with a dot or a hyphen

[Timus 2077](https://acm.timus.ru/problem.aspx?space=1&num=2077) · difficulty 6151 · strings, sorting

Original problem by Mikhail Rubinchik, prepared by Egor Shchelkonogov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every word of a set is written either whole, as a prefix followed by a
dot, or as a prefix and a suffix joined by a hyphen. A word fits such a
reduction if replacing the dot or the hyphen with some (possibly empty)
string gives the word. Each reduction must be fitted by its own word
only. Minimise the total length; then keep as many words whole as
possible; then use as few hyphens as possible; then maximise the total
length of the prefixes before hyphens. The answer is guaranteed to be
unique. The limits are 0.5 seconds and 32 MB.

## Input

n, 1 ≤ n ≤ 10⁶, then n distinct words of lower-case letters in
lexicographic order, with total length at most 10⁶.

## Output

The reductions, one per line, in the input order.

## Examples

### Example 1

Input:

```
4
aba
abaca
add
dd
```

Output:

```
aba
a-ca
add
dd
```

### Example 2

Input:

```
2
aa
aaaaa
```

Output:

```
aa
aaa.
```

### Example 3

Input:

```
2
abc
abcdabc
```

Output:

```
abc
abcd.
```

## Solution

Whether a reduction is fitted by another word does not depend on the
other reductions, so every criterion splits into one choice per word:
the shortest reduction, a whole word on a tie, then a dot rather than a
hyphen, then the longest prefix. The prefixes and suffixes are non-empty
(that is how the judge reads the statement). A word w of length m costs
m whole, a + 1 with a prefix of length a and a dot, and a + b + 1 with a
hyphen between a prefix of length a and a suffix of length b,
a + b ≤ m.

Dot. Since the words are sorted, the words sharing a prefix of w form a
contiguous range around w, and the shortest prefix that no other word
has is one longer than the longer common prefix of w with its two
neighbours.

Hyphen. Another word v fits w[..a]-w[m−b..] when v starts with the first
a letters of w, ends with its last b letters, and is at least a + b
long. The words with the prefix form a range [lo, hi] of the input
order. For the suffixes, the reversed words are sorted and walked with
a stack, which numbers the nodes of the suffix tree and gives the node
of every (word, b); each node keeps the list of its words by increasing
number, M entries in total for total length M. So the pair (a, b) is
unique when, in the list of the node of (w, b), the words with numbers
in [lo, hi] other than w are all shorter than a + b. Binary search finds
that part of the list, and a range maximum of the lengths (blocks of 32
with a sparse table over the blocks) checks it.

If (a, b) is not unique, neither is (a − 1, b): the prefix range only
grows and the length bound only drops. So a runs from m − 1 down to 1
while b only grows, at most 2m checks per word, each O(log n). The
ranges [lo, hi] for all prefixes come from two passes with stacks over
the sorted words: one stores the last word of every prefix range, the
other keeps the first one while the answers are made. Scanning a
downwards also means the first hyphen of a given cost has the longest
prefix, so only strictly cheaper ones replace it. Everything is
O(M log n), and the arrays take about 25 MB.

In the first example "a-a" would fit "aba" too, so "abaca" becomes
"a-ca", shorter than the whole word or "abac.". In the second example
"a-aa" is unique for "aaaaa", since "aa" is too short to hold both
parts, but "aaa." has the same length and a dot beats a hyphen.

## Language notes

The statement allows only C, C++ and Pascal, but the Timus submit form
also offers Rust 1.75, so there are C++ and Rust solutions; Go, Python
and Java cannot be submitted.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2077_strings_sorting.cpp](2077_strings_sorting.cpp) | G++ 13.2 x64 | strings, sorting | O(M log n) | AC | 0.234 s | 22020 KB |
| [2077_strings_sorting.rs](2077_strings_sorting.rs) | Rust 1.75 x64 | strings, sorting | O(M log n) | AC | 0.250 s | 22312 KB |
