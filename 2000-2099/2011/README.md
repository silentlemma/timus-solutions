# 2011. At Least Six Distinct Arrangements

[Timus 2011](https://acm.timus.ru/problem.aspx?space=1&num=2011) · difficulty 103 · combinatorics

Original problem by Alexey Kungurtsev, from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

You have `n` symbols, each of one of three types. Rearrange all of them
into a word of length `n`; equal symbols are indistinguishable. Decide
whether at least six different words are possible. Every available
symbol must be used exactly once.

## Input

The first line contains `n`, `1 ≤ n ≤ 100`. The second contains `n`
integers from 1 to 3 specifying symbol types. Time limit 0.5 seconds,
memory 64 MB.

## Output

Print `Yes` if there are at least six different words, or `No`
otherwise. Capitalization matters. The unique answer is compared token
by token.

## Checking

Outputs are compared token by token.

## Examples

```
6
1 2 2 3 3 3
```

```
Yes
```

The multiplicities are 1, 2 and 3. There are `6!/(1!·2!·3!)=60`
different words, so the answer is `Yes`.

## Solution

Pieces of the same kind are equal, so k pieces with c₁, c₂, c₃ of each
kind make k!/(c₁!·c₂!·c₃!) different words. Read the pieces one by one
and keep this count for the pieces read so far: when the k-th piece
comes and its kind now occurs c times, the count is multiplied by k and
divided by c, exactly. As soon as the count reaches 6 the answer is
`Yes`: the remaining pieces, appended in a fixed order, keep the words
different. If it never reaches 6, the answer is `No`. `O(n)`.

The count is at most 5 before each step, so 5 · 100 fits any integer
type; multiply before dividing.

Pitfalls:

- exactly six words is already `Yes`;
- do not compute the full factorials: they overflow.

## Optimized solutions

The optimized C++ solution counts the values as they are read with
`scanf` instead of `iostream` and a vector, and prints the answer as
soon as it is known: 116 KB instead of 380 KB, with the same time.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2011_combinatorics.cpp](2011_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.031 s | 380 KB | 11292493 |
| [2011_combinatorics.go](2011_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 1112 KB | 11292495 |
| [2011_combinatorics.java](2011_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.125 s | 1668 KB | 11303363 |
| [2011_combinatorics.py](2011_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.109 s | 516 KB | 11292497 |
| [2011_combinatorics.rs](2011_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 232 KB | 11292499 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2011_combinatorics_optimized.cpp](2011_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.015 s | 116 KB | 11303791 |
