# 1615. Tram Solitaire

[Timus 1615](https://acm.timus.ru/problem.aspx?space=1&num=1615) · difficulty 2101 · math

Original problem by Vladimir Yakovlev, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A shuffled deck has 2n cards: two suits, n ranks in each (2 ≤ n ≤
10 000). The cards are laid out one by one in a row from left to right.
After each card the row is sifted: while some two cards with exactly one
card between them share a suit or a rank, the left card of the leftmost
such pair is removed and the cards to its right close the gap. The
solitaire comes out if exactly two cards are left at the end. Print the
chance of that as an irreducible fraction.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

n.

## Output

The probability as `p/q`.

## Examples

### Example 1

Input:

```
2
```

Output:

```
2/3
```

## Solution

The answer is (n² + 3n − 2) / (2n(2n − 1)), reduced by the greatest
common divisor of its two parts. `O(log n)`.

Some facts behind it. A card is removed only as the left card of a pair,
so the last two cards of the deck always stay: no card ever lies two
places to their right. The solitaire comes out exactly when everything
before them is swept away. The formula itself was found by playing out
every deal for small decks: n = 2, 3, 4, 5 give 2/3, 8/15, 13/28 and
19/45, exactly these values, and random deals for n = 10, 30 and 100
agree with it. The chance of failure factors as
(n − 1)(3n − 2) / (2n(2n − 1)).

Pitfalls:

- the fraction must be reduced: for n = 6 it is 52/132 = 13/33 (test 05);
- 2n(2n − 1) reaches about 4·10⁸, so the product fits 32 bits, but the
  solutions use 64-bit integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1615_math.cpp](1615_math.cpp) | G++ 13.2 x64 | math | O(log n) | AC | 0.015 s | 128 KB |
| [1615_math.go](1615_math.go) | Go 1.14 x64 | math | O(log n) | AC | 0.031 s | 1060 KB |
| [1615_math.java](1615_math.java) | Java 1.8 | math | O(log n) | AC | 0.109 s | 1560 KB |
| [1615_math.py](1615_math.py) | Python 3.12 x64 | math | O(log n) | AC | 0.093 s | 328 KB |
| [1615_math.rs](1615_math.rs) | Rust 1.75 x64 | math | O(log n) | AC | 0.015 s | 232 KB |
