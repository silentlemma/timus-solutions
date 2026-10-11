# 1259. How to become a star

[Timus 1259](https://acm.timus.ru/problem.aspx?space=1&num=1259) · difficulty 398 · math

Original problem by Pavel Egorov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Fix an angle α with 0 < α < π. A polyline starts with the segment from
(0, 0) to (1, 0); each next segment is the previous one rotated by α
counterclockwise about its free end. The construction stops as soon as
the polyline closes, and the result is a star whose number of vertices
is the number of segments. How many different stars have exactly N
vertices (3 ≤ N ≤ 100 000)?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The number of stars with N vertices.

## Examples

### Example 1

Input:

```
5
```

Output:

```
2
```

### Example 2

Input:

```
9
```

Output:

```
3
```

## Solution

Rotating a segment about its far end by α makes the next segment point
in the direction of the previous one turned by β = α + π. So the
segments are unit vectors at angles 0, β, 2β, …, and the polyline closes
after k segments exactly when their sum is zero:

```text
1 + e^{iβ} + … + e^{i(k−1)β} = 0  ⇔  e^{ikβ} = 1 and e^{iβ} ≠ 1
```

Closing first after N segments means β = 2πm / N with gcd(m, N) = 1.
Since π < β < 2π, m runs over N/2 < m < N. The numbers coprime to N
come in pairs m and N − m, one on each side of N/2 (for N ≥ 3 neither
equals N/2), so the answer is φ(N) / 2, with Euler's totient φ found by
trial division. `O(√N)`.

Pitfalls:

- only turns between π and 2π are allowed, so the answer is half of
  φ(N), not all of it (a star and its mirror image are different
  polylines, but only one of them turns counterclockwise by α < π);
- a star must close for the first time at N: angles with gcd(m, N) > 1
  close earlier and give stars with fewer vertices.

The formula was compared for every N from 3 to 299 with summing the unit
steps for each candidate angle and noting when the sum first returns
to zero.

## Language notes

- All languages compute the totient by trial division.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1259_math.cpp](1259_math.cpp) | G++ 13.2 x64 | math | O(√N) | AC | 0.015 s | 128 KB |
| [1259_math.go](1259_math.go) | Go 1.14 x64 | math | O(√N) | AC | 0.031 s | 1076 KB |
| [1259_math.java](1259_math.java) | Java 1.8 | math | O(√N) | AC | 0.125 s | 1580 KB |
| [1259_math.py](1259_math.py) | Python 3.12 x64 | math | O(√N) | AC | 0.062 s | 424 KB |
| [1259_math.rs](1259_math.rs) | Rust 1.75 x64 | math | O(√N) | AC | 0.015 s | 224 KB |
