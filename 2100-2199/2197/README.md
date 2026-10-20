# 2197. The shortest repeating prefix of a string under block overwrites

[Timus 2197](https://acm.timus.ru/problem.aspx?space=1&num=2197) · difficulty 2200 · hashing, fenwick

Original problem by Konstantin Rychkov, from the ICPC Ural Regional Contest qualifier 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A string S of length N is printed as several copies of one of its
prefixes, and printing a prefix of length l once takes l² seconds. Q
times a pattern t_k from a fixed set overwrites S from position p.
Print the least printing time for the initial string and after each
overwrite. The limits are 3 seconds and 256 MB.

## Input

N, M and Q, 1 ≤ N ≤ 2 · 10⁵, 0 ≤ M, Q ≤ 2 · 10⁵, then S, then the M
patterns with total length up to 10⁶, then the overwrites p k.

## Output

Q + 1 times.

## Examples

### Example 1

Input:

```
4 3 3
abab
be
ebb
ee
3 1
1 2
2 3
```

Output:

```
8
16
16
4
```

## Solution

Printing N / l copies of a prefix of length l takes N · l seconds, so
the task is the shortest l that divides N and generates S.

The lengths that divide N and generate S are closed under gcd, so the
shortest one divides all the others. Starting from l = N, the solution
tries to divide l by each prime factor of N as long as the shorter
prefix still generates S; what remains is the shortest period. A
prefix of length c generates S exactly when the hash of S equals the
hash of the prefix repeated N / c times, a geometric sum
h(prefix) · (B^N − 1) / (B^c − 1), compared after multiplying out the
denominator. Two moduli make collisions negligible.

The hard part is hashing a string that changes by long overwrites.
All the text that can ever appear, S and every pattern, is put into one
source string with prefix hashes. The current S is a list of fragments,
each pointing to a piece of the source, and each fragment stores its
hash already shifted to its position in S, kept in a Fenwick tree by
starting position. An overwrite cuts the fragments at its two ends,
drops the ones inside, and adds one fragment for the pattern, so each
overwrite creates only a constant number of fragments. A prefix hash is
a Fenwick prefix sum over whole fragments plus the hash of the part of
the last fragment, read from the source. Answers are also cached by the
hash of the whole string.

In the example "abab" has period 2, so the time is 4 · 2 = 8, and
"eeee" has period 1, so it is 4.

Each query costs O(log N) per prime factor of N, and the overwrites
O(log N) per created or removed fragment.

## Language notes

- Python runs under PyPy and is accepted in 2.593 s of the 3 s. It also
  skips periods whose number of copies does not divide the sum of the
  character codes, since repeating a prefix repeats that sum. Under
  CPython 3.12 the largest tests here already take about 2.7 s, so it
  is not used.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2197_hashing_fenwick.cpp](2197_hashing_fenwick.cpp) | G++ 13.2 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 0.375 s | 32896 KB |
| [2197_hashing_fenwick.go](2197_hashing_fenwick.go) | Go 1.14 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 0.468 s | 65604 KB |
| [2197_hashing_fenwick.java](2197_hashing_fenwick.java) | Java 1.8 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 1.250 s | 71216 KB |
| [2197_hashing_fenwick.py](2197_hashing_fenwick.py) | PyPy 3.10 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 2.593 s | 94140 KB |
| [2197_hashing_fenwick.rs](2197_hashing_fenwick.rs) | Rust 1.75 x64 | hashing, fenwick | O((N + Q) log N · ω(N)) | AC | 0.328 s | 45500 KB |
