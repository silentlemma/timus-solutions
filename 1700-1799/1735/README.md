# 1735. Theft of the Century

[Timus 1735](https://acm.timus.ru/problem.aspx?space=1&num=1735) · difficulty 2824 · constructive

Original problem by Alexander Ipatov (idea by Artyom Skrobov), from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n bags of k bars each; every bag holds only gold bars of x
kg or only platinum bars of y kg, and the bars look the same. Choose
how many bars to take from each bag so that one exact weighing tells
which bags hold platinum, or report that it is impossible.

## Input

n, k, x and y (3 ≤ n ≤ 20, 1 ≤ k ≤ 10⁶, 1 ≤ x < y ≤ 10).

## Output

`YES` and the n counts, or `NO`. Any fitting counts are accepted.

## Examples

### Example 1

Input:

```
4 8 9 10
```

Output:

```
YES
4 5 6 8
```

## Solution

With counts c_i the scale shows x·Σc_i + (y − x)·P, where P is the sum
of the counts of the platinum bags. The first term is the same for
every arrangement, so the weighing tells the platinum bags exactly when
all 2ⁿ subset sums of the counts differ. In particular the counts are
positive and distinct, and x and y do not matter.

So the question is the smallest possible largest element of a set of n
positive integers with distinct subset sums. The Conway–Guy sequence
u₀ = 0, u₁ = 1, u_{m+1} = 2u_m − u_{m−r} with r = round(√(2m)) gives
the sets {u_n − u_i : 0 ≤ i < n}, which have distinct subset sums and
largest element u_n: 1, 2, 4, 7, 13, 24, 44, 84, 161, 309, … up to
267 420 for n = 20. The code prints that set if u_n ≤ k, otherwise `NO`.
`O(n)`.

For the example u₄ = 7 ≤ 8, and the set is 3, 5, 6, 7.

Pitfalls:

- powers of two, 1, 2, 4, …, also work but need 2ⁿ⁻¹ bars, far more
  than u_n for large n;
- a count of 0 hides its bag completely, so every bag must give at
  least one bar.

For n up to 6 a search shows that no set has a smaller largest element;
for larger n better sets exist (maximum 1157 for n = 12), though these
bounds match an independent accepted implementation for n from 3 to 20
on both sides of u_n. Every set printed was checked to have distinct
subset sums.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1735_constructive.cpp](1735_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 372 KB |
| [1735_constructive.go](1735_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.015 s | 1088 KB |
| [1735_constructive.java](1735_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1644 KB |
| [1735_constructive.py](1735_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 460 KB |
| [1735_constructive.rs](1735_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 216 KB |
