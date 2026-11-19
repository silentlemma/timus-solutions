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

## Checking

The repository uses a semantic checker and accepts any output satisfying these conditions. The repository checker requires exactly one integer. It accepts-1 exactly when the stored reference says no rotation exists. Otherwise any X in [0,N) is valid if moving the last X bytes of S to the front yields T; it does not require the smallest shift.

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

`1423_strings_optimized.rs`. Keep byte-based KMP and the same right-rotation index. Store prefix lengths in u32 and scan chained slices s followed by s without its last byte, replacing modulo on every text position without allocating a doubled string. Byte tokens preserve characters 33…255. O(N) time and space; direct output replaces Rust formatting.

Compared with `1423_strings.rs`: time 0.031 s → 0.031 s; memory 3052 KB → 1 804 KB.

`1423_strings_optimized.py`. Keep the same doubled-byte-string search and conversion from a left offset to right shift: (n-offset) mod n, or -1 if absent. Read the three input tokens through an unbuffered binary file and flush the answer before os._exit(0). The algorithm still stores O(n) bytes; the runtime/I/O changes are not a new asymptotic algorithm. CPython 3.12 uses its adaptive/Two-Way substring implementation, so this search remains O(n): [runtime source](https://raw.githubusercontent.com/python/cpython/v3.12.0/Objects/stringlib/fastsearch.h). This Accepted uses more memory than the retained base and does not achieve 30% improvement; admission is the separate top 30% rule with a better rank, while the rating-target star remains.

Compared with `1423_strings.py`: time 0.109 s → 0.093 s; memory 1372 KB → 1 592 KB.

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

Each optimized version has Accepted and meets a ranking or resource-improvement
admission criterion. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1423_strings_optimized.cpp`: time reduction -106.67%; memory
  reduction +40.82%; base: `1423_strings.cpp`.

- `1423_strings_optimized.go`: time reduction +0.00%; memory reduction
  +40.39%; base: `1423_strings.go`.

- `1423_strings_optimized.java`: time reduction +19.87%; memory
  reduction +39.97%; base: `1423_strings.java`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1423_strings_optimized.py`: time place 11/55, memory place 1/55 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [1423_strings_optimized.py](1423_strings_optimized.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 1592 KB | 11325463 |
| [1423_strings_optimized.rs](1423_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(N) time; O(N) space | AC | 0.031 s | 1804 KB | 11325527 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
