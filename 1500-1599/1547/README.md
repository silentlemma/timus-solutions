# 1547. Password Search

[Timus 1547](https://acm.timus.ru/problem.aspx?space=1&num=1547) · difficulty 857 · math

Original problem by Vladimir Yakovlev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

All passwords of lowercase letters of length 1 to N are listed by
length and then alphabetically: a, …, z, aa, …, zz, …. Split the list
into M consecutive ranges as evenly as possible, the first ranges one
longer when needed, and print each range as first-last
(1 ≤ N, M ≤ 50; there are at least M passwords).

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M.

## Output

M lines "first-last".

## Examples

### Example 1

Input:

```
5 4
```

Output:

```
a-fssst
fsssu-mmmmn
mmmmo-tgggg
tgggh-zzzzz
```

## Solution

There are T = 26 + 26² + … + 26ᴺ passwords, up to about 6·10⁷⁰. With
T = q·M + r, processor i (from 0) covers the passwords numbered from
i·q + min(i, r) + 1 to (i + 1)·q + min(i + 1, r).

Listing strings by length and then alphabetically is bijective base 26:
the k-th password (from 1) is k written with digits a = 1, …, z = 26.
To convert, repeatedly take (k − 1) mod 26 as the last letter and go on
with ⌊(k − 1) / 26⌋.

Python, Go and Java use their big integers. C++ and Rust keep numbers
as base-26 digit lists: T is 11…10 in base 26, division by M is long
division, the range ends are q times a small number plus a small
number, and the conversion subtracts 1 and drops the lowest digit.
`O(M·N)` digit operations.

Pitfalls:

- a range of one password is still printed as first-last, like a-a
  (test 03);
- the counts reach 71 digits (test 04);
- the first T mod M processors take the extra passwords (test 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1547_math.cpp](1547_math.cpp) | G++ 13.2 x64 | math | O(M * N) | AC | 0.015 s | 200 KB |
| [1547_math.go](1547_math.go) | Go 1.14 x64 | math | O(M * N) | AC | 0.031 s | 1348 KB |
| [1547_math.java](1547_math.java) | Java 1.8 | math | O(M * N) | AC | 0.125 s | 3264 KB |
| [1547_math.py](1547_math.py) | Python 3.12 x64 | math | O(M * N) | AC | 0.093 s | 400 KB |
| [1547_math.rs](1547_math.rs) | Rust 1.75 x64 | math | O(M * N) | AC | 0.015 s | 240 KB |
