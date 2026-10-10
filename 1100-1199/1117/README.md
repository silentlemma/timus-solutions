# 1117. Walking an in-order numbered binary tree from one number to another

[Timus 1117](https://acm.timus.ru/problem.aspx?space=1&num=1117) · difficulty 279 · math

Original problem by Alexander Somov, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The nodes of a perfect binary tree are numbered `1, 2, 3, …` in order:
every inner node has a number between those of its two children, all of
one subtree on the same side. A message goes from number `i` to number `j`
through every number in between, one step at a time; a step between `k`
and `k ± 1` costs as many days as there are tree nodes strictly between
them on the tree path (0 for a parent and its child). Find the total
number of days for `1 ≤ i, j ≤ 2^31 − 1`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`i j` on one line.

## Output

The number of days.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
1 5
```

Output:

```
2
```

## Solution

In an in-order numbered perfect tree, the height of node `x` above the
leaves is the number of trailing zero bits `tz(x)`: the leaves are the odd
numbers, their parents `2 mod 4`, and so on. Of two consecutive numbers
one is odd, a leaf, and the even one `e` is its ancestor at height
`tz(e)`, so the step costs `tz(e) − 1` days. Each even number strictly
between `i` and `j` is used by two steps, and an even endpoint by one.

With `c(e) = tz(e) − 1 = tz(e/2)`, the sum of `c` over the even numbers up
to `n` is `Σ_{y ≤ n/2} tz(y) = m − popcount(m)` for `m = ⌊n/2⌋` (each `y`
contributes its trailing zeros, and `Σ_{t≥1} ⌊m/2^t⌋ = m − popcount(m)`).
So for `i < j` the answer is `2·(G(j) − G(i − 1)) − c(i) − c(j)`, where
`G` is that sum and `c` of an odd number is 0. `O(1)`.

Pitfalls:

- the largest answer, for `1` and `2^31 − 1`, is `2147483586`, just 61
  below the signed 32-bit limit; the solutions use 64 bits to be safe;
- the order of `i` and `j` does not matter;
- the tree size is not given, but it does not matter: the in-order numbers
  and heights are the same in every perfect tree large enough to hold
  both numbers.

The answers were checked against a walk on the actual tree (the parent of
`x` is `x ± 2^tz(x)`) summing the path lengths step by step, for 300
random pairs below 3000, and the large tests against a direct loop over
every step.

## Language notes

- The trailing zeros and the bit counts come from built-ins:
  `__builtin_ctzll` and `__builtin_popcountll`, `math/bits`,
  `Long.numberOfTrailingZeros` and `Long.bitCount`, `trailing_zeros` and
  `count_ones`; Python counts the ones in `bin(m)`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1117_math.cpp](1117_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1117_math.go](1117_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1052 KB |
| [1117_math.java](1117_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1616 KB |
| [1117_math.py](1117_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB |
| [1117_math.rs](1117_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 224 KB |
