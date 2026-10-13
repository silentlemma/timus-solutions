# 1354. Palindrome. Again Palindrome

[Timus 1354](https://acm.timus.ru/problem.aspx?space=1&num=1354) · difficulty 139 · strings

Original problem by Denis Nazarov, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a word S1 of up to 10 000 Latin letters, find the shortest
non-empty word S2 such that S1S2 is a palindrome, and print S1S2.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The word S1 on one line.

## Output

The word S1S2.

## Examples

### Example 1

Input:

```
No
```

Output:

```
NoN
```

### Example 2

Input:

```
OnLine
```

Output:

```
OnLineniLnO
```

### Example 3

Input:

```
AbabaAab
```

Output:

```
AbabaAababA
```

## Solution

If S1S2 is a palindrome and S2 is no longer than S1, then S2 is the
reverse of some prefix of S1, and the rest of S1 after that prefix must
itself be a palindrome. So the shortest S2 comes from the longest
palindromic suffix of S1 that starts at position 1 or later: S2 has to
be non-empty, so S1 itself never counts, even if it is a palindrome.

A suffix X of the tail T = S1 without its first letter is a palindrome
exactly when X is also a prefix of reverse(T). Running the prefix
function over reverse(T) + `#` + T, its last value is the length L of
the longest such suffix, and the answer is S1 followed by the first
|S1| − L letters of S1 reversed. `O(|S1|)`.

Pitfalls:

- a palindrome still needs a letter: `abcba` gives `abcbabcba`
  (test 05);
- one letter is doubled, since the empty tail counts as a palindrome
  (test 04);
- upper and lower case are different letters (tests 03 and 07);
- checking every suffix directly can take 10⁸ steps on long runs of one
  letter (generated test 4).

The answers were compared with trying every prefix length directly on
300 random words of up to 12 letters, and the generated tests were
checked for being palindromes with no shorter addition.

## Language notes

- All five solutions use the same prefix function on bytes or
  characters.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1354_strings.cpp](1354_strings.cpp) | G++ 13.2 x64 | strings | O(len(S1)) | AC | 0.015 s | 396 KB |
| [1354_strings.go](1354_strings.go) | Go 1.14 x64 | strings | O(len(S1)) | AC | 0.031 s | 1540 KB |
| [1354_strings.java](1354_strings.java) | Java 1.8 | strings | O(len(S1)) | AC | 0.171 s | 960 KB |
| [1354_strings.py](1354_strings.py) | Python 3.12 x64 | strings | O(len(S1)) | AC | 0.109 s | 1216 KB |
| [1354_strings.rs](1354_strings.rs) | Rust 1.75 x64 | strings | O(len(S1)) | AC | 0.031 s | 336 KB |
