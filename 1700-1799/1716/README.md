# 1716. Alternative Solution

[Timus 1716](https://acm.timus.ru/problem.aspx?space=1&num=1716) · difficulty 740 · probability

Original problem by Alexander Pronchenkov, prepared by Daniil Ayzenshteyn, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every test of a problem has the answer YES (3 bytes) or NO (2 bytes).
A cheating program prints YES on the first test and on every later
test prints the answer of the previous one. Given the number of tests
n and the total size s of the answers, find the expected number of
failed tests over all orders of the tests, all equally likely.

## Input

n and s (1 ≤ n ≤ 5000, 2n ≤ s ≤ 3n).

## Output

The expected number of failed tests, with an error of at most 10⁻⁵.

## Examples

### Example 1

Input:

```
3 7
```

Output:

```
2.0000000
```

## Solution

The sizes give the counts: y = s − 2n answers are YES and k = n − y
are NO. By linearity of expectation, add up the chance that each test
fails. The first test fails when its answer is NO, with chance k/n.
Every later test fails when its answer differs from the one before.
Two given places hold a YES and a NO in either order with chance
2yk/(n(n − 1)). The n − 1 later tests add up to 2yk/n, so the
expectation is

k/n + 2yk/n = k(2y + 1)/n.

The example has y = 1 and k = 2, giving 2 · 3/3 = 2. `O(1)`.

Pitfalls:

- the first test compares with an imagined YES, not with nothing;
- k(2y + 1) reaches about 1.25 · 10⁷, well within 64-bit integers,
  and is divided only at the end;
- n = 1 needs no special case, as the formula has no n − 1 left.

The formula matches an exhaustive enumeration of all orders for every
n up to 7 and every number of YES answers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1716_probability.cpp](1716_probability.cpp) | G++ 13.2 x64 | probability | O(1) | AC | 0.015 s | 140 KB |
| [1716_probability.go](1716_probability.go) | Go 1.14 x64 | probability | O(1) | AC | 0.031 s | 1084 KB |
| [1716_probability.java](1716_probability.java) | Java 1.8 | probability | O(1) | AC | 0.109 s | 1820 KB |
| [1716_probability.py](1716_probability.py) | Python 3.12 x64 | probability | O(1) | AC | 0.078 s | 416 KB |
| [1716_probability.rs](1716_probability.rs) | Rust 1.75 x64 | probability | O(1) | AC | 0.062 s | 268 KB |
