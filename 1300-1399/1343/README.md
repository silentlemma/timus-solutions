# 1343. Fairy Tale

[Timus 1343](https://acm.timus.ru/problem.aspx?space=1&num=1343) · difficulty 417 · number_theory

Original problem by Pavel Atnashev, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The first k of 12 digits are given, 0 ≤ k ≤ 12. Print any 12-digit
number that starts with them and has no divisors other than 1 and
itself. An answer is guaranteed to exist.

Time limit: 1 second. Memory limit: 64 MB.

## Input

k on the first line, the k digits on the second.

## Output

The 12-digit number.

## Checking

The checker accepts any 12 digits that start with the given ones and
make a number with no other divisors.

## Examples

### Example 1

Input:

```
5
64631
```

Output:

```
646310554187
```

## Solution

Fill the free digits with zeros and count upwards until the number is
prime. Primes near 10¹² lie about 28 apart on average, and no gap below
10¹² is longer than a few hundred, so only a few hundred numbers are
ever tried. Each one is tested with the Miller–Rabin test using the
bases 2, 3, 5, 7, 11 and 13, which make no mistakes below 3 · 10¹².
With all 12 digits given, the number itself is the answer. The
number is printed with leading zeros, as a prefix of zeros asks for.

Pitfalls:

- the given digits can start with zeros, and the answer must keep them,
  like `000000000002` (tests 04 and 05);
- the squares inside the test reach 10²⁴, past 64 bits, so the
  multiplication modulo n needs care;
- with k = 0 the second line is empty (test 02).

## Language notes

- C++ and Rust multiply in 128 bits, and Go uses `bits.Mul64` and
  `bits.Rem64`. Java splits one factor into 20-bit halves, which keeps
  every product below 2⁶⁰ for n below 2⁴⁰.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1343_number_theory.cpp](1343_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(G·log N) | AC | 0.015 s | 392 KB |
| [1343_number_theory.go](1343_number_theory.go) | Go 1.14 x64 | number_theory | O(G·log N) | AC | 0.031 s | 1024 KB |
| [1343_number_theory.java](1343_number_theory.java) | Java 1.8 | number_theory | O(G·log N) | AC | 0.125 s | 1752 KB |
| [1343_number_theory.py](1343_number_theory.py) | Python 3.12 x64 | number_theory | O(G·log N) | AC | 0.078 s | 524 KB |
| [1343_number_theory.rs](1343_number_theory.rs) | Rust 1.75 x64 | number_theory | O(G·log N) | AC | 0.046 s | 216 KB |
