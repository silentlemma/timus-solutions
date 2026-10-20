# 2126. Red team wins: central trinomial coefficients modulo a prime

[Timus 2126](https://acm.timus.ru/problem.aspx?space=1&num=2126) · difficulty 1654 · math, combinatorics

Original problem by Alexander Zimin, from the t.me/umnik_team contest, Petrozavodsk training camp, summer 2018.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n people independently joins the red team, joins the blue team
or watches, each with probability 1/3. The larger team wins. With t the
probability that red wins, print t · 3ⁿ modulo a prime p, that is, the
number of the 3ⁿ choices in which red is larger. The limits are 1 second
and 64 MB.

## Input

n and p, 1 ≤ n ≤ 10¹⁸, 5 ≤ p < 10⁶, p prime.

## Output

The count modulo p.

## Examples

### Example 1

Input:

```
5 5
```

Output:

```
1
```

### Example 2

Input:

```
5 7
```

Output:

```
5
```

## Solution

Swapping the colours shows that red and blue win equally often, so the
answer is (3ⁿ − D) / 2, where D counts the draws. Give each person the
weight x for red, 1 for watching and x⁻¹ for blue: D is the constant
term of (x + 1 + x⁻¹)ⁿ, the central trinomial coefficient Tₙ. Division by
2 is a multiplication by (p + 1) / 2.

Since (1 + x + x²)ᵖ ≡ 1 + xᵖ + x²ᵖ modulo p, these coefficients satisfy
a Lucas property: Tₙ is the product of T_d over the base-p digits d of n.
The digits are below p < 10⁶, and Tₖ follows the recurrence

(k + 1) T_{k+1} = (2k + 1) Tₖ + 3k T_{k−1}.

To avoid a division at every step the programs carry Fₖ = k! · Tₖ, which
satisfies F_{k+1} = (2k + 1) Fₖ + 3k² F_{k−1}, and divide once by the
factorials at the end; the digits are sorted, so one pass reaches them
all. A digit above (p − 1) / 2 is first reflected with
T_{p−1−d} ≡ (−3)^{(p−1)/2 − d} T_d (mod p), so the pass never goes past
(p − 1) / 2. 3ⁿ comes from fast exponentiation, and the work is O(p).

In the first example T₅ = 51, 3⁵ = 243, and (243 − 51) / 2 = 96 ≡ 1
modulo 5.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2126_math_combinatorics.cpp](2126_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(p + log n) | AC | 0.015 s | 396 KB |
| [2126_math_combinatorics.go](2126_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(p + log n) | AC | 0.046 s | 1124 KB |
| [2126_math_combinatorics.java](2126_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(p + log n) | AC | 0.109 s | 456 KB |
| [2126_math_combinatorics.py](2126_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(p + log n) | AC | 0.140 s | 544 KB |
| [2126_math_combinatorics.rs](2126_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(p + log n) | AC | 0.046 s | 232 KB |
