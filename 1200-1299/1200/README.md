# 1200. How many horns and hooves to make

[Timus 1200](https://acm.timus.ru/problem.aspx?space=1&num=1200) · difficulty 256 · math

Original problem by Magaz Asanov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each horn earns `A` roubles and each hoof `B` roubles, with
`-10000 ≤ A, B ≤ 10000` given to two decimals. At most `K ≤ 10000` items
in total can be sold, and racketeers take the square of the number of
items of each kind. Choose `x` horns and `y` hooves with `x + y ≤ K` to
maximise `A·x + B·y − x² − y²`; among the best plans take the fewest
horns, then the fewest hooves.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

`A` and `B`, then `K`.

## Output

The best profit to two decimals, then `x` and `y`.

## Examples

### Example 1

Input:

```
34.20 61.70
45
```

Output:

```
1239.50
16 29
```

## Solution

Work in kopecks so that every profit is an exact integer:
`a·x − 100·x² + b·y − 100·y²` with `a`, `b` the prices times 100. Try
every `x` from 0 to `K`. For a fixed `x` the hoof part is a concave
parabola in `y`, so its best value on `0..K−x` is at the whole number just
below or just above the peak `b/200`, pulled into the range; try both and
keep the smaller `y` on a tie. Walking `x` upwards and replacing the best
only on a strictly larger profit gives the required tie-breaking. `O(K)`.

Pitfalls:

- with floating-point profits, two equal plans can compare as different
  and break the tie the wrong way;
- the profit can reach `5·10⁷` roubles, `5·10⁹` kopecks, beyond 32-bit
  integers;
- when both prices are negative the answer is to make nothing, and the
  profit must print as `0.00`, not `-0.00`.

The answers were compared with a separately written brute force over
every plan on 400 random inputs with small `K`.

## Language notes

- All languages read the prices as floating-point numbers and round them
  to kopecks, which is exact for two decimals in this range.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1200_math.cpp](1200_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 156 KB |
| [1200_math.go](1200_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.031 s | 1096 KB |
| [1200_math.java](1200_math.java) | Java 1.8 | math | O(K) | AC | 0.140 s | 2096 KB |
| [1200_math.py](1200_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.093 s | 488 KB |
| [1200_math.rs](1200_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 260 KB |
