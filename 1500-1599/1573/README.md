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

B, R and Y, then a positive K and the K different colors of the recipe
(Blue, Red or Yellow).

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

## Optimized solutions

The optimized C++ solution reads with `scanf` instead of `iostream` and
picks the bag by the first letter of the color, since Blue, Red and
Yellow start with different letters, instead of looking the name up in a
`std::map` of strings. A color goes into a buffer of 7 bytes, enough for
the longest name, Yellow, and the product is kept in `int`, which holds
it since it is at most 10⁶: {1573_math_optimized.cpp}.

The optimized Java solution parses the numbers digit by digit straight
from `System.in` instead of creating a `Scanner`, and picks the bag by
the first letter of the color, skipping the rest of the word, since
Blue, Red and Yellow start with different letters, instead of looking
the name up in a `HashMap` of boxed `Long` values. The product is kept
in `int`, which holds it since it is at most 10⁶:
{1573_math_optimized.java}.

The optimized Rust solution keeps the three bag sizes in three variables
and selects one with a `match` on the color name instead of building a
`HashMap`: {1573_math_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1573_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +69.23%; base: `1573_math.cpp`.

- `1573_math_optimized.java`: time reduction +12.80%; memory reduction
  +79.85%; base: `1573_math.java`.

- `1573_math_optimized.rs`: time reduction -206.67%; memory reduction
  +45.10%; base: `1573_math.rs`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1573_math.go](1573_math.go).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math.cpp](1573_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 416 KB | 11287812 |
| [1573_math.go](1573_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 1084 KB | 11287815 |
| [1573_math.java](1573_math.java) | Java 1.8 | math | O(K) | AC | 0.125 s | 1628 KB | 11287819 |
| [1573_math.py](1573_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.078 s | 452 KB | 11287817 |
| [1573_math.rs](1573_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.015 s | 408 KB | 11287824 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math_optimized.cpp](1573_math_optimized.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 128 KB | 11304264 |
| [1573_math_optimized.java](1573_math_optimized.java) | Java 1.8 | math | O(K) | AC | 0.109 s | 328 KB | 11304267 |
| [1573_math_optimized.rs](1573_math_optimized.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 224 KB | 11304268 |
