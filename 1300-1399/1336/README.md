# 1336. Problem of Ben Betsalel

[Timus 1336](https://acm.timus.ru/problem.aspx?space=1&num=1336) · difficulty 123 · math

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Write a whole number n, 1 ≤ n ≤ 10⁹, as the ratio of a square to a cube:
find whole numbers m and k from 1 to 10¹⁰⁰ with m² = k³ · n. Any such
pair is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number n.

## Output

m on the first line and k on the second.

## Checking

The checker accepts any m and k from 1 to 10¹⁰⁰ with m² = k³ · n.

## Examples

### Example 1

Input:

```
18
```

Output:

```
12
2
```

### Example 2

Input:

```
1
```

Output:

```
1
1
```

## Solution

Take k = n and m = n². Then m² = n⁴ = n³ · n. So a pair always exists,
which is also why the problem always has a solution. `O(1)`.

Pitfalls:

- m reaches 10¹⁸, which needs a 64-bit integer (test 03);
- the samples show smaller pairs; any correct one is accepted.

## Language notes

- All five solutions print n² and n.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1336_math.cpp](1336_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1336_math.go](1336_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB |
| [1336_math.java](1336_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB |
| [1336_math.py](1336_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 352 KB |
| [1336_math.rs](1336_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB |
