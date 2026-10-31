# 1012. Counting base-K numbers without two adjacent zeros, with long arithmetic

[Timus 1012](https://acm.timus.ru/problem.aspx?space=1&num=1012) · difficulty 181 · dp

Original problem: a harder version of [problem 1009](../1009/README.md).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the `N`-digit numbers in base `K` (the first digit is not zero) whose
digits contain no two zeros in a row. `2 ≤ K ≤ 10`, `N ≥ 2`, `N + K ≤ 1800`.

Time limit: 0.5 seconds. Memory limit: 16 MB.

## Input

`N` and `K`, each on its own line.

## Output

The count, in full.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
2
```

Output:

```
5
```

### Example 2

Input:

```
3
10
```

Output:

```
891
```

## Solution

The recurrence is the one of [problem 1009](../1009/README.md): count valid
prefixes by their last digit, `zero` ending with `0` and `other` with a
nonzero digit:

- `zero' = other`;
- `other' = (zero + other) · (K - 1)`;

starting from `zero = 0`, `other = K - 1`, and the answer is `zero + other`
after `N` digits.

What changes is the size: the answer has up to
about 1 800 decimal digits, so it needs long arithmetic. Only two operations
are used — the sum of two long numbers and the product of a long number by a
small one — both linear in the length. Store a long number as an array of
"digits" in base `10^9`, least significant first: a digit times `K - 1` plus
a carry fits in 64 bits. `N` steps of `O(L)` work, where `L` is the length of
the answer in limbs: about `1800 · 200` operations.

Only the two current values are kept, so the memory is `O(L)` — keeping the
whole table of `N` long numbers would also fit, but there is no need.

Pitfalls:

- 64-bit integers overflow after about 20 digits: the small version's
  solution is wrong here;
- when printing base-`10^9` limbs, every limb but the most significant one
  must be padded with leading zeros to 9 digits.

## Optimized solutions

The optimized C++ solution keeps `zero` and `other` in two static arrays
of 201 base-`10^9` limbs, enough because the answer is below
`K^N ≤ 10^N` with `N < 1800`, and makes a step of the recurrence in one
pass over the limbs, in place: the limb of `zero` takes the limb of
`other`, and the limb of `other` becomes the sum of
`(zero + other) · (K - 1)` and the carry, modulo `10^9`; the sum itself
stays below `18 · 10^9` and fits in 64 bits. No temporary vectors are
allocated and grown on every step: {1012_dp_optimized.cpp}.

The optimized Go solution replaces `math/big` with two fixed arrays of
201 base-`10^9` limbs, enough because the answer is below `K^N ≤ 10^N`
with `N < 1800`, and makes a step of the recurrence in one pass over the
limbs, in place, with the sum and the product by `K - 1` fused: the
intermediate value stays below `18 · 10^9` and fits in 64 bits. No new
big integers are allocated on every step, and the limbs are printed with
zero padding through a buffered writer: {1012_dp_optimized.go}.

The optimized Java solution replaces `BigInteger` with two `long` arrays
of 201 base-`10^9` limbs, enough because the answer is below
`K^N ≤ 10^N` with `N < 1800`, and makes a step of the recurrence in one
pass over the limbs, in place, with the sum and the product by `K - 1`
fused: the intermediate value stays below `18 · 10^9` and fits in a
`long`. It also reads the two numbers byte by byte instead of with
`Scanner`, and pads the limbs with zeros by hand:
{1012_dp_optimized.java}.

The optimized Rust solution keeps `zero` and `other` in two fixed arrays
of 201 base-`10^9` limbs, enough because the answer is below
`K^N ≤ 10^N` with `N < 1800`, and makes a step of the recurrence in one
pass over the limbs, in place: the intermediate value
`(zero + other) · (K - 1)` plus the carry stays below `18 · 10^9` and
fits in a `u64`. No new vectors are allocated for every sum and product,
and the limbs go straight to a `BufWriter` instead of into one more
string: {1012_dp_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1012_dp_optimized.cpp`: time reduction +0.00%; memory reduction
  +58.21%; base: `1012_dp.cpp`.

- `1012_dp_optimized.go`: time reduction -106.67%; memory reduction
  +48.83%; base: `1012_dp.go`.

- `1012_dp_optimized.java`: time reduction +25.60%; memory reduction
  +89.02%; base: `1012_dp.java`.

- `1012_dp_optimized.rs`: time reduction +0.00%; memory reduction
  +58.46%; base: `1012_dp.rs`.

## Language notes

- **Python**, **Go** (`math/big`) and **Java** (`BigInteger`) provide long
  integers.
- **C++** and **Rust** implement the two operations on base-`10^9` limbs.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1012_dp.cpp](1012_dp.cpp) | G++ 13.2 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 268 KB | 11278066 |
| [1012_dp.go](1012_dp.go) | Go 1.14 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 2056 KB | 11278067 |
| [1012_dp.java](1012_dp.java) | Java 1.8 | dp | O(N·L), L = length of the answer | AC | 0.125 s | 3860 KB | 11278076 |
| [1012_dp.py](1012_dp.py) | Python 3.12 x64 | dp | O(N·L), L = length of the answer | AC | 0.062 s | 340 KB | 11278071 |
| [1012_dp.rs](1012_dp.rs) | Rust 1.75 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 520 KB | 11278084 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1012_dp_optimized.cpp](1012_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 112 KB | 11307305 |
| [1012_dp_optimized.go](1012_dp_optimized.go) \* | Go 1.14 x64 | dp | O(N·L), L = length of the answer | AC | 0.031 s | 1052 KB | 11307309 |
| [1012_dp_optimized.java](1012_dp_optimized.java) \* | Java 1.8 | dp | O(N·L), L = length of the answer | AC | 0.093 s | 424 KB | 11307307 |
| [1012_dp_optimized.rs](1012_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 216 KB | 11307310 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
