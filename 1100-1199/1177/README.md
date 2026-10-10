# 1177. Matching strings against SQL like patterns

[Timus 1177](https://acm.timus.ru/problem.aspx?space=1&num=1177) · difficulty 1249 · strings

Original problem by Pavel Atnashev, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Answer up to 1000 questions of the form `'string' like 'pattern'`.
In a pattern, `%` matches any run of characters, `_` any one character,
`[...]` any one character from a set of single characters and ranges
`c1-c2`, and `[^...]` any one character outside such a set; everything
else matches itself. Strings and patterns have up to 100 characters with
codes 32–255, and a quote inside them is written twice.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines `'string' like 'pattern'`.

## Output

`YES` or `NO` for each line.

## Examples

### Example 1

Input:

```
15
'abcde' like 'a'
'abcde' like 'a%'
'abcde' like '%a'
'abcde' like 'b'
'abcde' like 'b%'
'abcde' like '%b'
'25%' like '_5[%]'
'_52' like '[_]5%'
'ab' like 'a[a-cdf]'
'ad' like 'a[a-cdf]'
'ab' like 'a[-acdf]'
'a-' like 'a[-acdf]'
'[]' like '[[]]'
'''''' like '_'''
'U' like '[^a-zA-Z0-9]'
```

Output:

```
NO
YES
NO
NO
NO
NO
YES
YES
YES
YES
NO
YES
YES
YES
NO
```

## Solution

Read each line as bytes and undo the doubled quotes in both parts. Then
walk through the pattern element by element, keeping the set of lengths
`i` such that the pattern so far can match exactly the first `i` bytes of
the string:

- a byte or `_` moves every `i` to `i + 1` if the next byte fits;
- a set does the same with its membership test;
- `%` keeps every length from the smallest one in the set onwards.

The answer is whether the full length is in the set at the end.
`O(n·m)` per question.

The set syntax needs care. After `[` an optional `^` negates; then come
items up to the first `]`. An item `a-b` is a range when there is a third
character and it is not `]`, otherwise `a` and `-` are separate
characters, so `[-acdf]` and `[a-]` contain a dash, and `[[]` is a set
with `[` alone. A `[` with no closing `]` matches nothing.

Pitfalls:

- characters above 127 are single bytes, so they must be compared and put
  in ranges as unsigned bytes, not decoded as text;
- an empty pattern matches only the empty string, and `%` matches it too;
- a range whose ends are reversed, like `[c-a]`, is empty.

The answers were compared with a separately written solution on 60,000
random questions with quotes, brackets, `^`, `-`, high bytes and unclosed
sets.

## Language notes

- Python keeps the set of lengths as a big-integer bitmask with one mask
  per byte of the string; the other languages use a boolean array per
  step. Java reads the input as Latin-1, so that every byte becomes the
  character with the same code.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1177_strings.cpp](1177_strings.cpp) | G++ 13.2 x64 | strings | O(n·m) per question | AC | 0.031 s | 372 KB |
| [1177_strings.go](1177_strings.go) | Go 1.14 x64 | strings | O(n·m) per question | AC | 0.015 s | 5424 KB |
| [1177_strings.java](1177_strings.java) | Java 1.8 | strings | O(n·m) per question | AC | 0.093 s | 5036 KB |
| [1177_strings.py](1177_strings.py) | Python 3.12 x64 | strings | O(n·m) per question | AC | 0.203 s | 1132 KB |
| [1177_strings.rs](1177_strings.rs) | Rust 1.75 x64 | strings | O(n·m) per question | AC | 0.015 s | 736 KB |
