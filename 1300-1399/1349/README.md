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

The optimized solutions print the same three answers. Java parses the
exponent by hand with `System.in.read` instead of `Scanner`: 0.062 s
instead of 0.125 s and 316 KB instead of 1612 KB. Rust writes the answer
as a byte string with `write_all` instead of `println!`: 0.031 s instead
of 0.062 s and 212 KB instead of 232 KB.

`1349_math_optimized.py`. Use the same complete case split as the basic lookup: n=1 gives 1 2 3, n=2 gives 3 4 5, all other allowed n give -1. Direct branches avoid allocating the tiny answer dictionary; they do not add a new number-theory algorithm. Time and auxiliary space O(1). The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1349_math.py`: time 0.093 s → 0.109 s; memory 336 KB → 172 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1349_math_optimized.py`: time place 85/130, memory place 1/130 in this comparable sample.

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
| [1349_math_optimized.py](1349_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 172 KB | 11325067 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
