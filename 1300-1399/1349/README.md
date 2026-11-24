# 1349. Farm

[Timus 1349](https://acm.timus.ru/problem.aspx?space=1&num=1349) · difficulty 51 · math

Original problem credited to Pierre Fermat, from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given n, 0 ≤ n ≤ 100, find three different integers a, b, c from 1 to
100 with aⁿ + bⁿ = cⁿ, the one with the smallest a, then the smallest
b, then the smallest c, or print −1 if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number n.

## Output

a, b and c, or −1.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
0
```

Output:

```
-1
```

### Example 2

Input:

```
1
```

Output:

```
1 2 3
```

## Solution

- n = 0: every power is 1, and 1 + 1 is never 1, so there is no answer.
- n = 1: a + b = c, and the smallest choice with three different numbers
  is 1 2 3.
- n = 2: the smallest Pythagorean triple, 3 4 5, is the first in the
  required order.
- n ≥ 3: by Fermat's last theorem aⁿ + bⁿ = cⁿ has no solution in positive
  integers.

`O(1)`.

Pitfalls:

- n = 0 has no answer even though every power is equal (test 01);
- the numbers must be different, which rules out answers like 1 1 2 for
  n = 1.

A search over all triples up to 100 for n from 0 to 5 gave the same
answers.

## Optimized solutions

`1349_math_optimized.py`. Keep the complete mathematical cases: positive witnesses exist only for powers one and two, with smallest triples 1,2,3 and 3,4,5; power zero and powers above two have no solution. Normalize the sole decimal token by stripping surrounding whitespace, an optional plus and leading zeros, then compare bytes with 1 and 2 instead of constructing an int or answer dictionary. Write the complete fixed answer before os._exit(0). Parsing costs O(I) for I input bytes, mathematical work is constant; no precomputed table of arbitrary answers. The new CPython time is 0.062 s with 644 KB, versus old PyPy 0.109 s/172 KB; the memory increase is explicit and the teaching version remains.

Exact-source Python 3.12 x64 Accepted #11327873: 0.062 s / 644 KB. Saved 2026-11-20 compiler-cohort ranks, time then memory: 5/130; 98/130. Strict admission uses time only below 1024 KB: top ten or top 15%, ties share rank and percentage cutoff rounds up. An asterisk remains for the separate first-place-in-both language target. The preserved previous variant has its own paired receipt #11325067 (PyPy 3.10 x64): 0.109 s / 172 KB; do not mix measurements or runtimes. All teaching sources remain unchanged.

- `1349_math_optimized.py`: 0.062 s / 644 KB; retained teaching base `1349_math.py`: 0.093 s / 336 KB.

The optimized solutions print the same three answers. Java parses the
exponent by hand with `System.in.read` instead of `Scanner`: 0.062 s
instead of 0.125 s and 316 KB instead of 1612 KB. Rust writes the answer
as a byte string with `write_all` instead of `println!`: 0.031 s instead
of 0.062 s and 212 KB instead of 232 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1349_math.cpp](1349_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11285147 |
| [1349_math.go](1349_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1064 KB | 11285150 |
| [1349_math.java](1349_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB | 11285153 |
| [1349_math.py](1349_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 336 KB | 11285152 |
| [1349_math.rs](1349_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.062 s | 232 KB | 11285154 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1349_math_optimized.java](1349_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.062 s | 316 KB | 11303601 |
| [1349_math_optimized.rs](1349_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 212 KB | 11303602 |
| [1349_math_optimized.py](1349_math_optimized.py) | Python 3.12 x64 | math | O(I) token input; O(1) mathematical cases | AC | 0.062 s | 644 KB | 11327873 |
