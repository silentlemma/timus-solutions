# 1059. The shortest postfix program for a polynomial

[Timus 1059](https://acm.timus.ru/problem.aspx?space=1&num=1059) · difficulty 680 · math

Original problem from the Rybinsk State Aviation Academy.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Write the shortest expression in reverse Polish notation that computes the
polynomial `a0·x^N + a1·x^(N−1) + … + aN` for any coefficients and any
`x` (`1 ≤ N ≤ 1000`). The expression may use the operations `+` and `*`,
the letter `X` for the argument and the number `i` for the coefficient
`ai`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`.

## Output

The expression, one element per line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
1
```

Output:

```
0
X
*
1
+
```

### Example 2

Input:

```
3
```

Output:

```
0
X
*
1
+
X
*
2
+
X
*
3
+
```

## Solution

Horner's scheme `(((a0·x + a1)·x + a2)·x + …)·x + aN` written in postfix
form is `0`, then `X * i +` for `i = 1 … N`: `4N + 1` elements.

Nothing shorter exists. Every coefficient must appear, which takes `N + 1`
operands. There is no way to copy a value, so `X` must appear at least `N`
times: an expression with `k` occurrences of `X` has degree at most `k`.
A postfix expression with `m` operands has exactly `m − 1` binary
operations, so at least `(2N + 1) + 2N = 4N + 1` elements are needed.
`O(N)`.

Pitfalls:

- the coefficient `ai` is written as the number `i`, not as `ai`;
- the order of the elements matters for the checker: the scheme starts
  with `0 X *`, as in the example.

## Language notes

- All languages print the same lines; the output of `N = 1000` has 4001
  lines, so it goes through buffered output.

## Optimized solutions

Write the same Horner steps as ASCII bytes, appending each coefficient directly to buffered output.

Rust submission 11317923 took 0.015 s and used 184 KB. The simple version took 0.015 s and used 228 KB.

Python writes each Horner step directly to the output buffer. This uses O(1) auxiliary space instead of storing the full expression. Python 3.12 x64, submission 11317951. Time 0.093 → 0.062 s, memory 336 → 352 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321881 · Java 1.8 №11321882 · Python 3.12 x64 №11321916 · Go 1.14 x64 №11322189 · Rust 1.75 x64 №11322190.

Go builds the output for Horner's method in a fixed byte buffer and writes it in one batch. Go 1.14 x64, submission 11321909. Time 0.031 → 0.015 s, memory 1080 → 344 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1059_math.cpp](1059_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 112 KB | 11321881 |
| [1059_math.go](1059_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1080 KB | 11322189 |
| [1059_math.java](1059_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 1572 KB | 11321882 |
| [1059_math.py](1059_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.093 s | 336 KB | 11321916 |
| [1059_math.rs](1059_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 228 KB | 11322190 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1059_math_optimized.rs](1059_math_optimized.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 184 KB | 11317923 |
| [1059_math_optimized.py](1059_math_optimized.py) \* | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 352 KB | 11317951 |
| [1059_math_optimized.go](1059_math_optimized.go) \* | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 344 KB | 11321909 |

\* The marked versions have room to improve in the ratings.
