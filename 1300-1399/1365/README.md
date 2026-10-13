# 1365. Testing Calculator

[Timus 1365](https://acm.timus.ru/problem.aspx?space=1&num=1365) · difficulty 4356 · parsing

Original problem by Alexander Klepinin, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every input line is an expression over the characters `0123456789+*/();`,
at most 50 of them, and the task is to print its value exactly as an old
calculator module of the jury does. All that is known: operations `+`,
`*` and `/` (integer division) are written in prefix form with any number
of arguments, `+3;6;10` is 19; terms written without an operation are
glued, `3;6;9` is 369; brackets are allowed, `(+3;6)(*2;3)` is 96; and a
part of an expression is evaluated the same way wherever it stands. The
rest had to be found by running the module itself. All values on the
way lie between 0 and 10⁹.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Expressions, one per line.

## Output

For the i-th line, `Expression i evaluates to: v` with its value v.

## Examples

### Example 1

Input:

```
(+3;6)(*2;3)
(+3;6)(/3;2)
```

Output:

```
Expression 1 evaluates to: 96
Expression 2 evaluates to: 91
```

## Solution

The module was a Java applet that today's browsers no longer run, so the
rules below are the ones an accepted solution follows:

- a term is a number, an operation sign with its arguments, or a whole
  expression in brackets (a missing `)` is fine);
- terms standing one after another are glued: their decimal forms are
  joined and read as a number again, so leading zeros vanish;
- the arguments of an operation are glued runs of terms separated by `;`;
  `/` divides left to right, and division by zero gives 0;
- outside an operation, at the top of a line or inside brackets, `;`
  glues the value of everything after it to what came before:
  `1;+2;3` is 1 glued to 5, that is 15;
- a missing first term contributes 1 to a glued run;
- `)` ends the run; only an unmatched `)` discards the rest of the line.

A recursive descent with three functions follows these rules: a term, an
operation folding its arguments, and a glued run, which is told whether
it stands inside an operation. Every line is read once: `O(n)` in the
length of the input. The rules were checked against an independent
evaluator on 10 000 random expressions.

Pitfalls:

- the second line of the example: `/3;2` is 1, glued after 9 it gives 91;
- `;` outside an operation glues the whole rest, not just the next term
  (test 05);
- an empty line or `()` gives 1, and `;` alone gives 11: a missing term on
  each side of it (test 03);
- `(0)(5)` is 5 and `0;0` is 0: the glued string is read as a number
  (test 06);
- `/7;0` gives 0 (test 04).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1365_parsing.cpp](1365_parsing.cpp) | G++ 13.2 x64 | parsing | O(n) | AC | 0.015 s | 412 KB |
| [1365_parsing.go](1365_parsing.go) | Go 1.14 x64 | parsing | O(n) | AC | 0.015 s | 1104 KB |
| [1365_parsing.java](1365_parsing.java) | Java 1.8 | parsing | O(n) | AC | 0.093 s | 676 KB |
| [1365_parsing.py](1365_parsing.py) | Python 3.12 x64 | parsing | O(n) | AC | 0.078 s | 692 KB |
| [1365_parsing.rs](1365_parsing.rs) | Rust 1.75 x64 | parsing | O(n) | AC | 0.031 s | 232 KB |
