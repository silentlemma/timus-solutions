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

## Optimized solutions

The optimized versions use the first and last supports to restrict the range of cuts to check. They stop scanning gaps once the left endpoint reaches the upper bound of that range.

Python 3.12 x64, submission 11319948. Time 0.156 → 0.156 s, memory 10892 → 8196 KB.

Rust 1.75 x64, submission 11319998. Time 0.015 → 0.015 s, memory 2664 → 596 KB.

Go 1.14 x64, submission 11320023. Time 0.078 → 0.031 s, memory 3336 → 1320 KB.

G++ 13.2 x64, submission 11320066. Time 0.093 → 0.015 s, memory 968 → 520 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321963 · Java 1.8 №11321964 · Python 3.12 x64 №11321965 · Rust 1.75 x64 №11321966 · Go 1.14 x64 №11322291.

Java 1.8, submission 11322007. Time 0.109 → 0.125 s, memory 1268 → 828 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1838_math.cpp](1838_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.093 s | 968 KB | 11321963 |
| [1838_math.go](1838_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.078 s | 3336 KB | 11322291 |
| [1838_math.java](1838_math.java) | Java 1.8 | math | O(n) | AC | 0.109 s | 1268 KB | 11321964 |
| [1838_math.py](1838_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.156 s | 10892 KB | 11321965 |
| [1838_math.rs](1838_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 2664 KB | 11321966 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1838_math_optimized.py](1838_math_optimized.py) | Python 3.12 x64 | math | O(n) | AC | 0.156 s | 8196 KB | 11319948 |
| [1838_math_optimized.rs](1838_math_optimized.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 596 KB | 11319998 |
| [1838_math_optimized.go](1838_math_optimized.go) \* | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1320 KB | 11320023 |
| [1838_math_optimized.cpp](1838_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 520 KB | 11320066 |
| [1838_math_optimized.java](1838_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 828 KB | 11322007 |

\* The marked versions have room to improve in the ratings.
