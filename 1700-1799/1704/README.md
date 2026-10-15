# 1704. Demodulation

[Timus 1704](https://acm.timus.ru/problem.aspx?space=1&num=1704) · difficulty 3193 · math

Original problem by Pavel Atnashev, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A text was sent bit by bit, eight bits per character from the lowest,
and t samples per bit. Sample k of a bit is an unknown level plus an
unknown amplitude times sin(2πk/t) for a one or sin(4πk/t) for a zero,
plus some noise. Given the n samples, recover the text.

## Input

n and t (0 < n ≤ 10000, 5 ≤ t ≤ 1000, n a multiple of 8t), then n
samples between 0 and 1 with at most five decimals, on one or more
lines.

## Output

The text: Latin letters, digits, punctuation and spaces. It decodes
uniquely.

## Examples

### Example 1

Input:

```
40 5
0.3 0.8 0.6 0.4 0.2
0.5 0.6 0.3 0.9 0.4
0.4 0.8 0.3 0.8 0.2
0.3 0.6 0.1 0.7 0.2
0.7 0.7 0.1 0.7 0.1
0.5 0.8 0.7 0.3 0.2
0.4 0.8 0.2 0.8 0.2
0.5 0.8 0.3 0.8 0.2
```

Output:

```
!
```

## Solution

Over a whole number of periods, sin(2πk/t) and sin(4πk/t) sum to zero
and are orthogonal: the sum of their products over k = 0 … t − 1 is 0
when t ≥ 5. So for the t samples of one bit, correlate them with both
waves, that is take the sums of sample × wave. The constant level adds
nothing to either sum. The wave that was sent adds its amplitude times
t/2 to its own sum and nothing to the other, and noise only blurs
this. Pick the larger sum as the bit, and assemble the characters from
their lowest bit up. `O(n)`.

Pitfalls:

- the level and the amplitude are unknown, but neither needs to be
  estimated, as the level cancels and the amplitude only scales;
- bits go from the lowest one within a character: the example's
  samples spell 10000100, which is 33, the code of !;
- the samples may be spread over the lines in any way (test 05).

The answers match an independent accepted implementation on the
statement's encoder run with random levels, amplitudes and noise.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1704_math.cpp](1704_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 296 KB |
| [1704_math.go](1704_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1312 KB |
| [1704_math.java](1704_math.java) | Java 1.8 | math | O(n) | AC | 0.078 s | 616 KB |
| [1704_math.py](1704_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 1364 KB |
| [1704_math.rs](1704_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 580 KB |
