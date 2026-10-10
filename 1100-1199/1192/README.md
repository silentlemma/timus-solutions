# 1192. How far a bouncing ball travels in a dream

[Timus 1192](https://acm.timus.ru/problem.aspx?space=1&num=1192) · difficulty 109 · math

Original problem by Igor Goldberg, from the Fifth Team Programming Championship for Schoolchildren, March 2, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A ball is thrown from an endless flat floor at `a` degrees to the
horizon with speed `V` m/s, under gravity `10` m/s² and without air. It
bounces off the floor at the same angle, losing kinetic energy by a
factor `K > 1` at every bounce, and pi is taken as `3.1415926535`. Find
how far from the start the ball can get, to two decimals.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`V` (up to 500000), `a` (0 to 90) and `K`.

## Output

The distance in metres, rounded to two decimals.

## Examples

### Example 1

Input:

```
5 15 2.50
```

Output:

```
2.08
```

## Solution

One flight at speed `v` and angle `a` covers `v²·sin(2a)/g`. A bounce
keeps the angle and divides the kinetic energy, so `v²`, by `K`. The
flights form a geometric series with ratio `1/K`, and its sum is the
first flight times `K/(K − 1)`. `O(1)`.

Pitfalls:

- pi must be the given `3.1415926535`: with it, a throw straight up still
  drifts a few metres at the largest speed, and the expected answers
  include that;
- the result can reach about `2.5·10¹⁴` when `K` is close to 1, still
  within the precision of a double for two decimals;
- `V = 0` or `a = 0` gives `0.00`.

The answers were compared with a separately written solution on every
test.

## Language notes

- Java prints with the US locale so that the decimal point is a dot.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1192_math.cpp](1192_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 152 KB |
| [1192_math.go](1192_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1096 KB |
| [1192_math.java](1192_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1920 KB |
| [1192_math.py](1192_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 416 KB |
| [1192_math.rs](1192_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 248 KB |
