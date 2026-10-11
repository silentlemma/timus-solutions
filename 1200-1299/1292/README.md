# 1292. Mars Space Stations

[Timus 1292](https://acm.timus.ru/problem.aspx?space=1&num=1292) · difficulty 380 · math

Original problem by Denis Musin, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Let F(x) be the sum of the cubes of the decimal digits of x, so
F(12) = 9. Space bases stand along a route: the first at distance K
from the route's end, and if the gap before base i is x, the gap after
it is F(x). The key K is a multiple of 3.

A ship is between bases N − 1 and N, at distance L from base N − 1.
For each of T ≤ 33 333 queries with 2 ≤ N ≤ 33 333 and
3 ≤ K ≤ 33 333, print the distance from the ship to base N.

Time limit: 1 second. Memory limit: 64 MB.

## Input

T, then T lines with N, K and L.

## Output

T lines with the distances.

## Examples

### Example 1

Input:

```
2
4 6 123
7 93 49
```

Output:

```
18
104
```

## Solution

Counting the route's end as base 0, the gap before base N is F applied
N − 1 times to K, and the answer is that gap minus L. The sample
confirms it: 6 → 216 → 225 → 141, and 141 − 123 = 18.

Applying F up to 33 332 times per query would be too slow for 33 333
queries, but the chain settles almost at once. Since d³ ≡ d (mod 3),
F keeps the remainder of the digit sum mod 3, so multiples of 3 stay
multiples of 3. F(153) = 1 + 125 + 27 = 153, and checking every
multiple of 3 up to 33 333 shows that each one reaches 153 within at
most 14 steps (12 558 is the slowest). So F is applied until either
N − 1 steps are done or the value is 153. `O(T · 14 · digits)`.

Pitfalls:

- the gap before base N takes N − 1 steps, not N − 2: the first base
  is already K away from the end (test 01);
- a chain can be cut just before it reaches 153 (test 03);
- the gap can be much larger than K, for example F(99) = 1458
  (test 05).

The answers were compared with applying F all N − 1 times.

## Language notes

- All languages read L as a 64-bit integer, since its upper bound is
  not stated.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1292_math.cpp](1292_math.cpp) | G++ 13.2 x64 | math | O(T * 14 * digits) | AC | 0.046 s | 136 KB |
| [1292_math.go](1292_math.go) | Go 1.14 x64 | math | O(T * 14 * digits) | AC | 0.015 s | 1452 KB |
| [1292_math.java](1292_math.java) | Java 1.8 | math | O(T * 14 * digits) | AC | 0.109 s | 4740 KB |
| [1292_math.py](1292_math.py) | Python 3.12 x64 | math | O(T * 14 * digits) | AC | 0.265 s | 7972 KB |
| [1292_math.rs](1292_math.rs) | Rust 1.75 x64 | math | O(T * 14 * digits) | AC | 0.001 s | 2124 KB |
