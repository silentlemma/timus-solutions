# 1327. Fuses

[Timus 1327](https://acm.timus.ru/problem.aspx?space=1&num=1327) · difficulty 47 · math

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A computer loses a fuse on every odd working day: on day 1, then on day
3, on day 5 and so on. Count the fuses lost from day A to day B
inclusive, 1 ≤ A ≤ B ≤ 10 000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A on the first line and B on the second.

## Output

The number of fuses.

## Examples

### Example 1

Input:

```
1
5
```

Output:

```
3
```

### Example 2

Input:

```
100
200
```

Output:

```
50
```

## Solution

Days 1 to x hold ⌊(x + 1) / 2⌋ odd days. The odd days from A to B are
those up to B minus those up to A − 1, which gives
⌊(B + 1) / 2⌋ − ⌊A / 2⌋. `O(1)`.

Pitfalls:

- a range of a single day gives 1 for an odd day and 0 for an even one
  (tests 03 and 04);
- both ends count when they are odd (tests 01 and 07).

## Language notes

- All five solutions use the same formula.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1327_math.cpp](1327_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1327_math.go](1327_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB |
| [1327_math.java](1327_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1624 KB |
| [1327_math.py](1327_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 404 KB |
| [1327_math.rs](1327_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 236 KB |
