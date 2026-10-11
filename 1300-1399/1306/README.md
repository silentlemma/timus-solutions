# 1306. Sequence Median

[Timus 1306](https://acm.timus.ru/problem.aspx?space=1&num=1306) · difficulty 145 · sorting

Original problem from the Second Ural Team Student Programming Championship, Yekaterinburg, April 3–4, 1998.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find the median of N ≤ 250 000 integers from 0 to 2³¹ − 1: the middle
element of the sorted sequence for odd N, and the mean of the two
middle elements for even N. Print it with one decimal.

Time limit: 1 second. Memory limit: 1 MB. The statement allows C, C++
and Pascal; the submit form also offers Rust.

## Input

N, then the N numbers, one per line.

## Output

The median with one decimal.

## Examples

### Example 1

Input:

```
4
3
6
4
5
```

Output:

```
4.5
```

## Solution

The whole sequence takes 250 000 · 4 bytes, about 1 MB, which is the
entire memory limit. But only the smaller half matters: the median is
the largest, or the mean of the two largest, of the ⌊N/2⌋ + 1 smallest
numbers.

So a max-heap keeps the ⌊N/2⌋ + 1 smallest numbers seen so far, about
500 KB. Each new number either joins it while it is not yet full, or
replaces the top when it is smaller than the top. At the end:

- for odd N the top is the median;
- for even N the top and, after one pop, the new top are the two middle
  elements.

`O(N log N)` time, `O(N / 2)` memory.

Pitfalls:

- two numbers near 2³¹ − 1 overflow even a 32-bit unsigned sum, so the
  sum is taken in 64 bits (tests 03 and 04);
- the mean is an integer or ends in .5, so it is printed exactly, without
  floating point (tests 01 and 08);
- C++ streams cost too much memory here, so the program reads with
  `scanf`.

## Language notes

- The statement allows only C, C++ and Pascal, but the Timus submit form
  also offers Rust 1.75, so there are C++ and Rust solutions; Go, Python
  and Java cannot be submitted.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1306_sorting.cpp](1306_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N) | AC | 0.203 s | 624 KB |
| [1306_sorting.rs](1306_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N) | AC | 0.031 s | 696 KB |
