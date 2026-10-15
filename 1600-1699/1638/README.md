# 1638. Bookworm

[Timus 1638](https://acm.timus.ru/problem.aspx?space=1&num=1638) · difficulty 66 · math

Original problem by Alex Samsonov, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A hundred volumes stand on a shelf in increasing order from left to
right, tightly packed. Each volume has pages of a given total thickness
and two covers of a given thickness. A worm starts at the first page of
one volume and gnaws straight through until it reaches the last page of
another volume. How long is its path?

## Input

Four positive integers up to 100: the thickness of the pages of a
volume, the thickness of a cover, the volume where the worm starts and
the volume where it stops.

## Output

The length of the path.

## Examples

### Example 1

Input:

```
10 1 1 2
```

Output:

```
2
```

## Solution

The trick is where the pages lie. A book standing on a shelf with its
spine outwards has its first page on the right and its last page on the
left, so the first page of volume a touches the cover facing volume
a + 1, and the last page of volume b touches the cover facing volume
b − 1. With w = pages + 2 · covers for a whole volume:

- a < b: only the right cover of a, the volumes in between and the left
  cover of b: 2 · cover + (b − a − 1) · w; the example gives 2;
- a > b: the worm also crosses all pages of both volumes:
  2 · pages + 2 · cover + (a − b − 1) · w;
- a = b: just the pages of that volume.

`O(1)`.

Pitfalls:

- the intuitive answer for volumes 1 and 2 is a whole book or two, but
  the worm passes only the two covers (the example);
- the reverse direction is much longer (test 02).

The answers match an independent accepted implementation on 200 random
tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1638_math.cpp](1638_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1638_math.go](1638_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1060 KB |
| [1638_math.java](1638_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1616 KB |
| [1638_math.py](1638_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 364 KB |
| [1638_math.rs](1638_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 236 KB |
