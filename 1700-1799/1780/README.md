# 1780. Gray Code

[Timus 1780](https://acm.timus.ru/problem.aspx?space=1&num=1780) · difficulty 894 · dp

Original problem by Dmitry Poletaev, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The reflected binary Gray code of length n lists all n-digit binary
strings; the string at position k is the Gray code of k. A paper holds
k and its code x in binary, of equal length, with some digits rubbed out
and shown as `?`. Restore both numbers if this can be done in exactly
one way.

## Input

k and x, each a string of 0, 1 and ? of the same length, at most 10⁵,
possibly with leading zeros.

## Output

The restored k and x, or `Ambiguity` if there are several ways, or
`Impossible` if there are none.

## Examples

### Example 1

Input:

```
0?1
0?0
```

Output:

```
011
010
```

### Example 2

Input:

```
?00
??0
```

Output:

```
Ambiguity
```

### Example 3

Input:

```
100
100
```

Output:

```
Impossible
```

## Solution

The list built by reflecting and prefixing puts at position k the
number k xor (k shifted right by one), so digit i of x, counted from
the left, is digit i of k xor digit i − 1 of k, with a 0 before the
first digit. Going from left to right, the readings of the first digits
can be counted by the last digit of k: a reading ending in k(i) = b
extends one ending in k(i − 1) = c when the paper allows k(i) = b and
x(i) = b xor c. The counts are capped at 2, which is all the answer
needs.

If exactly one reading exists, it is recovered from the end: at each
step only one earlier digit with a reading of its own leads on, and the
code digits follow from k. `O(n)`.

In the first example the middle digit of k must be 1, since a 0 would
give a code digit of 1 at the end, while the code ends in 0: k = 011,
x = 010.

Pitfalls:

- the first code digit equals the first digit of k;
- the counts can grow like 2ⁿ, so they are capped;
- leading zeros are part of the strings and must be kept.

The answers agree with a search over every k of up to 10 digits on 600
random papers and with an independent accepted implementation on 60
papers of up to 10⁵ digits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1780_dp.cpp](1780_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 1404 KB |
| [1780_dp.go](1780_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.046 s | 3692 KB |
| [1780_dp.java](1780_dp.java) | Java 1.8 | dp | O(n) | AC | 0.140 s | 5852 KB |
| [1780_dp.py](1780_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.234 s | 11024 KB |
| [1780_dp.rs](1780_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.046 s | 1496 KB |
