# 1385. Interesting Number

[Timus 1385](https://acm.timus.ru/problem.aspx?space=1&num=1385) · difficulty 247 · math

Original problem by Alexander Ipatov, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A number with 2N digits and no leading zero is interesting if it is
divisible both by the number made of its first N digits and by the
number made of its last N digits. Count the interesting numbers with
2N digits, 1 ≤ N ≤ 10 000.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number N.

## Output

The count.

## Examples

### Example 1

Input:

```
1
```

Output:

```
14
```

The fourteen numbers are 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77,
88 and 99.

## Solution

Write the number as A·10ᴺ + B with A of N digits and B < 10ᴺ. A divides
the number exactly when it divides B, so B = kA, and B < 10ᴺ ≤ 10A
leaves k from 1 to 9 (B = 0 cannot divide anything). Then B divides the
number exactly when kA divides A·10ᴺ, that is, when k divides 10ᴺ: k is
1, 2 or 5, plus 4 from N = 2 and 8 from N = 3. For each k, A runs from
10ᴺ⁻¹ while kA < 10ᴺ, which gives ⌈10ᴺ/k⌉ − 10ᴺ⁻¹ numbers.

So the answer is 14 for N = 1 and 155 for N = 2. From N = 3 on it is
900 + 400 + 150 + 100 + 25 = 1575 times 10ᴺ⁻³: the digits 1575 and
N − 3 zeros. `O(N)` for the output.

Pitfalls:

- the answer has up to 10 001 digits, so it is printed as a string
  (test 05);
- 4 does not divide 10 and 8 does not divide 100, so N = 1 and N = 2 are special
  (tests 01 and 02).

The counts for N up to 3 were checked by trying every number.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1385_math.cpp](1385_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 372 KB |
| [1385_math.go](1385_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1116 KB |
| [1385_math.java](1385_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 1648 KB |
| [1385_math.py](1385_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 392 KB |
| [1385_math.rs](1385_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 224 KB |
