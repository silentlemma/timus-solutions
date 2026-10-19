# 1838. Samurai's Stroke

[Timus 1838](https://acm.timus.ru/problem.aspx?space=1&num=1838) · difficulty 720 · math

Original problem by Denis Dublennykh, from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A bamboo stalk of length l lies on n supports. It is cut at one point
into two parts, and a part falls unless its centre of mass lies between
two supports under it. Find the total length of the points where a cut
makes at least one part fall, rounded up.

## Input

l and n (3 ≤ l ≤ 10⁹, 2 ≤ n ≤ 10⁵), then the n distinct support
positions in increasing order, all strictly between 0 and l. The whole
stalk lies stably.

## Output

The total length of the points where a part falls, rounded up.

## Examples

### Example 1

Input:

```
5 4
1 2 3 4
```

Output:

```
4
```

## Solution

Cut at x between supports sᵢ and sᵢ₊₁. The left part [0, x] rests on
s₁, …, sᵢ and stands when its centre x/2 lies in [s₁, sᵢ]; the right
part [x, l] rests on sᵢ₊₁, …, sₙ and stands when (x + l)/2 lies in
[sᵢ₊₁, sₙ]. So on this gap both stand for x in

[max(sᵢ, 2s₁, 2sᵢ₊₁ − l), min(sᵢ₊₁, 2sₙ − l, 2sᵢ)],

and a cut left of s₁ or right of sₙ always drops a part. Summing the
safe lengths over the n − 1 gaps and subtracting from l gives the
answer. Every bound is an integer, so the rounding never changes it.
`O(n)`.

In the example only the gap (2, 3) is safe: there the left centre x/2
is between 1 and 2, and the right centre (x + 5)/2 between 3 and 4. So
4 of the 5 units are painted.

Pitfalls:

- a part needs two supports under it, so a cut before the second
  support always drops the left part;
- single points, such as cuts right at a support, have no length and do
  not matter;
- 2sₙ stays below 2·10⁹ and fits in signed 32-bit integers.

The answers agree with a fine-grid count of the falling cuts on a few
hundred small stalks and with an independent accepted implementation
on the large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1838_math.cpp](1838_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.093 s | 984 KB |
| [1838_math.go](1838_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.078 s | 3324 KB |
| [1838_math.java](1838_math.java) | Java 1.8 | math | O(n) | AC | 0.093 s | 1300 KB |
| [1838_math.py](1838_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.171 s | 11024 KB |
| [1838_math.rs](1838_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 2668 KB |
