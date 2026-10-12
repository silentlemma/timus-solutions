# 1345. HTML

[Timus 1345](https://acm.timus.ru/problem.aspx?space=1&num=1345) · difficulty 1389 · parsing

Original problem by Pavel Egorov, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a correct Pascal program of up to 100 000 characters, wrap every
comment, keyword, string and number in `<span class=comment>`,
`<span class=keyword>`, `<span class=string>` or `<span class=number>`
and `</span>`, leaving everything else as it is. Anything inside a
comment belongs to the comment, and anything inside a string to the
string.

- A string is either text between two apostrophes with no apostrophe
  inside, or `#` followed by a nonempty run of digits, as long as possible.
- A number starts and ends with a digit and has only digits and at most
  one point; it is always the longest possible run.
- An identifier starts with a letter or `_` and goes on with letters,
  digits and `_`, also the longest possible run.
- A comment is `{` up to the next `}`, both included, or `//` up to the
  end of the line, without the line break. A comment inside a comment is
  part of the outer one.
- The keywords are 35 identifiers such as `begin`, `end` and
  `implementation`, in any letter case.

The text may contain bytes above 127, and its last line may have no
line break.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The program.

## Output

The program with the tags.

## Examples

### Example 1

Input:

```
Begin
  writeln('Hello world!');
end.
```

Output:

```
<span class=keyword>Begin</span>
  writeln(<span class=string>'Hello world!'</span>);
<span class=keyword>end</span>.
```

## Solution

Read the text left to right and decide by the first character what
starts here: `{` or `//` starts a comment, `'` or `#` with a digit a
string, a digit a number, a letter or `_` an identifier. Each one is
read whole and tagged as needed; any other character is copied. Since
whatever starts first takes everything up to its own end, a `{` inside a
string or a `'` inside a comment needs no special care. An identifier
gets the keyword tag when its lower-case form is in the list, and
reading identifiers whole keeps the digits of `a1` from being taken as
a number. `O(L)` for L characters.

Pitfalls:

- `1..10` is two numbers and a range, and `1.5.3` is the number `1.5`, a
  point and the number `3`: a point counts only with digits after it
  (test 04);
- `'it''s'` is two strings `'it'` and `'s'`, and `#13#10` two strings
  (test 05);
- a `{` comment ends at the first `}`, even with another `{` inside
  (test 03);
- the text is handled as bytes, so letters above 127 pass through
  unchanged (test 06), and a missing final line break stays missing
  (tests 01 and 08);
- Windows line breaks are read as plain line breaks, so a `//` comment
  does not take the carriage return.

## Language notes

- Every solution works on raw bytes; Python reads them as latin-1, which
  maps each byte to one character and back.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1345_parsing.cpp](1345_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 556 KB |
| [1345_parsing.go](1345_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.031 s | 1136 KB |
| [1345_parsing.java](1345_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.093 s | 1140 KB |
| [1345_parsing.py](1345_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 828 KB |
| [1345_parsing.rs](1345_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.062 s | 504 KB |
