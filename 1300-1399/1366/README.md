# 1366. Presents

[Timus 1366](https://acm.timus.ru/problem.aspx?space=1&num=1366) · difficulty 523 · math

Original problem: idea by Stanislav Vasiliev, prepared by Pavel Egorov, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n ≤ 1000 children brings a present, and the presents are
exchanged so that every child gets exactly one present and nobody keeps
their own. Count the ways to do it.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number n.

## Output

The number of exchanges.

## Examples

### Example 1

Input:

```
3
```

Output:

```
2
```

## Solution

An exchange is a permutation with no fixed point, a derangement. By
inclusion–exclusion their number is d(k) = Σ (−1)ⁱ · k! / i! over
i = 0 … k, and multiplying d(k − 1) by k gives every term of d(k) but
the last one, (−1)ᵏ. So d(1) = 0 and d(k) = k · d(k − 1) + (−1)ᵏ: start
from 0 and apply it for k = 2 … n.

The answer for n = 1000 has 2 568 digits, so it needs long arithmetic:
each step multiplies by a small number and adds or subtracts 1.
`O(n² log n)` digit operations.

Pitfalls:

- one child cannot exchange at all: the answer is 0 (test 02);
- d(21) is the first count that no longer fits in 64 bits (test 06);
- after the multiplication the number is at least 3 for k ≥ 3, so
  subtracting 1 never goes below zero.

The recurrence was compared with counting all permutations for n ≤ 8,
and with the inclusion–exclusion sum for n = 50.

The teaching C++ version stores individual decimal digits, lowest first. At step k, start the carry at +1 for even k and −1 for odd k. For each digit, multiply it by k and add the carry, keep the units digit and pass the quotient on as the next carry. This computes k·D(k−1)+(−1)^k in one pass. When k is odd, the previous index is even and D(k−1) is odd, so the lowest digit is positive and the first subtraction is safe. Output the digits in reverse order. Time O(n² log n), space O(n log n).

## Optimized solutions

Go, Java and Rust keep the derangement count but combine two recurrence steps. From D(k)=kD(k−1)+(−1)^k, for even k obtain D(k)=k(k−1)D(k−2)−(k−1). Start with D(2)=1. For n=1 output zero, and for odd n>1 finish with nD(n−1)−1. One pass over base-10⁹ limbs handles each pair, roughly halving the number of passes. The recurrence gives odd D at every even index, so its lowest limb is positive. The initial subtraction is smaller than the multiplication factor f, and the first product is at least f. Subsequent carries are in [0,f−1], so every intermediate is less than f·10⁹. As f≤999,000, a signed 64-bit integer suffices and the final carry fits one limb. Since D(n)<n!≤10³⁰⁰⁰, 334 limbs suffice and the full Go and Java output fits in 3001 bytes. Fixed limbs replace Go and Java big-integer temporaries. Go uses standard handles and fills its decimal buffer from the end. Java avoids Scanner. Rust starts at a C entry point and streams characters through the C runtime, using nine bytes to format each limb. Time O(n² log n) word operations, O(n log n) digits; all simple sources remain, with C++/Python bases reused for admitted fast coverage.

The accepted base implementations [1366_math.cpp](1366_math.cpp), [1366_math.py](1366_math.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The original Python, Go and Java files use their languages’ big integers. The original C++ and Rust files use base-10⁹ limbs. The optimized Go, Java and Rust files use fixed arrays of those limbs and combine two recurrence steps.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1366_math.cpp](1366_math.cpp) | G++ 13.2 x64 | math | O(n² log n) | AC | 0.031 s | 196 KB | 11285547 |
| [1366_math.go](1366_math.go) | Go 1.14 x64 | math | O(n² log n) | AC | 0.031 s | 1268 KB | 11285549 |
| [1366_math.java](1366_math.java) | Java 1.8 | math | O(n² log n) | AC | 0.125 s | 3320 KB | 11285574 |
| [1366_math.py](1366_math.py) \* | Python 3.12 x64 | math | O(n² log n) | AC | 0.093 s | 412 KB | 11285552 |
| [1366_math.rs](1366_math.rs) | Rust 1.75 x64 | math | O(n² log n) | AC | 0.046 s | 252 KB | 11285579 |
| [1366_combinatorics.cpp](1366_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n² log n) | AC | 0.015 s | 192 KB | 11315859 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1366_math_optimized.java](1366_math_optimized.java) \* | Java 1.8 | math | O(n² log n) | AC | 0.109 s | 380 KB | 11315509 |
| [1366_math_optimized.go](1366_math_optimized.go) \* | Go 1.14 x64 | math | O(n² log n) | AC | 0.015 s | 312 KB | 11315864 |
| [1366_math_optimized.rs](1366_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n² log n) | AC | 0.031 s | 52 KB | 11315876 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
