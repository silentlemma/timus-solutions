# 1595. Perfect Sequence

[Timus 1595](https://acm.timus.ru/problem.aspx?space=1&num=1595) · difficulty 1162 · constructive

Original problem by Alexander Bacherikov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Print a sequence of distinct positive integers, each at most 10¹³, that
contains all of 1, 2, …, N (1 ≤ N ≤ 250000), has at most 2N terms, and
in which the sum of the first k terms is divisible by k for every k. Any
such sequence is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The sequence, separated by spaces.

## Examples

### Example 1

Input:

```
3
```

Output:

```
1 3 2 6 8
```

## Solution

Place the numbers 1, 2, …, N in order, each after one extra term x: with
S the sum so far and k the position for x, x must make S + x divisible by
k, and then S + x + m divisible by k + 1 for the next number m. So
x ≡ a = −S (mod k) and x ≡ b = −S − m (mod k + 1). Since k and k + 1 are
coprime, the Chinese remainder theorem gives one class modulo k(k + 1),
and it is easy to write down: x = a + k·t, and k ≡ −1 (mod k + 1), so
t ≡ a − b (mod k + 1), with no inverse needed. Taking the first x of the
class above N keeps it apart from 1..N, and stepping by k(k + 1) past
the rare earlier extra terms keeps all terms distinct. The sequence has
exactly 2N terms, and `O(N)` steps with a hash set build it.

Each x stays below N + k(k + 1) unless it has to skip a used value, and
k < 2N, so the terms stay far below 10¹³; for N = 250000 the largest is
about 5·10⁸. The tests use a checker, which was run on every N up to
300 and on the largest N.

Pitfalls:

- the example answer is only one of many; the checker accepts any valid
  sequence;
- the prefix sums reach about 6·10¹³, beyond 32-bit integers;
- 500000 numbers make several megabytes of output, so the output is
  buffered rather than written number by number.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1595_constructive.cpp](1595_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.109 s | 17152 KB |
| [1595_constructive.go](1595_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.109 s | 11600 KB |
| [1595_constructive.java](1595_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.328 s | 34196 KB |
| [1595_constructive.py](1595_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.500 s | 18112 KB |
| [1595_constructive.rs](1595_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.078 s | 12540 KB |
