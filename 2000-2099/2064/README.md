# 2064. The highest of many zigzags

[Timus 2064](https://acm.timus.ru/problem.aspx?space=1&num=2064) · difficulty 976 · math, prefix_sums

Original problem by Nikita Sivukhin, prepared by Alexey Danilyuk and Nikita Sivukhin, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n caterpillars start on the ground at time 0. Caterpillar i climbs at
1 cm per minute for tᵢ minutes, then slides down at the same speed for
tᵢ minutes back to the ground, and repeats this forever. For each of q
moments find the height of the highest caterpillar. The limits are 3
seconds and 64 MB.

## Input

The number of caterpillars n, 1 ≤ n ≤ 10⁶, then the n values tᵢ,
1 ≤ tᵢ ≤ 10⁹, then the number of moments q, 1 ≤ q ≤ 10⁶, and the q
moments x, one per line, 1 ≤ x ≤ 10⁶.

## Output

For each moment, the largest height on its own line.

## Checking

Outputs are compared token by token.

## Examples

### Example 1

Input:

```
4
1 3 2 1
12
1
2
3
4
5
6
7
8
9
10
11
12
```

Output:

```
1
2
3
2
1
2
1
2
3
2
1
0
```

## Solution

At time x the caterpillar with parameter t is at height
t − |x − c|, where c is the odd multiple of t closest to x: it is a
row of tents of height t centred at t, 3t, 5t, … with feet at the even
multiples. Equivalently, its height is the distance from x to the
nearest multiple of 2t. The answer at x is the highest point of all
these tents, that is, max over all tents of h − |x − c|; a tent that
does not cover x gives at most 0 there, so it never wins.

Let X be the largest moment. A caterpillar with t ≥ X is still climbing
at every moment, at height x, which is exactly what a tent of height X
centred at X gives. For t < X only tents with centres up to 2X can be
nearest to a moment x ≤ X. So put the tents into an array: height[c] is
the tallest tent centred at c, filled by walking over c = t, 3t, 5t, …
up to 2X for every distinct t. This takes O(X log X) steps in all.

Then best[x] = max over c of height[c] − |x − c| is a distance
transform with slope 1: one sweep from left to right takes
best[x] = max(height[x], best[x − 1] − 1) for the tents on the left,
and one sweep from right to left does the same for the tents on the
right. The answer to each moment is read from the array. With sorting,
the time is O(n log n + X log X + q) and the memory O(n + X + q).

In the example the tents have heights 1 at odd times, 2 at 2, 6, 10, …
and 3 at 3, 9, 15, … At time 12 the nearest centres 10, 11, 13, 14 and
15 all give 0, so the answer is 0.

Pitfalls:

- the same t may appear many times: only distinct values matter;
- a caterpillar taller than every moment still counts, with height x;
- tents centred beyond the largest moment matter for the moments just
  before it.

## Language notes

Reading two million numbers needs fast input everywhere. The Python
solution uses a presence table of size T = 10⁶ + 1 instead of sorting
and runs on PyPy, with plain loops that the JIT handles well;
CPython takes about six seconds on the largest tests. Splitting the
whole input into words costs PyPy more than 64 MB, so the numbers are
parsed digit by digit from small pieces of input, kept in arrays, and
the answers are printed in small portions.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2064_math_prefix_sums.cpp](2064_math_prefix_sums.cpp) | G++ 13.2 x64 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.453 s | 33928 KB |
| [2064_math_prefix_sums.go](2064_math_prefix_sums.go) | Go 1.14 x64 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.562 s | 33868 KB |
| [2064_math_prefix_sums.java](2064_math_prefix_sums.java) | Java 1.8 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.468 s | 53828 KB |
| [2064_math_prefix_sums.py](2064_math_prefix_sums.py) | PyPy 3.10 x64 | math, prefix_sums | O(n + T + X log X + q) | AC | 0.875 s | 18808 KB |
| [2064_math_prefix_sums.rs](2064_math_prefix_sums.rs) | Rust 1.75 x64 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.265 s | 64076 KB |
