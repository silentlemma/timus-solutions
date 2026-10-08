# 1013. Counting base-K numbers without two adjacent zeros, modulo M

[Timus 1013](https://acm.timus.ru/problem.aspx?space=1&num=1013) · difficulty 196 · matrix

Original problem: the hardest version of [problems 1009](../1009/README.md) and [1012](../1012/README.md).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count, modulo `M`, the `N`-digit numbers in base `K` (the first digit is not
zero) whose digits contain no two zeros in a row. `2 ≤ N, K, M ≤ 10^18`.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, `K` and `M`, each on its own line.

## Output

The count modulo `M`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
2
1000
```

Output:

```
8
```

### Example 2

Input:

```
3
10
7
```

Output:

```
2
```

## Solution

The recurrence of [problem 1009](../1009/README.md) counts valid prefixes by
their last digit: `zero' = other`, `other' = (zero + other) · (K - 1)`,
starting from `(zero, other) = (0, K - 1)` after the first digit. It is a
linear map of the pair, so one step is a multiplication by the matrix

```text
A = | 0      1     |
    | K - 1  K - 1 |
```

and after `N` digits the pair is `A^(N-1) · (0, K - 1)`. With `N` up to
`10^18` the steps cannot be done one by one, but `A^(N-1)` can be computed by
**binary exponentiation**: square the matrix and multiply it into the result
for every set bit of `N - 1`, all modulo `M`. That is about 60 squarings of a
2×2 matrix, `O(log N)`.

The answer is `(A^(N-1)[0][1] + A^(N-1)[1][1]) · (K - 1) mod M`.

Pitfalls:

- `K - 1` and `M` are up to `10^18`, so the product of two residues is up to
  `10^36` and does not fit in 64 bits: multiply in 128 bits (`__int128`,
  `u128`, `bits.Mul64`) or with big integers;
- reduce `K - 1` modulo `M` first: it can be larger than `M`.

## Language notes

- **C++** (`unsigned __int128`) and **Rust** (`u128`) multiply in 128 bits.
- **Go** uses `bits.Mul64` and `bits.Div64` for the 128-bit product and its
  remainder.
- **Java** 8 has no 128-bit multiplication, so it uses `BigInteger`;
  **Python** integers are unbounded.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1013_matrix.cpp](1013_matrix.cpp) | G++ 13.2 x64 | matrix | O(log N) | AC | 0.015 s | 136 KB |
| [1013_matrix.go](1013_matrix.go) | Go 1.14 x64 | matrix | O(log N) | AC | 0.031 s | 1072 KB |
| [1013_matrix.java](1013_matrix.java) | Java 1.8 | matrix | O(log N) | AC | 0.125 s | 1868 KB |
| [1013_matrix.py](1013_matrix.py) | Python 3.12 x64 | matrix | O(log N) | AC | 0.078 s | 400 KB |
| [1013_matrix.rs](1013_matrix.rs) | Rust 1.75 x64 | matrix | O(log N) | AC | 0.031 s | 220 KB |
