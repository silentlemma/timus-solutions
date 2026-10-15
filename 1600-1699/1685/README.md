# 1685. Orthography

[Timus 1685](https://acm.timus.ru/problem.aspx?space=1&num=1685) · difficulty 184 · strings

Original problem by Eugene Krokhalev, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text is encoded by writing its middle character (number (1 + n) div 2
of n), then encoding the part to its left, then the part to its right.
Given the encoded line, restore the text.

## Input

One line of at most 20000 characters: Latin letters, spaces and
punctuation.

## Output

The original text.

## Examples

### Example 1

Input:

```
kyaVs alisse uop.
```

Output:

```
Vasya likes soup.
```

### Example 2

Input:

```
gtorhoprahy
```

Output:

```
orthography
```

## Solution

The encoding visits the positions of the text in a fixed order: the
middle of a range, then the left range, then the right one. That order
depends only on n, so replay it and put the i-th encoded character at
the i-th visited position. With 0-based ranges lo..hi the middle is
(lo + hi) div 2. An explicit stack replaces the recursion, though its
depth is only about log n. `O(n)`.

Pitfalls:

- the line may begin or end with spaces, which are characters of the
  text: strip only the line break;
- the text may hold several spaces in a row (test 05).

The answers match an independent accepted implementation and decode
the encoder's output back to random texts.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1685_strings.cpp](1685_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 388 KB |
| [1685_strings.go](1685_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1228 KB |
| [1685_strings.java](1685_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1672 KB |
| [1685_strings.py](1685_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 536 KB |
| [1685_strings.rs](1685_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.062 s | 248 KB |
