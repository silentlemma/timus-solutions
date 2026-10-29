# 2018. Counting Sequences with Bounded Runs

[Timus 2018](https://acm.timus.ru/problem.aspx?space=1&num=2018) · difficulty 102 · dp, prefix_sums

Original problem by Olga Soboleva, prepared by Alex Samsonov, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count length-`n` sequences over symbols 1 and 2. A consecutive run of ones
may have length at most `a`; a run of twos may have length at most `b`.
Two sequences are different if some position differs. Return the count
modulo `1,000,000,007`.

The limits are `1 ≤ a,b ≤ 300` and `max(a,b)+1 ≤ n ≤ 50,000`.
Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The only line contains `n a b`.

## Output

Print the number of valid sequences modulo `1,000,000,007`.

## Checking

Outputs are compared token by token.

## Examples

```
3 2 1
```

```
4
```

## Solution

Let one[i] be the number of valid sequences of length i that end with a
run of ones, and two[i] those that end with a run of twos. A sequence
ending with a run of r ones, 1 ≤ r ≤ a, is a sequence of length i − r
that ends with twos, followed by the run; the empty sequence counts once
on each side, one[0] = two[0] = 1. So

- one[i] = two[i − 1] + two[i − 2] + … + two[max(0, i − a)],
- two[i] = one[i − 1] + … + one[max(0, i − b)],

and the answer is one[n] + two[n] modulo 10⁹ + 7. Each sum is the
difference of two prefix sums of the same array, so every length takes
`O(1)`, `O(n)` in all.

In the example n = 3, a = 2, b = 1 the sequences are 112, 121, 211 and
212: 22 has a run of twos longer than b, 111 a run of ones longer
than a.

Pitfalls:

- the empty sequence counts once in each sum and never as an answer;
- the difference of two prefix sums modulo 10⁹ + 7 can be negative.

## Optimized solutions

The optimized Java solution keeps only the values the sums still need:
the last a + 1 values of two and the last b + 1 values of one, in
circular buffers, together with the two window sums, which are moved one
step for every length instead of being taken from prefix sums. It also
parses the three numbers by hand instead of using `Scanner`: 0.093 s
instead of 0.125 s and 408 KB instead of 3140 KB.

## Language notes

- Python's `%` already gives a nonnegative remainder; C++, Go and Java
  add the modulus before taking the remainder again, and Rust uses
  `rem_euclid`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2018_dp_prefix_sums.cpp](2018_dp_prefix_sums.cpp) | G++ 13.2 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 1368 KB | 11303350 |
| [2018_dp_prefix_sums.go](2018_dp_prefix_sums.go) | Go 1.14 x64 | dp, prefix_sums | O(n) | AC | 0.031 s | 2688 KB | 11303351 |
| [2018_dp_prefix_sums.java](2018_dp_prefix_sums.java) | Java 1.8 | dp, prefix_sums | O(n) | AC | 0.125 s | 3140 KB | 11303352 |
| [2018_dp_prefix_sums.py](2018_dp_prefix_sums.py) | Python 3.12 x64 | dp, prefix_sums | O(n) | AC | 0.156 s | 8624 KB | 11303354 |
| [2018_dp_prefix_sums.rs](2018_dp_prefix_sums.rs) | Rust 1.75 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 1648 KB | 11303355 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2018_dp_prefix_sums_optimized.java](2018_dp_prefix_sums_optimized.java) | Java 1.8 | dp, prefix_sums | O(n) | AC | 0.093 s | 408 KB | 11303659 |
