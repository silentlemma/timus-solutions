# 1577. E-mail

[Timus 1577](https://acm.timus.ru/problem.aspx?space=1&num=1577) · difficulty 469 · dp

Original problem by Igor Chevdar, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A server accepts a typed string when the real password is a
subsequence of it. Vasya has two passwords of lowercase letters, each up
to 2000 letters long, and wants one string accepted by both servers.
Count the different strings of the least possible length that contain
both passwords as subsequences, modulo 10⁹ + 7.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The two passwords, one per line.

## Output

The number of shortest common strings modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
b
ab
```

Output:

```
1
```

### Example 2

Input:

```
abcab
cba
```

Output:

```
4
```

## Solution

These are the shortest common supersequences of the two passwords a
and b. For the suffixes a[i:] and b[j:] keep their least length L(i, j)
and the number C(i, j) of different strings of that length. If a[i] =
b[j], every such string begins with that letter, and the rest is a
shortest one for a[i+1:] and b[j+1:]. Otherwise it begins with a[i] or
with b[j], and the rest is a shortest one for a[i+1:], b[j:] or for
a[i:], b[j+1:]. Strings with different first letters are different, so
the counts of the branches that reach the least length simply add up;
nothing is counted twice.

When one suffix is empty, the other one itself is the only answer. The
rows are filled from the ends of the passwords back, and row i needs
only row i + 1, so two rows suffice. `O(|a|·|b|)`, 4·10⁶ steps. The
results were checked against listing all strings of the least length on
250 random pairs of short passwords.

Pitfalls:

- different ways of interleaving can give the same string, as `aa` from
  `a` and `a`, so the count is over strings, not over ways (tests 03,
  05);
- passwords without a common letter give every interleaving,
  C(|a| + |b|, |a|), which needs the modulus (test gen4);
- Python runs under PyPy: the largest tests take about 1–2.5 s with
  CPython against a limit of 1 s, and about 0.15 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1577_dp.cpp](1577_dp.cpp) | G++ 13.2 x64 | dp | O(len(a) · len(b)) | AC | 0.031 s | 424 KB |
| [1577_dp.go](1577_dp.go) | Go 1.14 x64 | dp | O(len(a) · len(b)) | AC | 0.046 s | 1180 KB |
| [1577_dp.java](1577_dp.java) | Java 1.8 | dp | O(len(a) · len(b)) | AC | 0.187 s | 632 KB |
| [1577_dp.py](1577_dp.py) | PyPy 3.10 x64 | dp | O(len(a) · len(b)) | AC | 0.218 s | 8184 KB |
| [1577_dp.rs](1577_dp.rs) | Rust 1.75 x64 | dp | O(len(a) · len(b)) | AC | 0.031 s | 280 KB |
