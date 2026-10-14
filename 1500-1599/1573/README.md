# 1573. Alchemy

[Timus 1573](https://acm.timus.ru/problem.aspx?space=1&num=1573) · difficulty 108 · math

Original problem by Alexander Ipatov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Sandro has three bags of different reagents: B blue, R red and Y yellow
(1 … 100 each). A potion needs one reagent of each color in its recipe,
all colors different. Count the sets of reagents that make the potion.

Time limit: 1 second. Memory limit: 64 MB.

## Input

B, R and Y, then K and the K colors of the recipe (Blue, Red or
Yellow).

## Output

The number of ways.

## Examples

### Example 1

Input:

```
2 3 5
3
Red
Yellow
Blue
```

Output:

```
30
```

## Solution

Each color of the recipe takes one reagent from its own bag, and the
choices are independent, so the answer is the product of the sizes of
the bags the recipe names. It is at most 100³ = 10⁶. `O(K)`.

Pitfalls:

- the input lists the bags as blue, red, yellow, while the example's
  recipe lists red first;
- only the colors in the recipe count (tests 02, 03).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1573_math.cpp](1573_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 416 KB |
| [1573_math.go](1573_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 1084 KB |
| [1573_math.java](1573_math.java) | Java 1.8 | math | O(K) | AC | 0.125 s | 1628 KB |
| [1573_math.py](1573_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.078 s | 452 KB |
| [1573_math.rs](1573_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.015 s | 408 KB |
