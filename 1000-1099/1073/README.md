# 1073. The fewest square plots that cost exactly N

[Timus 1073](https://acm.timus.ru/problem.aspx?space=1&num=1073) · difficulty 140 · number_theory

Original problem by Stanislav Vasiliev, from the Ural State University Personal Contest Online, February 2001, Students Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A square plot with side `a` costs `a²`. Spend exactly `N` (`1 ≤ N ≤ 60000`)
on as few plots as possible, that is, write `N` as a sum of the fewest
squares of positive integers. Print how many plots that takes.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The smallest number of squares.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
344
```

Output:

```
3
```

## Solution

The answer is never more than 4: by Lagrange's theorem every positive
integer is a sum of four squares. The other cases are easy to tell
apart.

- 1 if `N` is a perfect square.
- 2 if `N − a²` is a perfect square for some `1 ≤ a < √N`; that is at most
  244 checks.
- 4 if `N = 4^a (8b + 7)`: by Legendre's three-square theorem these are
  exactly the numbers that are not sums of three squares. Divide by 4
  while possible and look at the remainder modulo 8.
- 3 otherwise.

`O(√N)`.

A dynamic programming solution over all amounts,
`best[v] = 1 + min best[v − a²]`, also fits in the limits for compiled
languages at `O(N√N)`, about 10 million steps, but it is slow in Python,
and the theorems make it unnecessary.

Pitfalls:

- the factor `4^a` matters: 28 = 4 · 7 also needs four squares, so testing
  only `N mod 8 = 7` is not enough;
- a square root in floating point is rounded before squaring back, so a
  result like `6.9999…` does not hide a perfect square.

The formula was checked against the dynamic programming for every `N` up
to 60000.

## Language notes

- Python uses `math.isqrt`, which is exact; the other languages round
  the floating-point square root, which is exact for numbers this small.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1073_number_theory.cpp](1073_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(√N) | AC | 0.015 s | 132 KB |
| [1073_number_theory.go](1073_number_theory.go) | Go 1.14 x64 | number_theory | O(√N) | AC | 0.031 s | 1076 KB |
| [1073_number_theory.java](1073_number_theory.java) | Java 1.8 | number_theory | O(√N) | AC | 0.109 s | 1596 KB |
| [1073_number_theory.py](1073_number_theory.py) | Python 3.12 x64 | number_theory | O(√N) | AC | 0.078 s | 440 KB |
| [1073_number_theory.rs](1073_number_theory.rs) | Rust 1.75 x64 | number_theory | O(√N) | AC | 0.015 s | 228 KB |
