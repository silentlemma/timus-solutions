# 1925. One Final Value to Match an Aggregate

[Timus 1925](https://acm.timus.ru/problem.aspx?space=1&num=1925) · difficulty 70 · math

Original problem by Pavel Ageev, from Ural Regional School Programming Contest 2012.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sequence of n past rounds is known. In round i, a displayed value bᵢ
had intended input bᵢ−2, but the actual input was gᵢ. The current round
displays k. Only the total over all n+1 rounds is checked: actual inputs
must sum to the sum of intended inputs. Choose a nonnegative integer
for the current round, or report that none exists. Past rounds need not
be individually correct. Limits: 1 second, 64 MB.

## Input

n,k with 1≤n,k≤100, followed by n pairs bᵢ,gᵢ, each in 0..100.

## Output

Print the required nonnegative integer, including zero if appropriate.
There is no upper bound of 100 on this output. If impossible, print
exactly `Big Bang!`, with its space, capitalization and exclamation mark.

## Checking

Compare whitespace-separated tokens exactly: either the integer or
the two tokens `Big` and `Bang!`.

## Examples

```
6 5
3 1
3 1
5 3
6 5
5 5
7 2
```

```
3
```

```
1 3
4 6
```

```
Big Bang!
```

## Solution

Let x be the current input. The check requires

```text
sum(gᵢ) + x = sum(bᵢ−2) + (k−2).
```

Rearranging gives x=k−2+sum(bᵢ−gᵢ−2). Start a signed balance at k−2
and add bᵢ−gᵢ−2 for every past pair. Inspect the sign only after all
pairs: output the balance if nonnegative, otherwise the failure phrase.

The equation has coefficient one on x, so this candidate is unique.
If it is nonnegative, substituting it satisfies the aggregate check.
If it is negative, no other nonnegative value can satisfy that equality.
This proves both outcomes.

An individual intended value or an intermediate balance may be negative.
Only the final total matters. For example k=100 with past pairs
(0,100),(100,0) yields 94, although the running balance becomes negative
after the first pair. With k=1 and pair (3,0), the correct answer is zero.

O(n) time. The arithmetic accumulator uses O(1) working space; these
implementations store the history or read the complete input, so their
total space is O(n).

There are n+1 rounds, including today. Subtract two for every round.
Do not reject early, validate each past round separately, clamp a negative
subtotal, or require k≥2. Zero is valid, and the final input may exceed
100. Preserve the exact failure phrase.

## Language notes

Use signed arithmetic, including in Rust. All intermediate balances fit
32-bit signed integers: the overall possible range is −10201..9898.
The upper end occurs at n=100,k=100 and every pair (100,0).
All five versions return a signed balance and format failure only at
the end; Python supplies history pairs lazily over buffered input.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1925_math.cpp](1925_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 428 KB |
| [1925_math.go](1925_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1088 KB |
| [1925_math.java](1925_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 1796 KB |
| [1925_math.py](1925_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 504 KB |
| [1925_math.rs](1925_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB |
