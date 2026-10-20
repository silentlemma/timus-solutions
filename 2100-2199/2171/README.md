# 2171. Numbers up to N covered by some of K arithmetic progressions

[Timus 2171](https://acm.timus.ru/problem.aspx?space=1&num=2171) · difficulty 1518 · math, number_theory

Original problem by Konstantin Rychkov, from the Ural School Programming Contest 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the integers from 1 to N that belong to at least one of K infinite
increasing arithmetic progressions bᵢ, bᵢ + dᵢ, … The limits are 2 seconds
and 256 MB.

## Input

N and K, 1 ≤ N ≤ 10⁹, 1 ≤ K ≤ 18, then the pairs bᵢ, dᵢ, 1 ≤ bᵢ, dᵢ ≤ 10⁹.

## Output

The count.

## Examples

### Example 1

Input:

```
15 2
3 5
6 2
```

Output:

```
7
```

## Solution

By inclusion and exclusion the answer is the sum over non-empty subsets
of the progressions of (−1)^(size + 1) times the number of values up to
N common to all of them. The common values of progressions form a
progression again, or nothing: two of them meet when the difference of
their starts is divisible by the gcd of the steps, and then the
extended Euclidean algorithm gives the first common value at or after
both starts, with the lcm as the step (the Chinese remainder theorem).

The subsets are visited depth first, adding one progression at a time
to the current intersection. A branch stops as soon as the intersection
is empty or starts beyond N, since adding more progressions cannot
bring it back. Once the step exceeds what is left up to N, the
intersection is a single value and is kept with step 0, which also keeps
the numbers small. At most 2¹⁸ subsets are visited, each in O(log) time.

In the example 3, 8, 13 and 6, 8, 10, 12, 14 share 8, so the answer is
3 + 5 − 1 = 7.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2171_math_number_theory.cpp](2171_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(2^K log C) | AC | 0.031 s | 216 KB |
| [2171_math_number_theory.go](2171_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(2^K log C) | AC | 0.046 s | 900 KB |
| [2171_math_number_theory.java](2171_math_number_theory.java) | Java 1.8 | math, number_theory | O(2^K log C) | AC | 0.156 s | 312 KB |
| [2171_math_number_theory.py](2171_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(2^K log C) | AC | 0.703 s | 492 KB |
| [2171_math_number_theory.rs](2171_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(2^K log C) | AC | 0.046 s | 24 KB |
