# 1086. The n-th prime number

[Timus 1086](https://acm.timus.ru/problem.aspx?space=1&num=1086) · difficulty 107 · number_theory

Original problem: folklore, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each of `k` numbers `n` (`1 ≤ n ≤ 15000`) print the `n`-th prime
number. 1 is not a prime.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`k` (`1 ≤ k ≤ 15000`), then `k` lines with `n`.

## Output

The `n`-th prime for each `n`, one per line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
3
2
5
7
```

Output:

```
5
3
11
17
```

## Solution

The 15000th prime is 163 841, so one sieve of Eratosthenes up to that
number lists every prime that can be asked for, and each query is an
index into the list. `O(L log log L)` for the sieve with `L = 163 842`,
`O(1)` per query.

Pitfalls:

- the first prime is 2, not 1;
- the sieve bound must cover the 15000th prime itself; it can be found
  once with any method and written into the program;
- there can be up to 15000 queries, so the primes are computed once,
  not for every query.

The answers were checked against primes found one by one by trial
division.

## Optimized solutions

The optimized Go solution sieves only the odd numbers, which halves the
sieve, stores exactly 15000 primes as `uint32`, which holds them since
they are below 163 842, instead of growing a slice of `int`, and reads
the numbers byte by byte and prints them with `strconv` instead of
`fmt`: {1086_number_theory_optimized.go}.

The optimized Java solution sieves only the odd numbers, which halves
the sieve, keeps an array of exactly 15000 primes instead of
163 842 slots, parses the input from 8 KB blocks instead of
`StreamTokenizer`, and prints the digits through an 8 KB byte buffer
instead of collecting the whole output in a `StringBuilder`:
{1086_number_theory_optimized.java}.

The optimized Python solution sieves only the odd numbers, which halves
the `bytearray`, keeps the primes in an `array` of 32-bit unsigned
integers, which holds them since they are below 163 842, instead of a
list of Python integers, reads the queries line by line instead of
splitting the whole input at once, and prints the answers in batches of
1024: {1086_number_theory_optimized.py}.

The optimized Rust solution sieves only the odd numbers, which halves
the sieve, stores exactly 15000 primes as `u32`, which holds them since
they are below 163 842, in a vector reserved in advance instead of a
growing `Vec<usize>`, and writes the answers through a `BufWriter`
instead of making a string for each answer and joining them:
{1086_number_theory_optimized.rs}.

The optimized C++ version keeps the same sieve algorithm, but represents only odd numbers in a packed bitset (about 10 KB). Its sorted list stores the low 16 bits of each of the 15000 primes in 30 KB. Every prime is below three times `2^16`; two boundary indices, computed while the primes are generated, tell whether to add zero, one or two multiples of `2^16` when answering. This preserves constant-time queries without a precomputed answer table. Total time is `O(L log log L + k)`, storage `O(L + P)` for sieve bound `L` and prime count `P`. The ordinary vector-based implementation remains the base version.

Source-matched Accepted runs: base 0.031 s / 212 KB; this version 0.015 s / 148 KB (submission 11307512). Memory is reduced by 30.19%; the one-tick time difference is not used as evidence of acceleration. The refreshed rating target is met.

{1086_number_theory_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1086_number_theory_optimized.cpp`: time reduction +51.61%; memory
  reduction +30.19%; base: `1086_number_theory.cpp`.

- `1086_number_theory_optimized.go`: time reduction +0.00%; memory
  reduction +48.87%; base: `1086_number_theory.go`.

- `1086_number_theory_optimized.java`: time reduction +16.13%; memory
  reduction +72.98%; base: `1086_number_theory.java`.

- `1086_number_theory_optimized.py`: time reduction +0.00%; memory
  reduction +64.25%; base: `1086_number_theory.py`.

- `1086_number_theory_optimized.rs`: time reduction +0.00%; memory
  reduction +50.79%; base: `1086_number_theory.rs`.

## Language notes

- Python crosses out multiples with slice assignment on a `bytearray`.
- C++, Go, Java and Rust start crossing out at `p²`; C++ and Java compute
  it in 64 bits to stay safe from overflow in the base C++ version and in Java.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1086_number_theory.cpp](1086_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log log L) | AC | 0.031 s | 212 KB | 11279046 |
| [1086_number_theory.go](1086_number_theory.go) | Go 1.14 x64 | number_theory | O(L log log L) | AC | 0.001 s | 2308 KB | 11279049 |
| [1086_number_theory.java](1086_number_theory.java) | Java 1.8 | number_theory | O(L log log L) | AC | 0.093 s | 2132 KB | 11279053 |
| [1086_number_theory.py](1086_number_theory.py) | Python 3.12 x64 | number_theory | O(L log log L) | AC | 0.093 s | 2764 KB | 11279050 |
| [1086_number_theory.rs](1086_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log log L) | AC | 0.001 s | 1268 KB | 11279055 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1086_number_theory_optimized.cpp](1086_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(L log log L) | AC | 0.015 s | 148 KB | 11307512 |
| [1086_number_theory_optimized.go](1086_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(L log log L) | AC | 0.015 s | 1180 KB | 11304263 |
| [1086_number_theory_optimized.java](1086_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(L log log L) | AC | 0.078 s | 576 KB | 11304023 |
| [1086_number_theory_optimized.py](1086_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(L log log L) | AC | 0.093 s | 988 KB | 11304024 |
| [1086_number_theory_optimized.rs](1086_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(L log log L) | AC | 0.001 s | 624 KB | 11304043 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
