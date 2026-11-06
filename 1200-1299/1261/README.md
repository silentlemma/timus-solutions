# 1261. Tips

[Timus 1261](https://acm.timus.ru/problem.aspx?space=1&num=1261) · difficulty 329 · number_theory

Original problem by Alexander Ipatov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Bills come in 1, 3, 9, 27, … trits, and the guest has exactly one bill
of each value. The bill is N trits (1 ≤ N ≤ 10⁷). The guest pays some
amount and the waiter keeps the change as a tip. The waiter is offended
unless the tip is positive and could itself be paid with distinct bills.
Find a payment and a tip; the payment may not exceed 4 294 967 291. Any
valid pair is accepted; if there is none, print 0.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The payment and the tip.

## Checking

Many pairs work, so the checker accepts any: the payment minus the tip
must be N, the tip positive, the payment within the limit, and both
written in base 3 with digits 0 and 1 only.

## Examples

### Example 1

Input:

```
5
```

Output:

```
9 4
```

## Solution

Both the payment P and the tip T are sums of distinct powers of 3, and
P − T = N. Write N in balanced ternary, with digits −1, 0 and 1: the
digits 1 make up P and the digits −1 make up T. Going from the low
digit, a remainder 1 gives a digit 1, a remainder 2 gives a digit −1
with a carry into the next place.

If N has no digit 2 in base 3, this leaves T = 0. Then take the lowest
power of 3 missing from P and add it to both sums: P keeps distinct
bills and T is that single bill. So the answer always exists and 0 is
never printed. P stays below 3¹⁶ ≈ 4.3 · 10⁷, far under the limit.
`O(log N)`.

Pitfalls:

- the tip must be positive: N = 1 cannot be paid as 1 with tip 0, and
  4 3 is one answer (test 02);
- the payment may need a bill larger than N: N = 10⁷ is paid with
  14 960 143 and a tip of 4 960 143 (test 03);
- the payment and the tip may share a bill: the tip is only a sum that
  could be paid, not bills taken from the guest.

Every N from 1 to 3000 and the two largest were run through the
checker.

## Optimized solutions

Go scans the balanced ternary digits using only the remaining amount, current power, payment and tip. A digit one adds a bill to the payment. A digit two adds that bill to the tip and carries one to the next digit. Remember the lowest unused bill so that a zero tip can be made positive by adding the same unused bill to both sums. Fixed byte buffers handle input and decimal output without a general-purpose scanner or number formatter. Go accesses the standard input and output handles directly.

The accepted base implementations [1261_number_theory.cpp](1261_number_theory.cpp), [1261_number_theory.java](1261_number_theory.java), [1261_number_theory.py](1261_number_theory.py), [1261_number_theory.rs](1261_number_theory.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- All languages build the balanced ternary digits in one loop.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1261_number_theory.cpp](1261_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log N) | AC | 0.015 s | 128 KB | 11284132 |
| [1261_number_theory.go](1261_number_theory.go) | Go 1.14 x64 | number_theory | O(log N) | AC | 0.031 s | 1068 KB | 11284133 |
| [1261_number_theory.java](1261_number_theory.java) \* | Java 1.8 | number_theory | O(log N) | AC | 0.125 s | 1612 KB | 11284139 |
| [1261_number_theory.py](1261_number_theory.py) \* | Python 3.12 x64 | number_theory | O(log N) | AC | 0.078 s | 432 KB | 11284137 |
| [1261_number_theory.rs](1261_number_theory.rs) \* | Rust 1.75 x64 | number_theory | O(log N) | AC | 0.046 s | 232 KB | 11284140 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1261_number_theory_optimized.go](1261_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(log N) | AC | 0.031 s | 308 KB | 11311230 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
