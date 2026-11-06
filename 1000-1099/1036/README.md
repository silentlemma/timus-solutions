# 1036. Balanced tickets with a given digit sum

[Timus 1036](https://acm.timus.ru/problem.aspx?space=1&num=1036) · difficulty 305 · dp

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

## Optimized solutions

All three variants use digit complementation to replace the target sum by the smaller of the two complementary sums. C++ and Rust keep two DP rows with six base-10⁹ limbs per entry. A sliding window adds the new term and subtracts the outgoing one, so each entry needs only one addition and at most one subtraction. Go uses the inclusion–exclusion formula above with reusable big integers. Each variant squares the count of one half. The Accepted runs used 116 KB in C++, 1204 KB in Go and 220 KB in Rust.

Measured time for Rust 1.75 x64 increases from 0.015 to 0.046 s.

The accepted base implementations [1036_dp.java](1036_dp.java), [1036_dp.py](1036_dp.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- **C++**, **Rust**: a small big-integer type in base `10^9` with addition
  and multiplication.
- **Go**: `math/big`; **Java**: `BigInteger`; **Python**: built-in
  integers.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1036_dp.cpp](1036_dp.cpp) | G++ 13.2 x64 | dp | O(N·S) big additions | AC | 0.031 s | 280 KB | 11278472 |
| [1036_dp.go](1036_dp.go) | Go 1.14 x64 | dp | O(N·S) big additions | AC | 0.015 s | 2728 KB | 11278473 |
| [1036_dp.java](1036_dp.java) \* | Java 1.8 | dp | O(N·S) big additions | AC | 0.140 s | 5728 KB | 11278476 |
| [1036_dp.py](1036_dp.py) \* | Python 3.12 x64 | dp | O(N·S) big additions | AC | 0.093 s | 512 KB | 11278474 |
| [1036_dp.rs](1036_dp.rs) | Rust 1.75 x64 | dp | O(N·S) big additions | AC | 0.015 s | 336 KB | 11278477 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1036_dp_optimized.cpp](1036_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N·S) big integer operations | AC | 0.015 s | 116 KB | 11310337 |
| [1036_combinatorics.go](1036_combinatorics.go) \* | Go 1.14 x64 | combinatorics | O(N²) big integer operations | AC | 0.015 s | 1204 KB | 11310374 |
| [1036_dp_optimized.rs](1036_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(N·S) big integer operations | AC | 0.046 s | 220 KB | 11310376 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
