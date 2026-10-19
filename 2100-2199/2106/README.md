# 2106. Decoding nested structures from a hex byte stream

[Timus 2106](https://acm.timus.ru/problem.aspx?space=1&num=2106) · difficulty 1068 · parsing

Original problem by Mikhail Vyatskov, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A binary protocol knows n structure types. A field is an int (4 bytes,
big-endian, unsigned), a string (its length as an int, then one byte per
lowercase letter) or a structure described earlier, whose fields follow
in order. The stream is a sequence of records: the 1-based number of a
structure type as an int, then that structure. Print the records as an
indented tree. The limits are 2 seconds and 64 MB.

## Input

n and l, 1 ≤ n ≤ 240, 2n ≤ l ≤ 10³, then l description lines: "struct
name" starts a type and each following line holds one field type after
a space. The last line is the stream as uppercase hex, at most 10⁴
digits.

Structure names are distinct, contain 1–10 lowercase Latin letters, and
cannot be "int", "string" or "struct". Each structure has at least one field.

## Output

For each record its type name, then the fields one per line, indented by
one space more than the owner: "int value", "string text", or the name
of a nested structure followed by its own fields.
The output is guaranteed not to exceed 30 KB.

## Examples

### Example 1

Input:

```
2 5
struct a
 string
struct b
 a
 int
000000020000000361626300000004000000010000000568656C6C6F
```

Output:

```
b
 a
  string abc
 int 4
a
 string hello
```

## Solution

Read the descriptions into a table of field types per structure and
decode the hex line into bytes. Then walk the stream with an explicit
stack of (structure, next field) pairs instead of recursion, since
structures can nest about 240 levels deep. At every step take the next
field of the top structure: an int prints one number, a string reads its
length and then that many bytes, and a structure prints its name and is
pushed. The indent of a line is the stack depth. A structure with all
fields done is popped, and an empty stack starts the next record.

Every byte is read once and every printed line costs its length, so the
work is linear in the input and the output.

In the example the stream holds 2 (type b), then the string "abc" of the
inner a, then 4, then record 1 (type a) with "hello".

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2106_parsing.cpp](2106_parsing.cpp) | G++ 13.2 x64 | parsing | O(L + output) | AC | 0.015 s | 528 KB |
| [2106_parsing.go](2106_parsing.go) | Go 1.14 x64 | parsing | O(L + output) | AC | 0.031 s | 1364 KB |
| [2106_parsing.java](2106_parsing.java) | Java 1.8 | parsing | O(L + output) | AC | 0.093 s | 1076 KB |
| [2106_parsing.py](2106_parsing.py) | Python 3.12 x64 | parsing | O(L + output) | AC | 0.078 s | 828 KB |
| [2106_parsing.rs](2106_parsing.rs) | Rust 1.75 x64 | parsing | O(L + output) | AC | 0.046 s | 476 KB |
