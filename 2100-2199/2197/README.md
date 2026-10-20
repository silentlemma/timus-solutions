# 2197. The shortest repeating prefix of a string under block overwrites

[Timus 2197](https://acm.timus.ru/problem.aspx?space=1&num=2197) · difficulty 1669 · hashing, fenwick

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
prefix of length c is tested by comparing the hash of S with the hash
of the prefix repeated N / c times, a geometric sum
h(prefix) · (B^N − 1) / (B^c − 1), compared after multiplying out the
denominator. For the two moduli, independently sample a base at each
run from 257 through modulus − 2. Resample if either B^N = 1 modulo its
modulus; since c divides N, this also ensures B^c − 1 is nonzero.
Hash equality is probabilistic, not an exact string comparison.

Pitfall: fixed public bases allow deliberately constructed collisions.
Tests 17 and 18 are nonconstant strings of prime length 17 that collide
with a constant string under the former parameters, even with equal
character sums. Their answer is 289, not 17. The same randomized bases
must be used for period checks, cached answers and unchanged-overwrite
checks; the algorithm still has a nonzero collision probability.

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

Let L be the total dictionary length. Each answer makes O(log N)
candidate checks, counting repeated removal of the same prime factor,
and each check costs O(log N). Overwrites cost O(log N) per created or
removed fragment; only O(N + Q) fragments are created overall. Including
input and preprocessing, expected total time is O(L + (N + Q + 1) log² N)
and space is O(L + N + Q), taking log N to be at least 1.

## Language notes

- Python also skips periods whose number of copies does not divide
  the sum of the character codes, since repeating a prefix repeats
  that sum. The table retains the published PyPy measurements; they
  have not been remeasured for the randomized version. CPython 3.12 and
  PyPy 3.10 were unavailable for local verification.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2197_hashing_fenwick.cpp](2197_hashing_fenwick.cpp) | G++ 13.2 x64 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 0.390 s | 33876 KB |
| [2197_hashing_fenwick.go](2197_hashing_fenwick.go) | Go 1.14 x64 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 0.468 s | 65620 KB |
| [2197_hashing_fenwick.java](2197_hashing_fenwick.java) | Java 1.8 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 1.390 s | 71404 KB |
| [2197_hashing_fenwick.py](2197_hashing_fenwick.py) | PyPy 3.10 x64 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 2.859 s | 95636 KB |
| [2197_hashing_fenwick.rs](2197_hashing_fenwick.rs) | Rust 1.75 x64 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 0.312 s | 45676 KB |
