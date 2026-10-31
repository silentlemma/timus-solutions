# 1423. String Tale

[Timus 1423](https://acm.timus.ru/problem.aspx?space=1&num=1423) · difficulty 170 · strings

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Strings S and T have the same length N (1 ≤ N ≤ 250 000) and consist of
characters with codes from 33 to 255. One cyclic shift moves the last
character of a string to the front. Print a number X (0 ≤ X < N) such
that X shifts turn S into T, or −1 if there is none; any X will do.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then S, then T.

## Output

X or −1.

## Examples

### Example 1

Input:

```
11
abracadabra
racadabraab
```

Output:

```
9
```

In the example, 9 shifts turn "abracadabra" into "racadabraab".

## Solution

X shifts to the right equal N − X shifts to the left, and the left
shifts of S by k are exactly the substrings of length N of S + S that
start at k < N. So find T in S + S: if it starts at position k, the
answer is (N − k) mod N, and if it does not occur, −1. The search is
Knuth–Morris–Pratt with the prefix function of T, run over S + S
without its last character; Python's built-in search of bytes is also
linear here. `O(N)`.

Pitfalls:

- a periodic S has several answers, so the tests use a checker
  (test 04);
- characters above 127 must be read as raw bytes; some readers decode
  them or even take code 160 for a space (test 05, gen3);
- a naive substring search can take quadratic time on strings of one
  repeated letter (gen2).

## Optimized solutions

The optimized C++ solution stores the prefix function in 18-bit fields
packed into an array of 32-bit words, since every value is below
N ≤ 250 000 < 2^18, and reads a field from two neighbouring words at
once; this costs a few shifts per access but takes about 0.56 MB instead
of 1 MB for `int` values. It also scans S twice instead of building S +
S, and reads S and T with `scanf` into two static buffers of
250 001 bytes instead of `std::string` with `cin`:
{1423_strings_optimized.cpp}.

The optimized Go solution keeps the prefix function in `int32` values
instead of 8-byte `int`, since every value is below N ≤ 250 000, and
reads S and T straight into byte arrays of exactly N bytes with
`io.ReadFull`, relying on both strings having length N, instead of
reading the whole input and splitting it into fields:
{1423_strings_optimized.go}.

The optimized Java solution reads the raw input in 64 KB blocks and cuts
S and T out of it by hand as `byte` arrays, comparing bytes, instead of
decoding the lines with `BufferedReader` into `char` arrays, which take
two bytes per character: {1423_strings_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1423_strings_optimized.cpp`: time reduction -106.67%; memory
  reduction +40.82%; base: `1423_strings.cpp`.

- `1423_strings_optimized.go`: time reduction +0.00%; memory reduction
  +40.39%; base: `1423_strings.go`.

- `1423_strings_optimized.java`: time reduction +19.87%; memory
  reduction +39.97%; base: `1423_strings.java`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1423_strings.cpp](1423_strings.cpp) | G++ 13.2 x64 | strings | O(N) | AC | 0.015 s | 1940 KB | 11286160 |
| [1423_strings.go](1423_strings.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 4268 KB | 11286161 |
| [1423_strings.java](1423_strings.java) | Java 1.8 | strings | O(N) | AC | 0.156 s | 5744 KB | 11307252 |
| [1423_strings.py](1423_strings.py) | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 1372 KB | 11286163 |
| [1423_strings.rs](1423_strings.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.031 s | 3052 KB | 11286168 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1423_strings_optimized.cpp](1423_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(N) | AC | 0.031 s | 1148 KB | 11307257 |
| [1423_strings_optimized.go](1423_strings_optimized.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 2544 KB | 11307255 |
| [1423_strings_optimized.java](1423_strings_optimized.java) | Java 1.8 | strings | O(N) | AC | 0.125 s | 3448 KB | 11307317 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
