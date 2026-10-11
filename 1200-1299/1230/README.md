# 1230. A program in a toy language that prints itself

[Timus 1230](https://acm.timus.ru/problem.aspx?space=1&num=1230) · difficulty 793 · strings

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Print a program in PIBAS, a small language defined in the statement,
that prints exactly its own text. A PIBAS program is one line of
statements separated by `;`. A statement either assigns a string
expression to a variable named by one capital letter, `V=expression`, or
prints one, `?expression`. An expression joins with `+` variables,
constants in single or double quotes (which cannot contain their own
quote character) and substrings `$(V,start,length)`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

There is no input.

## Output

The PIBAS program.

## Checking

Any program is accepted if it is valid PIBAS and prints exactly its own
text; the reference checker runs it with a small interpreter of the
grammar.

## Examples

There is no input, and any correct program is a valid answer, so the
statement gives no example output.

## Solution

The usual quine idea: keep most of the program in a string `A` and print
it twice, once inside quotes as the value being assigned and once as
code. The difficulty is the quotes. `A` sits between single quotes, so it
cannot contain a single quote, yet the code in it has to print both kinds
of quote. So the program first stores them in variables, `C="'"` and
`B='"'`, and the printing code only refers to `C` and `B`:

```text
C="'";B='"';A=';?"C="+B+C+B+";B="+C+B+C+";A="+C+A+C+A';?"C="+B+C+B+";B="+C+B+C+";A="+C+A+C+A
```

The final statement prints `C="'";B='"';A=` with the quotes taken from
the variables, then `'`, the text of `A`, `'` again and the text of `A`
once more, which is the whole program. Each solution prints this line,
built from its head and the text of `A`. `O(1)`.

Pitfalls:

- a constant may not contain its own quote, so neither kind of quote can
  be written directly inside `A`;
- `?` prints without a line break, so the program must print itself with
  nothing added between its parts.

The checker runs the printed program and compares what it prints with
its text.

## Language notes

- C++ and Rust use raw strings and Go backquotes for the two pieces;
  Python uses a triple-quoted string for the head, and Java escapes the
  double quotes.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1230_strings.cpp](1230_strings.cpp) | G++ 13.2 x64 | strings | O(1) | AC | 0.015 s | 80 KB |
| [1230_strings.go](1230_strings.go) | Go 1.14 x64 | strings | O(1) | AC | 0.001 s | 992 KB |
| [1230_strings.java](1230_strings.java) | Java 1.8 | strings | O(1) | AC | 0.031 s | 188 KB |
| [1230_strings.py](1230_strings.py) | Python 3.12 x64 | strings | O(1) | AC | 0.046 s | 284 KB |
| [1230_strings.rs](1230_strings.rs) | Rust 1.75 x64 | strings | O(1) | AC | 0.001 s | 176 KB |
