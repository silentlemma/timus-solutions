# 1393. Average Common Prefix

[Timus 1393](https://acm.timus.ru/problem.aspx?space=1&num=1393) · difficulty 1147 · strings

Original problem by Ilya Grebnov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

T is a string of n capital letters, 1 < n ≤ 250 000. Sort its n cyclic
shifts, equal ones included, and print the average length of the
longest common prefix of neighbouring shifts in this order, with at
least three digits after the point. Two equal shifts share all n
letters.

Time limit: 1.5 seconds. Memory limit: 16 MB.

## Input

n, then T.

## Output

The average common prefix.

## Examples

### Example 1

Input:

```
11
MISSISSIPPI
```

Output:

```
1.300
```

## Solution

Equal shifts make the order ambiguous and break the usual way of
finding common prefixes, so first strip them. Let p be the shortest
period of T as a cyclic string, found with the prefix function: T is a
word u of p letters repeated n / p times (p = n when there is no such
period). Every shift of T then appears n / p times in a row, which gives
p·(n / p − 1) neighbours with a common prefix of n. Two different shifts
of u differ within p letters, so their common prefix in T is the same
as in u.

The p rotations of u are all different. Sort them by prefix doubling
with counting sort: rotations sorted by their first 2ᵏ letters, then by
pairs of classes. Then Kasai's walk gives the common prefix of each
rotation with the one before it: going from rotation i to i + 1 loses
at most one letter, so the total work is linear. The answer is the sum
of both parts over n − 1, with the sum kept in 64 bits.
`O(n log n)`.

Pitfalls:

- equal shifts have a common prefix of n, not more: for AAAAA the
  answer is 5.000 (test 02 and generated test 2);
- the sum reaches about 6.25·10¹⁰ and needs 64 bits (generated test 2);
- a string of one letter but the last needs about log n doubling steps
  (generated test 3);
- the memory limit is 16 MB, so the arrays use 32-bit numbers.

The answers were compared on 1 500 random short strings, a third of
them periodic, with sorting all shifts and comparing them letter by
letter.

## Language notes

- Python finds p with `(T + T).find(T, 1)`, then builds the suffix array
  by induced sorting (SA-IS) in linear
  time instead of doubling, in flat `array` buffers and a `bytearray`,
  and runs under PyPy: on the judge it takes 0.42 s and 14 MB of the
  16 MB. The earlier version with doubling sorts and lists of integers
  exceeded the memory limit on the judge's test 30. `O(n)`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1393_strings.cpp](1393_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.109 s | 4928 KB |
| [1393_strings.go](1393_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.218 s | 9364 KB |
| [1393_strings.java](1393_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.218 s | 7948 KB |
| [1393_strings.py](1393_strings.py) | PyPy 3.10 x64 | strings | O(n) | AC | 0.421 s | 14104 KB |
| [1393_strings.rs](1393_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.109 s | 5504 KB |
