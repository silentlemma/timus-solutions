# 1654. Cipher Message

[Timus 1654](https://acm.timus.ru/problem.aspx?space=1&num=1654) · difficulty 60 · implementation

Original problem by Vladimir Yakovlev (idea by Alexander Klepinin), from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text without two equal neighbouring letters was encrypted by inserting,
many times, a pair of equal letters anywhere. Remove all inserted pairs
and print the original text.

## Input

One line of up to 200000 lowercase Latin letters.

## Output

The restored text (possibly empty).

## Examples

### Example 1

Input:

```
wwstdaadierfflitzzz
```

Output:

```
stierlitz
```

## Solution

Removing a pair of equal neighbours is like cancelling x · x = 1 in a
group where every letter is its own inverse, and such reductions always
end in the same text whatever order they take. The original text has no
equal neighbours, so it is exactly that reduced form.

A stack computes it in one pass: a letter equal to the top of the stack
cancels it, any other letter is pushed. `O(n)`.

Pitfalls:

- removing pairs can bring new equal letters together (`abba` vanishes
  completely, test 04), so a single left-to-right pass without a stack is
  not enough;
- three equal letters leave one (test 06);
- the answer may be an empty line (tests 02, 04).

The answers match an independent accepted implementation on 60 random
tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1654_implementation.cpp](1654_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 988 KB |
| [1654_implementation.go](1654_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 3072 KB |
| [1654_implementation.java](1654_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 3828 KB |
| [1654_implementation.py](1654_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 1424 KB |
| [1654_implementation.rs](1654_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 936 KB |
