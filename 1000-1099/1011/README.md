# 1011. The smallest population with a share strictly between two percentages

[Timus 1011](https://acm.timus.ru/problem.aspx?space=1&num=1011) · difficulty 247 · math, number_theory

Original problem from the Ural State University Championship 1997.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given two percentages `P` and `Q` (`0.01 ≤ P, Q ≤ 99.99`, at most two digits
after the decimal point, `P < Q`), find the smallest positive integer `n` for
which some integer `c` satisfies `P% < c / n < Q%`, both inequalities strict.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`P` and `Q`, separated by a space or a line break. They may be written as
integers (`13`) or with one or two decimals (`14.1`, `12.50`).

## Output

The smallest `n`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
10 12
```

Output:

```
9
```

### Example 2

Input:

```
12.5
12.6
```

Output:

```
127
```

## Solution

First, avoid floating point. Both bounds have at most two decimals, so
`p = 100·P` and `q = 100·Q` are integers (hundredths of a percent), and the
condition becomes `p·n < 10000·c < q·n`.

**Scan over n.** For a given `n` the smallest `c` above the lower bound is
`c = ⌊p·n / 10000⌋ + 1`; `n` works exactly when this `c` is still below the
upper bound, `10000·c < q·n`. Try `n = 1, 2, ...`. The interval has width at
least `1/10000`, so some `n ≤ 10000` always works (the largest answer is
5001); the scan is instant.

**Stern–Brocot tree.** The answer is the smallest denominator of a fraction
strictly inside `(p/10000, q/10000)`. Descend the Stern–Brocot tree from
the bounds `0/1` and `1/0`: take the mediant `(a + c)/(b + d)` of the current
bounds; if it is at or below the interval it becomes the new left bound, at
or above it the new right bound, otherwise it is the answer. The first
fraction of the tree that falls inside an interval is the one with the
smallest denominator.

Pitfalls:

- reading the bounds as floating-point numbers: `14.1` is not exact in
  binary, and a comparison with `c / n` at the boundary can go either way;
- both inequalities are strict: with `P = 12.5`, `1/8` is not inside;
- `n = 1` never works, since `0 < P` and `Q < 100`.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: the scan over `n` with 64-bit integers.
- **C++** and **Python** also descend the Stern–Brocot tree.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1011_math.cpp](1011_math.cpp) | G++ 13.2 x64 | math | O(answer) | AC | 0.015 s | 352 KB |
| [1011_math.go](1011_math.go) | Go 1.14 x64 | math | O(answer) | AC | 0.015 s | 1088 KB |
| [1011_math.java](1011_math.java) | Java 1.8 | math | O(answer) | AC | 0.125 s | 1580 KB |
| [1011_math.rs](1011_math.rs) | Rust 1.75 x64 | math | O(answer) | AC | 0.015 s | 228 KB |
| [1011_number_theory.cpp](1011_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(answer) tree steps | AC | 0.015 s | 352 KB |
| [1011_number_theory.py](1011_number_theory.py) | Python 3.12 x64 | number_theory | O(answer) tree steps | AC | 0.109 s | 468 KB |
