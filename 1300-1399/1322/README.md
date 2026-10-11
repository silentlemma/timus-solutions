# 1322. Spy

[Timus 1322](https://acm.timus.ru/problem.aspx?space=1&num=1322) · difficulty 179 · strings

Original problem: idea by Alexander Klepinin, prepared by Alexander Klepinin and Stanislav Vasiliev, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An encoder takes a text of up to 100 000 characters, writes all its
cyclic rotations, sorts them and outputs the last column of the sorted
table together with the number K of the row that holds the original
text. Given K and the last column, recover the text. The characters are
letters and the underscore, ordered as A to Z, then `_`, then a to z.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

The number K on the first line and the last column on the second.

## Output

The original text.

## Examples

### Example 1

Input:

```
3
rdarcaaaabb
```

Output:

```
abracadabra
```

## Solution

This is the inverse of the Burrows–Wheeler transform. The rows that end
with a character c turn into the rows that begin with c when c is moved
from the end to the front, and this keeps their order. The rows that
begin with c are sorted by what follows c, and that is exactly how the
rows ending with c are sorted. So the j-th row ending with c is the
j-th row beginning with c, rotated by one.

Sort the positions of the last column stably by character; call the
result order. Row order[j] then ends with the j-th character of the
sorted column, the one row j begins with, and row order[j] is row j
shifted left by one: the rotation that starts one character later.
Starting from row K and following order n times visits the rotations
starting at the second, third, … character of the text, and the last
character of each is the character just before its start, so the text
comes out in order. The given order of characters is their ASCII order,
so a counting sort over 128 codes does the stable sort in `O(n)` time.
Python uses its built-in stable comparison sort instead, giving
`O(n log n)` worst-case time. All implementations use `O(n)` extra space.

Pitfalls:

- for a periodic text several rows are equal and K may point at any of
  them; all lead to the same text (test 04);
- the capitals come before the underscore and the small letters after
  it (test 05);
- the sort must be stable, or equal characters get mixed up;
- the time limit is 0.25 seconds, so use buffered input and output.

The decoder was checked by encoding 400 random and periodic texts of up
to 12 characters by sorting their rotations directly.

## Language notes

- Python sorts the positions with the built-in stable sort; the other
  languages use a counting sort.
- Python and Rust read the whole input before parsing; Java collects
  lines before tokenizing, while C++ and Go read tokens from buffered input.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1322_strings.cpp](1322_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1036 KB |
| [1322_strings.go](1322_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2624 KB |
| [1322_strings.java](1322_strings.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 3152 KB |
| [1322_strings.py](1322_strings.py) | Python 3.12 x64 | strings | O(n log n) | AC | 0.078 s | 6308 KB |
| [1322_strings.rs](1322_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 1108 KB |
