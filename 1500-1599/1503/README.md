# 1503. Polynomial

[Timus 1503](https://acm.timus.ru/problem.aspx?space=1&num=1503) · difficulty 1710 · math

Original problem by Den Raskovalov, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a polynomial a0·x^N + a1·x^(N−1) + … + aN of degree N (1 ≤ N ≤ 5)
with integer coefficients (−100 ≤ ai ≤ 100, a0 ≠ 0), print all its real
roots in increasing order, each repeated as many times as its
multiplicity, to within 10⁻⁶.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the coefficients a0, a1, …, aN, one per line.

## Output

The real roots, one per line; nothing if there are none.

## Examples

### Example 1

Input:

```
2
1
-2
1
```

Output:

```
1
1
```

## Solution

Simple roots are easy: the polynomial changes sign at them, and between
two neighbouring sign changes of the derivative it is monotone, so it
changes sign at most once there. Find the derivative's sign changes the
same way, recursively, cut the interval |x| < 1 + max |ai / a0| (all roots
lie inside) at them, and bisect each piece where the signs at the ends
differ.

A root of even multiplicity does not change the sign, and an odd
multiple root is hard to pin down numerically, so first remove all
rational roots exactly, starting with zero. A rational root p/q in lowest
terms has p dividing aN and q dividing a0; test every such candidate
with exact arithmetic
(q^N·f(p/q) = 0) and divide it out by synthetic division by q·x − p,
which keeps integer coefficients. After that, a repeated real root is
irrational, and its algebraic conjugates repeat too, so the rest has
a squared quadratic with irrational roots as a factor. With degree at
most 5 and no rational roots left, that is only possible when the rest
is exactly a0·(x² + b·x + d)² of degree 4. Comparing coefficients, with
a0, …, a4 now the coefficients of that rest, u = 4·a0 and e = u·a2 − a1²,
this holds when 2·a1·e = a3·u² and e² = a4·u³. If a1² − 2e > 0, the
double roots are (−a1 ± √(a1² − 2e)) / u. Whatever remains has only simple
roots for the bisection.

Pitfalls:

- a double root only touches the axis, so a pure sign search misses it
  (test 01, the example);
- one root can have multiplicity 5 (test 02);
- repeated roots can be irrational (tests 03, 06, gen3);
- with no real roots the output is empty (test 04);
- a0 ≠ ±1 gives fractional rational roots (tests 05, 07);
- the root 0 does not fit the divisor search (every p divides 0), so
  strip zero constant terms first (test 08);
- the derivative's roots separate five simple roots for bisection
  (test 09);
- roots are compared with a tolerance, so the tests use a checker (all
  tests).

## Language notes

The C++ solution bisects in `long double` but prints a `double`: the
MinGW `printf` behind G++ on Windows may print `long double`
wrongly. Python approximates roots with `Fraction` and prints them as `float`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1503_math.cpp](1503_math.cpp) | G++ 13.2 x64 | math | O(N^3 * STEPS) | AC | 0.031 s | 220 KB |
| [1503_math.go](1503_math.go) | Go 1.14 x64 | math | O(N^3 * STEPS) | AC | 0.031 s | 1136 KB |
| [1503_math.java](1503_math.java) | Java 1.8 | math | O(N^3 * STEPS) | AC | 0.125 s | 1148 KB |
| [1503_math.py](1503_math.py) | Python 3.12 x64 | math | O(N^3 * STEPS) | AC | 0.140 s | 1144 KB |
| [1503_math.rs](1503_math.rs) | Rust 1.75 x64 | math | O(N^3 * STEPS) | AC | 0.046 s | 268 KB |
