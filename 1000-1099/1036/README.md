# 1036. Balanced tickets with a given digit sum

[Timus 1036](https://acm.timus.ru/problem.aspx?space=1&num=1036) · difficulty 304 · dp

Original problem from the Timus Online Judge problem set; the author and the contest are not stated.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A ticket number is a string of `2N` decimal digits (`1 ≤ N ≤ 50`); leading
zeros are allowed. A ticket is balanced when its first `N` digits and its
last `N` digits have equal sums. Given `S` (`0 ≤ S ≤ 1000`), count the
balanced tickets whose digits sum to `S`.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N` and `S` on one line.

## Output

The number of such tickets (it can have about a hundred digits).

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2 2
```

Output:

```
4
```

### Example 2

Input:

```
3 6
```

Output:

```
100
```

## Solution

Both halves of a balanced ticket with digit sum `S` sum to `S / 2`, so the
answer is `0` when `S` is odd, and otherwise `W^2`, where `W` is the number
of strings of `N` digits with sum `S / 2`: the two halves are chosen
independently.

`W` comes from a DP over the digits: `ways[k][t]` is the number of strings
of `k` digits with sum `t`, and `ways[k + 1][t]` is the sum of
`ways[k][t − d]` for the digits `d = 0..9`. Only sums up to `S / 2` are
needed, and `S / 2 > 9N` gives `0` at once. That is
`O(N · S)` additions.

The numbers do not fit in 64 bits: `W` reaches about `10^48` and the
answer about `10^97`, so the DP and the final square use big integers.

Pitfalls:

- an odd sum has no balanced tickets;
- the sum can be larger than any ticket allows (up to 1000 against
  `18N ≤ 900`);
- leading zeros count: `0101` is a ticket of four digits.

An alternative is the closed form by inclusion–exclusion,
`W = Σ (−1)^k C(N, k) C(S/2 − 10k + N − 1, N − 1)`; the tests were checked
with it.

## Language notes

- **C++**, **Rust**: a small big-integer type in base `10^9` with addition
  and multiplication.
- **Go**: `math/big`; **Java**: `BigInteger`; **Python**: built-in
  integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1036_dp.cpp](1036_dp.cpp) | G++ 13.2 x64 | dp | O(N·S) big additions | AC | 0.031 s | 280 KB |
| [1036_dp.go](1036_dp.go) | Go 1.14 x64 | dp | O(N·S) big additions | AC | 0.015 s | 2728 KB |
| [1036_dp.java](1036_dp.java) | Java 1.8 | dp | O(N·S) big additions | AC | 0.140 s | 5728 KB |
| [1036_dp.py](1036_dp.py) | Python 3.12 x64 | dp | O(N·S) big additions | AC | 0.093 s | 512 KB |
| [1036_dp.rs](1036_dp.rs) | Rust 1.75 x64 | dp | O(N·S) big additions | AC | 0.015 s | 336 KB |
