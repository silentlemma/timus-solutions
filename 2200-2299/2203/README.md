# 2203. Counting shop trips when two ingredients run out on their own schedules

[Timus 2203](https://acm.timus.ru/problem.aspx?space=1&num=2203) · difficulty 1757 · math, number_theory

Original problem by Valentin Zuev, from the University Academic School Olympiad in Informatics 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sandwich needs A grams of bread and B grams of sausage, sold in
loaves of X grams and sticks of Y grams. Whenever the stock is short for
the next sandwich, one trip buys the fewest loaves and sticks that make
it possible. Starting with nothing and making N sandwiches, how many
trips are there? The limits are 1 second and 256 MB.

## Input

A, B, X, Y and N, 1 ≤ A, B ≤ 100, 1 ≤ X, Y, N ≤ 10⁹.

## Output

The number of trips.

## Examples

### Example 1

Input:

```
30 20 90 30 4
```

Output:

```
3
```

### Example 2

Input:

```
5 6 7 72 100
```

Output:

```
74
```

### Example 3

Input:

```
99 100 37 47 1000000000
```

Output:

```
1000000000
```

## Solution

If X ≤ A, whatever is left over is less than one loaf and so less than
a sandwich needs, and every sandwich needs a trip; the same holds for
Y ≤ B. Then the answer is N.

Otherwise each trip buys at most one loaf. Number the sandwiches from 0;
loaf j (from 0) is bought before sandwich k exactly when (k + 1)A > jX
for the first time, that is k = ⌊jX / A⌋. With g = gcd(A, X), P = X / g
and E = A / g, the bread trips are ⌊jP / E⌋, a pattern of E trips that
repeats every P sandwiches, and there are ⌈NA / X⌉ of them below N. The
sausage trips work the same way with their own P' and E'.

A trip buys both when a sandwich index is in both patterns, and the
answer is the bread trips plus the sausage trips minus those shared
ones. For each of the E · E' ≤ 10⁴ pairs of residues
r = ⌊iP / E⌋ and r' = ⌊jP' / E'⌋, the indices r + sP = r' + tP' form, by
the Chinese remainder theorem, either nothing (when gcd(P, P') does not
divide r' − r) or one arithmetic progression with step lcm(P, P'), whose
members below N are counted directly.

In the first example the bread trips are 0 and 3 and the sausage trips
are 0, 1 and 3, so the shared ones are 0 and 3 and the answer is
2 + 3 − 2 = 3.

This takes O(AB + log XY).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2203_math_number_theory.cpp](2203_math_number_theory.cpp) | G++ 13.2 x64 | math, number_theory | O(AB + log XY) | AC | 0.015 s | 184 KB |
| [2203_math_number_theory.go](2203_math_number_theory.go) | Go 1.14 x64 | math, number_theory | O(AB + log XY) | AC | 0.031 s | 912 KB |
| [2203_math_number_theory.java](2203_math_number_theory.java) | Java 1.8 | math, number_theory | O(AB + log XY) | AC | 0.093 s | 172 KB |
| [2203_math_number_theory.py](2203_math_number_theory.py) | Python 3.12 x64 | math, number_theory | O(AB + log XY) | AC | 0.093 s | 324 KB |
| [2203_math_number_theory.rs](2203_math_number_theory.rs) | Rust 1.75 x64 | math, number_theory | O(AB + log XY) | AC | 0.031 s | 20 KB |
