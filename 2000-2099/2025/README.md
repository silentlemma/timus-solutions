# 2025. Maximize pairs across groups

[Timus 2025](https://acm.timus.ru/problem.aspx?space=1&num=2025) · difficulty 60 · math

Original problem by Alexey Danilyuk, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Partition `n` distinct objects into between two and `k` nonempty groups.
Every object must belong to exactly one group. An unordered pair
contributes one if its two objects are in different groups, and zero
otherwise. Find the largest possible total number of contributing pairs.
Only the maximum count is required, not a partition.

There are `1 ≤ T ≤ 10` independent test cases. Each satisfies `2 ≤ k ≤ n
≤ 10000`. Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains `T`. Each of the next `T` lines contains `n` and `k`.

## Output

For each case, print one integer on a separate line, in the input order.

## Checking

Outputs are compared token by token.

## Examples

```
3
6 3
5 5
4 2
```

```
12
10
4
```

## Solution

First, using all `k` groups is best. If only `m < k` groups are used,
then `n ≥ k > m` forces some group to contain at least two objects.
Split it into two nonempty parts of sizes `a` and `b`. All existing
cross-group pairs remain, while the `ab > 0` pairs between the two new
parts become contributing pairs. Thus using fewer groups is worse.

For exactly `k` groups with sizes `s₁, …, sₖ`, the number of cross-group
pairs is `(n² - Σ sᵢ²) / 2`. The square `n²` counts all ordered object
pairs; the squares of the group sizes remove pairs within groups,
including self-pairs. The remaining cross-group pairs occur twice, so
divide by two.

We therefore minimize the sum of squared sizes. Suppose two group sizes
are `a ≥ b+2`. Moving one object from the larger group to the smaller
changes their squared-size sum by `(a-1)² + (b+1)² - a² - b² = -2(a-b-1)
< 0`. It increases the cross-group total by `a-b-1`. Hence an optimum
has no sizes differing by two or more. Repeatedly making such improving
transfers ends with balanced sizes; all such balanced partitions have
the same squared-size sum and therefore attain the maximum.

Let `q = n // k` and `r = n % k`. Exactly `r` groups have size `q+1`,
and the other `k-r` groups have size `q`. They are nonempty because `k ≤
n`. The answer is `(n² - (k-r)q² - r(q+1)²) / 2`. Compute it with
integer division only; the numerator is even, since each integer square
has the same parity as the integer itself.

The sample uses sizes `2,2,2`, giving 12 pairs; five singleton groups
give 10 pairs; sizes `2,2` give 4 pairs. As further checks, `k = n`
gives `n(n-1)/2`, while `k = 2` gives `floor(n²/4)`.

Each test takes `O(1)` arithmetic time and `O(1)` working space.
Processing all tests takes `O(T)` time. Input or output buffering uses
up to `O(T)` storage in these programs; C++ and Go process cases with
fixed-size buffers.

Pitfalls:

- The statement allows at most `k` groups; justify why exactly `k` is optimal.
- Groups must be nonempty, and all objects must be assigned once.
- Use the remainder to distinguish sizes `q` and `q+1`; do not use a
  real-valued average.
- Count unordered pairs once: the square formula needs division by two.
- Read every test case and print exactly one answer per line. At the
  largest input, the answer is 49995000; wide integer intermediates keep
  all products exact.

## Language notes

C++ uses `long long`, Go `int64`, Java `long`, and Rust `u64` for the
arithmetic. Python uses exact integers and `divmod`. Rust's unsigned
subtraction is safe because the within-group square sum cannot exceed
`n²`. All ports use integer quotient and remainder; none constructs the
actual partition. CPython needs no alternate runtime.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2025_math.cpp](2025_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 444 KB |
| [2025_math.go](2025_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1128 KB |
| [2025_math.java](2025_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 392 KB |
| [2025_math.py](2025_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB |
| [2025_math.rs](2025_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB |
