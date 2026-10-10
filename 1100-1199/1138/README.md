# 1138. The longest run of jobs where every raise is a whole number of percent

[Timus 1138](https://acm.timus.ru/problem.aspx?space=1&num=1138) · difficulty 203 · dp

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A programmer's first salary was exactly `s`, every next salary is a
positive integer larger than the previous one by a whole number of
percent, and the last salary is at most `n`, with `1 ≤ n, s ≤ 10000`. Find
the largest possible number of jobs, counting the first one.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n` and `s`.

## Output

The largest number of jobs.

## Examples

### Example 1

Input:

```
10 2
```

Output:

```
5
```

## Solution

A raise from salary `a` to `b > a` is `100·(b − a) / a` percent, a whole
number exactly when `a` divides `100·(b − a)`. With `g = gcd(a, 100)` that
means `a / g` divides `b − a`, so the salaries reachable from `a` are
`a + a/g, a + 2a/g, …`. Let `jobs[a]` be the longest run from `s` ending at
`a`, with `jobs[s] = 1`. Salaries only grow, so going up from `s` and
pushing `jobs[a] + 1` to every reachable `b ≤ n` fills the table in order;
the answer is its largest value. The step `a/g` is at least `a/100`, so
the pushes add up to about `100·n·ln n` at worst and far fewer in
practice.

Pitfalls:

- the raise must be positive, so `b > a`;
- `n = s` gives one job;
- if `s > n`, no run fits at all and the answer is `0`;
- working with `a / gcd(a, 100)` avoids testing every percentage.

The answers were compared with a check of every pair of salaries on
every test and on 300 random inputs up to 400.

## Language notes

- All languages fill the same table by pushing forward.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1138_dp.cpp](1138_dp.cpp) | G++ 13.2 x64 | dp | O(n log n) | AC | 0.015 s | 224 KB |
| [1138_dp.go](1138_dp.go) | Go 1.14 x64 | dp | O(n log n) | AC | 0.031 s | 1144 KB |
| [1138_dp.java](1138_dp.java) | Java 1.8 | dp | O(n log n) | AC | 0.125 s | 1680 KB |
| [1138_dp.py](1138_dp.py) | Python 3.12 x64 | dp | O(n log n) | AC | 0.093 s | 508 KB |
| [1138_dp.rs](1138_dp.rs) | Rust 1.75 x64 | dp | O(n log n) | AC | 0.015 s | 256 KB |
