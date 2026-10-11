# 1274. Fractional arithmetic

[Timus 1274](https://acm.timus.ru/problem.aspx?space=1&num=1274) · difficulty 678 · math

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Add, subtract, multiply or divide two fractions written as mixed
numbers, such as `-7 3/4`, `8 1/2`, `-7/11`, `0` or `11`. The sign is
written only for negative numbers, a zero integer part is left out
when there is a fraction, and the fraction is left out when it is zero.
Input fractions may be reducible; the answer must be written the same
way, fully reduced. Integer parts and numerators are at most 30 000,
denominators from 1 to 30 000, for the input and the answer alike.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The first fraction, the operation sign, the second fraction, each on
its own line.

## Output

The result.

## Examples

### Example 1

Input:

```
-3 1/6
+
2/4
```

Output:

```
-2 2/3
```

## Solution

Turn each operand into a signed numerator over a denominator:
w n/d becomes ±(w·d + n)/d. Apply the operation with the usual
formulas, move a negative denominator's sign to the numerator, and
divide both by their greatest common divisor. Then write the sign, the
integer part and the remainder over the denominator, leaving out
whichever parts are zero. Intermediate products stay below 10¹⁸, well
inside 64 bits. `O(log 30000)`.

Pitfalls:

- a zero result is written `0`, without a sign (tests 02, 09);
- an integer result has no fraction part, and a result of magnitude below
  one has no integer part (tests 04, 06);
- dividing by a negative number moves the sign into the denominator,
  which must be moved back (test 04);
- the operation `-` on its own line must not be mistaken for the sign of
  a fraction.

The answers were compared with Python's `Fraction` on 300 generated
cases.

## Language notes

- All languages parse the fraction from its words, keeping the sign
  apart, and print with the same three cases.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1274_math.cpp](1274_math.cpp) | G++ 13.2 x64 | math | O(log 30000) | AC | 0.015 s | 424 KB |
| [1274_math.go](1274_math.go) | Go 1.14 x64 | math | O(log 30000) | AC | 0.031 s | 1068 KB |
| [1274_math.java](1274_math.java) | Java 1.8 | math | O(log 30000) | AC | 0.109 s | 784 KB |
| [1274_math.py](1274_math.py) | Python 3.12 x64 | math | O(log 30000) | AC | 0.078 s | 544 KB |
| [1274_math.rs](1274_math.rs) | Rust 1.75 x64 | math | O(log 30000) | AC | 0.031 s | 244 KB |
