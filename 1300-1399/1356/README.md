# 1356. Something Easier

[Timus 1356](https://acm.timus.ru/problem.aspx?space=1&num=1356) · difficulty 298 · number_theory

Original problem by Aleksandr Bikbaev, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each of T ≤ 20 numbers N, 2 ≤ N ≤ 10⁹, write N as a sum of as few
primes as possible and print those primes.

Time limit: 1 second. Memory limit: 64 MB.

## Input

T, then T lines with N.

## Output

For each N, one line with the primes. Any sum with the fewest primes is
accepted.

## Examples

### Example 1

Input:

```
7
2
27
85
192
14983
3
7
```

Output:

```
2
23 2 2
2 83
11 181
14983
3
7
```

## Solution

- If N is prime, one prime is enough.
- If N is even, two primes are enough: Goldbach's conjecture is unproven
  but has been checked far beyond 10⁹. Try p = 2, 3, 4, … until p and
  N − p are both prime.
- If N is odd, a sum of two primes must contain 2, since two odd primes
  add up to an even number. So two primes work exactly when N − 2 is
  prime.
- Otherwise three primes are needed and enough: take the largest prime
  p ≤ N − 4. The rest N − p is even and at least 4, so it splits into
  two primes as above.

Primality is tested with Miller–Rabin on bases 2, 3, 5, 7, which is
exact for every number below 3.2·10⁹. Prime gaps below 10⁹ are under
300, and over 200 000 even numbers just below 10⁹ the smallest
Goldbach prime never exceeded 919, so each answer needs only a few
hundred tests. `O(T · g · log N)`, with g the number of candidates
tried.

Pitfalls:

- an odd N never splits into two odd primes, so the case with 2 must
  be checked separately (`85 = 2 + 83` in the example);
- 4 = 2 + 2 is the only even split that uses 2 (test 03);
- the rest after the largest prime must be at least 4, since 2 is not
  a sum of two primes;
- T can be 0 (test 04).

The answers were checked to be primes with the right sum and the fewest
terms for every N up to 20 000 and for 2 000 random N up to 10⁹, and
the Miller–Rabin test was compared with trial division on 203 000
numbers. The tests are judged by a checker that accepts any shortest
sum.

## Language notes

- The products in Miller–Rabin stay below 10¹⁸, so 64-bit integers are
  enough in every language.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1356_number_theory.cpp](1356_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·g·log N) | AC | 0.015 s | 192 KB |
| [1356_number_theory.go](1356_number_theory.go) | Go 1.14 x64 | number_theory | O(T·g·log N) | AC | 0.031 s | 1100 KB |
| [1356_number_theory.java](1356_number_theory.java) | Java 1.8 | number_theory | O(T·g·log N) | AC | 0.109 s | 516 KB |
| [1356_number_theory.py](1356_number_theory.py) | Python 3.12 x64 | number_theory | O(T·g·log N) | AC | 0.109 s | 664 KB |
| [1356_number_theory.rs](1356_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·g·log N) | AC | 0.015 s | 224 KB |
