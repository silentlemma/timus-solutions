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

## Optimized solutions

Go parses the digits directly from the buffered input bytes. Go 1.14 x64, submission 11318448. Time 0.031 → 0.015 s, memory 1068 → 968 KB.

Python reads byte strings and reduces the fractional remainder after extracting the whole part. Python 3.12 x64, submission 11318456. Time 0.078 → 0.093 s, memory 544 → 540 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321879 · Go 1.14 x64 №11322040 · Java 1.8 №11322043 · Python 3.12 x64 №11322042 · Rust 1.75 x64 №11322044.

Java reuses a fixed byte buffer to read each line and parses the digits in place. Java 1.8, submission 11321991. Time 0.109 → 0.078 s, memory 784 → 356 KB.

Rust reduces the fraction with Euclid's algorithm and formats the integers into a fixed buffer. Rust 1.75 x64, submission 11323303. Time 0.046 → 0.062 s, memory 232 → 44 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1274_math.cpp](1274_math.cpp) | G++ 13.2 x64 | math | O(log 30000) | AC | 0.015 s | 408 KB | 11321879 |
| [1274_math.go](1274_math.go) | Go 1.14 x64 | math | O(log 30000) | AC | 0.046 s | 1048 KB | 11322040 |
| [1274_math.java](1274_math.java) | Java 1.8 | math | O(log 30000) | AC | 0.093 s | 740 KB | 11322043 |
| [1274_math.py](1274_math.py) | Python 3.12 x64 | math | O(log 30000) | AC | 0.078 s | 556 KB | 11322042 |
| [1274_math.rs](1274_math.rs) | Rust 1.75 x64 | math | O(log 30000) | AC | 0.046 s | 232 KB | 11322044 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1274_math_optimized.go](1274_math_optimized.go) \* | Go 1.14 x64 | math | O(log 30000) | AC | 0.015 s | 968 KB | 11318448 |
| [1274_math_optimized.py](1274_math_optimized.py) \* | Python 3.12 x64 | math | O(log 30000) | AC | 0.093 s | 540 KB | 11318456 |
| [1274_math_optimized.java](1274_math_optimized.java) | Java 1.8 | math | O(log 30000) | AC | 0.078 s | 356 KB | 11321991 |
| [1274_math_optimized.rs](1274_math_optimized.rs) \* | Rust 1.75 x64 | math | O(log 30000) | AC | 0.062 s | 44 KB | 11323303 |

\* The marked versions have room to improve in the ratings.
