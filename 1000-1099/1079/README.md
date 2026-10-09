# 1079. The largest term of Stern's sequence up to n

[Timus 1079](https://acm.timus.ru/problem.aspx?space=1&num=1079) · difficulty 111 · dp

Original problem by Emil Kelevedzhiev, from the Informatics Tournament of the Winter Mathematical Festival, Varna 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The sequence is `a₀ = 0`, `a₁ = 1`, `a₂ᵢ = aᵢ` and
`a₂ᵢ₊₁ = aᵢ + aᵢ₊₁` for `i ≥ 1`. For each given `n`
(`1 ≤ n ≤ 99 999`) print the largest of `a₀, a₁, …, aₙ`.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Up to ten lines with `n`, then a line with 0.

## Output

The maximum for each `n`, one per line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
10
0
```

Output:

```
3
4
```

## Solution

Every term refers only to terms with smaller indices, so one pass from 2
to 99 999 fills the whole table, and a second running maximum
`best[i] = max(best[i − 1], aᵢ)` answers every query at once. `O(N)` for
the table, `O(1)` per query.

This is Stern's diatomic sequence. Its records are Fibonacci numbers,
reached near `n = (2^k ± 1)/3`; the largest value up to 99 999 is 2584,
so 32-bit integers are plenty.

Pitfalls:

- the queries come in any order and end with 0, which is not a query;
- the recurrence for odd indices uses `aᵢ₊₁`, which is still smaller than
  `2i + 1`, so the order of the pass is right.

The answers were checked against the definition computed by a memoised
recursion and a plain scan for every query.

## Language notes

- All languages build both tables before reading the queries.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1079_dp.cpp](1079_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 960 KB |
| [1079_dp.go](1079_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 2764 KB |
| [1079_dp.java](1079_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 2364 KB |
| [1079_dp.py](1079_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.125 s | 3280 KB |
| [1079_dp.rs](1079_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 1004 KB |
