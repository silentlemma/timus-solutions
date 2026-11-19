# 1295. Crazy Notions

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · difficulty 151 · number_theory

Original problem by Den Raskovalov, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

How many zeros does the decimal number 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ end with,
for 1 ≤ n ≤ 300 000?

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The number n.

## Output

The number of trailing zeros.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
1
```

Output:

```
1
```

### Example 2

Input:

```
3
```

Output:

```
2
```

## Solution

The sum has more than 180 000 digits for the largest n, but its trailing
zeros are limited by the power of 2 in it. Let S = 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ.

- n = 1: S = 10, one zero.
- Even n: 1ⁿ + 3ⁿ ≡ 1 + 1 = 2 (mod 4), and 2ⁿ, 4ⁿ are multiples of 4,
  so S is divisible by 2 but not by 4.
- Odd n ≥ 3: 3ⁿ ≡ 3 (mod 8), so 1ⁿ + 3ⁿ ≡ 4 (mod 8), while 2ⁿ and 4ⁿ
  are multiples of 8; S is divisible by 4 but not by 8.

So S never ends in three zeros, and S mod 100 decides everything: 2
zeros if it is 0, 1 zero if it ends in 0, none otherwise. The four
powers modulo 100 come from fast exponentiation. `O(log n)`.

In fact the answer depends only on n mod 20: 0 when 4 divides n, 2
when n leaves 3 mod 4 or 5 mod 20, and 1 otherwise. The solutions
compute it directly rather than rely on this table.

Pitfalls:

- n leaving 1 mod 4 usually gives one zero, but n = 5, 25, … give two
  (tests 05 and 06);
- the full sum can be built with big integers, but it is never needed:
  only its last two digits matter.

The results were compared with the exact big-integer sum for every n
up to 3000.

## Optimized solutions

The optimized Java solution parses `n` by hand from a 4 KB buffer filled
from `System.in` instead of creating a `Scanner`, so the JVM does not
load the scanner and its regular expressions; the powers modulo 100 are
the same: {1295_number_theory_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1295_number_theory_optimized.java`: time reduction +12.80%; memory
  reduction +79.75%; base: `1295_number_theory.java`.

`1295_number_theory_optimized.py`. Keep the same modulo-100 argument for the number of trailing zeroes. Compute 1+pow(2,n,100)+pow(3,n,100)+pow(4,n,100) directly rather than a generator over four bases. Modular exponentiation never constructs the huge powers. The proven bound of at most two trailing zeroes makes remainder zero mean two, divisibility by ten mean one, otherwise zero. Time O(log n) bounded modular operations and O(1) state. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1295_number_theory.py`: time 0.093 s → 0.125 s; memory 464 KB → 200 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1295_number_theory_optimized.py`: time place 37/57, memory place 1/57 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB | 11284634 |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB | 11284638 |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB | 11284648 |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB | 11284644 |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB | 11284651 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory_optimized.java](1295_number_theory_optimized.java) | Java 1.8 | number_theory | O(log n) | AC | 0.109 s | 324 KB | 11305839 |
| [1295_number_theory_optimized.py](1295_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(log n) | AC | 0.125 s | 200 KB | 11325070 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
