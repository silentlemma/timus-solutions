# 1448. Lighting in Hogwarts

[Timus 1448](https://acm.timus.ru/problem.aspx?space=1&num=1448) · difficulty 580 · constructive

Original problem by Alexander Mironenko (idea) and Stanislav Vasiliev (text and programming), from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A corridor has N lamps in a row (1 ≤ N ≤ 10⁶), each fully on or off.
Argus Filch wants brightness b percent (0 ≤ b ≤ 100) spread as evenly as
possible: print a row of N digits 0 and 1 such that on every stretch of
L consecutive lamps the number of lamps on differs from L b / 100 by at
most 2.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then b.

## Output

The row of lamps. Any fitting row is accepted.

## Examples

### Example 1

Input:

```
10
33
```

Output:

```
0100100100
```

## Solution

Turn lamp i (counting from 0) on exactly when ⌊(i + 1) b / 100⌋ is
larger than ⌊i b / 100⌋. Then the lamps on among the first k number
⌊k b / 100⌋, so a stretch from l to r holds ⌊r b / 100⌋ − ⌊l b / 100⌋
lamps, which differs from (r − l) b / 100 by less than 1, well within
the allowed 2. The pattern repeats every 100 lamps, since adding 100 to
i adds exactly b to both floors. `O(N)`.

Pitfalls:

- b = 0 and b = 100 give rows of identical digits (tests 02, 03, 05, gen1,
  gen2);
- buffer output for up to a million digits to avoid per-digit calls
  (gen1 to gen7);
- the row of the example is only one of many valid answers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1448_constructive.cpp](1448_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1164 KB |
| [1448_constructive.go](1448_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 2088 KB |
| [1448_constructive.java](1448_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 3036 KB |
| [1448_constructive.py](1448_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 2244 KB |
| [1448_constructive.rs](1448_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 2056 KB |
