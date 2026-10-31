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

## Optimized solutions

The optimized C++ solution packs into each entry of `order` the
character its row ends with: the low 7 bits hold the character code,
below 128, and the bits above hold the row, below 100 000 < 2^17, so an
entry fits in 32 bits. Following the rows then reads one array instead
of two, and each character is printed with `putchar` right away instead
of building the text in a string. The column is read with `scanf` into a
static buffer of 100 001 bytes instead of `iostream` and `std::string`:
{1322_strings_optimized.cpp}.

The optimized Java solution packs into each entry of `order` the
character its row ends with: the low 7 bits hold the character code,
below 128, and the bits above hold the row, below 100 000 < 2^17, so an
entry fits in an `int`. Following the rows then reads one array instead
of two, and each character goes straight to a `BufferedOutputStream`
instead of into a `char` array and a `String`. The column is read byte
by byte from 4 KB blocks into a `byte` array of 100 000 entries, instead
of collecting the lines in a `StringBuilder` and copying them into
`char` arrays: {1322_strings_optimized.java}.

The optimized Python solution replaces the built-in `sorted` with a
counting sort over the 128 codes and stores `order` in an `array("I")`
of 32-bit entries instead of a list of Python integers. Each entry also
holds the character its row ends with: the low 7 bits hold the character
code, below 128, and the bits above hold the row, below 100 000 < 2^17,
so an entry fits in 32 bits. The text is built in a `bytearray` instead
of a list of one-character strings. The counting sort is a loop in
Python, slower than `sorted`, so the gain is mostly in memory:
{1322_strings_optimized.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1322_strings_optimized.cpp`: time reduction +0.00%; memory reduction
  +43.24%; base: `1322_strings.cpp`.

- `1322_strings_optimized.java`: time reduction +0.00%; memory reduction
  +70.69%; base: `1322_strings.java`.

- `1322_strings_optimized.py`: time reduction -39.74%; memory reduction
  +84.08%; base: `1322_strings.py`.

## Language notes

- Python sorts the positions with the built-in stable sort; the other
  languages use a counting sort.
- Python and Rust read the whole input before parsing; Java collects
  lines before tokenizing, while C++ and Go read tokens from buffered input.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1322_strings.cpp](1322_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1036 KB | 11284953 |
| [1322_strings.go](1322_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2624 KB | 11284954 |
| [1322_strings.java](1322_strings.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 3152 KB | 11284956 |
| [1322_strings.py](1322_strings.py) | Python 3.12 x64 | strings | O(n log n) | AC | 0.078 s | 6308 KB | 11284955 |
| [1322_strings.rs](1322_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 1108 KB | 11284957 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1322_strings_optimized.cpp](1322_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.001 s | 588 KB | 11307290 |
| [1322_strings_optimized.java](1322_strings_optimized.java) \* | Java 1.8 | strings | O(n) | AC | 0.093 s | 924 KB | 11307302 |
| [1322_strings_optimized.py](1322_strings_optimized.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.109 s | 1004 KB | 11307297 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
