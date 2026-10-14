# 1528. Sequence

[Timus 1528](https://acm.timus.ru/problem.aspx?space=1&num=1528) · difficulty 272 · math

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

With f(1) = g(1) = 1,
f(n) = 1 + f(1)g(1) + … + f(n − 1)g(n − 1) and
g(n) = 1 + 2g(1) + … + 2g(n − 1) − g(n − 1)². For up to 5000 cases
(1 ≤ n ≤ 10000, 2 ≤ p ≤ 2·10⁹), print f(n) mod p.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

Pairs n and p, one per line, ending with 0 0.

## Output

f(n) mod p for each case.

## Examples

### Example 1

Input:

```
1 2
2 11
0 0
```

Output:

```
1
2
```

## Solution

Both sequences have closed forms. If g(i) = i for i < n, then
g(n) = 1 + (n − 1)n − (n − 1)² = n. Then f(n) − f(n − 1) =
f(n − 1)·(n − 1), so f(n) = n·f(n − 1) = n!. So each case asks for
n! mod p. When n ≥ p, p itself is one of the factors and the answer
is 0. Otherwise multiply up to n, reducing modulo p as you go; the
products stay below 2·10¹³, within 64 bits. That is up to 5·10⁷
multiplications for all cases, fast in compiled languages (O(n) per case). In Python
the plain loop takes about 6 seconds, so the Python solution keeps the
exact factorials of every multiple of 100 as big integers and reduces
one of them, then multiplies at most 99 more factors: O(n log n) bit
operations per case.

Pitfalls:

- the formulas look heavy, but g(n) = n and f(n) = n! (all tests);
- n ≥ p gives 0 at once (test 02, gen3);
- p reaches 2·10⁹, so the products need 64 bits (test 03, gen1);
- a prime p just above n is a good check: Wilson's theorem gives
  (p − 1)! ≡ −1 (test 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1528_math.cpp](1528_math.cpp) | G++ 13.2 x64 | math | O(n) per case | AC | 0.328 s | 132 KB |
| [1528_math.go](1528_math.go) | Go 1.14 x64 | math | O(n) per case | AC | 0.343 s | 1224 KB |
| [1528_math.java](1528_math.java) | Java 1.8 | math | O(n) per case | AC | 0.609 s | 904 KB |
| [1528_math.py](1528_math.py) | Python 3.12 x64 | math | O(n log n) bit operations per case | AC | 0.359 s | 17900 KB |
| [1528_math.rs](1528_math.rs) | Rust 1.75 x64 | math | O(n) per case | AC | 0.250 s | 520 KB |
