# 1408. Polynomial Multiplication

[Timus 1408](https://acm.timus.ru/problem.aspx?space=1&num=1408) · difficulty 1213 · parsing

Original problem by Vladimir Yakovlev, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two polynomials in variables a to z are given, one per line: terms
joined by + and -, each term a product of an optional coefficient (up
to 100, maybe with leading zeros, the first one maybe negative) and
factors X or X^N, with spaces anywhere. Print their product in a fixed
form: like terms and like factors merged, no zero terms or zero powers,
no coefficients or powers equal to 1 except for the term "1" and the
polynomial "0", factors in alphabetical order, terms by decreasing total
degree and then by decreasing power of a, of b and so on.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The two polynomials.

## Output

The product on one line, spaced as in the example.

## Examples

### Example 1

Input:

```
x*y*z + 4*x^2*y - 2*z*y*y^4 - 1
x + 7*z
```

Output:

```
-2*x*y^5*z - 14*y^5*z^2 + 4*x^3*y + 29*x^2*y*z + 7*x*y*z^2 - x - 7*z
```

## Solution

Drop every space first; then a polynomial is a sign, a term, a sign, a
term and so on. A term is factors joined by *: a number multiplies the
coefficient and a letter, with an optional ^ and a number, adds to the
power of that letter. Keep a polynomial as a map from the 26 powers to
the coefficient, so like terms add up as they are read. Multiply every
pair of terms, adding the powers and multiplying the coefficients, drop
the zero coefficients, and sort by total degree and then by the powers
from a to z, all decreasing. The first term carries a bare "-" when
negative, later ones " + " or " - "; the coefficient is printed unless
it is 1 and the term has a variable. `O(T₁·T₂·26)` for T₁ and T₂ terms.

Pitfalls:

- spaces can stand inside numbers and between ^ and the power (tests 07
  and 12);
- a zero product prints "0", even when one factor is 0 before any
  multiplication (tests 03 and 11);
- a power 0 and a coefficient 0 must vanish, a power 1 is not written
  (tests 06 and 07);
- the forum reports a test with lines longer than 100 characters, so
  the lines are read whole.

The tests include the cases from the forum and are judged by exact
comparison.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1408_parsing.cpp](1408_parsing.cpp) | G++ 13.2 x64 | parsing | O(T1·T2·26) | AC | 0.031 s | 504 KB |
| [1408_parsing.go](1408_parsing.go) | Go 1.14 x64 | parsing | O(T1·T2·26) | AC | 0.031 s | 2412 KB |
| [1408_parsing.java](1408_parsing.java) | Java 1.8 | parsing | O(T1·T2·26) | AC | 0.171 s | 6860 KB |
| [1408_parsing.py](1408_parsing.py) | Python 3.12 x64 | parsing | O(T1·T2·26) | AC | 0.078 s | 1272 KB |
| [1408_parsing.rs](1408_parsing.rs) | Rust 1.75 x64 | parsing | O(T1·T2·26) | AC | 0.015 s | 1132 KB |
