# 1559. TruCoders Linguistics

[Timus 1559](https://acm.timus.ru/problem.aspx?space=1&num=1559) · difficulty 4082 · parsing

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A language is given by an expression of at most 10000 characters built
from lowercase letters (one word of one letter), 0 (the empty set),
brackets, concatenation, union `|` and star `*` (any number of
repetitions, including none, which gives the empty word). Three people
can learn at most 10¹⁰⁰⁰⁰⁰ words each. Print F if they can learn the
whole language together and N otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

One line with the expression.

## Output

F or N.

## Examples

### Example 1

Input:

```
((a|b)(c|d))
```

Output:

```
F
```

## Solution

The answer is N exactly when the language is infinite. A finite language
from an expression of length L has at most 2^L words: a letter or 0 has
at most 1, a union adds sizes, a concatenation multiplies them, and a
star over a finite language with no non-empty word gives just the empty
word, so each character at most doubles the bound. And 2^10000 is about
10³⁰¹¹, far below 3·10¹⁰⁰⁰⁰⁰.

For every subexpression it is enough to know four things: is the set
non-empty, does it hold the empty word, does it hold a non-empty word,
and is it infinite. A union joins them with "or". A concatenation is
empty if either part is empty, and otherwise holds the empty word if
both parts do, a non-empty word if either does, and is infinite if
either is. A star is never empty, always holds the empty word, and is
infinite exactly when its argument holds a non-empty word.

Brackets may nest about 5000 deep, so the expression is read with an
explicit stack instead of recursion. Each level of brackets keeps the
union so far, the concatenation so far and its last symbol, which a
following star still applies to. This takes O(L) time. The results
were checked against a brute force that lists the words up to a fixed
length on random expressions.

Pitfalls:

- a star does not always give infinitely many words: 0* and (0|(0)*)* are
  just the empty word (tests 03, 05);
- an empty factor empties a whole concatenation, star and all: a*0 has
  no words (test 04);
- the limit 10¹⁰⁰⁰⁰⁰ only looks like a number to compare with: even
  2000 choices of two letters give only 2^2000 words (test gen7);
- recursion over 5000 nested brackets may overflow the stack (test gen1).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1559_parsing.cpp](1559_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 520 KB |
| [1559_parsing.go](1559_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.046 s | 1308 KB |
| [1559_parsing.java](1559_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.125 s | 680 KB |
| [1559_parsing.py](1559_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.093 s | 1152 KB |
| [1559_parsing.rs](1559_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.046 s | 380 KB |
