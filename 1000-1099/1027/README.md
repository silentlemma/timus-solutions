# 1027. Checking brackets and comments in a toy language

[Timus 1027](https://acm.timus.ru/problem.aspx?space=1&num=1027) · difficulty 637 · parsing

Original problem by Leonid Volkov and Alexey Lysenko, from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text of at most 10 000 characters is a correct program if it splits into
plain text, comments and arithmetic expressions as follows:

- a **comment** starts with `(*` and ends with the next `*)`; it may contain
  anything and may appear anywhere, also inside an expression; it must be
  closed;
- an **arithmetic expression** starts with `(` (not followed by `*`) and ends
  with the matching `)`; between them only the characters `=+-*/0123456789`,
  brackets and line breaks are allowed (no spaces), and the brackets must be
  balanced;
- the remaining **plain text** may contain any characters except `(` and
  `)`.

Print `YES` if the text is a correct program and `NO` otherwise.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The text: Latin letters, digits, brackets, arithmetic signs, spaces and line
breaks.

## Output

`YES` or `NO`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
Program text (1+2) more words (* a comment ) with a bracket *) end
```

Output:

```
YES
```

### Example 2

Input:

```
just a) bracket
```

Output:

```
NO
```

## Solution

One left-to-right pass with a single counter `depth` — the nesting level of
the arithmetic expression we are in (0 in plain text).

- At `(*` a comment starts, wherever we are: find the first `*)` **after**
  the opening pair and jump past it; if there is none, the answer is `NO`.
  Comments do not change `depth`.
- `(` opens a bracket: `depth + 1`.
- `)` closes one: if `depth` is 0, the bracket is in plain text — `NO`;
  otherwise `depth - 1`.
- Any other character is fine in plain text; inside an expression
  (`depth > 0`) it must be one of `=+-*/0123456789` or a line break.

At the end `depth` must be 0. `O(length)`.

Pitfalls:

- `(*)` is **not** a closed comment: the search for `*)` starts after `(*`;
- comments do not nest: in `(* (*) *)` the comment ends at the first `*)`
  and the last `)` is a stray bracket;
- `(*` always starts a comment, so an expression can never begin with `*`
  right after its bracket — but `((*c*)*1)` is fine: the comment sits
  between `(` and `*`;
- a space inside an expression makes the program wrong; a line break does
  not;
- on Windows the line breaks may be `\r\n`: treat `\r` like `\n`.

## Language notes

The same scan in every language; the text is read as raw bytes or as a
whole string.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1027_parsing.cpp](1027_parsing.cpp) | G++ 13.2 x64 | parsing | O(length) | AC | 0.015 s | 160 KB |
| [1027_parsing.go](1027_parsing.go) | Go 1.14 x64 | parsing | O(length) | AC | 0.031 s | 1080 KB |
| [1027_parsing.java](1027_parsing.java) | Java 1.8 | parsing | O(length) | AC | 0.093 s | 452 KB |
| [1027_parsing.py](1027_parsing.py) | Python 3.12 x64 | parsing | O(length) | AC | 0.093 s | 408 KB |
| [1027_parsing.rs](1027_parsing.rs) | Rust 1.75 x64 | parsing | O(length) | AC | 0.015 s | 232 KB |
