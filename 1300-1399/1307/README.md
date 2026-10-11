# 1307. Archiver

[Timus 1307](https://acm.timus.ru/problem.aspx?space=1&num=1307) · difficulty 1293 · strings

Original problem: idea by Leonid Volkov, prepared by Pavel Egorov and Leonid Volkov, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The input is a piece of English literature, 20 000 to 200 000
characters long. Print an "archive" of it: a program in Pascal, C or
C++, whose first line is `{PAS}`, `/*C*/` or `//CPP` to name the
language, that prints exactly the original text when compiled and run,
and that is strictly shorter than the text.

Time limit: 1 second. Memory limit: 4 MB.

## Input

The text.

## Output

The archive.

## Checking

Timus compiles the archive and compares what it prints with the text.
Our checker cannot compile C++, so it only accepts archives in the one
layout these solutions print (shown below) and runs that layout itself:
it checks the fixed lines, decodes the strings and the table, and
compares the result with the input. For inputs of at least 20 000
characters it also checks that the archive is shorter. The sample input
is shorter than that, so for it any valid archive is accepted, even a
longer one.

## Examples

### Example 1

Input:

```
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657
```

Output:

```
//CPP
#include <cstdio>
const char *d[] = {
"123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657\n",
0};
int main() {
    const char *t[256] = {0};
    for (int k = 0; d[k]; k++)
        for (const char *p = d[k]; *p; p++)
            if (t[(unsigned char)*p]) fputs(t[(unsigned char)*p], stdout);
            else putchar(*p);
    return 0;
}
```

## Solution

The archive is a small C++ program around the text, stored in string
literals, and it has to save more than the program costs (a few
hundred characters plus a line per code).

English is full of the same short pieces: " the ", "and", "th", "e "
and so on. A literary text, on the other hand, never uses many of the
printable characters, such as `#`, `$`, `@` or `~`. So the encoder walks
through a fixed list of common pieces, newline first. Each piece whose
uses would save more than the table line it costs gets the next unused
printable character, and every use of the piece in the text is
replaced by that character. Pieces are plain text and codes are never
letters or spaces, so later pieces never match inside earlier codes,
and decoding is a single pass with no nesting.

The archive then holds:

- the coded text in string literals of 1000 characters each, so no
  compiler limit on literal length is reached;
- a table `t[code] = "piece";` for the codes in use;
- a loop that prints `t[c]` for a code and `c` itself otherwise.

`"`, `\` and `?` are escaped in the literals (the last one so that no
`??` trigraph can appear), and newlines are written as `\n` when they
have no code. Carriage returns are dropped from the input: the archive
prints `\n`, and the judge's text mode turns it back into a line end.

On our English-like test texts the archive is about 55–60 % of the
input. `O(P · L)` for P pieces and a text of length L, with only the text
and the output in memory.

Pitfalls:

- 4 MB is not much: building a string object per character (an easy
  way to escape the text) would not fit, so the text is coded in place
  and written out chunk by chunk;
- the archives were compiled with g++ and run, and they reproduced the
  test texts exactly, backslashes and question marks included.

## Language notes

- All five languages print byte-for-byte the same archive, and its
  first line is `//CPP` whatever language the encoder is in.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1307_strings.cpp](1307_strings.cpp) | G++ 13.2 x64 | strings | O(P * L) | AC | 0.062 s | 368 KB |
| [1307_strings.go](1307_strings.go) | Go 1.14 x64 | strings | O(P * L) | AC | 0.062 s | 1724 KB |
| [1307_strings.java](1307_strings.java) | Java 1.8 | strings | O(P * L) | AC | 0.140 s | 1072 KB |
| [1307_strings.py](1307_strings.py) | Python 3.12 x64 | strings | O(P * L) | AC | 0.046 s | 928 KB |
| [1307_strings.rs](1307_strings.rs) | Rust 1.75 x64 | strings | O(P * L) | AC | 0.031 s | 736 KB |
