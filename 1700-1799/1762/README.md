# 1762. Search for a Hiding-Place

[Timus 1762](https://acm.timus.ru/problem.aspx?space=1&num=1762) · difficulty 1685 · math

Original problem by Alexander Larin, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A hall of n by m tiles has exits in its four corners. A walker enters
at one corner and moves diagonally, one tile at a time, turning by 90°
at each wall, until reaching a corner. Every tile stepped on is turned
over, from white to grey or back. Count the grey tiles at the end.

## Input

n and m (2 ≤ n, m ≤ 1 000 000).

## Output

The number of grey tiles.

## Examples

### Example 1

Input:

```
7 5
```

Output:

```
11
```

### Example 2

Input:

```
2 3
```

Output:

```
3
```

## Solution

Number the tiles from 0 to a = n − 1 across and 0 to b = m − 1 down.
Unfolded at the walls, the walk is a straight diagonal, and it first
meets a corner after L = lcm(a, b) steps, so it steps on L + 1 tiles
counting repeats. A tile can only be met once in each of the two
diagonal directions, so it ends up grey unless the walk crosses itself
there, and the answer is L + 1 minus twice the number of crossings.

With g = gcd(a, b), the walk runs only along the lines x − y ≡ 0 and
x + y ≡ 0 modulo 2g, since its time t matches ±x modulo 2a and ±y
modulo 2b. A tile on lines of both kinds has x and y divisible by g,
with x/g and y/g of the same parity. Inside the hall every such point
is a crossing; on a wall the walk only bounces off it. So with
A = a/g and B = b/g, the crossings are the pairs 1 ≤ X < A, 1 ≤ Y < B
of the same parity: ⌊A/2⌋·⌊B/2⌋ odd pairs plus
⌊(A−1)/2⌋·⌊(B−1)/2⌋ even ones. `O(log n)` for the gcd.

In the first example a = 6, b = 4, g = 2, L = 12, A = 3, B = 2, and the
only crossing is X = Y = 1, the tile (2, 2): 13 − 2 = 11.

Pitfalls:

- L reaches about 10¹², so 64 bits are needed;
- a bounce off a wall steps on that tile once, not twice;
- simulating the walk takes up to 10¹² steps.

The formula agrees with a simulation of the walk for every hall up to
69 by 69 tiles and with an independent accepted implementation on 100
cases up to the limits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1762_math.cpp](1762_math.cpp) | G++ 13.2 x64 | math | O(log n) | AC | 0.015 s | 128 KB |
| [1762_math.go](1762_math.go) | Go 1.14 x64 | math | O(log n) | AC | 0.031 s | 1084 KB |
| [1762_math.java](1762_math.java) | Java 1.8 | math | O(log n) | AC | 0.140 s | 1568 KB |
| [1762_math.py](1762_math.py) | Python 3.12 x64 | math | O(log n) | AC | 0.078 s | 444 KB |
| [1762_math.rs](1762_math.rs) | Rust 1.75 x64 | math | O(log n) | AC | 0.046 s | 244 KB |
