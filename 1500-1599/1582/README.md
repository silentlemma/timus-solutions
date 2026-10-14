# 1582. Bookmakers

[Timus 1582](https://acm.timus.ru/problem.aspx?space=1&num=1582) · difficulty 123 · math

Original problem by Sergey Pupyrev, prepared by Vladimir Yakovlev, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A match has three outcomes with the best odds k₁, k₂ and k₃ (0.01 …
100): a bet of x on the right outcome pays k·x, a wrong one pays
nothing. Split bets totalling 1000 pounds over the three outcomes so as
to get back the most in the worst case, and print that amount rounded to
the nearest integer.

Time limit: 1 second. Memory limit: 64 MB.

## Input

k₁, k₂ and k₃.

## Output

The guaranteed payout, rounded.

## Examples

### Example 1

Input:

```
3.5 3.5 3.5
```

Output:

```
1167
```

### Example 2

Input:

```
1.25 10.0 5.75
```

Output:

```
931
```

## Solution

Bet xᵢ on outcome i, with x₁ + x₂ + x₃ = 1000; outcome i pays kᵢ·xᵢ. If
the three payouts differ, moving a little money from the best-paid
outcome to the worst-paid one raises the minimum, so in the best split
all payouts are equal to some P. Then xᵢ = P / kᵢ, and the total gives

P = 1000 / (1/k₁ + 1/k₂ + 1/k₃).

The three terms are added one after another in double precision, and
the payout is rounded half up as ⌊P + 0.5⌋. `O(1)`.

Pitfalls:

- with odds above 3 each, the guaranteed payout is more than the
  stake, as in the first example;
- an exact half rounds up: odds 2, 10 and 25 give 1562.5 and the answer
  1563, while `printf("%.0f")` would round to even and print 1562
  (test 08);
- Python's `sum` adds floats with extra precision since version 3.12,
  so the Python solution adds the three terms one by one, like the
  others.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1582_math.cpp](1582_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 152 KB |
| [1582_math.go](1582_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1068 KB |
| [1582_math.java](1582_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1724 KB |
| [1582_math.py](1582_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 404 KB |
| [1582_math.rs](1582_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 252 KB |
