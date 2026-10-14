# 1601. AntiCAPS

[Timus 1601](https://acm.timus.ru/problem.aspx?space=1&num=1601) · difficulty 91 · implementation

Original problem by Denis Musin, from the Ninth Ural State University Open Personal Contest, March 1, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Angela writes chat messages in capital letters. Fix a message of up to
10000 characters: sentences end with `.`, `!` or `?`, the first letter
of each sentence stays capital and every other letter becomes small.
Spaces, line breaks and the marks `,`, `-`, `:` stay as they are.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The message.

## Output

The fixed message.

## Examples

### Example 1

Input:

```
HI THERE!
HOW DID YOU KNOW I AM A BLONDE?
```

Output:

```
Hi there!
How did you know i am a blonde?
```

## Solution

Walk through the message once, remembering whether the next letter opens
a sentence. It does at the start and after every `.`, `!` or `?`; the
first letter after that keeps its capital, and every other letter is
turned into a small one. Everything else is copied unchanged, line
breaks included, so the message is processed as raw bytes: `O(n)`. The
results were compared byte for byte with an independent implementation
on generated messages.

Pitfalls:

- a sentence may continue over several lines, so a line break does not
  start a new sentence (test 04);
- commas, dashes and colons do not end a sentence (test 02);
- a mark can sit right before a letter with no space (test 03), and a
  run such as `?!` ends one sentence, not two.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1601_implementation.cpp](1601_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 88 KB |
| [1601_implementation.go](1601_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 936 KB |
| [1601_implementation.java](1601_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 432 KB |
| [1601_implementation.py](1601_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 436 KB |
| [1601_implementation.rs](1601_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 236 KB |
