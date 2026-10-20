# 2130. A number consistent with divisibility answers so far

[Timus 2130](https://acm.timus.ru/problem.aspx?space=1&num=2130) · difficulty 961 · math, number_theory

Original problem by Kirill Borozdin and Nikita Sivukhin, prepared by Vladimir Leskov, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A hidden integer x lies between 1 and 10¹². Each of n moves tells
whether x is divisible by some dᵢ. After every move print any number in
the same range that agrees with all answers so far, or −1 if none
exists. Any such number is accepted. The limits are 2.5 seconds and
256 MB.

## Input

n, 1 ≤ n ≤ 10⁵, then n pairs dᵢ, tᵢ with 1 ≤ dᵢ ≤ 10⁶; tᵢ = 1 means "yes".

## Output

A suitable number or −1 after every move.

## Checking

A checker decides for every move whether a suitable number exists and
verifies each printed number against the answers so far.

## Examples

### Example 1

Input:

```
3
10 1
5 0
100500 0
```

Output:

```
100500
-1
-1
```

### Example 2

Input:

```
6
2 1
5 0
3 1
1 1
5 1
100500 0
```

Output:

```
12
12
12
12
-1
-1
```

### Example 3

Input:

```
6
1000000 1
999999 1
2 0
999998 1
999997 1
999996 1
```

Output:

```
999999000000
999999000000
-1
-1
-1
-1
```

## Solution

Every valid number is a multiple of L, the least common multiple of the
divisors answered "yes". L itself is the best candidate: if some valid x
exists, then L divides x, and a "no" divisor d does not divide x, so it
does not divide L either. So the answer is L when L ≤ 10¹² and no "no"
divisor divides L, and −1 otherwise; once it is −1 it stays −1, since
the answers only add conditions.

A new "no" divisor is checked against the current L once. A "yes" that
does not change L changes nothing, and a change of L at least doubles
it, so L changes at most about 40 times before passing 10¹². Only then
are all stored "no" divisors checked again, which keeps the total work
at O(40 n).

In the second example 2 and 3 give L = 6, but 5 is a "no" divisor and
the later "yes" for 5 makes L = 30 divisible by 5, so the answer becomes
−1; the sample prints 12, another multiple of 6.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2130_math_number_theory.cpp](2130_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(n log X) | AC | 0.062 s | 1220 KB |
| [2130_math_number_theory.go](2130_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(n log X) | AC | 0.046 s | 7616 KB |
| [2130_math_number_theory.java](2130_math_number_theory.java) | Java 1.8 | math, number_theory | O(n log X) | AC | 0.125 s | 8892 KB |
| [2130_math_number_theory.py](2130_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(n log X) | AC | 0.343 s | 18092 KB |
| [2130_math_number_theory.rs](2130_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(n log X) | AC | 0.031 s | 4564 KB |
