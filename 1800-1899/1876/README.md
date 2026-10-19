# 1876. Centipede's Morning

[Timus 1876](https://acm.timus.ru/problem.aspx?space=1&num=1876) · difficulty 55 · math

Original problem by Mikhail Rubinchik, from the Ural Regional School Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A centipede has 40 left and 40 right legs, and under the bed there are
a left and b right slippers. It first dresses the left legs: pulling
out a slipper takes a second. A left slipper goes on the next left leg.
A right slipper takes one more second, either to put it on a bare right
leg or, if all right legs are dressed, to throw it away. Then the right
legs are dressed the same way. How many seconds does it take in the
worst case?

## Input

a and b (40 ≤ a, b ≤ 100).

## Output

The worst-case number of seconds.

## Examples

### Example 1

Input:

```
40 40
```

Output:

```
120
```

## Solution

Let k right slippers come out while the left legs are being dressed;
the left phase costs 40 + 2k seconds. If k ≥ 40, all right legs are
already dressed and the right phase is empty. The worst such case
draws all b right slippers first: 2b + 40 seconds. If k < 40, the right
phase may first pull out all a − 40 spare left slippers at two seconds
each, then the 40 − k missing rights. The total is 2a + k, largest at
k = 39: 2a + 39. The answer is max(2b + 40, 2a + 39). `O(1)`.

With 40 slippers of each kind both ways give at most 120 seconds.

Pitfalls:

- the spare left slippers can only be drawn in the right phase, so the
  left phase must not dress all right legs: the worst is 39 of them;
- once all right legs are dressed, nothing more happens after the left
  phase;
- with a = 41 and b = 40 the second case already wins: 121 against
  120.

The formula agrees with a search over every order of drawing slippers
for all inputs, and with an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1876_math.cpp](1876_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1876_math.go](1876_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1076 KB |
| [1876_math.java](1876_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1600 KB |
| [1876_math.py](1876_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 376 KB |
| [1876_math.rs](1876_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB |
