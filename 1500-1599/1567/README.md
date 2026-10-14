# 1567. SMS-spam

[Timus 1567](https://acm.timus.ru/problem.aspx?space=1&num=1567) · difficulty 41 · implementation

Original problem by Denis Musin, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Petya types a slogan of at most 1000 characters on a phone without
predictive input and charges one rouble per key press. A character
costs as many presses as its place on its key:

| key | characters |
|-----|------------|
| 1 | a b c |
| 2 | d e f |
| 3 | g h i |
| 4 | j k l |
| 5 | m n o |
| 6 | p q r |
| 7 | s t u |
| 8 | v w x |
| 9 | y z |
| 0 | . , ! |
| # | space |

The slogan holds lowercase words, spaces, commas, points and
exclamation marks. Print its price.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The slogan on one line.

## Output

The number of presses.

## Examples

### Example 1

Input:

```
pokupaite gvozdi tolko v kompanii gvozdederov i tovarischi!
```

Output:

```
114
```

## Solution

A table maps every character to its place on its key, counted from 1,
and the answer is the sum over the line. The line is read whole, since
spaces cost a press too. `O(n)`.

Pitfalls:

- the key 9 holds only y and z, so z costs 2 (test 03);
- the space is a character of its own on the key #, one press each,
  also when two spaces stand together (test 05);
- reading word by word loses the spaces.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1567_implementation.cpp](1567_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 376 KB |
| [1567_implementation.go](1567_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1048 KB |
| [1567_implementation.java](1567_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 424 KB |
| [1567_implementation.py](1567_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 380 KB |
| [1567_implementation.rs](1567_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 224 KB |
