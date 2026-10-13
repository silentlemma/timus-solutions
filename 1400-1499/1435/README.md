# 1435. Financial Error

[Timus 1435](https://acm.timus.ru/problem.aspx?space=1&num=1435) · difficulty 994 · math

Original problem by Evgeny Krokhalev, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N numbers (N ≤ 200 000, each at most 2³¹ − 1) were copied from a
report, and their sum differs from the report's total (at most 10¹⁶).
The copying mistake swapped two neighbouring digits of one number;
neither the copy nor the true number has leading zeros. Print "Input
has no error." if the sums agree, "Error in record #L. Correct number
is: K." for a record that a swap explains, or "Unrecoverable error."

Time limit: 0.4 seconds. Memory limit: 64 MB.

## Input

N, the N copied numbers, then the report's total.

## Output

One of the three lines.

## Examples

### Example 1

Input:

```
3
12
26
45
119
```

Output:

```
Error in record #2. Correct number is: 62.
```

## Solution

Swapping the digits a at 10^(i+1) and b at 10^i changes a number by
(b − a)·10^(i+1) + (a − b)·10^i = 9·(b − a)·10^i. So the difference D
between the total and the sum must be 9 times c·10^i with 1 ≤ |c| ≤ 9:
divide D by 9, strip the factors of 10 to get i, and what is left is c.
Then scan the records as strings for one whose digits at 10^(i+1) and
10^i differ by exactly c, skipping a swap that would move a zero to the
front, and report the first such record with the two digits swapped
back. `O(N)`.

Pitfalls:

- the true number may exceed 32 bits, as in 1900000000 for
  9100000000 (test 04);
- 90 cannot be a copy of 09 and 10 not of 01 (tests 02, 06);
- the total itself was not miscopied (test 07);
- reading 200 000 numbers within 0.4 seconds needs fast input; the
  solutions read everything at once.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1435_math.cpp](1435_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.046 s | 8972 KB |
| [1435_math.go](1435_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.093 s | 14588 KB |
| [1435_math.java](1435_math.java) | Java 1.8 | math | O(N) | AC | 0.171 s | 18360 KB |
| [1435_math.py](1435_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.187 s | 15852 KB |
| [1435_math.rs](1435_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 8336 KB |
