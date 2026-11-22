# 1104. The smallest base in which a number is divisible by the base minus one

[Timus 1104](https://acm.timus.ru/problem.aspx?space=1&num=1104) · difficulty 95 · number_theory

Original problem by Igor Goldberg, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A number is written with the digits `0`–`9` and the letters `A`–`Z`
(`A` = 10, …, `Z` = 35), at most `10^6` of them. Find the smallest base
`k`, `2 ≤ k ≤ 36`, in which this string is a valid number divisible by
`k − 1`. Print `No solution.` if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

One line with the digits.

## Output

`k` in decimal, or `No solution.`

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
A1A
```

Output:

```
22
```

## Solution

Since `k ≡ 1 (mod k − 1)`, every power of `k` is 1 modulo `k − 1`, and a
number in base `k` has the same remainder as the sum of its digits, the
same rule as divisibility by 9 in decimal. So compute the digit sum `S`
and the largest digit `m` once, then try `k` from `max(m + 1, 2)` up to
36 and print the first one for which `k − 1` divides `S`. `O(L)` for `L`
digits.

Pitfalls:

- the base must exceed every digit, so the search starts at `m + 1`;
- base 2 divides everything by 1, so a number of zeros and ones always
  has the answer 2, including a single `0`;
- the digit sum is at most `35 · 10^6` and fits in 32 bits.

The answers were checked by converting the whole string in every base
with Python's big integers and taking the remainder directly.

## Optimized solutions

`1104_number_theory_optimized.go`. Keep the digit-sum divisibility test: in radix b the number is congruent to its digit sum modulo b-1. Scan the input token once to accumulate the sum and greatest digit, starting the greatest value at one so the first candidate base is at least two. Try bases greatest+1..36 in increasing order and emit the first divisor, or exactly No solution. Both new versions stream bytes without retaining the number string; Rust also removes its digit vector. L<=10^6 bounds the sum by 35·10^6, safely within signed 32 bits. Time O(L+36), O(1) auxiliary state plus fixed runtime buffers. Portable os.Stdin.Read/os.Stdout.Write and direct integer conversion use fixed 4096-byte input and output buffers. Partial writes are handled before reusing the output buffer. The original simple Accepted source is preserved.

Compared with `1104_number_theory.go`: time 0.031 s → 0.031 s; memory 6608 KB → 812 KB.

`1104_number_theory_optimized.rs`. Keep the digit-sum divisibility test: in radix b the number is congruent to its digit sum modulo b-1. Scan the input token once to accumulate the sum and greatest digit, starting the greatest value at one so the first candidate base is at least two. Try bases greatest+1..36 in increasing order and emit the first divisor, or exactly No solution. Both new versions stream bytes without retaining the number string; Rust also removes its digit vector. L<=10^6 bounds the sum by 35·10^6, safely within signed 32 bits. Time O(L+36), O(1) auxiliary state plus fixed runtime buffers. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1104_number_theory.rs`: time 0.015 s → 0.031 s; memory 7048 KB → 60 KB.

The optimized solutions (C++, Java, Python) never store the line of up to
`10^6` digits: they read the input in chunks of 4 KB (64 KB in Python) and
add the digits up on the way, so the memory stays small whatever the
length. Python turns a whole chunk into digit values at once with
`bytes.translate` and sums it with `sum`, without a loop over the
characters in Python code. C++: 0.015 s instead of 0.093 s and 96 KB
instead of 2640 KB; Java: 372 KB instead of 5448 KB, with the same time;
Python: 0.109 s instead of 0.265 s and 588 KB instead of 17808 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1104_number_theory_optimized.go`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

`1104_number_theory_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1104_number_theory.cpp](1104_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L) | AC | 0.093 s | 2640 KB | 11279172 |
| [1104_number_theory.go](1104_number_theory.go) | Go 1.14 x64 | number_theory | O(L) | AC | 0.031 s | 6608 KB | 11279173 |
| [1104_number_theory.java](1104_number_theory.java) | Java 1.8 | number_theory | O(L) | AC | 0.109 s | 5448 KB | 11279175 |
| [1104_number_theory.py](1104_number_theory.py) | Python 3.12 x64 | number_theory | O(L) | AC | 0.265 s | 17808 KB | 11279174 |
| [1104_number_theory.rs](1104_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L) | AC | 0.015 s | 7048 KB | 11279176 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1104_number_theory_optimized.cpp](1104_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(L) | AC | 0.015 s | 96 KB | 11303551 |
| [1104_number_theory_optimized.java](1104_number_theory_optimized.java) | Java 1.8 | number_theory | O(L) | AC | 0.109 s | 372 KB | 11303552 |
| [1104_number_theory_optimized.py](1104_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(L) | AC | 0.109 s | 588 KB | 11303553 |
| [1104_number_theory_optimized.go](1104_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(L+36) | AC | 0.031 s | 812 KB | 11328265 |
| [1104_number_theory_optimized.rs](1104_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(L+36) | AC | 0.031 s | 60 KB | 11325127 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
