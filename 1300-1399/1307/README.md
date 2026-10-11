# 1307. Archiver

[Timus 1307](https://acm.timus.ru/problem.aspx?space=1&num=1307) · difficulty 1275 · strings

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
characters it also checks that the archive is shorter. For the shorter
sample, only the size check is waived.

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

English repeats short pieces such as " the ", "and", "th", "e ", as
well as whole words. Literary text usually leaves some printable
characters unused, such as `#`, `$`, `@` or `~`. The encoder ranks common
pieces and up to 300 word variants, with or without a leading space, by
expected saving. A piece gets the next unused printable character if
replacing its non-overlapping uses saves more than a conservative
estimate of its table-line cost.

Candidates use only characters present in the text, while codes are
absent from it, so later replacements cannot consume earlier codes and
decoding is a single pass with no nesting.

The archive then holds:

- the coded text in string literals of at most 1000 coded characters
  each, so no compiler limit on literal length is reached;
- a table `t[code] = "piece";` for the codes in use;
- a loop that prints `t[c]` for a code and `c` itself otherwise.

`"`, `\` and `?` are escaped in the literals (the last one so that no
`??` trigraph can appear), and newlines are written as `\n` when they
have no code. Carriage returns are dropped from the input, converting
CRLF to LF.

On our non-sample test texts the archive is about 26.3–61.3 % of the input.

Pitfalls:

- 4 MB is not much: a string object per character can exceed it. C++, Go,
  Java and Rust code the text in place; Python replaces strings. All five
  write the output chunk by chunk;
- the archives were compiled with g++ and run, and they reproduced the
  test texts exactly, backslashes and question marks included.

## Language notes

- All five languages print byte-for-byte the same archive, and its
  first line is `//CPP` whatever language the encoder is in.
- The memory limit is 4 MB. Go and Java keep a word as its start alone
  (it runs to the end of its letters) in an array sized by a first
  counting pass, and turn only the 300 chosen words into strings. Go also
  lowers the garbage collector's target; Java sorts with its own heapsort
  and anonymous classes, because pairs as objects, `TimSort`'s buffer and
  the lambda machinery took it past the limit.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1307_strings.cpp](1307_strings.cpp) | G++ 13.2 x64 | strings | O(L * K * (log L + P)) | AC | 0.078 s | 1068 KB |
| [1307_strings.go](1307_strings.go) | Go 1.14 x64 | strings | O(L * K * (log L + P)) | AC | 0.125 s | 2576 KB |
| [1307_strings.java](1307_strings.java) | Java 1.8 | strings | O(L * K * (log L + P)) | AC | 0.281 s | 1516 KB |
| [1307_strings.py](1307_strings.py) | Python 3.12 x64 | strings | O(L * K * (log L + P)) | AC | 0.156 s | 2696 KB |
| [1307_strings.rs](1307_strings.rs) | Rust 1.75 x64 | strings | O(L * K * (log L + P)) | AC | 0.093 s | 2352 KB |
