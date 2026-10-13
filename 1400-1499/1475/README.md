# 1475. Ryaba Hen

[Timus 1475](https://acm.timus.ru/problem.aspx?space=1&num=1475) · difficulty 3669 · math

Original problem by Alexander Ipatov (idea by Alexander Toropov), from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A roof's left slope rises from (0, 0) through (l, H), which is not its
top. An egg, treated as a point, is dropped from height h above (l, H),
falls with g = 10, bounces elastically off the slope (angle of incidence equals
angle of reflection, even at the very bottom), and so on until it
leaves the roof. Count the bounces for up to 1000 tests with
1 ≤ H, l ≤ 10¹⁰⁰ and 1 ≤ h ≤ 10.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

The number of tests, then lines H l h.

## Output

The number of bounces for each test.

## Examples

### Example 1

Input:

```
2
1 2 1
1 2 10
```

Output:

```
1
1
```

## Solution

Let the slope make angle a with the ground and take axes along it,
downhill, and across it. Gravity then has components g·sin a along and
−g·cos a across. The egg arrives with speed v = √(2gh) straight down;
after the bounce it moves away from the slope at v·cos a and downhill
at v·sin a. The motion across is the same after every bounce, so each
flight lasts 2v/g, while the speed along the slope grows by
2v·sin a per flight. Adding the flights up, the k-th bounce after the
first is 4h·sin a·k(k + 1) down the slope.

The slope from (l, H) to the bottom is L = √(l² + H²) long and
sin a = H / L, so that bounce happens when 4hH·k(k + 1) ≤ l² + H². With
q = ⌊(l² + H²) / (4hH)⌋ the largest such k satisfies (2k + 1)² ≤ 4q + 1,
so k = ⌊(⌊√(4q + 1)⌋ − 1) / 2⌋, and the answer is k + 1, counting the
first bounce. Complexities assume quadratic arithmetic on D-digit inputs.

Pitfalls:

- H and l reach 10¹⁰⁰ and their squares 10²⁰⁰, so everything must be
  exact integers; floating point misses the boundary (test 02, gen3);
- a bounce exactly at the bottom of the slope still counts (test 02);
- the answer is at least 1, even when h is large and the slope is
  short (tests 01, 03).

## Language notes

- C++ and Rust have no big integers built in: the solutions keep
  numbers as 32-bit limbs and set k bit by bit from the top, checking
  4hH·k(k + 1) ≤ l² + H² with multiplications only; that is `O(D³)`
  per test, still quick for 101 digits.
- Java 8 has no `BigInteger.sqrt`, so the square root is Newton's
  method.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1475_math.cpp](1475_math.cpp) | G++ 13.2 x64 | math | O(D^3) per test | AC | 0.046 s | 208 KB |
| [1475_math.go](1475_math.go) | Go 1.14 x64 | math | O(D^2 log D) per test | AC | 0.015 s | 2020 KB |
| [1475_math.java](1475_math.java) | Java 1.8 | math | O(D^2 log D) per test | AC | 0.125 s | 4748 KB |
| [1475_math.py](1475_math.py) | Python 3.12 x64 | math | O(D^2) per test | AC | 0.062 s | 604 KB |
| [1475_math.rs](1475_math.rs) | Rust 1.75 x64 | math | O(D^3) per test | AC | 0.046 s | 356 KB |
