# 1057. Sums of K different powers of B in a range

[Timus 1057](https://acm.timus.ru/problem.aspx?space=1&num=1057) · difficulty 717 · combinatorics

Original problem from the Rybinsk State Aviation Academy.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the integers in `[X, Y]` (`1 ≤ X ≤ Y ≤ 2^31 − 1`) that are sums of
exactly `K` different powers of `B` with integer exponents
(`1 ≤ K ≤ 20`, `2 ≤ B ≤ 10`).

Time limit: 1 second. Memory limit: 64 MB.

## Input

`X` and `Y`, then `K`, then `B`.

## Output

The count.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
15 20
2
2
```

Output:

```
3
```

### Example 2

Input:

```
1 100
1
10
```

Output:

```
3
```

## Solution

Distinct negative powers of `B` add up to less than 1, so an integer sum
uses non-negative exponents only. Such a number is exactly one whose base
`B` digits are all 0 or 1, with `K` ones. Count them in `[0, n]` with a
function `f(n)`; the answer is `f(Y) − f(X − 1)`.

For `f(n)`, write `n` in base `B` (at most 31 digits):

1. if some digit is greater than 1, every 0/1 string that agrees with `n`
   above that digit is below `n` whatever follows, so that digit and all
   lower ones can be replaced by 1 without changing the count;
2. now all digits are 0 or 1: walk from the top keeping the number of ones
   taken; at a digit 1, choosing 0 instead leaves the `i` lower positions
   free, which gives `C(i, K − ones)` numbers; choosing 1 continues;
3. at the end, `n` itself counts if it has exactly `K` ones.

`O(log_B Y)` with a small table of binomial coefficients.

Pitfalls:

- the digits must be 0 or 1 in base `B`; a digit 2 or more is not a sum of
  *different* powers;
- `f(X − 1)` with `X = 1` is `f(0) = 0`;
- for `B = 10` there are only 10 positions below `2^31`, so `K > 10`
  gives 0.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: a Pascal triangle up to 32.
  **Python**: `math.comb`, which returns 0 when `k > n`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1057_combinatorics.cpp](1057_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(log Y) | AC | 0.001 s | 204 KB |
| [1057_combinatorics.go](1057_combinatorics.go) | Go 1.14 x64 | combinatorics | O(log Y) | AC | 0.015 s | 1080 KB |
| [1057_combinatorics.java](1057_combinatorics.java) | Java 1.8 | combinatorics | O(log Y) | AC | 0.125 s | 1656 KB |
| [1057_combinatorics.py](1057_combinatorics.py) | Python 3.12 x64 | combinatorics | O(log Y) | AC | 0.078 s | 512 KB |
| [1057_combinatorics.rs](1057_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(log Y) | AC | 0.046 s | 252 KB |
