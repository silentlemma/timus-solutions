# 1057. Sums of K different powers of B in a range

[Timus 1057](https://acm.timus.ru/problem.aspx?space=1&num=1057) · difficulty 718 · combinatorics

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

1. if a digit exceeds 1, take the highest such digit: every 0/1 string
   agreeing with `n` above it is below `n` whatever follows, so it and all
   lower digits can be replaced by 1 without changing the count;
2. now all digits are 0 or 1: walk from the top keeping the number of ones
   taken; at a digit 1, choosing 0 instead leaves the `i` lower positions
   free, which gives `C(i, K − ones)` numbers; choosing 1 continues;
3. at the end, the resulting bound counts if it has exactly `K` ones.

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

## Optimized solutions

Rust scans the digits in base B and uses a precomputed Pascal table for the remaining choices. Rust 1.75 x64, submission 11323261. Time 0.015 → 0.015 s, memory 236 → 44 KB.

The PyPy version scans the bound with descending powers of the base and computes binomial coefficients as needed without storing the digits. Submission 11323987 took 0.125 s and used 268 KB, versus 0.078 s and 500 KB for the simple version.

Python scans the digits of the bound from left to right, computing binomial coefficients only when needed. A digit above one ends the scan because every remaining binary digit pattern is below the bound.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321895 · Java 1.8 №11321896 · Go 1.14 x64 №11322186 · Python 3.12 x64 №11322187 · Rust 1.75 x64 №11322188.

Go scans the digits from most significant to least significant and updates the binomial coefficient for the remaining positions as it goes. Go 1.14 x64, submission 11322843. Time 0.031 → 0.015 s, memory 1072 → 276 KB.

Java reads four integers directly from the input stream and scans the bound using descending powers of the base. It computes binomial coefficients as needed, with constant extra space. Submission 11323981 took 0.093 s and used 384 KB, versus 0.109 s and 1624 KB for the simple version.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1057_combinatorics.cpp](1057_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(log Y) | AC | 0.015 s | 188 KB | 11321895 |
| [1057_combinatorics.go](1057_combinatorics.go) | Go 1.14 x64 | combinatorics | O(log Y) | AC | 0.031 s | 1072 KB | 11322186 |
| [1057_combinatorics.java](1057_combinatorics.java) | Java 1.8 | combinatorics | O(log Y) | AC | 0.109 s | 1624 KB | 11321896 |
| [1057_combinatorics.py](1057_combinatorics.py) | Python 3.12 x64 | combinatorics | O(log Y) | AC | 0.078 s | 500 KB | 11322187 |
| [1057_combinatorics.rs](1057_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(log Y) | AC | 0.015 s | 236 KB | 11322188 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1057_combinatorics_optimized.rs](1057_combinatorics_optimized.rs) \* | Rust 1.75 x64 | combinatorics | O(log_B X) | AC | 0.015 s | 44 KB | 11323261 |
| [1057_combinatorics_optimized.py](1057_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O((log Y)²) | AC | 0.125 s | 268 KB | 11323987 |
| [1057_combinatorics_optimized.go](1057_combinatorics_optimized.go) \* | Go 1.14 x64 | combinatorics | O(log Y) | AC | 0.015 s | 276 KB | 11322843 |
| [1057_combinatorics_optimized.java](1057_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O((log Y)²) | AC | 0.093 s | 384 KB | 11323981 |

\* The marked solutions can improve their target rankings.
